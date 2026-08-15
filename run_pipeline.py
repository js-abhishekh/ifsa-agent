"""
run_pipeline.py — CLI entrypoint for the FRTB-SA LangGraph pipeline.

Usage:
  python run_pipeline.py                      # uses built-in mock portfolio
  python run_pipeline.py --portfolio portfolio.json

The mock portfolio contains:
  - Two GIRR (IRS) positions in the USD bucket (5Y long, 10Y short)
  - One Equity option position (EM large-cap, RELIANCE)

Without an OpenAI API key set in .env, the pipeline automatically falls
back to the static Basel Annex tables for risk weights and correlations.
"""
import sys
import argparse
import json

# Ensure stdout can print Unicode emojis (like 🚩) on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from src.graph.build_graph  import build_frtb_graph
from src.graph.state        import PortfolioPosition


# ── Mock portfolio (IRS + Equity) ─────────────────────────────────────────────
def mock_irs_equity_portfolio() -> list[PortfolioPosition]:
    return [
        PortfolioPosition(
            instrument_id="IRS_001", risk_class="GIRR",
            bucket="USD", risk_factor="5Y",
            sensitivity=125_000.0, currency="USD",
        ),
        PortfolioPosition(
            instrument_id="IRS_002", risk_class="GIRR",
            bucket="USD", risk_factor="10Y",
            sensitivity=-80_000.0, currency="USD",
        ),
        PortfolioPosition(
            instrument_id="EQOPT_001", risk_class="Equity",
            bucket="EM_LargeCap", risk_factor="RELIANCE",
            sensitivity=45_000.0, currency="INR",
        ),
    ]


def load_portfolio_from_json(path: str) -> list[PortfolioPosition]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [PortfolioPosition(**item) for item in data]


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="FRTB-SA capital charge pipeline")
    parser.add_argument(
        "--portfolio", default=None,
        help="Path to a JSON file containing a list of PortfolioPosition dicts",
    )
    parser.add_argument(
        "--pdf", default=None,
        help="Path to a bank disclosure PDF for automated auditing",
    )
    parser.add_argument(
        "--max_retries", type=int, default=2,
        help="Maximum LLM retrieval retry attempts (default: 2)",
    )
    args = parser.parse_args()

    portfolio = (
        load_portfolio_from_json(args.portfolio)
        if args.portfolio
        else mock_irs_equity_portfolio()
    )

    print(f"\n{'='*60}")
    print("  FRTB-SA Agentic Pipeline")
    print(f"{'='*60}")
    print(f"  Portfolio positions : {len(portfolio)}")
    print(f"  Risk classes        : {sorted({p.risk_class for p in portfolio})}")
    print(f"  Max retries         : {args.max_retries}")
    print(f"{'='*60}\n")

    app = build_frtb_graph()

    initial_state = {
        "user_query": "Compute FRTB-SA capital charges for the attached portfolio",
        "document_path": args.pdf,
        "portfolio_inputs": portfolio,
        "retry_count":  0,
        "max_retries":  args.max_retries,
        "validation_errors": [],
        "audit_flags": [],
    }

    import asyncio
    final_state = asyncio.run(app.ainvoke(initial_state))

    # ── Output ──────────────────────────────────────────────────────────────
    audit_flags = final_state.get("audit_flags", [])
    if audit_flags:
        print("\n" + "="*60)
        filename = args.pdf.split("/")[-1].split("\\")[-1] if args.pdf else "Document"
        print(f"🚩 FRTB-SA Regulatory Audit Flags for {filename}")
        print("="*60)
        for i, flag in enumerate(audit_flags, 1):
            # The flag comes pre-formatted from the node
            lines = flag.split("\n", 1)
            if len(lines) == 2:
                print(f"{i}. {lines[0]}")
                print(f"{lines[1]}\n")
            else:
                print(f"{i}. {flag}\n")

    print("\n=== FINAL COMPLIANCE SUMMARY ===")
    print(final_state.get("final_compliance_summary") or "No summary produced.")

    print("\n=== CALCULATED METRICS ===")
    for m in final_state.get("calculated_metrics", []):
        print(f"  {m.risk_class:15s} | {m.metric_name:20s} | aggregated = {m.aggregated_value:>15,.2f}")
        for bucket, charge in m.bucket_level.items():
            print(f"    bucket [{bucket}] = {charge:,.2f}")

    blocking = [e for e in final_state.get("validation_errors", []) if e.severity == "blocking"]
    warnings  = [e for e in final_state.get("validation_errors", []) if e.severity == "warning"]

    if blocking:
        print("\n=== BLOCKING ERRORS ===")
        for e in blocking:
            print(f"  [BLOCKING] ({e.node}) {e.message}")

    if warnings:
        print("\n=== WARNINGS ===")
        for e in warnings:
            print(f"  [WARN] ({e.node}) {e.message}")

    return final_state


if __name__ == "__main__":
    main()
