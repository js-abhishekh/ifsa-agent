"""
src/graph/nodes/logic_extractor.py

LangGraph Node B — Regulatory Logic & Parameter Extractor.

Responsibilities:
  1. Group retrieved clause texts by risk class.
  2. Call the LLM (temp=0, structured JSON output) to extract:
       - risk weights, correlations, formula references
  3. Validate the JSON against the ExtractedLogic Pydantic schema.
  4. Cross-check LLM-extracted risk weights against the static Basel Annex
     tables in risk_weights.py; raise a ValidationError if divergence > tolerance.
  5. Fall back to static tables if the vector store was empty (no PDFs ingested).

The LLM is ONLY used here — never for arithmetic.
"""
import json
from src.graph.state import (
    AgentState, ExtractedLogic, CalculationParameter, ValidationError
)
from src.quant.risk_weights import RISK_WEIGHTS_BY_CLASS, CORRELATIONS_BY_CLASS
from src.config import (
    LLM_MODEL,
    FALLBACK_LLM_MODEL,
    GEMINI_API_KEY,
    OPENAI_API_KEY,
    OPENROUTER_API_KEY,
    LLM_BASE_URL,
    RISK_WEIGHT_TOLERANCE,
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
        }
        if LLM_BASE_URL:
            kwargs["base_url"] = LLM_BASE_URL
        
        _llm = ChatOpenAI(**kwargs)
        _llm_available = True
        print(f"[logic_extractor] LLM initialized: {LLM_MODEL} (endpoint: {LLM_BASE_URL or 'OpenAI default'})")
except Exception as e:
    print(f"[logic_extractor] LLM init note: {e} - defaulting to static Basel tables.")
    _llm_available = False


EXTRACTION_SYSTEM_PROMPT = """\
You are a regulatory parameter extraction engine for FRTB-SA.
Given regulatory clause text, extract ONLY explicitly stated numeric risk weights,
correlation parameters (rho, gamma), and bucket definitions.
Do NOT infer or estimate values not explicitly present in the text.
Return strict JSON matching this schema exactly:

{
  "risk_class": "<GIRR|CSR_NonSec|CSR_Sec|Equity|Commodity|FX>",
  "formula_ref": "<clause id / description>",
  "risk_weights": {"<bucket_or_tenor>": <float>},
  "correlations": {"<rho_or_gamma_key>": <float>},
  "parameters": [
    {"param_name": "...", "value": <float>, "source_clause_id": "...", "confidence": <0-1>}
  ],
  "is_complete": <bool>,
  "missing_fields": ["..."]
}

Set is_complete=false and list missing_fields if the text does not contain enough
numeric detail to run the calculation for that risk class.
Return ONLY the JSON object, no markdown fences, no commentary."""


def _static_fallback(risk_class: str) -> ExtractedLogic:
    """Build an ExtractedLogic from the static Basel Annex tables."""
    rw = RISK_WEIGHTS_BY_CLASS.get(risk_class, {})
    corr = CORRELATIONS_BY_CLASS.get(risk_class, {})
    return ExtractedLogic(
        risk_class=risk_class,
        formula_ref="Static Basel Annex (fallback — no PDF ingested)",
        risk_weights=rw,
        correlations=corr,
        is_complete=bool(rw),
        missing_fields=[] if rw else ["risk_weights"],
    )


def _cross_check_risk_weights(
    extracted: ExtractedLogic,
    errors: list[ValidationError],
) -> None:
    """Compare LLM-extracted risk weights against static Basel Annex tables.

    Appends a ValidationError (warning severity) for any key that deviates
    beyond RISK_WEIGHT_TOLERANCE.
    """
    static_rw = RISK_WEIGHTS_BY_CLASS.get(extracted.risk_class, {})
    for key, llm_val in extracted.risk_weights.items():
        if key in static_rw:
            diff = abs(llm_val - static_rw[key])
            if diff > RISK_WEIGHT_TOLERANCE:
                errors.append(ValidationError(
                    severity="warning",
                    node="logic_extractor",
                    message=(
                        f"{extracted.risk_class} risk weight '{key}': "
                        f"extracted={llm_val:.4f} vs Basel Annex={static_rw[key]:.4f} "
                        f"(diff={diff:.4f} > tolerance={RISK_WEIGHT_TOLERANCE})"
                    ),
                ))


def _extract_json_payload(raw_text: str) -> dict:
    """Robustly parse JSON object from LLM response text."""
    text = raw_text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        # Remove opening and closing backtick lines
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines).strip()
    
    # Try direct parse
    try:
        return json.loads(text)
    except Exception:
        # Extract outermost JSON object {...}
        import re
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            return json.loads(m.group(0))
        raise ValueError(f"No JSON object found in response: {text[:200]}")


async def logic_extractor_node(state: AgentState) -> AgentState:
    """Extract regulatory parameters for each risk class.
    
    If the LLM is unavailable or the store is empty, falls back to
    the static Basel Annex tables so the pipeline can still run.
    """
    global _llm
    import asyncio
    errors = list(state.get("validation_errors", []))
    retrieved = state.get("retrieved_regulatory_nodes", [])

    # Group texts by risk type
    grouped: dict[str, list[str]] = {}
    for node in retrieved:
        grouped.setdefault(node.risk_type, []).append(node.text)

    # Also ensure every portfolio risk class is represented
    for p in state.get("portfolio_inputs", []):
        if p.risk_class not in grouped:
            grouped[p.risk_class] = []

    extracted: list[ExtractedLogic] = []

    for risk_class, texts in grouped.items():
        # If no retrieved text, use static fallback directly
        if not texts or not _llm_available:
            logic = _static_fallback(risk_class)
            extracted.append(logic)
            continue

        combined_text = "\n\n---\n\n".join(texts)
        try:
            print(f"[logic_extractor] Calling Nemotron Ultra for {risk_class} parameter extraction...")
            response = await asyncio.to_thread(
                _llm.invoke,
                [
                    {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
                    {"role": "user",   "content": f"Risk class: {risk_class}\n\nClause text:\n{combined_text}"},
                ],
            )
            payload = _extract_json_payload(response.content)
            payload["parameters"] = [
                CalculationParameter(**p) for p in payload.get("parameters", [])
            ]
            logic = ExtractedLogic(**payload)
            print(f"[logic_extractor] Successfully extracted {risk_class} logic via LLM (is_complete={logic.is_complete})")
        except Exception as e:
            # Parse failure → fall back to static tables + log error
            errors.append(ValidationError(
                severity="warning",
                node="logic_extractor",
                message=f"{risk_class}: LLM extraction failed ({e}); using static Basel Annex tables",
            ))
            logic = _static_fallback(risk_class)

        # Cross-check extracted values against static tables
        _cross_check_risk_weights(logic, errors)

        # If LLM returned incomplete but static tables have data, merge
        if not logic.is_complete:
            static = _static_fallback(risk_class)
            if static.is_complete:
                # Fill in missing fields from static tables
                if not logic.risk_weights:
                    logic.risk_weights = static.risk_weights
                if not logic.correlations:
                    logic.correlations = static.correlations
                logic.is_complete = bool(logic.risk_weights)

        extracted.append(logic)

    state["extracted_calculation_logic"] = extracted
    state["validation_errors"] = errors
    return state
