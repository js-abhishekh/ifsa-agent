"""
src/ingestion/run_marker.py

Ingestion orchestrator: PDF → Marker → Chunk → ChromaDB.

Usage:
  python -m src.ingestion.run_marker \\
      --pdf data/raw_pdfs/frtb_sbm_chapter.pdf \\
      --chapter SBM_Delta_Vega \\
      --risk_type GIRR

Notes:
  - Marker must be installed: pip install marker-pdf
  - On CPU-only machines use --batch_multiplier 1 (slow but functional)
  - Always diff 2-3 pages of the produced .md against the source PDF before
    indexing the full document (formula subscripts are a common corruption point)
"""
import argparse
import subprocess
from pathlib import Path

from src.ingestion.chunker      import chunk_markdown
from src.ingestion.vector_store import RegulatoryStore
from src.config                 import RAW_PDF_DIR, MARKER_OUT_DIR


def ingest_chapter(
    pdf_path: str | Path,
    chapter: str,
    risk_type: str,
    batch_multiplier: int = 2,
) -> int:
    """Run Marker on a PDF chapter, chunk the output, and upsert to ChromaDB.

    Args:
        pdf_path:         Path to the source PDF.
        chapter:          Logical chapter name used as metadata + chunk_id prefix.
        risk_type:        FRTB risk class ("GIRR", "Equity", …).
        batch_multiplier: Marker batch multiplier (reduce to 1 for CPU-only).

    Returns:
        Number of chunks ingested.
    """
    pdf_path = Path(pdf_path)
    out_dir  = MARKER_OUT_DIR / chapter

    print(f"[run_marker] Running Marker on {pdf_path.name} → {out_dir}")
    subprocess.run(
        [
            "marker_single",
            str(pdf_path),
            str(out_dir),
            "--batch_multiplier", str(batch_multiplier),
            "--langs", "English",
        ],
        check=True,
    )

    md_files = list(out_dir.rglob("*.md"))
    if not md_files:
        raise FileNotFoundError(f"Marker produced no .md files in {out_dir}")

    md_text = md_files[0].read_text(encoding="utf-8")
    chunks  = chunk_markdown(md_text, chapter=chapter, risk_type=risk_type)

    store = RegulatoryStore()
    store.upsert_chunks(chunks)

    print(f"[run_marker] Ingested {len(chunks)} chunks from '{chapter}' (risk_type={risk_type})")
    return len(chunks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest a FRTB PDF chapter into ChromaDB")
    parser.add_argument("--pdf",   required=True, help="Path to the PDF file")
    parser.add_argument("--chapter", required=True, help="Chapter name (used as metadata key)")
    parser.add_argument("--risk_type", required=True, help="FRTB risk class: GIRR | Equity | …")
    parser.add_argument("--batch_multiplier", type=int, default=2)
    args = parser.parse_args()

    ingest_chapter(
        pdf_path=args.pdf,
        chapter=args.chapter,
        risk_type=args.risk_type,
        batch_multiplier=args.batch_multiplier,
    )
