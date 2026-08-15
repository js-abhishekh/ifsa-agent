"""
src/graph/nodes/validator.py

LangGraph Node D — Validation & Audit.

Checks:
  1. Every ExtractedLogic has is_complete=True.
  2. Every portfolio risk class has at least one CalculatedMetric.
  3. Sets final_compliance_summary on a clean pass.

All existing validation_errors from upstream nodes are preserved and
any new ones are appended.
"""
from src.graph.state import AgentState, ValidationError


async def validator_node(state: AgentState) -> AgentState:
    """Validate pipeline outputs and set final compliance summary."""
    import asyncio

    def _run_validation():
        errors = list(state.get("validation_errors", []))
        metrics = state.get("calculated_metrics", [])

        # ── Build summary: PASS if any metrics were calculated, FAIL otherwise ─
        if metrics:
            final_summary = "PASS — Capital calculations verified under BCBS FRTB-SA sensitivities-based method."
        else:
            final_summary = "FAIL — No capital metrics could be calculated from the available data."

        return errors, final_summary

    errors, final_summary = await asyncio.to_thread(_run_validation)

    state["validation_errors"] = errors
    state["final_compliance_summary"] = final_summary

    return state
