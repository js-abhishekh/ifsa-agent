"""
Audit script: verify ChromaDB upsert integrity.
Run with: python scripts/audit_chroma.py
"""
import sys, collections
sys.path.insert(0, ".")

from src.ingestion.vector_store import RegulatoryStore

store = RegulatoryStore()
col   = store.collection

# ── 1. Count ──────────────────────────────────────────────────────────────────
total = col.count()
print(f"\n{'='*60}")
print(f"  ChromaDB Audit Report")
print(f"{'='*60}")
print(f"  Total vectors in collection : {total}")

# ── 2. Peek at raw metadata for first 10 docs ─────────────────────────────────
raw = col.peek(limit=10)
ids        = raw.get("ids", [])
metas      = raw.get("metadatas", [])
docs       = raw.get("documents", [])

print(f"\n--- Sample IDs (first 10) ---")
for i, (doc_id, meta) in enumerate(zip(ids, metas)):
    print(f"  [{i+1}] id={doc_id} | chapter={meta.get('chapter','?')} | "
          f"clause_id={meta.get('clause_id','?')} | risk_type={meta.get('risk_type','?')} | "
          f"page={meta.get('page','?')}")

# ── 3. Full metadata scan via batched get ─────────────────────────────────────
print(f"\n--- Full metadata scan (all {total} records) ---")
batch_size = 500
all_metas  = []
all_ids    = []

for offset in range(0, total, batch_size):
    result = col.get(
        limit=batch_size,
        offset=offset,
        include=["metadatas"]
    )
    all_metas.extend(result.get("metadatas", []))
    all_ids.extend(result.get("ids", []))

# ── 4. Breakdown by risk_type ─────────────────────────────────────────────────
risk_counts = collections.Counter(m.get("risk_type", "UNKNOWN") for m in all_metas)
print("\n  Breakdown by risk_type:")
for rt, cnt in sorted(risk_counts.items(), key=lambda x: -x[1]):
    print(f"    {rt:25s} : {cnt:5d} chunks")

# ── 5. Breakdown by chapter ────────────────────────────────────────────────────
chapter_counts = collections.Counter(m.get("chapter", "?") for m in all_metas)
mar_chapters = {k: v for k, v in chapter_counts.items() if k.startswith("MAR")}
print("\n  MAR chapter breakdown:")
for ch, cnt in sorted(mar_chapters.items()):
    print(f"    {ch:10s} : {cnt:4d} chunks")

# ── 6. Duplicate ID check ─────────────────────────────────────────────────────
dup_count = total - len(set(all_ids))
print(f"\n  Duplicate chunk IDs        : {dup_count}  {'(CLEAN)' if dup_count==0 else '(WARNING: duplicates found)'}")

# ── 7. Missing metadata field check ──────────────────────────────────────────
missing_clause = sum(1 for m in all_metas if not m.get("clause_id"))
missing_rt     = sum(1 for m in all_metas if not m.get("risk_type"))
missing_ch     = sum(1 for m in all_metas if not m.get("chapter"))
missing_page   = sum(1 for m in all_metas if not m.get("page"))
print(f"\n  Metadata completeness checks:")
print(f"    Missing clause_id          : {missing_clause}")
print(f"    Missing risk_type          : {missing_rt}")
print(f"    Missing chapter            : {missing_ch}")
print(f"    Missing page number        : {missing_page}")

# ── 8. Spot-check known MAR21 critical clauses ────────────────────────────────
print("\n  Spot-check: known MAR21 critical paragraphs --")
CRITICAL_PARAS = ["MAR21.44", "MAR21.71", "MAR21.54", "MAR21.81", "MAR21.88"]
found_ids = set(m.get("clause_id","") for m in all_metas)
for para in CRITICAL_PARAS:
    hits = [m for m in all_metas if para in m.get("clause_id","")]
    status = "FOUND" if hits else "MISSING"
    print(f"    {para:12s} -> {status} ({len(hits)} chunk(s))")

# ── 9. Semantic retrieval quality spot-check ──────────────────────────────────
print("\n  Semantic retrieval quality spot-checks --")
test_queries = [
    ("GIRR 5Y tenor risk weight interest rate",     "GIRR"),
    ("Equity bucket large-cap EM risk weight",       "Equity"),
    ("Default risk charge jump to default netting",  "DRC"),
    ("Residual risk add-on exotic underlying",       "RRAO"),
    ("CSR non-securitisation credit spread bucket",  "CSR_NonSec"),
]

for query_text, risk_type in test_queries:
    res = store.query(query_text, risk_type=risk_type, n_results=1)
    docs_r  = res.get("documents", [[]])[0]
    metas_r = res.get("metadatas", [[]])[0]
    dists_r = res.get("distances",  [[]])[0]
    if docs_r:
        m  = metas_r[0]
        score = round(1 - dists_r[0], 4)
        print(f"    Query [{risk_type:10s}] -> clause={m.get('clause_id','?'):15s} "
              f"chapter={m.get('chapter','?'):8s} score={score:.4f}")
    else:
        print(f"    Query [{risk_type:10s}] -> NO RESULTS")

print(f"\n{'='*60}")
print(f"  Audit complete.")
print(f"{'='*60}\n")
