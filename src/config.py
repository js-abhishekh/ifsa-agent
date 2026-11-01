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
GEMINI_API_KEY     = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY     = os.getenv("OPENAI_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

if GEMINI_API_KEY:
    default_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    default_model = "gemini-3.6-flash"
    default_fallback = "gemini-3.6-flash"
elif OPENROUTER_API_KEY:
    default_base_url = "https://openrouter.ai/api/v1"
    default_model = "nvidia/llama-3.1-nemotron-70b-instruct:free"
    default_fallback = "meta-llama/llama-3.3-70b-instruct:free"
elif OPENAI_API_KEY:
    default_base_url = ""
    default_model = "gpt-4o"
    default_fallback = "gpt-4o-mini"
else:
    default_base_url = ""
    default_model = "gemini-3.6-flash"
    default_fallback = "gemini-3.6-flash"

LLM_BASE_URL       = os.getenv("LLM_BASE_URL", default_base_url)
LLM_MODEL          = os.getenv("LLM_MODEL", default_model)
FALLBACK_LLM_MODEL = os.getenv("FALLBACK_LLM_MODEL", default_fallback)

# ── Multi-Provider Fallback ───────────────────────────────────────────────────
# If primary is Gemini and OpenRouter is available, automatically fall back across providers
if GEMINI_API_KEY and OPENROUTER_API_KEY:
    FALLBACK_BASE_URL = os.getenv("FALLBACK_BASE_URL", "https://openrouter.ai/api/v1")
    FALLBACK_MODEL    = os.getenv("FALLBACK_MODEL", "nvidia/nemotron-3-ultra-550b-a55b:free")
    FALLBACK_API_KEY  = OPENROUTER_API_KEY
elif OPENROUTER_API_KEY and OPENAI_API_KEY:
    FALLBACK_BASE_URL = os.getenv("FALLBACK_BASE_URL", "")
    FALLBACK_MODEL    = os.getenv("FALLBACK_MODEL", "gpt-4o-mini")
    FALLBACK_API_KEY  = OPENAI_API_KEY
else:
    FALLBACK_BASE_URL = os.getenv("FALLBACK_BASE_URL", "")
    FALLBACK_MODEL    = os.getenv("FALLBACK_MODEL", FALLBACK_LLM_MODEL)
    FALLBACK_API_KEY  = GEMINI_API_KEY or OPENROUTER_API_KEY or OPENAI_API_KEY


def create_llm_client(is_fallback: bool = False):
    """Instantiate a ChatOpenAI client for either primary or secondary fallback provider."""
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        return None

    if is_fallback:
        if not FALLBACK_API_KEY:
            return None
        kwargs = {
            "model": FALLBACK_MODEL,
            "api_key": FALLBACK_API_KEY,
            "temperature": 0,
            "request_timeout": 120,
        }
        if FALLBACK_BASE_URL:
            kwargs["base_url"] = FALLBACK_BASE_URL
        return ChatOpenAI(**kwargs)
    else:
        api_key = GEMINI_API_KEY or OPENROUTER_API_KEY or OPENAI_API_KEY
        if not api_key:
            return None
        kwargs = {
            "model": LLM_MODEL,
            "api_key": api_key,
            "temperature": 0,
            "request_timeout": 120,
        }
        if LLM_BASE_URL:
            kwargs["base_url"] = LLM_BASE_URL
        return ChatOpenAI(**kwargs)


# ── Chunking ──────────────────────────────────────────────────────────────────
MAX_CHUNK_TOKENS  = int(os.getenv("MAX_CHUNK_TOKENS", "500"))
CHARS_PER_TOKEN   = 4   # heuristic
MAX_CHUNK_CHARS   = MAX_CHUNK_TOKENS * CHARS_PER_TOKEN

# ── Validation ────────────────────────────────────────────────────────────────
# Max allowable divergence (in absolute terms) between LLM-extracted risk
# weight and static Basel Annex table value before a ValidationError is raised.
RISK_WEIGHT_TOLERANCE = 0.001   # 10 bps
