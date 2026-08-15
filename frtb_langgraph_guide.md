# FRTB-SA Agentic Pipeline: Implementation Blueprint
### Marker → ChromaDB → LangGraph, deterministic quant core

This guide treats the LLM strictly as a **retrieval and structuring layer**. All arithmetic — bucket-level Delta/Vega/Curvature aggregation, correlation matrices, DRC banding, RRAO add-ons — is executed in pure, unit-tested Python. The graph exists to orchestrate *which clause maps to which calculation*, not to do the calculation.

---

## 0. Directory Structure

```
frtb-agent/
├── data/
│   ├── raw_pdfs/                  # source RBI/BCBS FRTB circulars
│   ├── marker_output/             # markdown + extracted images/tables
│   └── chroma_db/                 # persistent vector store
├── src/
│   ├── ingestion/
│   │   ├── run_marker.py
│   │   ├── chunker.py
│   │   └── vector_store.py
│   ├── graph/
│   │   ├── state.py
│   │   ├── nodes/
│   │   │   ├── retriever.py
│   │   │   ├── logic_extractor.py
│   │   │   ├── quant_engine.py
│   │   │   └── validator.py
│   │   ├── routing.py
│   │   └── build_graph.py
│   ├── quant/
│   │   ├── sbm_delta.py
│   │   ├── sbm_vega.py
│   │   ├── sbm_curvature.py
│   │   ├── drc.py
│   │   ├── rrao.py
│   │   └── risk_weights.py        # static regulatory tables (Basel Annex)
│   └── config.py
├── tests/
│   └── test_quant_core.py
├── run_pipeline.py                # CLI entrypoint (Step 5)
├── requirements.txt
└── .env
```

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install marker-pdf chromadb langgraph langchain-core langchain-openai \
            pydantic sentence-transformers tiktoken numpy python-dotenv
```

---

## Step 1 — Document Ingestion & Chunking

### 1.1 Run Marker on an isolated test chapter first

Don't index the whole manual on the first pass. Slice a 5–10 page chapter (e.g., "Delta and Vega Risk Charge" section) with a PDF tool (`pikepdf` / `qpdf`) and run Marker against just that.

```bash
pip install marker-pdf
marker_single data/raw_pdfs/frtb_sbm_chapter.pdf \
    data/marker_output/ \
    --batch_multiplier 2 \
    --langs English
```

This produces `frtb_sbm_chapter/frtb_sbm_chapter.md` plus an `images/` folder. Marker preserves table structure as Markdown pipe-tables and keeps LaTeX-like inline formulas reasonably intact — but **always manually diff 2–3 pages against the source PDF** before trusting it on the full document. Regulatory formula subscripts (e.g., $\rho_{kl}$) are the most common corruption point.

### 1.2 Structure-aware chunker

Naive fixed-token chunking will slice a table or a formula block in half. The chunker below walks the Markdown AST-style using regex-delimited "protected blocks" (tables, fenced code/math blocks) and never splits inside one.

```python
# src/ingestion/chunker.py
import re
from dataclasses import dataclass, field
from typing import List

@dataclass
class Chunk:
    text: str
    chunk_id: str
    clause_id: str | None = None
    chapter: str | None = None
    risk_type: str | None = None
    metadata: dict = field(default_factory=dict)

TABLE_BLOCK = re.compile(r"(\|.+\|\n\|[-:| ]+\|\n(?:\|.+\|\n?)+)")
MATH_BLOCK = re.compile(r"(\$\$.+?\$\$)", re.DOTALL)
CLAUSE_HEADER = re.compile(r"^(#{1,4})\s*(?:Para(?:graph)?\s*)?(\d+[\.\d]*)\s*(.*)$", re.MULTILINE)

MAX_TOKENS = 500  # heuristic; ~4 chars/token
CHARS_PER_TOKEN = 4

def _protect_blocks(md_text: str) -> tuple[str, dict]:
    """Replace tables/math with placeholders so splitting logic ignores their internal newlines."""
    placeholders = {}
    def _stash(match, prefix):
        key = f"__{prefix}_{len(placeholders)}__"
        placeholders[key] = match.group(0)
        return key

    md_text = TABLE_BLOCK.sub(lambda m: _stash(m, "TABLE"), md_text)
    md_text = MATH_BLOCK.sub(lambda m: _stash(m, "MATH"), md_text)
    return md_text, placeholders

