# IFSA FRTB-SA Agentic Auditor

An autonomous regulatory compliance audit and capital calculation engine built for the **Fundamental Review of the Trading Book Standardised Approach (FRTB-SA / BCBS 352)**.

The system processes bank disclosure PDFs and trading book portfolios, audits regulatory reporting against Basel III / IFSA standards, resolves risk weights and correlation matrices using a hybrid vector-retrieval / LLM pipeline, and deterministically computes SBM capital charges across GIRR, CSR, Equity, FX, and Commodity risk classes.

---

## Architecture & Pipeline Execution

```
[ Bank PDF / Portfolio JSON ]
              │
              ▼
   [ backend/routers/upload.py ] ──► Regex Scanners & PyMuPDF Worker
              │
              ▼
   [ src/graph/build_graph.py ] (LangGraph StateGraph)
        │
        ├─► 1. audit_document   (Extracts text, flags reporting violations)
        │
        ├─► 2. retrieve         (ChromaDB semantic search for Basel MAR clauses)
        │
        ├─► 3. extract_logic    (Pydantic-structured LLM extraction + static Annex fallbacks)
        │
        ├─► 4. execute_quant    (Deterministic NumPy SBM Delta/Vega/Curvature core)
        │
        └─► 5. validate         (Cross-bucket mathematical validation & bounds check)
              │
              ▼
    [ backend/routers/stream.py ] ──► SSE Event Stream (sse-starlette)
              │
              ▼
    [ frontend/app/run/[runId]/page.tsx ] (Next.js 16 + React 19 Workspace)
```

The pipeline separates non-deterministic language extraction from deterministic financial arithmetic:

