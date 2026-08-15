"""
src/ingestion/ingest_basel_pdf.py

Comprehensive ingestion script for the consolidated Basel Framework PDF (BaselFramework.pdf).

Parses all 1,982 pages of the Basel Framework using PyMuPDF:
  1. Cleans footers, page numbers, and version stamps.
  2. Tracks chapter boundaries across all 138 regulatory chapters (MAR, CRE, CAP, RBC, LCR, NSF, etc.).
  3. Extracts individual clauses (e.g., MAR21.4, MAR21.44, CRE20.15, CAP10.3).
  4. Assigns granular risk_type metadata (GIRR, Equity, CSR_NonSec, CSR_Sec, Commodity, FX, DRC, RRAO, CreditRisk, Capital, etc.).
  5. Exports clean Markdown artifacts to data/marker_output/BaselFramework/.
  6. Upserts all chunks into ChromaDB (RegulatoryStore).
"""
import re
import sys
import time
from pathlib import Path
from typing import List, Dict, Tuple

import pymupdf

from src.config import DATA_DIR, MARKER_OUT_DIR
from src.ingestion.chunker import Chunk, chunk_markdown
from src.ingestion.vector_store import RegulatoryStore


# ── Regulatory Module & Chapter Mappings ─────────────────────────────────────
# Map chapter codes to primary risk_type / category metadata
def infer_risk_type(chapter_code: str, clause_id: str, text: str) -> str:
    """Infer granular risk_type metadata based on chapter code, clause ID, and content."""
    code = chapter_code.upper()
    
    # Granular FRTB-SA SBM Risk Class mapping (MAR21)
    if code == "MAR21":
        # Extract paragraph number if present (e.g., MAR21.44 -> 44)
        m_para = re.search(r"\.([0-9]+)$", clause_id)
        if m_para:
            para_num = int(m_para.group(1))
            if 44 <= para_num <= 53:
                return "GIRR"
            elif 54 <= para_num <= 70:
                return "CSR_NonSec"
            elif 71 <= para_num <= 80:
                return "Equity"
            elif 81 <= para_num <= 87:
                return "Commodity"
            elif 88 <= para_num <= 91:
                return "FX"
            elif 92 <= para_num <= 99:
                return "CSR_Sec"

        # Content keyword fallback
        text_lower = text.lower()
        if "interest rate" in text_lower or "yield curve" in text_lower:
            return "GIRR"
        elif "credit spread" in text_lower or "securitisation" in text_lower:
            return "CSR_NonSec"
        elif "equity" in text_lower or "stock" in text_lower:
            return "Equity"
        elif "commodity" in text_lower or "freight" in text_lower:
            return "Commodity"
        elif "foreign exchange" in text_lower or "fx" in text_lower:
            return "FX"
        return "GIRR"  # SBM default

    elif code == "MAR22":
        return "DRC"
    elif code == "MAR23":
        return "RRAO"
    elif code.startswith("MAR"):
        return "MarketRisk"
    elif code.startswith("CRE"):
        return "CreditRisk"
    elif code.startswith("CAP"):
        return "Capital"
    elif code.startswith("RBC"):
        return "RiskBasedCapital"
    elif code.startswith("OPE") or code.startswith("OPR"):
        return "OperationalRisk"
    elif code.startswith("LCR") or code.startswith("NSF"):
        return "Liquidity"
    elif code.startswith("LEX"):
        return "LargeExposures"
    elif code.startswith("SRP"):
        return "SupervisoryReview"
    elif code.startswith("DIS"):
        return "Disclosure"
    elif code.startswith("SCO"):
        return "Scope"
    elif code.startswith("BCP"):
        return "CorePrinciples"
    return "BaselFramework"


# ── Noise Filtering Regexes ──────────────────────────────────────────────────
FOOTER_RE = re.compile(
    r"^\d+/\d+$|^Downloaded on .*$|^Version effective as of .*$|^First version in the format .*$",
    re.IGNORECASE
)
CHAPTER_HDR_RE = re.compile(r"^([A-Z]{3}\d{2})\s*(.*)$")