def _restore(text: str, placeholders: dict) -> str:
    for key, original in placeholders.items():
        text = text.replace(key, original)
    return text

def chunk_markdown(md_text: str, chapter: str, risk_type: str) -> List[Chunk]:
    protected_text, placeholders = _protect_blocks(md_text)

    # split on clause-level headers so each chunk maps to a citable clause_id
    sections = CLAUSE_HEADER.split(protected_text)
    chunks: List[Chunk] = []

    # sections list layout after re.split with 3 groups: [preamble, hlevel, clause_id, title, body, hlevel, ...]
    idx = 0
    preamble = sections[0]
    i = 1
    while i < len(sections):
        hlevel, clause_id, title = sections[i], sections[i+1], sections[i+2]
        body = sections[i+3] if i + 3 < len(sections) else ""
        i += 4

        full_body = _restore(body, placeholders)
        sub_chunks = _split_by_length(full_body, clause_id, title)

        for j, sc in enumerate(sub_chunks):
            chunks.append(Chunk(
                text=f"### {clause_id} {title}\n{sc}",
                chunk_id=f"{chapter}_{clause_id}_{j}",
                clause_id=clause_id,
                chapter=chapter,
                risk_type=risk_type,
                metadata={"title": title.strip(), "part": j}
            ))
        idx += 1

    return chunks

def _split_by_length(body: str, clause_id: str, title: str) -> List[str]:
    """Split long clause bodies on paragraph boundaries, never mid-table/mid-formula
    (tables/math were already restored to full text, so we treat them as atomic
    by refusing to split lines that start inside a '|' table or '$$' block)."""
    max_chars = MAX_TOKENS * CHARS_PER_TOKEN
    if len(body) <= max_chars:
        return [body]

    paragraphs = body.split("\n\n")
    out, current = [], ""
    for p in paragraphs:
        is_atomic = p.strip().startswith("|") or p.strip().startswith("$$")
        if is_atomic:
            # never break an atomic block regardless of length
            if current:
                out.append(current)
                current = ""
            out.append(p)
            continue
        if len(current) + len(p) > max_chars and current:
            out.append(current)
            current = p
        else:
            current += ("\n\n" if current else "") + p
    if current:
        out.append(current)
    return out
```

### 1.3 Embedding + ChromaDB storage with metadata filtering

```python
# src/ingestion/vector_store.py
import chromadb
from chromadb.utils import embedding_functions
from src.ingestion.chunker import Chunk

class RegulatoryStore:
    def __init__(self, persist_dir: str = "data/chroma_db",
                 collection_name: str = "frtb_sa_clauses",
                 embed_model: str = "BAAI/bge-large-en-v1.5"):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=embed_model)
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embed_fn,
            metadata={"hnsw:space": "cosine"}
        )

    def upsert_chunks(self, chunks: list[Chunk]):
        self.collection.upsert(
            ids=[c.chunk_id for c in chunks],
            documents=[c.text for c in chunks],
            metadatas=[{
                "clause_id": c.clause_id or "",
                "chapter": c.chapter or "",
                "risk_type": c.risk_type or "",
                **c.metadata
            } for c in chunks]
        )

    def query(self, query_text: str, risk_type: str | None = None,
              chapter: str | None = None, n_results: int = 6):
        where = {}
        if risk_type:
            where["risk_type"] = risk_type
        if chapter:
            where["chapter"] = chapter
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results,
            where=where or None
        )
```

Ingestion driver:

```python
# src/ingestion/run_marker.py (orchestration wrapper, not the CLI itself)
import subprocess
from pathlib import Path
from src.ingestion.chunker import chunk_markdown
from src.ingestion.vector_store import RegulatoryStore

def ingest_chapter(pdf_path: str, chapter: str, risk_type: str):
    out_dir = Path("data/marker_output") / chapter
    subprocess.run(["marker_single", pdf_path, str(out_dir)], check=True)

    md_file = next(out_dir.rglob("*.md"))
    md_text = md_file.read_text(encoding="utf-8")

    chunks = chunk_markdown(md_text, chapter=chapter, risk_type=risk_type)
    store = RegulatoryStore()
    store.upsert_chunks(chunks)
    print(f"Ingested {len(chunks)} chunks from {chapter}")

if __name__ == "__main__":
    ingest_chapter("data/raw_pdfs/frtb_sbm_chapter.pdf", chapter="SBM_Delta_Vega", risk_type="GIRR")
