"""
src/config.py — centralised configuration for the FRTB-SA pipeline.
All path and model settings are read from environment variables (.env),
with sensible defaults for local development.
"""
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# ── Paths ─────────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR      = PROJECT_ROOT / "data"
RAW_PDF_DIR   = DATA_DIR / "raw_pdfs"
MARKER_OUT_DIR = DATA_DIR / "marker_output"
CHROMA_DIR    = Path(os.getenv("CHROMA_PERSIST_DIR", str(DATA_DIR / "chroma_db")))

# ── ChromaDB ──────────────────────────────────────────────────────────────────
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "frtb_sa_clauses")
EMBED_MODEL       = os.getenv("EMBED_MODEL", "BAAI/bge-large-en-v1.5")

# ── LLM ───────────────────────────────────────────────────────────────────────
GEMINI_API_KEY     = os.getenv("GEMINI_API_KEY", "AIzaSyDZOiw_CCsqb0ZIM8fIo78JM8uEs5iT4Pc")
OPENAI_API_KEY     = os.getenv("OPENAI_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

LLM_BASE_URL       = os.getenv("LLM_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/" if GEMINI_API_KEY else "")
LLM_MODEL          = os.getenv("LLM_MODEL", "gemini-3.1-flash-lite" if GEMINI_API_KEY else "gpt-4o")
FALLBACK_LLM_MODEL = os.getenv("FALLBACK_LLM_MODEL", "gemini-3.6-flash")

# ── Chunking ──────────────────────────────────────────────────────────────────
MAX_CHUNK_TOKENS  = int(os.getenv("MAX_CHUNK_TOKENS", "500"))
CHARS_PER_TOKEN   = 4   # heuristic
MAX_CHUNK_CHARS   = MAX_CHUNK_TOKENS * CHARS_PER_TOKEN

# ── Validation ────────────────────────────────────────────────────────────────
# Max allowable divergence (in absolute terms) between LLM-extracted risk
# weight and static Basel Annex table value before a ValidationError is raised.
RISK_WEIGHT_TOLERANCE = 0.001   # 10 bps
