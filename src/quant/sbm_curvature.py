"""
src/quant/sbm_curvature.py

FRTB-SA Sensitivity-Based Method — Curvature Risk Charge (MAR21.6).

Curvature captures non-linear risk (second-order effects) for options.
Each position must carry cvr_up and cvr_down scenario P&L values.

Formula:
  CVR_k = -min(V(x_k + RW_k^curvature) - V(x_k) - s_k * RW_k^delta, 0)
        + -min(V(x_k - RW_k^curvature) - V(x_k) + s_k * RW_k^delta, 0)

In the sensitivity-input model (no full repricing), positions provide
pre-computed cvr_up / cvr_down values directly.

K_b (curvature) = sqrt(max(0, Σ CVR_k^2 + Σ_{k≠l} ρ_kl^2 CVR_k CVR_l))
Cross-bucket: sqrt(max(0, Σ K_b^2 + Σ_{b≠c} γ_bc^2 S_b S_c))
"""
import math
from src.graph.state import PortfolioPosition, ExtractedLogic, CalculatedMetric


def _cvr(position: PortfolioPosition) -> float:
    """Net curvature risk position CVR_k.

    Requires position.cvr_up and position.cvr_down to be set.
    Returns sum of downside losses (positive = capital charge).
    """
    up   = position.cvr_up   or 0.0
    down = position.cvr_down or 0.0
    return max(-up, 0.0) + max(-down, 0.0)


def _bucket_curvature_kb(
    positions: list[PortfolioPosition],
    correlations: dict[str, float],
) -> float:
    """K_b for curvature: uses ρ_kl² (squared correlations) per MAR21.6."""
    cvr_map = {p.instrument_id: _cvr(p) for p in positions}
    ids = [p.instrument_id for p in positions]
    rfs = {p.instrument_id: p.risk_factor for p in positions}

    sum_sq = sum(cvr_map[i] ** 2 for i in ids)

    cross = 0.0
    for k_idx in range(len(ids)):
        for l_idx in range(k_idx + 1, len(ids)):
            k, l = ids[k_idx], ids[l_idx]
            rf_k, rf_l = rfs[k], rfs[l]
            rho = (
                correlations.get(f"{rf_k}_{rf_l}")
                or correlations.get(f"{rf_l}_{rf_k}")
                or correlations.get("rho_intra_default")
                or correlations.get("rho_default", 1.0)
            )
            cross += 2 * (rho ** 2) * cvr_map[k] * cvr_map[l]

    return math.sqrt(max(sum_sq + cross, 0.0))


def sbm_curvature_charge(
    positions: list[PortfolioPosition],
    logic: ExtractedLogic,
) -> CalculatedMetric:
    """Compute the SBM Curvature risk charge (MAR21.6).

    Positions must have cvr_up / cvr_down populated; positions without
    those fields are skipped (treat as linear — zero curvature charge).
    """
    curvature_positions = [p for p in positions if p.cvr_up is not None or p.cvr_down is not None]

    by_bucket: dict[str, list[PortfolioPosition]] = {}
    for p in curvature_positions:
        by_bucket.setdefault(p.bucket, []).append(p)

    bucket_kb_values: dict[str, float] = {}
    bucket_sb_values: dict[str, float] = {}

    for bucket, bpos in by_bucket.items():
        kb = _bucket_curvature_kb(bpos, logic.correlations)
        raw_sum = sum(_cvr(p) for p in bpos)
        sb = max(min(raw_sum, kb), -kb)
        bucket_kb_values[bucket] = kb
        bucket_sb_values[bucket] = sb

    gamma = logic.correlations.get("gamma_bc") or logic.correlations.get("gamma_bc_default", 0.0)
    buckets = list(bucket_kb_values.keys())
    kb_vals = [bucket_kb_values[b] for b in buckets]
    sb_vals = [bucket_sb_values[b] for b in buckets]

    sum_sq = sum(k ** 2 for k in kb_vals)
    cross = sum(
        2 * (gamma ** 2) * sb_vals[i] * sb_vals[j]
        for i in range(len(buckets))
        for j in range(i + 1, len(buckets))
    )
    aggregated = math.sqrt(max(sum_sq + cross, 0.0))

    return CalculatedMetric(
        risk_class=logic.risk_class,
        metric_name="curvature_charge",
        bucket_level=bucket_kb_values,
        aggregated_value=aggregated,
        formula_used="MAR21.6 Curvature Kb (rho^2) + cross-bucket gamma^2",
    )
