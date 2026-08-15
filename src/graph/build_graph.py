"""
src/graph/build_graph.py

Assembles the FRTB-SA LangGraph StateGraph.

Node topology:
  retrieve → extract_logic → execute_quant → validate
                              ↑                   |
                         retry_bump ←─────────────┤ [retry_retrieval]
                                                  |
                         request_missing_inputs ←─┘ [request_missing_inputs]
                                                  |
                                                 END
"""
from langgraph.graph import StateGraph, END
from src.graph.state import AgentState
from src.graph.nodes.retriever      import retriever_node
from src.graph.nodes.logic_extractor import logic_extractor_node
from src.graph.nodes.quant_engine   import quant_execution_node
from src.graph.nodes.validator      import validator_node
from src.graph.nodes.document_auditor import document_auditor_node
from src.graph.routing              import route_after_validation


# ── Utility nodes (pure state transforms, no I/O) ─────────────────────────────
def _increment_retry(state: AgentState) -> AgentState:
    state["retry_count"] = state.get("retry_count", 0) + 1
    # Clear previous extraction results so the retriever fetches fresh content
    state["retrieved_regulatory_nodes"] = []
    state["extracted_calculation_logic"] = []
    state["calculated_metrics"] = []
    state["validation_errors"] = []
    return state


def _request_missing_inputs(state: AgentState) -> AgentState:
    state["final_compliance_summary"] = "FAIL — Missing required regulatory parameters or manual inputs to complete FRTB-SA calculation."
    return state


# ── Graph assembly ─────────────────────────────────────────────────────────────
def build_frtb_graph():
    """Build and compile the FRTB-SA LangGraph application."""
    graph = StateGraph(AgentState)

    # Register nodes
    graph.add_node("audit_document",         document_auditor_node)
    graph.add_node("retrieve",               retriever_node)
    graph.add_node("extract_logic",          logic_extractor_node)
    graph.add_node("execute_quant",          quant_execution_node)
    graph.add_node("validate",               validator_node)
    graph.add_node("retry_bump",             _increment_retry)
    graph.add_node("request_missing_inputs", _request_missing_inputs)

    # Linear flow
    graph.set_entry_point("audit_document")
    graph.add_edge("audit_document","retrieve")
    graph.add_edge("retrieve",     "extract_logic")
    graph.add_edge("extract_logic","execute_quant")
    graph.add_edge("execute_quant","validate")

    # Conditional routing after validation
    graph.add_conditional_edges(
        "validate",
        route_after_validation,
        {
            "end":                    END,
            "retry_retrieval":        "retry_bump",
            "request_missing_inputs": "request_missing_inputs",
        },
    )

    # Retry loop back to retriever
    graph.add_edge("retry_bump", "retrieve")

    # Terminal escalation
    graph.add_edge("request_missing_inputs", END)

    return graph.compile()
