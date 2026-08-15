"""
src/quant/sbm_vega.py

FRTB-SA Sensitivity-Based Method — Vega Risk Charge (MAR21.5).

Structure is identical to Delta but uses vega sensitivities as inputs
and applies vega risk weights (uniform 55% across all risk classes per MAR21.5).

Vega WS_k = vega_sensitivity_k × VRW_k
VRW_k = min(RW_k, RW_max) where RW_k is the delta risk weight for that bucket
and RW_max = 55% per MAR21.58.

For simplicity and regulatory conservatism we use a flat VRW = 0.55 here;
override via logic.risk_weights if the extracted logic contains bucket-specific values.
"""
import math
from src.graph.state import PortfolioPosition, ExtractedLogic, CalculatedMetric
from src.quant.sbm_delta import bucket_kb, _bucket_sb


FLAT_VEGA_RISK_WEIGHT = 0.55   # MAR21.5 cap


def compute_vega_weighted_sensitivities(
    positions: list[PortfolioPosition],
    risk_weights: dict[str, float],
) -> dict[str, float]:
    """Return {instrument_id: VWS_k} for vega positions.

    Lookup: risk_factor → bucket → "vega_default" → flat 55%.
    """
    ws: dict[str, float] = {}
    for p in positions:
        vrw = (
            risk_weights.get(f"vega_{p.risk_factor}")
            or risk_weights.get(f"vega_{p.bucket}")
            or risk_weights.get("vega_default")
            or FLAT_VEGA_RISK_WEIGHT
        )
        ws[p.instrument_id] = p.sensitivity * vrw
    return ws


def sbm_vega_charge(
    positions: list[PortfolioPosition],
    logic: ExtractedLogic,
) -> CalculatedMetric:
    """Compute the SBM Vega risk charge (MAR21.5)."""
    by_bucket: dict[str, list[PortfolioPosition]] = {}
    for p in positions:
        by_bucket.setdefault(p.bucket, []).append(p)

    bucket_kb_values: dict[str, float] = {}
    bucket_sb_values: dict[str, float] = {}

    for bucket, bpos in by_bucket.items():
        ws = compute_vega_weighted_sensitivities(bpos, logic.risk_weights)
        kb = bucket_kb(bpos, ws, logic.correlations)
        sb = _bucket_sb(bpos, ws, kb)
        bucket_kb_values[bucket] = kb
        bucket_sb_values[bucket] = sb

    gamma = logic.correlations.get("gamma_bc") or logic.correlations.get("gamma_bc_default", 0.0)
    buckets = list(bucket_kb_values.keys())
    kb_vals = [bucket_kb_values[b] for b in buckets]
    sb_vals = [bucket_sb_values[b] for b in buckets]

    sum_sq = sum(k ** 2 for k in kb_vals)
    cross = sum(
        2 * gamma * sb_vals[i] * sb_vals[j]
        for i in range(len(buckets))
        for j in range(i + 1, len(buckets))
    )
    aggregated = math.sqrt(max(sum_sq + cross, 0.0))

    return CalculatedMetric(
        risk_class=logic.risk_class,
        metric_name="vega_charge",
        bucket_level=bucket_kb_values,
        aggregated_value=aggregated,
        formula_used="MAR21.5 Vega Kb aggregation (VRW=55% cap)",
    )
