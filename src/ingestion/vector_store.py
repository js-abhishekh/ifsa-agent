"""
src/ingestion/vector_store.py

ChromaDB wrapper for the FRTB regulatory clause vector store.

Collection metadata layout per chunk:
  - clause_id   : e.g. "21.4"
  - chapter     : e.g. "SBM_Delta_Vega"
  - risk_type   : e.g. "GIRR"
  - title       : clause heading text
  - part        : int (0-based sub-chunk index within a clause)
"""
from src.ingestion.chunker import Chunk
from src.config import CHROMA_DIR, CHROMA_COLLECTION, EMBED_MODEL

try:
    import chromadb
    from chromadb.utils import embedding_functions
    _CHROMA_AVAILABLE = True
except ImportError:
    _CHROMA_AVAILABLE = False


class RegulatoryStore:
    """Persistent ChromaDB vector store for FRTB regulatory clauses."""

    def __init__(
        self,
        persist_dir: str | None = None,
        collection_name: str | None = None,
        embed_model: str | None = None,
    ):
        persist_dir      = persist_dir      or str(CHROMA_DIR)
        collection_name  = collection_name  or CHROMA_COLLECTION
        embed_model      = embed_model      or EMBED_MODEL

        self._available = _CHROMA_AVAILABLE
        if not _CHROMA_AVAILABLE:
            print("[vector_store] WARNING: chromadb not installed — store unavailable. "
                  "Run: pip install chromadb sentence-transformers")
            self.collection = None
            return

        self.client = chromadb.PersistentClient(path=persist_dir)

        # Prefer BGE (high accuracy) → fall back to Chroma's built-in default
        # embedding (uses onnxruntime with all-MiniLM-L6-v2, no torch needed).
        try:
            self.embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name=embed_model
            )
            _ef_name = f"SentenceTransformer({embed_model})"
        except Exception:
            self.embed_fn = embedding_functions.DefaultEmbeddingFunction()
            _ef_name = "DefaultEmbeddingFunction (onnxruntime)"

        print(f"[vector_store] Embedding function: {_ef_name}")
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embed_fn,
            metadata={"hnsw:space": "cosine"},
        )

    # ── Write ──────────────────────────────────────────────────────────────────
    def upsert_chunks(self, chunks: list[Chunk]) -> None:
        """Upsert a batch of Chunk objects into the collection."""
        if not chunks or not self._available:
            return
        self.collection.upsert(
            ids=[c.chunk_id for c in chunks],
            documents=[c.text for c in chunks],
            metadatas=[
                {
                    "clause_id": c.clause_id or "",
                    "chapter":   c.chapter   or "",
                    "risk_type": c.risk_type or "",
                    **c.metadata,
                }
                for c in chunks
            ],
        )

    # ── Read ───────────────────────────────────────────────────────────────────
    def query(
        self,
        query_text: str,
        risk_type: str | None = None,
        chapter: str | None = None,
        n_results: int = 6,
    ) -> dict:
        """Semantic search with optional metadata pre-filtering.

        Returns the raw ChromaDB query result dict:
          {"documents": [[...]], "metadatas": [[...]], "distances": [[...]]}
        """
        where: dict = {}
        if risk_type and chapter:
            where = {"$and": [{"risk_type": risk_type}, {"chapter": chapter}]}
        elif risk_type:
            where = {"risk_type": risk_type}
        elif chapter:
            where = {"chapter": chapter}

        if not self._available or self.collection is None:
            return {"documents": [[]], "metadatas": [[]], "distances": [[]]}
        return self.collection.query(
            query_texts=[query_text],
            n_results=min(n_results, self.collection.count() or 1),
            where=where or None,
        )

    # ── Introspection ──────────────────────────────────────────────────────────
    def count(self) -> int:
        if not self._available or self.collection is None:
            return 0
        return self.collection.count()

    def peek(self, n: int = 5) -> dict:
        if not self._available or self.collection is None:
            return {}
        return self.collection.peek(limit=n)
