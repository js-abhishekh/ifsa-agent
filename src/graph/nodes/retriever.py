"""
src/graph/nodes/retriever.py

LangGraph Node A — Regulatory Document Retriever.

For each unique risk class present in the portfolio, issues one semantic
query to ChromaDB and collects the top-N most relevant regulatory clauses.
Results are stored in state["retrieved_regulatory_nodes"].
"""
from src.graph.state import AgentState, RegulatoryNode
import threading
from src.ingestion.vector_store import RegulatoryStore

# Singleton store — initialised once at import time to avoid repeated
# ChromaDB client construction on every node invocation.
_store: RegulatoryStore | None = None
_store_lock = threading.Lock()


def _get_store() -> RegulatoryStore:
    global _store
    with _store_lock:
        if _store is None:
            print("[retriever] Initializing RegulatoryStore (this may take a moment to download embedding model weights)...", flush=True)
            _store = RegulatoryStore()
            print("[retriever] RegulatoryStore successfully initialized!", flush=True)
        return _store


# Query templates per risk class — verbose enough to hit clause-level headers
_QUERY_TEMPLATES: dict[str, str] = {
    "GIRR":       "GIRR interest rate risk weight tenor bucket correlation delta vega curvature standardised approach MAR21",
    "CSR_NonSec": "CSR non-securitisation credit spread risk weight bucket correlation delta vega MAR21",
    "CSR_Sec":    "CSR securitisation correlation trading book risk weight bucket MAR21",
    "Equity":     "Equity risk weight bucket large-cap small-cap EM DM correlation delta vega MAR21",
    "Commodity":  "Commodity risk weight bucket energy freight metal grain correlation delta vega MAR21",
    "FX":         "FX foreign exchange risk weight correlation delta vega standardised approach MAR21",
}


async def retriever_node(state: AgentState) -> AgentState:
    """Retrieve relevant regulatory clauses for all portfolio risk classes.

    Augments state with:
        retrieved_regulatory_nodes: list[RegulatoryNode]
    """
    import asyncio
    positions = state.get("portfolio_inputs", [])
    risk_classes = {p.risk_class for p in positions}

    # If no portfolio positions exist, skip ChromaDB query entirely
    if not risk_classes:
        print("[retriever] No positions in portfolio; skipping regulatory rule retrieval.", flush=True)
        state["retrieved_regulatory_nodes"] = []
        return state

    store = await asyncio.to_thread(_get_store)
    nodes: list[RegulatoryNode] = []

    store_count = await asyncio.to_thread(store.count)
    if store_count > 0:
        for rc in risk_classes:
            query = _QUERY_TEMPLATES.get(rc, f"{rc} risk weight bucket correlation standardised approach")
            try:
                results = await asyncio.to_thread(store.query, query_text=query, risk_type=rc, n_results=6)
            except Exception as e:
                print(f"[retriever] Warning: query for {rc} failed with error: {e}", flush=True)
                continue

            docs   = results.get("documents", [[]])[0]
            metas  = results.get("metadatas", [[]])[0]
            dists  = results.get("distances",  [[]])[0]

            for doc, meta, dist in zip(docs, metas, dists):
                nodes.append(RegulatoryNode(
                    clause_id=meta.get("clause_id", "unknown"),
                    chapter=meta.get("chapter",   "unknown"),
                    risk_type=meta.get("risk_type", rc),
                    text=doc,
                    relevance_score=round(1.0 - dist, 4),
                ))

    state["retrieved_regulatory_nodes"] = nodes
    return state
