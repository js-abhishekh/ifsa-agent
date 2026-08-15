"""
src/quant/drc.py

FRTB-SA Default Risk Charge (MAR22).

DRC is NOT correlation-based aggregation — it uses a jump-to-default (JTD)
banding approach:
  1. Compute JTD loss for each obligor.
  2. Net long and short JTD within the same obligor across instruments (subject to
     a 0.5 credit factor for short positions on non-securitisation exposures).
  3. Group net JTD into credit quality buckets (corporates / sovereigns / local govt).
  4. Within each bucket, apply a risk weight (LGD × PD) and aggregate as DRC_b.
  5. DRC = Σ DRC_b  (no cross-bucket netting).

Inputs (via PortfolioPosition):
  - notional   : gross JTD loss (absolute value; sign determined by long/short)
  - sensitivity: used as net signed JTD (positive = long, negative = short)
  - bucket     : credit quality bucket ("IG_Corporate", "HY_Corporate",
                 "IG_Sovereign", "HY_Sovereign", "IG_Local", "HY_Local")
  - risk_factor: obligor identifier (for netting)
"""
from src.graph.state import PortfolioPosition, ExtractedLogic, CalculatedMetric

# Default risk weights (LGD × PD approximation) per credit quality bucket
# Source: MAR22.9 (non-securitisation)
DEFAULT_DRC_RISK_WEIGHTS: dict[str, float] = {
    "IG_Corporate":  0.03,
    "HY_Corporate":  0.12,
    "IG_Sovereign":  0.015,
    "HY_Sovereign":  0.06,
    "IG_Local":      0.03,
    "HY_Local":      0.12,
    "NR":            0.15,   # Non-rated: treated as HY
    "default":       0.12,
}

SHORT_CREDIT_FACTOR = 0.5   # MAR22.11 — 50% credit for short non-sec positions


def _net_jtd_by_obligor(positions: list[PortfolioPosition]) -> dict[str, float]:
    """Net JTD exposures by obligor (risk_factor field).

    Shorts receive 50% credit per MAR22.11.
    Longs are recognised in full (sensitivity > 0).
    """
    net: dict[str, float] = {}
    for p in positions:
        jdt = p.sensitivity  # signed: positive = long, negative = short
        # Apply short credit factor
        effective_jtd = jdt if jdt >= 0 else jdt * SHORT_CREDIT_FACTOR
        net[p.risk_factor] = net.get(p.risk_factor, 0.0) + effective_jtd
    return net


def drc_charge(
    positions: list[PortfolioPosition],
    logic: ExtractedLogic,
) -> CalculatedMetric:
    """Compute the Default Risk Charge (MAR22).

    DRC = Σ_b max(RW_b × net_JTD_b, 0)
    No cross-bucket netting is permitted.
    """
    # Use extracted risk weights if available; fall back to static defaults
    rw_table = logic.risk_weights if logic.risk_weights else DEFAULT_DRC_RISK_WEIGHTS

    # Net JTD per obligor
    net_jtd = _net_jtd_by_obligor(positions)

    # Map obligors to their bucket (from positions)
    obligor_bucket: dict[str, str] = {p.risk_factor: p.bucket for p in positions}

    # Aggregate net JTD by bucket
    bucket_net: dict[str, float] = {}
    for obligor, jtd in net_jtd.items():
        bucket = obligor_bucket.get(obligor, "default")
        bucket_net[bucket] = bucket_net.get(bucket, 0.0) + jtd

    # Apply risk weights — only long-side (positive net JTD) attracts capital
    bucket_drc: dict[str, float] = {}
    for bucket, net in bucket_net.items():
        rw = rw_table.get(bucket) or rw_table.get("default", 0.12)
        bucket_drc[bucket] = max(rw * net, 0.0)

    aggregated = sum(bucket_drc.values())

    return CalculatedMetric(
        risk_class=logic.risk_class,
        metric_name="drc_charge",
        bucket_level=bucket_drc,
        aggregated_value=aggregated,
        formula_used="MAR22 JTD banding + 50% short credit factor",
    )