```

---

## Step 2 — LangGraph State Definition

Use Pydantic (not bare `TypedDict`) so malformed LLM output fails validation immediately rather than silently propagating bad numbers into the quant engine.

```python
# src/graph/state.py
from typing import Literal, Optional
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

RiskClass = Literal["GIRR", "CSR_NonSec", "CSR_Sec", "Equity", "Commodity", "FX"]

class PortfolioPosition(BaseModel):
    instrument_id: str
    risk_class: RiskClass
    bucket: str
    risk_factor: str            # e.g. tenor "5Y", equity name, commodity type
    sensitivity: float          # PV01, vega sensitivity, etc.
    notional: Optional[float] = None
    currency: str = "USD"

class RegulatoryNode(BaseModel):
    clause_id: str
    chapter: str
    risk_type: str
    text: str
    relevance_score: float

class CalculationParameter(BaseModel):
    param_name: str             # e.g. "risk_weight_GIRR_5Y"
    value: float
    source_clause_id: str
    confidence: float

class ExtractedLogic(BaseModel):
    risk_class: RiskClass
    formula_ref: str            # e.g. "Kb aggregation, para 21.3"
    risk_weights: dict[str, float] = Field(default_factory=dict)
    correlations: dict[str, float] = Field(default_factory=dict)   # "rho_kl" keys
    parameters: list[CalculationParameter] = Field(default_factory=list)
    is_complete: bool = False
    missing_fields: list[str] = Field(default_factory=list)

class CalculatedMetric(BaseModel):
    risk_class: RiskClass
    metric_name: Literal["delta_charge", "vega_charge", "curvature_charge", "drc_charge", "rrao_charge"]
    bucket_level: dict[str, float] = Field(default_factory=dict)
    aggregated_value: float
    formula_used: str

class ValidationError(BaseModel):
    severity: Literal["blocking", "warning"]
    node: str
    message: str

class AgentState(TypedDict, total=False):
    user_query: str
    portfolio_inputs: list[PortfolioPosition]
    retrieved_regulatory_nodes: list[RegulatoryNode]
    extracted_calculation_logic: list[ExtractedLogic]
    calculated_metrics: list[CalculatedMetric]
    validation_errors: list[ValidationError]
    final_compliance_summary: Optional[str]
    retry_count: int
    max_retries: int
```

---

## Step 3 — Graph Nodes

### Node A — Retriever

```python
# src/graph/nodes/retriever.py
from src.graph.state import AgentState, RegulatoryNode
from src.ingestion.vector_store import RegulatoryStore

store = RegulatoryStore()

def retriever_node(state: AgentState) -> AgentState:
    positions = state["portfolio_inputs"]
    risk_classes = {p.risk_class for p in positions}

    nodes: list[RegulatoryNode] = []
    for rc in risk_classes:
        query = f"{rc} risk weight bucket correlation delta vega curvature standardized approach"
        results = store.query(query_text=query, risk_type=rc, n_results=5)

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        dists = results["distances"][0]

        for doc, meta, dist in zip(docs, metas, dists):
            nodes.append(RegulatoryNode(
                clause_id=meta.get("clause_id", "unknown"),
                chapter=meta.get("chapter", "unknown"),
                risk_type=meta.get("risk_type", rc),
                text=doc,
                relevance_score=1 - dist,
            ))

    state["retrieved_regulatory_nodes"] = nodes
    return state
```

### Node B — Logic & Parameter Extractor (structured LLM output)

```python
# src/graph/nodes/logic_extractor.py
import json
from src.graph.state import AgentState, ExtractedLogic, CalculationParameter
from langchain_openai import ChatOpenAI  # swap for your provider

llm = ChatOpenAI(model="gpt-4o", temperature=0)

EXTRACTION_SYSTEM_PROMPT = """You are a regulatory parameter extraction engine for FRTB-SA.
Given regulatory clause text, extract ONLY explicitly stated numeric risk weights,
correlation parameters (rho), and bucket definitions. Do NOT infer or estimate values
that are not explicitly present in the text. Return strict JSON matching this schema:

{
  "risk_class": "<GIRR|CSR_NonSec|CSR_Sec|Equity|Commodity|FX>",
  "formula_ref": "<clause id / description>",
  "risk_weights": {"<bucket_or_tenor>": <float>},
  "correlations": {"<rho_key>": <float>},
  "parameters": [{"param_name": "...", "value": <float>, "source_clause_id": "...", "confidence": <0-1>}],
  "is_complete": <bool>,
  "missing_fields": ["..."]
}

Set is_complete=false and list missing_fields if the clause text does not contain
enough numeric detail to run the calculation for that risk class."""

