"""
src/graph/nodes/quant_engine.py

LangGraph Node C — Deterministic Quant Execution.

Dispatches each completed ExtractedLogic entry to the appropriate quant
module.  The LLM is NOT involved here — all arithmetic is pure Python.

Dispatch table:
  risk_class  →  metric_name       →  module function
  ─────────────────────────────────────────────────────
  *           →  delta_charge      →  sbm_delta.sbm_delta_charge
  *           →  vega_charge       →  sbm_vega.sbm_vega_charge
  *           →  curvature_charge  →  sbm_curvature.sbm_curvature_charge
  *           →  drc_charge        →  drc.drc_charge
  *           →  rrao_charge       →  rrao.rrao_charge

By default the node computes delta for all risk classes.
Vega, curvature, DRC and RRAO are computed when positions carry the
relevant fields (cvr_up/cvr_down for curvature; notional for RRAO/DRC).
"""
from src.graph.state import AgentState, CalculatedMetric, ValidationError
from src.quant.sbm_delta     import sbm_delta_charge
from src.quant.sbm_vega      import sbm_vega_charge
from src.quant.sbm_curvature import sbm_curvature_charge
from src.quant.drc           import drc_charge
from src.quant.rrao          import rrao_charge


def _has_vega(positions) -> bool:
    """Positions are vega positions if risk_factor contains 'vega' or sensitivity
    appears alongside option-style metadata."""
    return any("vega" in (p.risk_factor or "").lower() for p in positions)


def _has_curvature(positions) -> bool:
    return any(p.cvr_up is not None or p.cvr_down is not None for p in positions)


def _has_notional(positions) -> bool:
    return any(p.notional is not None for p in positions)


def _has_rrao_positions(positions) -> bool:
    return any(
        p.risk_factor in ("exotic", "other_residual") for p in positions
    )


async def quant_execution_node(state: AgentState) -> AgentState:
    """Run deterministic capital calculations for all complete extracted logics."""
    import asyncio

    def _run_calculations():
        metrics: list[CalculatedMetric] = []
        errors = list(state.get("validation_errors", []))

        for logic in state.get("extracted_calculation_logic", []):
            if not logic.is_complete:
                continue   # validator handles the missing-params branch

            positions = [
                p for p in state.get("portfolio_inputs", [])
                if p.risk_class == logic.risk_class
            ]
            if not positions:
                continue

            # ── Delta (always computed for SBM risk classes) ───────────────────
            sbm_classes = {"GIRR", "CSR_NonSec", "CSR_Sec", "Equity", "Commodity", "FX"}
            if logic.risk_class in sbm_classes:
                try:
                    metrics.append(sbm_delta_charge(positions, logic))
                except KeyError as e:
                    errors.append(ValidationError(
                        severity="blocking", node="quant_engine",
                        message=f"{logic.risk_class} delta: {e}",
                    ))

            # ── Vega ───────────────────────────────────────────────────────────
            if _has_vega(positions):
                try:
                    metrics.append(sbm_vega_charge(positions, logic))
                except KeyError as e:
                    errors.append(ValidationError(
                        severity="warning", node="quant_engine",
                        message=f"{logic.risk_class} vega: {e}",
                    ))

            # ── Curvature ──────────────────────────────────────────────────────
            if _has_curvature(positions):
                try:
                    metrics.append(sbm_curvature_charge(positions, logic))
                except Exception as e:
                    errors.append(ValidationError(
                        severity="warning", node="quant_engine",
                        message=f"{logic.risk_class} curvature: {e}",
                    ))

            # ── DRC (credit positions with notional) ───────────────────────────
            credit_classes = {"CSR_NonSec", "CSR_Sec"}
            if logic.risk_class in credit_classes and _has_notional(positions):
                try:
                    metrics.append(drc_charge(positions, logic))
                except Exception as e:
                    errors.append(ValidationError(
                        severity="warning", node="quant_engine",
                        message=f"{logic.risk_class} DRC: {e}",
                    ))

            # ── RRAO (residual risk positions) ─────────────────────────────────
            if _has_rrao_positions(positions) and _has_notional(positions):
                try:
                    metrics.append(rrao_charge(positions, logic))
                except Exception as e:
                    errors.append(ValidationError(
                        severity="warning", node="quant_engine",
                        message=f"{logic.risk_class} RRAO: {e}",
                    ))

        return metrics, errors

    metrics, errors = await asyncio.to_thread(_run_calculations)

    state["calculated_metrics"] = metrics
    state["validation_errors"]  = errors
    return state
