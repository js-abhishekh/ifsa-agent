"""
tests/test_quant_core.py

Unit tests for the deterministic quant core, validated against Basel BCBS
worked examples (FRTB QIS documentation).

Test structure:
  TestWeightedSensitivities  — WS_k = s × RW
  TestBucketKb               — K_b formula with known WS and rho
  TestCrossBucketDelta       — cross-bucket aggregation with gamma
  TestVegaCharge             — vega risk charge (flat VRW=55%)
  TestCurvatureCharge        — curvature using pre-computed CVR values
  TestDRC                    — DRC banding + short credit factor
  TestRRAO                   — RRAO flat add-on rates
  TestEdgeCases              — zero/negative sensitivities, missing risk weights

All expected values are computed analytically and cross-checked with a
hand-calculation for the 2-position GIRR example from MAR21 worked examples.
"""
import math
import pytest
from src.graph.state       import PortfolioPosition, ExtractedLogic, CalculationParameter
from src.quant.sbm_delta   import (
    compute_weighted_sensitivities, bucket_kb, sbm_delta_charge
)
from src.quant.sbm_vega    import sbm_vega_charge
from src.quant.sbm_curvature import sbm_curvature_charge
from src.quant.drc         import drc_charge
from src.quant.rrao        import rrao_charge


# ── Helpers ───────────────────────────────────────────────────────────────────
def _girr_logic(rw: dict, corr: dict) -> ExtractedLogic:
    return ExtractedLogic(
        risk_class="GIRR",
        formula_ref="test",
        risk_weights=rw,
        correlations=corr,
        is_complete=True,
    )

def _eq_logic(rw: dict, corr: dict) -> ExtractedLogic:
    return ExtractedLogic(
        risk_class="Equity",
        formula_ref="test",
        risk_weights=rw,
        correlations=corr,
        is_complete=True,
    )


# ── TestWeightedSensitivities ──────────────────────────────────────────────────
class TestWeightedSensitivities:
    def test_basic(self):
        pos = [PortfolioPosition(
            instrument_id="A", risk_class="GIRR", bucket="USD",
            risk_factor="5Y", sensitivity=100.0,
        )]
        ws = compute_weighted_sensitivities(pos, {"5Y": 0.011})
        assert ws["A"] == pytest.approx(1.1)

    def test_bucket_fallback(self):
        """Falls back to bucket key when risk_factor not found."""
        pos = [PortfolioPosition(
            instrument_id="B", risk_class="Equity", bucket="EM_LargeCap",
            risk_factor="UNKNOWN_STOCK", sensitivity=50.0,
        )]
        ws = compute_weighted_sensitivities(pos, {"EM_LargeCap": 0.55})
        assert ws["B"] == pytest.approx(27.5)

    def test_default_fallback(self):
        """Falls back to 'default' key."""
        pos = [PortfolioPosition(
            instrument_id="C", risk_class="FX", bucket="USD_EUR",
            risk_factor="USD_EUR", sensitivity=200.0,
        )]
        ws = compute_weighted_sensitivities(pos, {"default": 0.15})
        assert ws["C"] == pytest.approx(30.0)

    def test_missing_key_raises(self):
        pos = [PortfolioPosition(
            instrument_id="D", risk_class="GIRR", bucket="USD",
            risk_factor="42Y", sensitivity=100.0,
        )]
        with pytest.raises(KeyError):
            compute_weighted_sensitivities(pos, {"5Y": 0.011})