def logic_extractor_node(state: AgentState) -> AgentState:
    grouped: dict[str, list[str]] = {}
    for node in state["retrieved_regulatory_nodes"]:
        grouped.setdefault(node.risk_type, []).append(node.text)

    extracted: list[ExtractedLogic] = []
    for risk_class, texts in grouped.items():
        combined_text = "\n\n---\n\n".join(texts)
        response = llm.invoke([
            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
            {"role": "user", "content": f"Risk class: {risk_class}\n\nClause text:\n{combined_text}"}
        ])
        try:
            payload = json.loads(response.content)
            payload["parameters"] = [CalculationParameter(**p) for p in payload.get("parameters", [])]
            extracted.append(ExtractedLogic(**payload))
        except Exception as e:
            extracted.append(ExtractedLogic(
                risk_class=risk_class, formula_ref="parse_error",
                is_complete=False, missing_fields=[f"json_parse_error: {e}"]
            ))

    state["extracted_calculation_logic"] = extracted
    return state
```

### Node C — Quant Execution Node (deterministic, pure Python)

The math never touches the LLM. Example: SBM Delta risk charge aggregation per Basel MAR21.

```python
# src/quant/sbm_delta.py
import math
from src.graph.state import PortfolioPosition, ExtractedLogic, CalculatedMetric

def compute_weighted_sensitivities(positions: list[PortfolioPosition],
                                    risk_weights: dict[str, float]) -> dict[str, float]:
    """WS_k = risk_factor_sensitivity * risk_weight_k"""
    ws = {}
    for p in positions:
        rw = risk_weights.get(p.risk_factor) or risk_weights.get(p.bucket)
        if rw is None:
            raise KeyError(f"No risk weight found for {p.risk_factor} / bucket {p.bucket}")
        ws[p.instrument_id] = p.sensitivity * rw
    return ws

def bucket_kb(positions: list[PortfolioPosition], weighted_sens: dict[str, float],
              correlations: dict[str, float]) -> float:
    """
    Kb = sqrt( max(0, sum(WS_k^2) + sum_{k != l} rho_kl * WS_k * WS_l) )
    Basel MAR21.4 (SBM Delta bucket aggregation formula).
    """
    ids = [p.instrument_id for p in positions]
    sum_sq = sum(weighted_sens[i] ** 2 for i in ids)

    cross_term = 0.0
    for k_idx, k in enumerate(ids):
        for l_idx, l in enumerate(ids):
            if k_idx >= l_idx:
                continue
            rho_key = f"{positions[k_idx].risk_factor}_{positions[l_idx].risk_factor}"
            rho = correlations.get(rho_key, correlations.get("default", 1.0))
            cross_term += 2 * rho * weighted_sens[k] * weighted_sens[l]

    inner = sum_sq + cross_term
    return math.sqrt(max(inner, 0.0))

def sbm_delta_charge(positions: list[PortfolioPosition], logic: ExtractedLogic) -> CalculatedMetric:
    by_bucket: dict[str, list[PortfolioPosition]] = {}
    for p in positions:
        by_bucket.setdefault(p.bucket, []).append(p)

    bucket_charges: dict[str, float] = {}
    for bucket, bucket_positions in by_bucket.items():
        ws = compute_weighted_sensitivities(bucket_positions, logic.risk_weights)
        bucket_charges[bucket] = bucket_kb(bucket_positions, ws, logic.correlations)

    # Cross-bucket aggregation: sqrt(sum(Kb^2) + sum gamma_bc * Sb * Sc), simplified here
    # to a conservative sum-of-squares roll-up when cross-bucket gamma is not extracted.
    gamma_default = logic.correlations.get("gamma_bc", 0.0)
    kb_values = list(bucket_charges.values())
    sum_sq = sum(k ** 2 for k in kb_values)
    cross = 0.0
    for i in range(len(kb_values)):
        for j in range(i + 1, len(kb_values)):
            cross += 2 * gamma_default * kb_values[i] * kb_values[j]
    aggregated = math.sqrt(max(sum_sq + cross, 0.0))

    return CalculatedMetric(
        risk_class=logic.risk_class,
        metric_name="delta_charge",
        bucket_level=bucket_charges,
        aggregated_value=aggregated,
        formula_used="MAR21.4 Kb aggregation"
    )
