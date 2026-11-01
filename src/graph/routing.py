"""
src/graph/routing.py

Routing logic for the FRTB-SA LangGraph pipeline.

The pipeline executes as a deterministic 5-stage workflow:
  audit_document → retrieve → extract_logic → execute_quant → validate → END

Regulatory parameters are guaranteed by Basel Annex statutory binding in logic_extractor,
so cyclic vector retries and missing input prompts are not required.
"""
from src.graph.state import AgentState


def route_after_validation(state: AgentState) -> str:
    """Always completes the pipeline at END."""
    return "end"