# ── TestBucketKb ──────────────────────────────────────────────────────────────
class TestBucketKb:
    """MAR21.4: K_b = sqrt(max(0, Σ WS_k² + Σ_{k≠l} ρ_kl WS_k WS_l))"""

    def _make_positions(self, ids, rf_map):
        return [
            PortfolioPosition(instrument_id=i, risk_class="GIRR", bucket="USD",
                              risk_factor=rf_map[i], sensitivity=1.0)
            for i in ids
        ]

    def test_single_position(self):
        """K_b with one position = |WS_k|."""
        pos = self._make_positions(["A"], {"A": "5Y"})
        ws = {"A": 1100.0}
        kb = bucket_kb(pos, ws, {})
        assert kb == pytest.approx(1100.0)

    def test_perfectly_correlated(self):
        """Two positions, rho=1 → K_b = |WS_1 + WS_2|."""
        pos = self._make_positions(["A", "B"], {"A": "5Y", "B": "10Y"})
        ws = {"A": 1000.0, "B": 500.0}
        kb = bucket_kb(pos, ws, {"5Y_10Y": 1.0})
        assert kb == pytest.approx(1500.0)

    def test_anti_correlated(self):
        """rho=-1, equal WS → K_b = 0."""
        pos = self._make_positions(["A", "B"], {"A": "5Y", "B": "10Y"})
        ws = {"A": 800.0, "B": 800.0}
        kb = bucket_kb(pos, ws, {"5Y_10Y": -1.0})
        assert kb == pytest.approx(0.0)

    def test_partial_correlation(self):
        """Analytical: WS=(3,4), rho=0.5 → inner=9+16+12=37 → K_b=sqrt(37)"""
        pos = self._make_positions(["A", "B"], {"A": "5Y", "B": "10Y"})
        ws = {"A": 3.0, "B": 4.0}
        kb = bucket_kb(pos, ws, {"rho_default": 0.5})
        assert kb == pytest.approx(math.sqrt(37.0))

    def test_irs_book_worked_example(self):
        """GIRR IRS book: 5Y WS=1375, 10Y WS=-880, rho(5Y,10Y)=0.905
           inner = 1375² + (-880)² + 2×0.905×1375×(-880)
                 = 1890625 + 774400 - 2186100
                 = 478925
           K_b = sqrt(478925) ≈ 692.04
        """
        pos = [
            PortfolioPosition(instrument_id="IRS_001", risk_class="GIRR",
                              bucket="USD", risk_factor="5Y", sensitivity=125_000.0),
            PortfolioPosition(instrument_id="IRS_002", risk_class="GIRR",
                              bucket="USD", risk_factor="10Y", sensitivity=-80_000.0),
        ]
        rw   = {"5Y": 0.011, "10Y": 0.011}
        corr = {"5Y_10Y": 0.905}
        ws   = compute_weighted_sensitivities(pos, rw)
        kb   = bucket_kb(pos, ws, corr)
        # WS_5Y = 125000×0.011 = 1375, WS_10Y = -80000×0.011 = -880
        inner = 1375**2 + 880**2 + 2 * 0.905 * 1375 * (-880)
        assert kb == pytest.approx(math.sqrt(max(inner, 0.0)), rel=1e-4)

    def test_statutory_equity_correlation_fallback(self):
        """When no correlation is provided, Equity distinct names use Basel MAR21.76 statutory 0.25 instead of 1.0."""
        pos = [
            PortfolioPosition(instrument_id="EQ_1", risk_class="Equity", bucket="EM_LargeCap", risk_factor="TATA", sensitivity=100.0),
            PortfolioPosition(instrument_id="EQ_2", risk_class="Equity", bucket="EM_LargeCap", risk_factor="INFY", sensitivity=100.0),
        ]
        ws = {"EQ_1": 55.0, "EQ_2": 55.0}  # assuming 0.55 RW
        # Empty correlations dict
        kb = bucket_kb(pos, ws, {}, risk_class="Equity")
        # inner = 55^2 + 55^2 + 2 * 0.25 * 55 * 55 = 3025 + 3025 + 1512.5 = 7562.5
        expected = math.sqrt(7562.5)
        assert kb == pytest.approx(expected, rel=1e-4)

    def test_statutory_csr_correlation_fallback(self):
        """When no correlation is provided, CSR distinct issuers use Basel MAR21.58 statutory 0.35 instead of 1.0."""
        pos = [
            PortfolioPosition(instrument_id="BOND_1", risk_class="CSR_NonSec", bucket="IG_Corp", risk_factor="ISSUER_A", sensitivity=1000.0),
            PortfolioPosition(instrument_id="BOND_2", risk_class="CSR_NonSec", bucket="IG_Corp", risk_factor="ISSUER_B", sensitivity=1000.0),
        ]
        ws = {"BOND_1": 20.0, "BOND_2": 20.0}
        kb = bucket_kb(pos, ws, {}, risk_class="CSR_NonSec")
        # inner = 20^2 + 20^2 + 2 * 0.35 * 20 * 20 = 400 + 400 + 280 = 1080
        expected = math.sqrt(1080.0)
        assert kb == pytest.approx(expected, rel=1e-4)

    def test_zero_correlation_not_bypassed(self):
        """An explicit rho=0.0 in the correlations dict must be honoured, not treated as missing.
        Old or-chain bug: correlations.get("5Y_10Y") == 0.0 was falsy, so it would
        fall through to the statutory default (0.80 for GIRR). The is-None fix prevents this.
        """
        pos = [
            PortfolioPosition(instrument_id="A", risk_class="GIRR", bucket="USD", risk_factor="5Y", sensitivity=100.0),
            PortfolioPosition(instrument_id="B", risk_class="GIRR", bucket="USD", risk_factor="10Y", sensitivity=100.0),
        ]
        ws = {"A": 1.0, "B": 1.0}
        # Explicit zero correlation between the two tenors → perfect offset → K_b = 0
        kb = bucket_kb(pos, ws, {"5Y_10Y": 0.0}, risk_class="GIRR")
        # inner = 1^2 + 1^2 + 2*0.0*1*1 = 2 → K_b = sqrt(2)
        assert kb == pytest.approx(math.sqrt(2.0), rel=1e-4)



