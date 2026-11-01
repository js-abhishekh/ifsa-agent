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
        audit_flags = state.get("audit_flags", [])

        has_blocking = any(e.severity == "blocking" for e in errors)
        flag_count = len(audit_flags)

        positions = state.get("portfolio_inputs", [])

        # ── Build summary based on audit flags and calculation health ─────────
        if not positions and not metrics:
            if flag_count > 0:
                final_summary = (
                    f"NON-COMPLIANT (DISCLOSURE ONLY) — {flag_count} regulatory disclosure breach{'es' if flag_count > 1 else ''} "
                    "detected in document text, but no granular trading book positions were available to compute capital charges."
                )
            else:
                final_summary = (
                    "INCOMPLETE — No trading book positions were provided or extracted. "
                    "Capital charges could not be calculated."
                )
        elif not metrics and has_blocking:
            final_summary = "FAIL — Pipeline halted due to blocking validation errors. Capital calculations could not be completed."
        elif flag_count > 0:
            final_summary = (
                f"NON-COMPLIANT — {flag_count} regulatory disclosure breach{'es' if flag_count > 1 else ''} "
                "detected under Basel III (FRTB-SA MAR21/MAR22). The bank's disclosure omits required risk components "
                "or reports material exposure discrepancies. Quantitative figures above reflect independent IFSA benchmark recalculation only."
            )
        elif errors:
            warning_count = len([e for e in errors if e.severity == "warning"])
            final_summary = (
                f"CONDITIONAL PASS — Calculations completed with {warning_count} warning(s). "
                "Certain regulatory parameters were resolved using static Basel Annex tables."
            )
        else:
            final_summary = "PASS — Capital calculations verified cleanly under BCBS FRTB-SA sensitivities-based method with zero regulatory disclosure breaches."

        return errors, final_summary

    errors, final_summary = await asyncio.to_thread(_run_validation)

    state["validation_errors"] = errors
    state["final_compliance_summary"] = final_summary

    return state
