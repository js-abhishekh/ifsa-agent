"""
tests/test_logic_extractor.py

Unit tests for regulatory parameter cross-checking and binding in logic_extractor.
Validates that statutory Basel Annex numbers are strictly enforced and LLM hallucinations
are corrected with an audit trail.
"""
import pytest
from src.graph.state import ExtractedLogic, ValidationError
from src.graph.nodes.logic_extractor import _bind_and_cross_check_parameters, _static_fallback
from src.quant.risk_weights import RISK_WEIGHTS_BY_CLASS, CORRELATIONS_BY_CLASS


class TestLogicExtractorBinding:
    def test_risk_weight_hallucination_overridden(self):
        """When the LLM hallucinates a risk weight, it must be overridden with the statutory value."""
        # GIRR 5Y statutory weight is 0.011. Simulate LLM hallucinating 0.55 (50x error).
        logic = ExtractedLogic(
            risk_class="GIRR",
            formula_ref="MAR21.44",
            risk_weights={"5Y": 0.55, "1Y": 0.016},
            correlations={},
            is_complete=False,
        )
        errors: list[ValidationError] = []

        _bind_and_cross_check_parameters(logic, errors)

        # Value must be corrected to prescribed Basel statutory value 0.011
        assert logic.risk_weights["5Y"] == pytest.approx(0.011)
        assert logic.risk_weights["1Y"] == pytest.approx(0.016)

        # An audit warning must be recorded
        warning_messages = [e.message for e in errors if e.severity == "warning"]
        assert any("5Y" in msg and "diverged" in msg and "corrected" in msg.lower() for msg in warning_messages)

    def test_missing_statutory_buckets_backfilled(self):
        """Any buckets omitted by the LLM must be backfilled from the Basel Annex tables."""
        logic = ExtractedLogic(
            risk_class="GIRR",
            formula_ref="MAR21.44",
            risk_weights={"1Y": 0.016},  # Only extracted 1Y, missed 5Y, 10Y, 30Y, etc.
            correlations={},
            is_complete=False,
        )
        errors: list[ValidationError] = []

        _bind_and_cross_check_parameters(logic, errors)

        # All prescribed GIRR tenors must be present
        for tenor in ["0.25Y", "0.5Y", "1Y", "2Y", "3Y", "5Y", "10Y", "15Y", "20Y", "30Y"]:
            assert tenor in logic.risk_weights
            assert logic.risk_weights[tenor] == pytest.approx(RISK_WEIGHTS_BY_CLASS["GIRR"][tenor])

        assert logic.is_complete is True

    def test_correlation_hallucination_overridden(self):
        """Correlation discrepancies beyond tolerance must be overridden to prescribed statutory values."""
        # Equity cross-bucket gamma_bc default is 0.15. Simulate LLM hallucinating 0.95.
        logic = ExtractedLogic(
            risk_class="Equity",
            formula_ref="MAR21.75",
            risk_weights={"EM_LargeCap": 0.55},
            correlations={"gamma_bc_default": 0.95},
            is_complete=False,
        )
        errors: list[ValidationError] = []

        _bind_and_cross_check_parameters(logic, errors)

        assert logic.correlations["gamma_bc_default"] == pytest.approx(0.15)
        assert any("gamma_bc_default" in e.message and "diverged" in e.message for e in errors)

    def test_static_fallback_complete(self):
        """_static_fallback returns complete prescribed statutory values without errors."""
        logic = _static_fallback("Equity")
        assert logic.is_complete is True
        assert logic.risk_weights["EM_LargeCap"] == pytest.approx(0.55)
        assert "gamma_bc_default" in logic.correlations


class TestEmptyPortfolioHandling:
    def test_empty_portfolio_retriever_skips(self):
        import asyncio
        from src.graph.nodes.retriever import retriever_node
        state = {"portfolio_inputs": [], "retrieved_regulatory_nodes": ["stale_dummy"]}
        res = asyncio.run(retriever_node(state))
        assert res["retrieved_regulatory_nodes"] == []

    def test_empty_portfolio_logic_extractor_skips(self):
        import asyncio
        from src.graph.nodes.logic_extractor import logic_extractor_node
        state = {"portfolio_inputs": [], "extracted_calculation_logic": ["stale_dummy"]}
        res = asyncio.run(logic_extractor_node(state))
        assert res["extracted_calculation_logic"] == []

    def test_empty_portfolio_validator_summary(self):
        import asyncio
        from src.graph.nodes.validator import validator_node
        state = {
            "portfolio_inputs": [],
            "calculated_metrics": [],
            "audit_flags": [],
            "validation_errors": [],
        }
        res = asyncio.run(validator_node(state))
        assert "INCOMPLETE" in res["final_compliance_summary"]
        assert "No trading book positions" in res["final_compliance_summary"]
