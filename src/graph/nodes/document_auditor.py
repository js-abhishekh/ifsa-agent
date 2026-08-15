"""
src/graph/nodes/document_auditor.py

LangGraph Node — Automated Regulatory Document Auditor.

Responsibility:
Reads the bank's Pillar 3 / Market Risk PDF disclosure and audits it against 
FRTB-SA standards (looking for missing curvature/vega, bad shocks, anomalous FX risk).
Returns a list of formatted audit flags.
"""
import os
import json
import pymupdf
from src.graph.state import AgentState
from src.config import (
    LLM_MODEL,
    FALLBACK_LLM_MODEL,
    GEMINI_API_KEY,
    OPENAI_API_KEY,
    OPENROUTER_API_KEY,
    LLM_BASE_URL,
)

_llm = None
_llm_available = False

try:
    from langchain_openai import ChatOpenAI
    api_key = GEMINI_API_KEY or OPENROUTER_API_KEY or OPENAI_API_KEY
    if api_key:
        kwargs = {
            "model": LLM_MODEL,
            "api_key": api_key,
            "temperature": 0,
            "request_timeout": 120,
        }
        if LLM_BASE_URL:
            kwargs["base_url"] = LLM_BASE_URL
        
        _llm = ChatOpenAI(**kwargs)
        _llm_available = True
        print(f"[document_auditor] LLM initialized: {LLM_MODEL}")
except Exception as e:
    print(f"[document_auditor] LLM init note: {e} - auditor bypassed.")
    _llm_available = False


AUDITOR_PROMPT = """\
You are an expert FRTB-SA regulatory auditor. Your job is to analyze the provided 
bank disclosure text and identify any regulatory breaches or major discrepancies 
regarding market risk capital under the Basel III Sensitivities-Based Method (SBM).

Specifically look for:
1. Blanket exclusion of Vega and Curvature capital charges.
2. Invalid curvature methodologies (e.g., asymmetric shocking, only using upward shocks).
3. Highly suspicious discrepancies in FX Risk (e.g., massive notional with exactly zero capital charge).

Return your findings as strict JSON matching this schema exactly:
{
  "flags": [
    {
      "title": "<Short description of the breach>",
      "location": "<Where in the text it was found (Page/Table)>",
      "quote": "<Exact quote from the text demonstrating the breach>",
      "issue": "<Explanation of why this violates FRTB-SA rules (e.g. MAR21 or MAR22)>"
    }
  ]
}

Return ONLY the JSON object. If there are no issues, return {"flags": []}.
"""

def _extract_json_payload(raw_text: str) -> dict:
    """Robustly parse JSON object from LLM response text."""
    text = raw_text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines).strip()
    
    try:
        return json.loads(text)
    except Exception:
        import re
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            return json.loads(m.group(0))
        return {"flags": []}


async def document_auditor_node(state: AgentState) -> AgentState:
    """Read the PDF and extract audit flags using the LLM."""
    global _llm
    import asyncio
    doc_path = state.get("document_path")
    flags = list(state.get("audit_flags", []))

    if not doc_path or not os.path.exists(doc_path):
        return state

    if not _llm_available:
        print("[document_auditor] LLM unavailable, skipping audit.")
        return state

    print(f"[document_auditor] Extracting text from {doc_path} for audit...")
    try:
        def _read_pdf():
            doc = pymupdf.open(doc_path)
            full_text = ""
            for i, page in enumerate(doc):
                full_text += f"\n--- PAGE {i+1} ---\n"
                full_text += page.get_text()
            doc.close()
            return full_text

        full_text = await asyncio.to_thread(_read_pdf)


        # Multi-section sampling: Instead of taking a single 25k block from the start,
        # we find all occurrences of audit-relevant keywords across the full PDF
        # and extract a ~3k character window around each match, up to 40k total chars.
        MAX_TOTAL_CHARS = 40000
        WINDOW_SIZE = 3000
        HALF_WINDOW = WINDOW_SIZE // 2
        
        if len(full_text) > MAX_TOTAL_CHARS:
            keywords = ["market risk", "trading book", "frtb", "sensitivity",
                        "capital charge", "vega", "curvature", "delta",
                        "exclusion", "notional", "fx risk", "foreign exchange"]
            
            # Find all keyword indices
            indices = []
            lower_text = full_text.lower()
            for kw in keywords:
                start = 0
                while True:
                    idx = lower_text.find(kw, start)
                    if idx == -1:
                        break
                    indices.append(idx)
                    start = idx + len(kw)
            
            indices.sort()
            
            # Merge overlapping windows
            merged_intervals = []
            for idx in indices:
                start_idx = max(0, idx - HALF_WINDOW)
                end_idx = min(len(full_text), idx + HALF_WINDOW)
                
                if not merged_intervals:
                    merged_intervals.append([start_idx, end_idx])
                else:
                    last = merged_intervals[-1]
                    if start_idx <= last[1]:
                        last[1] = max(last[1], end_idx)
                    else:
                        merged_intervals.append([start_idx, end_idx])
            
            # Construct sampled text
            sampled_text = ""
            for interval in merged_intervals:
                chunk = full_text[interval[0]:interval[1]]
                if len(sampled_text) + len(chunk) > MAX_TOTAL_CHARS:
                    # Append as much as we can fit and stop
                    remaining = MAX_TOTAL_CHARS - len(sampled_text)
                    sampled_text += f"\n...[SECTION START]...\n{chunk[:remaining]}\n...[SECTION TRUNCATED]...\n"
                    break
                sampled_text += f"\n...[SECTION START]...\n{chunk}\n...[SECTION END]...\n"
                
            if not sampled_text:
                 sampled_text = full_text[:MAX_TOTAL_CHARS] # Fallback if no keywords found
            full_text = sampled_text

        print(f"[document_auditor] Calling LLM to audit document ({len(full_text)} characters, multi-section sampled)...")


        import time
        max_retries = 3
        response = None
        for attempt in range(max_retries):
            try:
                response = await asyncio.to_thread(
                    _llm.invoke,
                    [
                        {"role": "system", "content": AUDITOR_PROMPT},
                        {"role": "user", "content": f"Document Text:\n{full_text}"},
                    ],
                )
                break
            except Exception as e:
                print(f"[document_auditor] Attempt {attempt+1} failed ({e}). Switching to fallback model {FALLBACK_LLM_MODEL}...")
                _llm = ChatOpenAI(
                    model=FALLBACK_LLM_MODEL,
                    api_key=GEMINI_API_KEY or OPENROUTER_API_KEY or OPENAI_API_KEY,
                    base_url=LLM_BASE_URL,
                    temperature=0,
                    request_timeout=120,
                )
                if attempt < max_retries - 1:
                    await asyncio.sleep(2)
                else:
                    raise e

        payload = _extract_json_payload(response.content)

        for flag in payload.get("flags", []):
            formatted_flag = (
                f"{flag['title']}\n"
                f"Where in PDF: {flag['location']}\n"
                f"What it says: \"{flag['quote']}\"\n"
                f"The Issue: {flag['issue']}"
            )
            flags.append(formatted_flag)

        state["audit_flags"] = flags
        print(f"[document_auditor] Found {len(state['audit_flags'])} regulatory flags.")
    except Exception as e:
        print(f"[document_auditor] Document audit failed: {e}")

    return state