1. **Document Ingestion & Disclosure Parsing**: When a PDF is uploaded via [backend/routers/upload.py](backend/routers/upload.py), [backend/services/pdf_extractor.py](backend/services/pdf_extractor.py) uses [PyMuPDF](https://pymupdf.readthedocs.io/) to parse raw text streams. It filters market risk sections using regex heuristics (`girr`, `pv01`, `capital charge`, `sbm`, `tenor`) before generating structured `PortfolioPosition` records.
2. **Document Auditing (`audit_document`)**: Defined in [src/graph/nodes/document_auditor.py](src/graph/nodes/document_auditor.py), this node cross-checks bank disclosures against Basel compliance requirements, flagging missing risk classes, unhedged positions, or non-compliant disclosures.
3. **Regulatory Clause Retrieval (`retrieve`)**: [src/graph/nodes/retriever.py](src/graph/nodes/retriever.py) queries an embedded [ChromaDB](https://www.trychroma.com/) collection to find relevant Basel MAR regulatory paragraphs for the portfolio's active risk classes.
4. **Parameter Extraction (`extract_logic`)**: In [src/graph/nodes/logic_extractor.py](src/graph/nodes/logic_extractor.py), LLM calls extract risk weights and intra-bucket correlations into Pydantic models. If API credentials are not provided or extraction fails, it falls back to the static regulatory Annex tables in [src/quant/risk_weights.py](src/quant/risk_weights.py).
5. **Deterministic Quant Engine (`execute_quant`)**: Implemented in [src/graph/nodes/quant_engine.py](src/graph/nodes/quant_engine.py) and [src/quant/](src/quant/), all financial calculations execute in pure Python/NumPy without LLM involvement:
   - **SBM Delta**: [src/quant/sbm_delta.py](src/quant/sbm_delta.py) computes net weighted sensitivities ($WS_k$), intra-bucket aggregation ($K_b = \sqrt{\sum_k WS_k^2 + \sum_{k \neq l} \rho_{kl} WS_k WS_l}$), and inter-bucket aggregation across correlation matrix $\gamma_{bc}$.
   - **SBM Vega & Curvature**: [src/quant/sbm_vega.py](src/quant/sbm_vega.py) and [src/quant/sbm_curvature.py](src/quant/sbm_curvature.py) aggregate optionality and non-linear delta shifts.
   - **Default Risk Charge (DRC) & RRAO**: [src/quant/drc.py](src/quant/drc.py) and [src/quant/rrao.py](src/quant/rrao.py) apply jump-to-default and residual risk add-ons.
6. **Integrity Validation (`validate`)**: [src/graph/nodes/validator.py](src/graph/nodes/validator.py) checks calculated metrics against Basel boundary conditions (such as correlation matrix positive semi-definiteness and variance bounds).
7. **Real-time Event Streaming**: Node transitions, execution logs, and audit flags are dispatched to an in-memory queue in [backend/services/run_store.py](backend/services/run_store.py) and streamed to the UI over HTTP SSE via [backend/routers/stream.py](backend/routers/stream.py).

---

## Notable Implementation Techniques

- **Server-Sent Events (SSE) with Connection Keepalives**: Real-time pipeline events stream through [backend/routers/stream.py](backend/routers/stream.py) using an async generator and 10-second timeout pings to prevent network timeouts, consumed client-side using the [EventSource API](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) via [frontend/hooks/usePipelineSSE.ts](frontend/hooks/usePipelineSSE.ts).
- **Asynchronous Execution & Event Queues**: Utilizes Python's native [asyncio.wait_for](https://docs.python.org/3/library/asyncio-task.html) and [async generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*) to bridge synchronous quant functions with concurrent SSE consumers.
- **HTML5 Drag-and-Drop Ingestion**: Built directly on native browser events ([dragover](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragover_event), [dragleave](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragleave_event), and [drop](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/drop_event)) in [frontend/app/page.tsx](frontend/app/page.tsx) to handle raw PDF stream handoffs without third-party wrapper components.
- **Targeted Font Subsetting with `unicode-range`**: In [frontend/app/globals.css](frontend/app/globals.css), `@font-face` declarations use [unicode-range](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/unicode-range) (`U+0030-0039, U+002C, U+002E...`) to render numbers in Inter for tabular legibility while displaying labels in Milligram.
- **Font Rendering Optimization**: Employs [font-display: swap](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) combined with local fallback definitions (`local("MilligramTrial")`, `local("Inter")`) to eliminate Flash of Invisible Text (FOIT) during client-side hydration.
- **Client Session Isolation & Parameter Forwarding**: Encodes extracted portfolio state into URL query strings with [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) and caches immutable audit results in [sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) across Next.js dynamic routing hops ([frontend/app/run/[runId]/page.tsx](frontend/app/run/[runId]/page.tsx)).
- **CSS Custom Properties Design Tokens**: Leverages [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) declared in [frontend/app/globals.css](frontend/app/globals.css) and [DESIGN.md](DESIGN.md) to implement the high-contrast editorial aesthetic specified in the design guide.

---

## Core Libraries & Technologies

- **[LangGraph](https://langchain-ai.github.io/langgraph/)**: Coordinates execution state, node progression, and checkpointing for the multi-step regulatory workflow.
- **[FastAPI](https://fastapi.tiangolo.com/) & [Uvicorn](https://www.uvicorn.org/)**: Asynchronous Python API gateway serving REST endpoints and SSE channels.
- **[sse-starlette](https://github.com/sysid/sse-starlette)**: ASGI-compliant Server-Sent Events utility powering the real-time event pipeline.
- **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)**: High-performance C-backed PDF engine used for targeted text and tabular disclosure extraction.
- **[ChromaDB](https://www.trychroma.com/)**: Embedded vector database storing partitioned Basel III MAR text embeddings.
- **[Pydantic v2](https://docs.pydantic.dev/)**: Performs strict schema enforcement on LLM-extracted regulatory parameters and portfolio positions.
- **[Next.js 16](https://nextjs.org/) & [React 19](https://react.dev/)**: Frontend application framework configured with the App Router, client-side hydration, and dynamic route segments.
- **[Recharts](https://recharts.org/)**: Declarative chart library used to visualize cross-bucket risk distributions and sensitivity matrices.
- **[Lucide React](https://lucide.dev/)**: Icon set used across pipeline navigation rails and status indicators.
- **[Milligram Typography](https://www.futurefonts.xyz/valerio-monaco/milligram)**: Editorial display typeface bundled in [frontend/public/fonts/](frontend/public/fonts/) (`Regular`, `Medium`, `Bold`, and `Compressed` cuts).
- **[Inter](https://fonts.google.com/specimen/Inter)**: Variable sans-serif font applied to numbers, data grids, and UI system elements.

---

## Project Structure

```text
ifsa-agent/
├── .dockerignore
├── .env.example
├── .gitignore
├── DESIGN.md
├── Dockerfile
├── docker-compose.yml
├── frtb_langgraph_guide.md
├── requirements.txt
├── run_pipeline.py
├── start.sh
├── backend/
│   ├── routers/
│   └── services/
├── data/
│   ├── chroma_db/
│   ├── marker_output/
│   ├── raw_pdfs/
│   └── uploads/
├── frontend/
│   ├── app/
│   │   └── run/
│   │       └── [runId]/
│   │           └── results/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   └── public/
│       └── fonts/
├── scripts/
├── src/
│   ├── graph/
│   │   └── nodes/
│   ├── ingestion/
│   └── quant/
└── tests/
```

### Directory Descriptions

- **[backend/](backend/)**: FastAPI server code. Contains route definitions in [backend/routers/](backend/routers/) (upload, run triggers, SSE streaming) and state management in [backend/services/](backend/services/).
- **[data/](data/)**: Document store containing regulatory PDFs, vector index files, sample test portfolios, and ephemeral user uploads.
- **[frontend/](frontend/)**: Next.js 16 application containing App Router pages, pipeline inspection panels in `frontend/components/`, data models in `frontend/lib/`, and custom Milligram typefaces in `frontend/public/fonts/`.
- **[src/graph/](src/graph/)**: LangGraph orchestration engine. Defines pipeline state models ([src/graph/state.py](src/graph/state.py)), graph assembly ([src/graph/build_graph.py](src/graph/build_graph.py)), and isolated node handlers in [src/graph/nodes/](src/graph/nodes/).
- **[src/ingestion/](src/ingestion/)**: Document processing modules for PDF markdown conversion, text chunking, and ChromaDB vector indexing.
- **[src/quant/](src/quant/)**: Pure-Python quant calculation engine covering SBM Delta, Vega, Curvature, Default Risk Charge (DRC), Residual Risk Add-On (RRAO), and static Basel III regulatory lookup tables.
- **[tests/](tests/)**: Unit and integration test suite covering quantitative formulas, edge-case correlation matrices, and logic extractors.
