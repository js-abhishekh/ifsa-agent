import pymupdf
import json
import logging
import asyncio
from typing import Tuple, List, Dict, Any
from pathlib import Path
from src.config import LLM_MODEL, GEMINI_API_KEY, OPENAI_API_KEY, OPENROUTER_API_KEY, LLM_BASE_URL
from src.graph.state import PortfolioPosition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

logger = logging.getLogger(__name__)

def use_sample_portfolio() -> List[Dict[str, Any]]:
    # Loads data/pnb_portfolio.json as a fallback (it's a JSON array)
    sample_path = Path("data/pnb_portfolio.json")
    try:
        if sample_path.exists():
            with open(sample_path, "r") as f:
                data = json.load(f)
                # It's either a list directly or {"positions": [...]}
                return data if isinstance(data, list) else data.get("positions", [])
        return []
    except Exception as e:
        logger.error(f"Error loading sample portfolio: {e}")
        return []

async def extract_portfolio_from_pdf(file_path: str) -> Tuple[List[Dict[str, Any]], str, str]:
    try:
        def _read_pdf():
            tables_context = ""
            doc = pymupdf.open(file_path)
            for i, page in enumerate(doc):
                tabs = page.find_tables()
                if tabs and tabs.tables:
                    for t_idx, tab in enumerate(tabs.tables):
                        df = tab.extract()
                        if df:
                            tables_context += f"\n--- Table {t_idx+1} on Page {i+1} ---\n"
                            for row in df:
                                clean_row = [str(x).strip().replace('\n', ' ') if x is not None else '' for x in row]
                                tables_context += " | ".join(clean_row) + "\n"
            doc.close()
            return tables_context
            
        try:
            tables_text = await asyncio.to_thread(_read_pdf)
        except Exception as e:
            return [], "failed", f"Failed to read PDF tables: {e}"

        if not tables_text.strip():
            return [], "failed", "No tables found in the PDF document."

        # Keep within limits, tables usually take less space than full text
        MAX_CHARS = 150000
        excerpt = tables_text[:MAX_CHARS]

        llm = ChatOpenAI(
            model=LLM_MODEL,
            api_key=GEMINI_API_KEY or OPENAI_API_KEY or OPENROUTER_API_KEY or "dummy",
            base_url=LLM_BASE_URL,
            temperature=0,
            request_timeout=120,
        )

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

        response = await llm.ainvoke(messages)
        content = response.content

        start_idx = content.find('{')
        end_idx = content.rfind('}')
        if start_idx != -1 and end_idx != -1:
            json_str = content[start_idx:end_idx+1]
            data = json.loads(json_str)
            positions = data.get("positions", [])
            
            if not positions:
                msg = data.get("message", "No granular position data found in PDF tables.")
                return [], "partial", msg
            
            valid_positions = []
            for p in positions:
                try:
                    # Clean float strings
                    for key in ['sensitivity', 'notional']:
                        if key in p and isinstance(p[key], str):
                            p[key] = float(p[key].replace(',', '').replace('$', '').strip())
                    
                    # Validates against PortfolioPosition model
                    pos = PortfolioPosition(**p)
                    valid_positions.append(pos.model_dump())
                except Exception as ve:
                    valid_positions.append(p)  # fallback to dict
            
            return valid_positions, "success", "Extraction successful"
        else:
            return [], "failed", "LLM did not return valid JSON."
            
    except Exception as e:
        logger.error(f"Error extracting portfolio tables: {e}")
        return [], "failed", f"An error occurred during extraction: {e}"