```

```python
# src/graph/nodes/quant_engine.py
from src.graph.state import AgentState, CalculatedMetric
from src.quant.sbm_delta import sbm_delta_charge

def quant_execution_node(state: AgentState) -> AgentState:
    metrics: list[CalculatedMetric] = []
    errors = state.get("validation_errors", [])

    for logic in state["extracted_calculation_logic"]:
        if not logic.is_complete:
            continue  # validator node handles the missing-params branch
        positions = [p for p in state["portfolio_inputs"] if p.risk_class == logic.risk_class]
        if not positions:
            continue
        try:
            metrics.append(sbm_delta_charge(positions, logic))
            # sbm_vega_charge(...) / sbm_curvature_charge(...) follow the same pattern
        except KeyError as e:
            from src.graph.state import ValidationError
            errors.append(ValidationError(severity="blocking", node="quant_engine",
                                           message=f"{logic.risk_class}: {e}"))

    state["calculated_metrics"] = metrics
    state["validation_errors"] = errors
    return state
```

### Node D — Validation & Audit Node

```python
# src/graph/nodes/validator.py
from src.graph.state import AgentState, ValidationError

def validator_node(state: AgentState) -> AgentState:
    errors = list(state.get("validation_errors", []))

    incomplete = [l for l in state["extracted_calculation_logic"] if not l.is_complete]
    for logic in incomplete:
        errors.append(ValidationError(
            severity="blocking",
            node="logic_extractor",
            message=f"{logic.risk_class} incomplete: missing {logic.missing_fields}"
        ))

    covered_classes = {m.risk_class for m in state.get("calculated_metrics", [])}
    required_classes = {p.risk_class for p in state["portfolio_inputs"]}
    for rc in required_classes - covered_classes:
        errors.append(ValidationError(
            severity="blocking", node="quant_engine",
            message=f"No calculated metric produced for risk class {rc}"
        ))

    state["validation_errors"] = errors

    if not any(e.severity == "blocking" for e in errors):
        totals = ", ".join(f"{m.risk_class}/{m.metric_name}: {m.aggregated_value:.2f}"
                            for m in state["calculated_metrics"])
        state["final_compliance_summary"] = f"PASS — {totals}"
    return state
```

---

## Step 4 — Graph Wiring & Conditional Routing

```python
# src/graph/routing.py
from src.graph.state import AgentState

def route_after_validation(state: AgentState) -> str:
    blocking = [e for e in state.get("validation_errors", []) if e.severity == "blocking"]
    if not blocking:
        return "end"

    retry_count = state.get("retry_count", 0)
    max_retries = state.get("max_retries", 2)
    if retry_count >= max_retries:
        return "request_missing_inputs"

    # if the failure originated at extraction (missing regulatory detail), loop back
    # to retrieval with a broader query; if it's a portfolio-input problem, escalate.
    extraction_failures = [e for e in blocking if e.node == "logic_extractor"]
    if extraction_failures:
        return "retry_retrieval"
    return "request_missing_inputs"
```

```python
# src/graph/build_graph.py
from langgraph.graph import StateGraph, END
from src.graph.state import AgentState
from src.graph.nodes.retriever import retriever_node
from src.graph.nodes.logic_extractor import logic_extractor_node
from src.graph.nodes.quant_engine import quant_execution_node
from src.graph.nodes.validator import validator_node
from src.graph.routing import route_after_validation

def _increment_retry(state: AgentState) -> AgentState:
    state["retry_count"] = state.get("retry_count", 0) + 1
    return state

def _request_missing_inputs(state: AgentState) -> AgentState:
    missing = [e.message for e in state["validation_errors"] if e.severity == "blocking"]
    state["final_compliance_summary"] = (
        "INCOMPLETE — manual input required:\n" + "\n".join(f"- {m}" for m in missing)
    )
    return state

