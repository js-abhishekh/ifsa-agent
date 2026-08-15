"""
src/quant/rrao.py

FRTB-SA Residual Risk Add-On (MAR23).

RRAO is the simplest of the three FRTB SA charge components:
  RRAO = Σ_i  notional_i × add_on_rate_i

Add-on rates (MAR23.6):
  - Exotic underlying instruments:              1.0% (0.01) of gross notional
  - Other residual-risk instruments (gap risk,  0.1% (0.001) of gross notional
    correlation risk, behavioural risk, etc.)

Instruments eligible for RRAO:
  - Instruments with non-linear payoffs not captured by delta/vega/curvature
  - Instruments referencing exotic underlyings (longevity, weather, NDF correlation, …)

In the PortfolioPosition model we reuse:
  - notional    : gross notional of the instrument
  - risk_factor : "exotic" | "other_residual"  (determines the add-on rate)
  - bucket      : optional grouping tag (not used in aggregation here)
"""
from src.graph.state import PortfolioPosition, ExtractedLogic, CalculatedMetric

EXOTIC_RATE          = 0.010   # 1.0% MAR23.6(a)
OTHER_RESIDUAL_RATE  = 0.001   # 0.1% MAR23.6(b)


def _addon_rate(risk_factor: str, logic_rw: dict[str, float]) -> float:
    """Resolve the RRAO add-on rate for a given risk_factor.

    Precedence: extracted logic → Basel default.
    """
    if risk_factor in logic_rw:
        return logic_rw[risk_factor]
    if risk_factor.lower() == "exotic":
        return EXOTIC_RATE
    return OTHER_RESIDUAL_RATE


def rrao_charge(
    positions: list[PortfolioPosition],
    logic: ExtractedLogic,
) -> CalculatedMetric:
    """Compute the Residual Risk Add-On (MAR23).

    RRAO = Σ |notional_i| × add_on_rate_i
    Notional must be set on each position; positions with notional=None are skipped.
    """
    bucket_charges: dict[str, float] = {}
    total = 0.0

    for p in positions:
        if p.notional is None:
            continue
        rate = _addon_rate(p.risk_factor, logic.risk_weights)
        charge = abs(p.notional) * rate
        bucket_charges[p.bucket] = bucket_charges.get(p.bucket, 0.0) + charge
        total += charge

    return CalculatedMetric(
        risk_class=logic.risk_class,
        metric_name="rrao_charge",
        bucket_level=bucket_charges,
        aggregated_value=total,
        formula_used="MAR23 gross notional × add-on rate (1%/0.1%)",
    )
