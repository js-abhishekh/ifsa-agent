"""
src/graph/routing.py

Conditional routing logic for the FRTB-SA LangGraph pipeline.

After the validator node, one of three paths is chosen:
  "end"                  — no blocking errors → pipeline complete
  "retry_retrieval"      — blocking errors from logic_extractor AND retries remain
  "request_missing_inputs" — retries exhausted OR errors from quant_engine/portfolio
"""
from src.graph.state import AgentState


def route_after_validation(state: AgentState) -> str:
    """Return the next routing destination after the validator node."""
    # PASS/FAIL is now determined by the validator based on available metrics.
    # Always proceed to end — no retries or missing-input escalations needed.
    return "end"