def build_frtb_graph():
    graph = StateGraph(AgentState)

    graph.add_node("retrieve", retriever_node)
    graph.add_node("extract_logic", logic_extractor_node)
    graph.add_node("execute_quant", quant_execution_node)
    graph.add_node("validate", validator_node)
    graph.add_node("retry_bump", _increment_retry)
    graph.add_node("request_missing_inputs", _request_missing_inputs)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "extract_logic")
    graph.add_edge("extract_logic", "execute_quant")
    graph.add_edge("execute_quant", "validate")

    graph.add_conditional_edges(
        "validate",
        route_after_validation,
        {
            "end": END,
            "retry_retrieval": "retry_bump",
            "request_missing_inputs": "request_missing_inputs",
        }
    )
    graph.add_edge("retry_bump", "retrieve")
    graph.add_edge("request_missing_inputs", END)

    return graph.compile()
```

---

## Step 5 — Sample Run

```python
# run_pipeline.py
from src.graph.build_graph import build_frtb_graph
from src.graph.state import PortfolioPosition

def mock_irs_portfolio() -> list[PortfolioPosition]:
    return [
        PortfolioPosition(instrument_id="IRS_001", risk_class="GIRR", bucket="USD",
                           risk_factor="5Y", sensitivity=125_000.0, currency="USD"),
        PortfolioPosition(instrument_id="IRS_002", risk_class="GIRR", bucket="USD",
                           risk_factor="10Y", sensitivity=-80_000.0, currency="USD"),
        PortfolioPosition(instrument_id="EQOPT_001", risk_class="Equity", bucket="EM_LargeCap",
                           risk_factor="RELIANCE", sensitivity=45_000.0, currency="INR"),
    ]

if __name__ == "__main__":
    app = build_frtb_graph()

    initial_state = {
        "user_query": "Compute FRTB-SA Delta risk charge for the attached IRS + Equity option book",
        "portfolio_inputs": mock_irs_portfolio(),
        "retry_count": 0,
        "max_retries": 2,
    }

    final_state = app.invoke(initial_state)

    print("\n=== FINAL COMPLIANCE SUMMARY ===")
    print(final_state.get("final_compliance_summary"))

    print("\n=== CALCULATED METRICS ===")
    for m in final_state.get("calculated_metrics", []):
        print(f"{m.risk_class} | {m.metric_name} | aggregated={m.aggregated_value:,.2f}")
        print(f"  buckets: {m.bucket_level}")

    print("\n=== VALIDATION ERRORS ===")
    for e in final_state.get("validation_errors", []):
        print(f"[{e.severity.upper()}] ({e.node}) {e.message}")
```

```bash
python run_pipeline.py
```

Expected shape of output on a clean run:

```
=== FINAL COMPLIANCE SUMMARY ===
PASS — GIRR/delta_charge: 41230.55, Equity/delta_charge: 15750.00

=== CALCULATED METRICS ===
GIRR | delta_charge | aggregated=41,230.55
  buckets: {'USD': 41230.55}
Equity | delta_charge | aggregated=15,750.00
  buckets: {'EM_LargeCap': 15750.00}

=== VALIDATION ERRORS ===
```

On an incomplete run (e.g., risk weight missing from retrieved clause text), you'd instead see the graph loop through `retry_retrieval` up to `max_retries`, then fall through to `request_missing_inputs` with a specific, addressable message rather than a silent wrong number.

---

## Build Order & Notes

1. **Unit-test the quant core first, independent of the graph.** Write `tests/test_quant_core.py` against Basel worked examples (BCBS publishes SBM worked examples in the FRTB QIS documentation) before wiring any LLM node to it. If `sbm_delta_charge` is wrong, no amount of good retrieval fixes it.
2. **Pin the risk weight / correlation tables as a static fallback** (`src/quant/risk_weights.py`) sourced directly from the Basel Annex, and treat LLM-extracted parameters as *overrides that must match the static table within tolerance* — flag a `validation_error` if the extracted risk weight for a known bucket diverges from the regulatory table by more than a few bps. This catches Marker/OCR corruption and LLM hallucination in one check.
3. **Vega and Curvature nodes** (`sbm_vega.py`, `sbm_curvature.py`) follow the identical `compute_weighted_sensitivities` → `bucket_kb` → cross-bucket aggregation pattern; curvature additionally needs the up/down shock scenario values (`CVR_k^+`, `CVR_k^-`) as extra `PortfolioPosition` fields.
4. **DRC and RRAO** are structurally different (jump-to-default banding and residual add-on respectively, not correlation-based aggregation) — build them as separate node branches feeding into the same `calculated_metrics` list rather than trying to force them through `sbm_delta_charge`'s shape.
5. Once this passes deterministic tests end-to-end on the mock portfolio, that's the right point to add FastAPI/Streamlit — not before.