def _make_para_re(chapter_code: str) -> re.Pattern:
    """Build a chapter-specific paragraph regex.

    For MAR21, valid paragraphs are "21.4", "21.44", etc.
    This prevents false positives on table cell values like "0.5" or footnotes like "1.75".
    The chapter digits are the last 2 characters of the chapter code.
    """
    ch_digits = chapter_code[3:]          # e.g. "21" from "MAR21"
    # Also allow single-digit minor (21.4) or double (21.44) or triple (21.100)
    return re.compile(rf"^({re.escape(ch_digits)}\.\d{{1,3}})\s*(.*)$")

def _clean_clause_id(chapter_code: str, para_str: str) -> str:
    """Produce canonical clause_id without double-prefix.

    e.g.  chapter=MAR21, para_str=21.4  -> MAR21.4
          chapter=MAR21, para_str=21.44 -> MAR21.44
    """
    ch_digits = chapter_code[3:]          # "21"
    # Strip the leading chapter digits + dot so we don't get "MAR21.21.4"
    if para_str.startswith(ch_digits + "."):
        sub = para_str[len(ch_digits) + 1:]   # "4" or "44"
    else:
        sub = para_str
    return f"{chapter_code}.{sub}"        # "MAR21.4"


def parse_basel_pdf(pdf_path: Path) -> Tuple[List[Chunk], str, str]:
    """Parse the Basel Framework PDF into structured Chunks and Markdown strings.

    Returns:
        (chunks, full_markdown, mar_markdown)
    """
    print(f"[ingest_basel_pdf] Opening {pdf_path.name}...")
    t0 = time.time()
    doc = pymupdf.open(str(pdf_path))
    total_pages = len(doc)
    print(f"[ingest_basel_pdf] Document loaded successfully: {total_pages} pages.")

    current_chapter = "SCO10"
    current_module  = "SCO"
    current_title   = "Scope and definitions"
    current_para_re = _make_para_re("SCO10")

    clauses_extracted = []
    full_md_lines = ["# Consolidated Basel Framework\n"]
    mar_md_lines  = ["# Basel Framework — Market Risk (MAR / FRTB)\n"]

    for p_idx in range(total_pages):
        page_num = p_idx + 1
        page = doc[p_idx]
        blocks = page.get_text("blocks")

        for b in blocks:
            text = b[4].strip()
            if not text:
                continue

            lines = [l.strip() for l in text.split("\n") if l.strip()]
            if not lines:
                continue

            first_line = lines[0]

            # Filter out footers and page numbers
            if FOOTER_RE.match(first_line) or "Downloaded on" in first_line:
                continue

            # Detect Chapter Headers (e.g. MAR21, CRE20, CAP10)
            m_ch = CHAPTER_HDR_RE.match(first_line)
            if m_ch:
                code = m_ch.group(1)
                title = m_ch.group(2)
                current_chapter = code
                current_module  = code[:3]
                current_para_re = _make_para_re(code)   # rebuild per chapter
                if title:
                    current_title = title
                full_md_lines.append(f"\n## {current_chapter} {current_title}\n")
                if current_module == "MAR":
                    mar_md_lines.append(f"\n## {current_chapter} {current_title}\n")
                continue

            # Detect Clause / Paragraph Headers using chapter-specific regex
            # e.g. for MAR21 only matches lines starting with "21.X"
            m_para = current_para_re.match(first_line)
            if m_para:
                para_str  = m_para.group(1)
                clause_id = _clean_clause_id(current_chapter, para_str)
                
                risk_type = infer_risk_type(current_chapter, clause_id, text)
                heading_title = m_para.group(2) or current_title

                body_text = "\n".join(lines[1:]) if len(lines) > 1 else text
                formatted_text = f"### {clause_id} {heading_title}\n{text}"

                chunk_id = f"{current_chapter}_{clause_id.replace('.', '_')}_{len(clauses_extracted)}"

                chunk = Chunk(
                    text=formatted_text,
                    chunk_id=chunk_id,
                    clause_id=clause_id,
                    chapter=current_chapter,
                    risk_type=risk_type,
                    metadata={
                        "title": heading_title,
                        "module": current_module,
                        "page": page_num,
                    }
                )
                clauses_extracted.append(chunk)

                full_md_lines.append(f"\n{formatted_text}\n")
                if current_module == "MAR":
                    mar_md_lines.append(f"\n{formatted_text}\n")
            else:
                # Regular paragraph block
                full_md_lines.append(text)
                if current_module == "MAR":
                    mar_md_lines.append(text)

    t1 = time.time()
    print(f"[ingest_basel_pdf] Extracted {len(clauses_extracted)} clauses from {total_pages} pages in {t1 - t0:.2f}s.")

    full_md = "\n".join(full_md_lines)
    mar_md  = "\n".join(mar_md_lines)

    return clauses_extracted, full_md, mar_md


