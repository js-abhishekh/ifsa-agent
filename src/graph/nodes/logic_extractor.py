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
    FALLBACK_MODEL,
    RISK_WEIGHT_TOLERANCE,
    create_llm_client,
)

_primary_llm = create_llm_client(is_fallback=False)
_fallback_llm = create_llm_client(is_fallback=True)
_llm_available = (_primary_llm is not None or _fallback_llm is not None)

if _primary_llm:
    print(f"[logic_extractor] Primary LLM initialized: {LLM_MODEL}")
elif _fallback_llm:
    print(f"[logic_extractor] Fallback LLM initialized: {FALLBACK_MODEL}")
else:
    print("[logic_extractor] LLM not available - defaulting to static Basel tables.")


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


def _bind_and_cross_check_parameters(
    extracted: ExtractedLogic,
    errors: list[ValidationError],
) -> None:
    """Validate and strictly bind extracted parameters to statutory Basel Annex tables.

    Under the Basel III / FRTB-SA framework (MAR21), regulatory risk weights and
    correlations are statutory constants. If the LLM extracts a value that deviates
    beyond RISK_WEIGHT_TOLERANCE, or fails to extract a standard bucket:
      1. An audit ValidationError is logged noting the exact divergence.
      2. The parameter is overridden with the prescribed statutory value.
      3. Any missing statutory buckets or correlation parameters are backfilled.
      4. The logic is marked complete and ready for deterministic quant calculations.
    """
    static_rw = RISK_WEIGHTS_BY_CLASS.get(extracted.risk_class, {})
    static_corr = CORRELATIONS_BY_CLASS.get(extracted.risk_class, {})

    # 1. Enforce statutory Risk Weights
    for key, llm_val in list(extracted.risk_weights.items()):
        if key in static_rw:
            diff = abs(llm_val - static_rw[key])
            if diff > RISK_WEIGHT_TOLERANCE:
                errors.append(ValidationError(
                    severity="warning",
                    node="logic_extractor",
                    message=(
                        f"{extracted.risk_class} risk weight '{key}': "
                        f"extracted={llm_val:.4f} diverged from Basel Annex={static_rw[key]:.4f} "
                        f"(diff={diff:.4f} > tolerance={RISK_WEIGHT_TOLERANCE}). "
                        f"Automatically corrected to prescribed statutory Basel value."
                    ),
                ))
                extracted.risk_weights[key] = static_rw[key]

    # Backfill missing statutory risk weights from the Basel Annex table
    for key, static_val in static_rw.items():
        if key not in extracted.risk_weights:
            extracted.risk_weights[key] = static_val

    # 2. Enforce statutory Correlations
    for key, llm_corr in list(extracted.correlations.items()):
        if key in static_corr:
            diff = abs(llm_corr - static_corr[key])
            if diff > RISK_WEIGHT_TOLERANCE:
                errors.append(ValidationError(
                    severity="warning",
                    node="logic_extractor",
                    message=(
                        f"{extracted.risk_class} correlation '{key}': "
                        f"extracted={llm_corr:.4f} diverged from Basel Annex={static_corr[key]:.4f} "
                        f"(diff={diff:.4f} > tolerance={RISK_WEIGHT_TOLERANCE}). "
                        f"Automatically corrected to prescribed statutory Basel value."
                    ),
                ))
                extracted.correlations[key] = static_corr[key]

    # Backfill missing statutory correlations from the Basel Annex table
    for key, static_val in static_corr.items():
        if key not in extracted.correlations:
            extracted.correlations[key] = static_val

    if static_rw:
        extracted.is_complete = True
        extracted.missing_fields = []


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
    import asyncio
    errors = list(state.get("validation_errors", []))
    retrieved = state.get("retrieved_regulatory_nodes", [])

    positions = state.get("portfolio_inputs", [])
    if not positions:
        print("[logic_extractor] No portfolio positions; skipping regulatory parameter extraction.")
        state["extracted_calculation_logic"] = []
        return state

    # Group texts by risk type
    grouped: dict[str, list[str]] = {}
    for node in retrieved:
        grouped.setdefault(node.risk_type, []).append(node.text)

    # Also ensure every portfolio risk class is represented
    for p in positions:
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
            response = None
            try:
                if _primary_llm:
                    print(f"[logic_extractor] Calling {LLM_MODEL} for {risk_class} parameter extraction...")
                    response = await asyncio.to_thread(
                        _primary_llm.invoke,
                        [
                            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
                            {"role": "user",   "content": f"Risk class: {risk_class}\n\nClause text:\n{combined_text}"},
                        ],
                    )
            except Exception as pe:
                print(f"[logic_extractor] Primary LLM failed ({pe}). Trying fallback model ({FALLBACK_MODEL})...")
                if _fallback_llm:
                    response = await asyncio.to_thread(
                        _fallback_llm.invoke,
                        [
                            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
                            {"role": "user",   "content": f"Risk class: {risk_class}\n\nClause text:\n{combined_text}"},
                        ],
                    )
                else:
                    raise pe

            if response is None:
                raise RuntimeError("No response from primary or fallback model.")

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

        # Cross-check and strictly bind extracted values to prescribed statutory tables
        _bind_and_cross_check_parameters(logic, errors)

        extracted.append(logic)

    state["extracted_calculation_logic"] = extracted
    state["validation_errors"] = errors
    return state