# ── TestCrossBucketDelta ──────────────────────────────────────────────────────
class TestCrossBucketDelta:
    def test_single_bucket_equals_kb(self):
        """With one bucket, cross-bucket term is 0, so Delta = K_b."""
        pos = [PortfolioPosition(
            instrument_id="IRS_001", risk_class="GIRR",
            bucket="USD", risk_factor="5Y", sensitivity=125_000.0,
        )]
        logic = _girr_logic({"5Y": 0.011}, {})
        metric = sbm_delta_charge(pos, logic)
        assert metric.aggregated_value == pytest.approx(125_000.0 * 0.011, rel=1e-4)

    def test_two_bucket_gamma_zero(self):
        """gamma=0 → Delta = sqrt(K_b1² + K_b2²)."""
        pos = [
            PortfolioPosition(instrument_id="A", risk_class="GIRR",
                              bucket="USD", risk_factor="5Y", sensitivity=100.0),
            PortfolioPosition(instrument_id="B", risk_class="GIRR",
                              bucket="EUR", risk_factor="5Y", sensitivity=100.0),
        ]
        logic = _girr_logic({"5Y": 1.0}, {"gamma_bc": 0.0})
        metric = sbm_delta_charge(pos, logic)
        # K_b(USD)=100, K_b(EUR)=100, gamma=0 → sqrt(10000+10000) = 141.42
        assert metric.aggregated_value == pytest.approx(math.sqrt(20000), rel=1e-4)

    def test_metric_name_and_formula(self):
        pos = [PortfolioPosition(
            instrument_id="X", risk_class="Equity",
            bucket="EM_LargeCap", risk_factor="RELIANCE", sensitivity=45_000.0,
        )]
        logic = _eq_logic({"EM_LargeCap": 0.55}, {})
        metric = sbm_delta_charge(pos, logic)
        assert metric.metric_name == "delta_charge"
        assert "MAR21" in metric.formula_used
        assert metric.risk_class == "Equity"


# ── TestVegaCharge ────────────────────────────────────────────────────────────
class TestVegaCharge:
    def test_flat_vrw(self):
        """Vega with flat 55% VRW and single position."""
        pos = [PortfolioPosition(
            instrument_id="OPT_001", risk_class="GIRR",
            bucket="USD", risk_factor="5Y", sensitivity=10_000.0,
        )]
        logic = _girr_logic({}, {})   # no explicit vega RW → uses flat 55%
        metric = sbm_vega_charge(pos, logic)
        assert metric.metric_name == "vega_charge"
        assert metric.aggregated_value == pytest.approx(10_000.0 * 0.55, rel=1e-4)


# ── TestCurvatureCharge ───────────────────────────────────────────────────────
class TestCurvatureCharge:
    def test_no_loss_positions(self):
        """cvr_up and cvr_down both positive → CVR_k=0 → charge=0."""
        pos = [PortfolioPosition(
            instrument_id="OPT_001", risk_class="Equity",
            bucket="EM_LargeCap", risk_factor="RELIANCE",
            sensitivity=0.0, cvr_up=500.0, cvr_down=300.0,
        )]
        logic = _eq_logic({}, {})
        metric = sbm_curvature_charge(pos, logic)
        assert metric.aggregated_value == pytest.approx(0.0)

    def test_both_scenarios_loss(self):
        """cvr_up=-200, cvr_down=-150 → CVR_k = 200+150 = 350."""
        pos = [PortfolioPosition(
            instrument_id="OPT_001", risk_class="Equity",
            bucket="EM_LargeCap", risk_factor="RELIANCE",
            sensitivity=0.0, cvr_up=-200.0, cvr_down=-150.0,
        )]
        logic = _eq_logic({}, {})
        metric = sbm_curvature_charge(pos, logic)
        assert metric.aggregated_value == pytest.approx(350.0)


