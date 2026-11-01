"""
src/graph/build_graph.py

Assembles the FRTB-SA LangGraph StateGraph.

Pipeline topology:
  audit_document → retrieve → extract_logic → execute_quant → validate → END
"""
from langgraph.graph import StateGraph, END
from src.graph.state import AgentState
from src.graph.nodes.retriever        import retriever_node
from src.graph.nodes.logic_extractor  import logic_extractor_node
from src.graph.nodes.quant_engine     import quant_execution_node
from src.graph.nodes.validator        import validator_node
from src.graph.nodes.document_auditor import document_auditor_node


def build_frtb_graph():
    """Build and compile the linear FRTB-SA LangGraph application."""
    graph = StateGraph(AgentState)

    # Register nodes
    graph.add_node("audit_document", document_auditor_node)
    graph.add_node("retrieve",       retriever_node)
    graph.add_node("extract_logic",  logic_extractor_node)
    graph.add_node("execute_quant",  quant_execution_node)
    graph.add_node("validate",       validator_node)

    # Linear flow
    graph.set_entry_point("audit_document")
    graph.add_edge("audit_document", "retrieve")
    graph.add_edge("retrieve",       "extract_logic")
    graph.add_edge("extract_logic",  "execute_quant")
    graph.add_edge("execute_quant",  "validate")
    graph.add_edge("validate",       END)

    return graph.compile()
