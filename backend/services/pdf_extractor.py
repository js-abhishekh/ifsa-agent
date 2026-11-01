import pymupdf
import json
import logging
import asyncio
from typing import Tuple, List, Dict, Any
from pathlib import Path
from src.config import LLM_MODEL, FALLBACK_MODEL, create_llm_client
from src.graph.state import PortfolioPosition
from langchain_core.messages import SystemMessage, HumanMessage

logger = logging.getLogger(__name__)


def load_demo_portfolio() -> List[Dict[str, Any]]:
    """Load the PNB demo portfolio JSON for the explicit sample-analysis flow.

    This is ONLY used by the /sample-portfolio demo endpoint where the user has
    intentionally clicked 'Execute Sample Analysis'. It must never be called as a
    silent fallback for a user-uploaded PDF.
    """
    sample_path = Path("data/pnb_portfolio.json")
    try:
        if sample_path.exists():
            with open(sample_path, "r") as f:
                data = json.load(f)
                # It's either a list directly or {"positions": [...]}
                return data if isinstance(data, list) else data.get("positions", [])
        return []
    except Exception as e:
        logger.error(f"Error loading demo portfolio: {e}")
        return []


async def extract_portfolio_from_pdf(file_path: str) -> Tuple[List[Dict[str, Any]], str, str]:
    """Extract FRTB portfolio positions from a bank disclosure PDF.

    Returns:
        (positions, status, message)
        - status is one of: "success" | "partial" | "failed"
        - positions is empty list on "partial" or "failed"
        - message describes the specific failure reason

    Raises nothing — all errors are captured in the returned status/message.
    """
    try:
        def _read_pdf():
            import re
            MARKET_KEYWORDS = [
                r"\brisk\b", r"\bgirr\b", r"\binterest\b", r"\bequity\b", r"\bequities\b",
                r"\bforex\b", r"\bfx\b", r"\bcurrency\b", r"\bcommodity\b", r"\bcommodities\b",
                r"\bcredit\b", r"\bspread\b", r"\bpv01\b", r"\bdv01\b", r"\bsensitivity\b",
                r"\bsensitivities\b", r"\btrading\b", r"\bduration\b", r"\bnotional\b",
                r"\bexposure\b", r"\bderivative\b", r"\bderivatives\b", r"\bhedge\b",
                r"\bhedging\b", r"\bnii\b", r"\bvar\b", r"\bcurvature\b", r"\bvega\b",
                r"\bsecuriti\b", r"\binvestment\b", r"\binvestments\b", r"\bbond\b",
                r"\bbonds\b", r"\byield\b", r"\btenor\b", r"\bmaturity\b", r"\bmaturities\b",
                r"\bcapital charge\b", r"\bsbm\b", r"\brwa\b"
            ]
            kw_regex = re.compile("|".join(MARKET_KEYWORDS), re.IGNORECASE)

            all_tables = []
            filtered_tables = []
            doc = pymupdf.open(file_path)
            for i, page in enumerate(doc):
                tabs = page.find_tables()
                if tabs and tabs.tables:
                    for t_idx, tab in enumerate(tabs.tables):
                        df = tab.extract()
                        if df:
                            t_lines = [f"\n--- Table {t_idx+1} on Page {i+1} ---"]
                            t_raw = []
                            for row in df:
                                clean_row = [str(x).strip().replace('\n', ' ') if x is not None else '' for x in row]
                                t_lines.append(" | ".join(clean_row))
                                t_raw.extend(clean_row)
                            table_text = "\n".join(t_lines) + "\n"
                            all_tables.append(table_text)
                            if kw_regex.search(" ".join(t_raw)):
                                filtered_tables.append(table_text)
            doc.close()
            target = filtered_tables if filtered_tables else all_tables
            return "".join(target)

        try:
            tables_text = await asyncio.to_thread(_read_pdf)
        except Exception as e:
            return [], "failed", (
                f"Could not read the PDF file: {e}. "
                "Please ensure the file is a valid, non-password-protected PDF."
            )

        if not tables_text.strip():
            return [], "failed", (
                "No machine-readable tables were found in this PDF. "
                "The document may be a scanned image or contain only text. "
                "Please upload a PDF with structured tables containing market risk data "
                "(e.g., GIRR sensitivity tables, equity exposure schedules, FX notionals)."
            )

        # Keep within limits, tables usually take less space than full text
        MAX_CHARS = 150000
        excerpt = tables_text[:MAX_CHARS]

        primary_llm = create_llm_client(is_fallback=False)
        fallback_llm = create_llm_client(is_fallback=True)

        if not primary_llm and not fallback_llm:
            return [], "failed", "No valid LLM credentials configured. Please set GEMINI_API_KEY, OPENROUTER_API_KEY, or OPENAI_API_KEY."

        system_prompt = """You are an expert at reading bank trading book disclosures and market risk reports.
I am providing you with ALL the tables extracted from a bank's disclosure PDF.
Scan all the tables and numeric values. Identify and extract data relevant to calculating market risk capital charges (FRTB).
Look for: Interest Rate Risk (GIRR), Equity Risk, Foreign Exchange Risk (FX), Credit Spread Risk (CSR_NonSec, CSR_Sec), and Commodity Risk.
Also look for aggregated risk exposures, notional amounts, or PV01 sensitivities.

Derive or extract structured portfolio positions based on the tables. 
For each relevant value you find, create a position entry:
- instrument_id: A descriptive ID based on the table/metric (e.g., "INT_RATE_RISK", "EQUITY_EXPOSURE")
- risk_class: MUST be one of: GIRR, CSR_NonSec, CSR_Sec, Equity, Commodity, FX
- bucket: Derive an appropriate bucket (e.g., "INR", "USD", "EM_LargeCap", "default")
- risk_factor: The specific risk factor or row label (e.g., "50bps_shock", "Net_NPA", "Counterparty_Credit")
- sensitivity: The numeric amount, exposure, or sensitivity (e.g. PV01, NII impact).
- notional: (Optional) The notional amount or total exposure.
- currency: The currency if mentioned, otherwise "INR" or "USD".

Here is an EXACT example of how the JSON output must look:
{
  "positions": [
    {
      "instrument_id": "POS_GIRR_SHOCK",
      "risk_class": "GIRR",
      "bucket": "INR",
      "risk_factor": "50bps_impact",
      "sensitivity": 23766.40,
      "notional": null,
      "currency": "INR"
    },
    {
      "instrument_id": "POS_EQ_BANKING_BOOK",
      "risk_class": "Equity",
      "bucket": "EM_LargeCap",
      "risk_factor": "Associates_Outside_India",
      "sensitivity": 3415.88,
      "notional": null,
      "currency": "INR"
    }
  ]
}

If absolutely NO market risk or relevant numeric data is found in the tables, return:
{"positions": [], "message": "Reason why no relevant market risk tables were found"}

Return ONLY the JSON object, no markdown code blocks, no commentary."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=excerpt)
        ]

        response = None
        last_error = None

        if primary_llm:
            try:
                response = await primary_llm.ainvoke(messages)
            except Exception as e:
                logger.warning(f"Primary model ({LLM_MODEL}) failed: {e}. Trying fallback model ({FALLBACK_MODEL})...")
                last_error = e

        if response is None and fallback_llm:
            try:
                response = await fallback_llm.ainvoke(messages)
                logger.info(f"Fallback model ({FALLBACK_MODEL}) succeeded.")
            except Exception as e:
                logger.error(f"Fallback model ({FALLBACK_MODEL}) also failed: {e}")
                last_error = e

        if response is None:
            return [], "failed", (
                f"The AI extraction model failed to respond: {last_error}. "
                "Please check your API key configuration and try again."
            )

        content = response.content

        start_idx = content.find('{')
        end_idx = content.rfind('}')
        if start_idx == -1 or end_idx == -1:
            return [], "failed", (
                "The AI model did not return valid JSON. "
                "This is a transient issue — please try uploading again."
            )

        json_str = content[start_idx:end_idx+1]
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as e:
            return [], "failed", f"Could not parse the AI model's response as JSON: {e}"

        raw_positions = data.get("positions", [])

        if not raw_positions:
            llm_reason = data.get("message", "")
            return [], "partial", (
                "No FRTB-relevant market risk positions were identified in this document. "
                + (f"AI reason: {llm_reason} " if llm_reason else "")
                + "Please upload a bank trading book disclosure or Pillar 3 market risk annex "
                "that contains sensitivity tables for GIRR, Equity, FX, CSR, or Commodity risk."
            )

        valid_positions: List[Dict[str, Any]] = []
        skipped = 0
        for p in raw_positions:
            try:
                # Normalise numeric fields that the LLM may return as strings
                for key in ["sensitivity", "notional"]:
                    if key in p and isinstance(p[key], str):
                        p[key] = float(p[key].replace(",", "").replace("$", "").strip())

                pos = PortfolioPosition(**p)
                valid_positions.append(pos.model_dump())
            except Exception as ve:
                # Drop the invalid row and record how many were skipped
                logger.warning(f"Skipping invalid position row (validation error: {ve}): {p}")
                skipped += 1

        if not valid_positions:
            return [], "failed", (
                f"The AI extracted {len(raw_positions)} position row(s) from the PDF, "
                "but none passed schema validation (missing required fields such as "
                "risk_class, bucket, sensitivity). "
                "Please verify the document contains FRTB-compatible market risk tables."
            )

        skip_note = f" ({skipped} malformed row(s) were skipped)" if skipped else ""
        return valid_positions, "success", f"Extraction successful{skip_note}"

    except Exception as e:
        logger.error(f"Unexpected error extracting portfolio tables: {e}")
        return [], "failed", f"An unexpected error occurred during extraction: {e}"