# ── TestDRC ───────────────────────────────────────────────────────────────────
class TestDRC:
    def test_long_only(self):
        """Single long IG_Corporate position: DRC = RW × JTD = 0.03 × 1M."""
        pos = [PortfolioPosition(
            instrument_id="BOND_001", risk_class="CSR_NonSec",
            bucket="IG_Corporate", risk_factor="ISSUER_A",
            sensitivity=1_000_000.0,
        )]
        logic = ExtractedLogic(
            risk_class="CSR_NonSec", formula_ref="test",
            risk_weights={"IG_Corporate": 0.03},
            correlations={}, is_complete=True,
        )
        metric = drc_charge(pos, logic)
        assert metric.aggregated_value == pytest.approx(30_000.0, rel=1e-4)

    def test_short_credit_factor(self):
        """Short position gets 50% credit: effective JTD = -500k → net=+1M-500k=500k → DRC=15k."""
        pos = [
            PortfolioPosition(
                instrument_id="BOND_LONG", risk_class="CSR_NonSec",
                bucket="IG_Corporate", risk_factor="ISSUER_A",
                sensitivity=1_000_000.0,
            ),
            PortfolioPosition(
                instrument_id="BOND_SHORT", risk_class="CSR_NonSec",
                bucket="IG_Corporate", risk_factor="ISSUER_A",
                sensitivity=-1_000_000.0,
            ),
        ]
        logic = ExtractedLogic(
            risk_class="CSR_NonSec", formula_ref="test",
            risk_weights={"IG_Corporate": 0.03},
            correlations={}, is_complete=True,
        )
        metric = drc_charge(pos, logic)
        # Net JTD = 1M + (-1M × 0.5) = +500k; DRC = 0.03 × 500k = 15k
        assert metric.aggregated_value == pytest.approx(15_000.0, rel=1e-4)


# ── TestRRAO ──────────────────────────────────────────────────────────────────
class TestRRAO:
    def test_exotic(self):
        """Exotic: 1% of notional."""
        pos = [PortfolioPosition(
            instrument_id="EXOTIC_001", risk_class="Equity",
            bucket="exotic", risk_factor="exotic",
            sensitivity=0.0, notional=10_000_000.0,
        )]
        logic = _eq_logic({}, {})
        metric = rrao_charge(pos, logic)
        assert metric.aggregated_value == pytest.approx(100_000.0)

    def test_other_residual(self):
        """Other residual: 0.1% of notional."""
        pos = [PortfolioPosition(
            instrument_id="RESID_001", risk_class="GIRR",
            bucket="other", risk_factor="other_residual",
            sensitivity=0.0, notional=5_000_000.0,
        )]
        logic = _girr_logic({}, {})
        metric = rrao_charge(pos, logic)
        assert metric.aggregated_value == pytest.approx(5_000.0)

    def test_no_notional_skipped(self):
        """Positions without notional are skipped → charge=0."""
        pos = [PortfolioPosition(
            instrument_id="NO_NOTIONAL", risk_class="Equity",
            bucket="exotic", risk_factor="exotic", sensitivity=0.0,
        )]
        logic = _eq_logic({}, {})
        metric = rrao_charge(pos, logic)
        assert metric.aggregated_value == pytest.approx(0.0)


# ── TestEdgeCases ─────────────────────────────────────────────────────────────
class TestEdgeCases:
    def test_zero_sensitivity(self):
        pos = [PortfolioPosition(
            instrument_id="ZERO", risk_class="GIRR", bucket="USD",
            risk_factor="5Y", sensitivity=0.0,
        )]
        logic = _girr_logic({"5Y": 0.011}, {})
        metric = sbm_delta_charge(pos, logic)
        assert metric.aggregated_value == pytest.approx(0.0)

    def test_negative_sensitivity_kb_non_negative(self):
        """K_b must always be >= 0."""
        pos = [PortfolioPosition(
            instrument_id="SHORT", risk_class="GIRR", bucket="USD",
            risk_factor="5Y", sensitivity=-500_000.0,
        )]
        logic = _girr_logic({"5Y": 0.011}, {})
        metric = sbm_delta_charge(pos, logic)
        assert metric.aggregated_value >= 0.0

    def test_missing_risk_weight_raises(self):
        pos = [PortfolioPosition(
            instrument_id="UNKNOWN", risk_class="GIRR", bucket="USD",
            risk_factor="999Y", sensitivity=100.0,
        )]
        logic = _girr_logic({"5Y": 0.011}, {})
        with pytest.raises(KeyError):
            sbm_delta_charge(pos, logic)