def run_basel_ingestion(pdf_path: Path | None = None, reset: bool = False) -> int:
    """Run full ingestion of BaselFramework.pdf into ChromaDB and Markdown artifacts.

    Args:
        pdf_path: Path to the PDF. Defaults to data/raw_pdfs/BaselFramework.pdf.
        reset:    If True, delete and recreate the ChromaDB collection before ingesting.
    """
    if pdf_path is None:
        pdf_path = DATA_DIR / "raw_pdfs" / "BaselFramework.pdf"

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found at {pdf_path}")

    # 1. Parse PDF
    chunks, full_md, mar_md = parse_basel_pdf(pdf_path)

    # 1b. Optionally reset the collection
    if reset:
        print("[ingest_basel_pdf] Resetting ChromaDB collection...")
        import chromadb
        from src.config import CHROMA_DIR, CHROMA_COLLECTION
        client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        try:
            client.delete_collection(name=CHROMA_COLLECTION)
            print(f"[ingest_basel_pdf] Deleted collection '{CHROMA_COLLECTION}'.")
        except Exception:
            pass

    # 2. Write Markdown Artifacts
    out_dir = MARKER_OUT_DIR / "BaselFramework"
    out_dir.mkdir(parents=True, exist_ok=True)

    full_md_path = out_dir / "Basel_Full_Framework.md"
    mar_md_path  = out_dir / "Basel_MAR_Market_Risk.md"

    full_md_path.write_text(full_md, encoding="utf-8")
    mar_md_path.write_text(mar_md, encoding="utf-8")
    print(f"[ingest_basel_pdf] Saved Markdown artifacts to:\n  - {full_md_path}\n  - {mar_md_path}")

    # 3. Upsert to ChromaDB Vector Store
    print("[ingest_basel_pdf] Upserting chunks to ChromaDB vector store...")
    store = RegulatoryStore()
    
    # Upsert in batches of 500 for optimal memory & progress reporting
    batch_size = 500
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        store.upsert_chunks(batch)
        print(f"  Upserted batch {i // batch_size + 1}/{(len(chunks) + batch_size - 1) // batch_size} ({len(batch)} chunks)")

    total_store_count = store.count()
    print(f"[ingest_basel_pdf] [OK] Ingestion complete! Total items in ChromaDB collection: {total_store_count}")

    # Print Breakdown by Risk Type
    counts_by_risk: Dict[str, int] = {}
    for c in chunks:
        counts_by_risk[c.risk_type] = counts_by_risk.get(c.risk_type, 0) + 1

    print("\n=== INGESTED CHUNKS BY RISK TYPE / MODULE ===")
    for rt, cnt in sorted(counts_by_risk.items(), key=lambda x: x[1], reverse=True):
        print(f"  {rt:20s} : {cnt:4d} chunks")

    return len(chunks)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf",   default=str(DATA_DIR / "raw_pdfs" / "BaselFramework.pdf"))
    ap.add_argument("--reset", action="store_true", help="Delete and recreate the ChromaDB collection before ingesting")
    args = ap.parse_args()
    run_basel_ingestion(Path(args.pdf), reset=args.reset)
