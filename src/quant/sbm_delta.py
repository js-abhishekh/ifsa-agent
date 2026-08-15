"""
src/quant/sbm_delta.py

FRTB-SA Sensitivity-Based Method — Delta Risk Charge (MAR21.4).

Formula hierarchy:
  1. Weighted sensitivity:  WS_k = s_k × RW_k
  2. Bucket aggregation:    K_b  = sqrt(max(0, Σ WS_k² + Σ_{k≠l} ρ_kl WS_k WS_l))
  3. Cross-bucket charge:   Delta = sqrt(max(0, Σ K_b² + Σ_{b≠c} γ_bc S_b S_c))
     where S_b = max(min(Σ WS_k, K_b), -K_b)  (capital-floored bucket sum)

The math is entirely deterministic; no LLM calls occur here.
"""
import math
from src.graph.state import PortfolioPosition, ExtractedLogic, CalculatedMetric


# ── Step 1: Weighted sensitivities ────────────────────────────────────────────
def compute_weighted_sensitivities(
    positions: list[PortfolioPosition],
    risk_weights: dict[str, float],
) -> dict[str, float]:
    """Return {instrument_id: WS_k} for every position.

    Lookup order: risk_factor → bucket → fallback "default".

    Raises:
        KeyError: if no risk weight can be resolved for a position.
    """
    ws: dict[str, float] = {}
    for p in positions:
        rw = (
            risk_weights.get(p.risk_factor)
            or risk_weights.get(p.bucket)
            or risk_weights.get("default")
        )
        if rw is None:
            raise KeyError(
                f"No risk weight for instrument '{p.instrument_id}' "
                f"(risk_factor='{p.risk_factor}', bucket='{p.bucket}')"
            )
        ws[p.instrument_id] = p.sensitivity * rw
    return ws


# ── Step 2: Within-bucket K_b ─────────────────────────────────────────────────
def bucket_kb(
    positions: list[PortfolioPosition],
    weighted_sens: dict[str, float],
    correlations: dict[str, float],
) -> float:
    """Compute K_b for a single bucket.

    K_b = sqrt(max(0, Σ WS_k² + Σ_{k≠l} ρ_kl WS_k WS_l))

    Correlation lookup order for pair (k, l):
      "{rf_k}_{rf_l}" → "{rf_l}_{rf_k}" → "rho_intra_default" → "rho_default" → 1.0
    """
    ids = [p.instrument_id for p in positions]
    rfs = {p.instrument_id: p.risk_factor for p in positions}

    sum_sq = sum(weighted_sens[i] ** 2 for i in ids)

    cross_term = 0.0
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
            cross_term += 2 * rho * weighted_sens[k] * weighted_sens[l]

    return math.sqrt(max(sum_sq + cross_term, 0.0))


# ── Step 3: Cross-bucket aggregation ─────────────────────────────────────────
def _bucket_sb(
    bucket_positions: list[PortfolioPosition],
    weighted_sens: dict[str, float],
    kb: float,
) -> float:
    """S_b = max(min(Σ WS_k, K_b), -K_b) — the capital-floored bucket sum."""
    raw_sum = sum(weighted_sens[p.instrument_id] for p in bucket_positions)
    return max(min(raw_sum, kb), -kb)


# ── Public entry point ────────────────────────────────────────────────────────
def sbm_delta_charge(
    positions: list[PortfolioPosition],
    logic: ExtractedLogic,
) -> CalculatedMetric:
    """Compute the SBM Delta risk charge for one risk class.

    Args:
        positions: All positions for the risk class.
        logic:     Extracted regulatory logic (risk weights, correlations).

    Returns:
        CalculatedMetric with per-bucket K_b values and the final aggregated charge.
    """
    # Group positions by bucket
    by_bucket: dict[str, list[PortfolioPosition]] = {}
    for p in positions:
        by_bucket.setdefault(p.bucket, []).append(p)

    bucket_kb_values: dict[str, float] = {}
    bucket_sb_values: dict[str, float] = {}

    for bucket, bpos in by_bucket.items():
        ws = compute_weighted_sensitivities(bpos, logic.risk_weights)
        kb = bucket_kb(bpos, ws, logic.correlations)
        sb = _bucket_sb(bpos, ws, kb)
        bucket_kb_values[bucket] = kb
        bucket_sb_values[bucket] = sb

    # Cross-bucket aggregation
    gamma = logic.correlations.get("gamma_bc") or logic.correlations.get("gamma_bc_default", 0.0)
    buckets = list(bucket_kb_values.keys())
    kb_vals = [bucket_kb_values[b] for b in buckets]
    sb_vals = [bucket_sb_values[b] for b in buckets]

    sum_sq = sum(k ** 2 for k in kb_vals)
    cross = 0.0
    for i in range(len(buckets)):
        for j in range(i + 1, len(buckets)):
            cross += 2 * gamma * sb_vals[i] * sb_vals[j]

    aggregated = math.sqrt(max(sum_sq + cross, 0.0))

    return CalculatedMetric(
        risk_class=logic.risk_class,
        metric_name="delta_charge",
        bucket_level=bucket_kb_values,
        aggregated_value=aggregated,
        formula_used="MAR21.4 Kb aggregation + cross-bucket gamma",
    )
