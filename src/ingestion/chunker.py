"""
src/ingestion/chunker.py

Structure-aware Markdown chunker for FRTB regulatory documents.

Design principles:
  - Pipe-table blocks and $$…$$ math blocks are "protected" — they
    are never split internally, regardless of length.
  - Splitting happens on clause-level headers (##/### Para X.Y …).
  - Within a clause body, further splitting happens on paragraph
    boundaries only when the body exceeds MAX_CHUNK_CHARS.
"""
import re
from dataclasses import dataclass, field
from typing import List, Tuple

from src.config import MAX_CHUNK_CHARS


# ── Regex patterns ────────────────────────────────────────────────────────────
# Full pipe-table: header row | separator row | 1+ data rows
TABLE_BLOCK = re.compile(
    r"(\|.+\|\n\|[-:| ]+\|\n(?:\|.+\|\n?)+)",
    re.MULTILINE,
)

# Display math: $$ … $$  (allow multiline)
MATH_BLOCK = re.compile(r"(\$\$.+?\$\$)", re.DOTALL)

# Clause-level headers: ## / ### / #### optionally followed by "Para X.Y"
CLAUSE_HEADER = re.compile(
    r"^(#{1,4})\s*(?:Para(?:graph)?\s*)?(\d+[\.\d]*)\s*(.*)$",
    re.MULTILINE,
)


# ── Data model ────────────────────────────────────────────────────────────────
@dataclass
class Chunk:
    text: str
    chunk_id: str
    clause_id: str | None = None
    chapter: str | None = None
    risk_type: str | None = None
    metadata: dict = field(default_factory=dict)


# ── Internal helpers ──────────────────────────────────────────────────────────
def _protect_blocks(md_text: str) -> Tuple[str, dict]:
    """Replace tables and math blocks with unique placeholders.

    Returns the modified text and a dict mapping placeholder → original block.
    Placeholders contain no newlines so that downstream split-on-newline logic
    treats each block as a single opaque token.
    """
    placeholders: dict[str, str] = {}

    def _stash(match: re.Match, prefix: str) -> str:
        key = f"__{prefix}_{len(placeholders)}__"
        placeholders[key] = match.group(0)
        return key

    md_text = TABLE_BLOCK.sub(lambda m: _stash(m, "TABLE"), md_text)
    md_text = MATH_BLOCK.sub(lambda m: _stash(m, "MATH"),  md_text)
    return md_text, placeholders


def _restore(text: str, placeholders: dict) -> str:
    for key, original in placeholders.items():
        text = text.replace(key, original)
    return text


def _split_by_length(body: str, placeholders: dict) -> List[str]:
    """Split a clause body on paragraph boundaries, never inside
    a protected block.  Placeholders are restored before returning.
    """
    if len(body) <= MAX_CHUNK_CHARS:
        return [_restore(body, placeholders)]

    paragraphs = body.split("\n\n")
    out: List[str] = []
    current = ""

    for p in paragraphs:
        stripped = p.strip()
        # Placeholders start with __TABLE_ or __MATH_ — treat as atomic
        is_atomic = stripped.startswith("__TABLE_") or stripped.startswith("__MATH_")

        if is_atomic:
            if current:
                out.append(current)
                current = ""
            out.append(p)
            continue

        if len(current) + len(p) > MAX_CHUNK_CHARS and current:
            out.append(current)
            current = p
        else:
            current += ("\n\n" if current else "") + p

    if current:
        out.append(current)

    return [_restore(chunk, placeholders) for chunk in out]


# ── Public API ────────────────────────────────────────────────────────────────
def chunk_markdown(md_text: str, chapter: str, risk_type: str) -> List[Chunk]:
    """Parse a Marker-produced Markdown file and return a list of Chunks.

    Each Chunk maps to a single citable clause (paragraph number) from the
    regulatory document.  Long clause bodies are further split on paragraph
    boundaries but protected blocks are always kept atomic.

    Args:
        md_text:   Full Markdown text produced by Marker.
        chapter:   Logical chapter name (e.g. "SBM_Delta_Vega").
        risk_type: FRTB risk class string (e.g. "GIRR", "Equity").

    Returns:
        List[Chunk] — each with a stable chunk_id derived from chapter +
        clause_id + part index.
    """
    protected_text, placeholders = _protect_blocks(md_text)

    # re.split with capture groups yields:
    #   [preamble, hlevel₀, clause_id₀, title₀, body₀, hlevel₁, …]
    sections = CLAUSE_HEADER.split(protected_text)

    chunks: List[Chunk] = []

    # Skip the preamble (sections[0]) — it usually just has the doc title
    i = 1
    while i + 3 <= len(sections):
        _hlevel   = sections[i]
        clause_id = sections[i + 1].strip()
        title     = sections[i + 2].strip()
        body      = sections[i + 3] if i + 3 < len(sections) else ""
        i += 4

        sub_chunks = _split_by_length(body, placeholders)
        for j, sc in enumerate(sub_chunks):
            chunks.append(Chunk(
                text=f"### {clause_id} {title}\n{sc}",
                chunk_id=f"{chapter}_{clause_id}_{j}",
                clause_id=clause_id,
                chapter=chapter,
                risk_type=risk_type,
                metadata={"title": title, "part": j},
            ))

    return chunks
