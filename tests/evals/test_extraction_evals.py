"""
tests/evals/test_extraction_evals.py

Eval harness for the logic_extractor and retriever nodes.

Metrics measured:
  - Extraction Exact Match:  Are extracted risk weights ≈ ground-truth values?
  - Retrieval Hit Rate:       Does ChromaDB return a clause containing the expected MAR ref?
  - Fallback Trigger Rate:   What fraction of cases trigger static Annex fallback?
  - Completeness Accuracy:   Does is_complete match expectation?

Run with:
    pytest tests/evals/test_extraction_evals.py -v --tb=short

To run evals only:
    pytest tests/evals/ -m eval -v
"""
import json
import asyncio
import math
from pathlib import Path
from typing import Any

import pytest

from src.graph.nodes.logic_extractor import (
    _static_fallback,
    _bind_and_cross_check_parameters,
    EXTRACTION_SYSTEM_PROMPT,
    _extract_json_payload,
    _primary_llm,
    _fallback_llm,
    _llm_available,
)
from src.graph.state import ExtractedLogic, CalculationParameter, ValidationError
from src.graph.nodes.retriever import retriever_node
from src.graph.state import AgentState, PortfolioPosition

GOLDEN_PATH = Path(__file__).parent / "golden_dataset.json"
TOLERANCE = 1e-4          # risk weight numeric tolerance
RETRIEVAL_RECALL_TARGET = 0.80   # Hit@3 recall — lower than 95% until the vector store is populated
FALLBACK_RATE_LIMIT = 0.30       # warn if > 30% cases use static fallback without LLM


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def golden() -> list[dict]:
    return json.loads(GOLDEN_PATH.read_text())


@pytest.fixture(scope="module")
def llm():
    """Return the active LLM client (primary or fallback) or None."""
    return _primary_llm or _fallback_llm


# ── Helpers ───────────────────────────────────────────────────────────────────

def _invoke_extraction(llm_client, risk_class: str, clause_text: str) -> dict:
    """Call the LLM extraction pipeline and return raw payload dict."""
    response = llm_client.invoke([
        {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
        {"role": "user",   "content": f"Risk class: {risk_class}\n\nClause text:\n{clause_text}"},
    ])
    return _extract_json_payload(response.content)


def _approx_equal(extracted: float, expected: float, tol: float = TOLERANCE) -> bool:
    return math.isclose(extracted, expected, abs_tol=tol)


# ── Extraction: Exact Match Evals ─────────────────────────────────────────────

class TestExtractionAccuracy:
    """Eval: LLM must extract risk weights that match the golden dataset."""

    @pytest.mark.eval
    def test_all_risk_weight_exact_match(self, golden, llm):
        """
        For every golden case that has expected risk weights, extracted values
        must be within TOLERANCE of the published Basel Annex figures.
        Reports per-case pass/fail and aggregates an overall pass rate.
        """
        if not llm:
            pytest.skip("No LLM configured — set OPENROUTER_API_KEY or OPENAI_API_KEY in .env")

        cases_with_weights = [g for g in golden if g["expected_risk_weights"]]
        results = []

        for case in cases_with_weights:
            try:
                payload = _invoke_extraction(llm, case["risk_class"], case["clause_text"])
                payload["parameters"] = [CalculationParameter(**p) for p in payload.get("parameters", [])]
                logic = ExtractedLogic(**payload)
                errors: list[ValidationError] = []
                _bind_and_cross_check_parameters(logic, errors)
            except Exception as e:
                results.append({"id": case["id"], "passed": False, "reason": str(e)})
                continue

            mismatches = []
            for key, expected_val in case["expected_risk_weights"].items():
                extracted_val = logic.risk_weights.get(key)
                if extracted_val is None:
                    mismatches.append(f"{key}: missing")
                elif not _approx_equal(extracted_val, expected_val):
                    mismatches.append(f"{key}: got {extracted_val}, expected {expected_val}")

            passed = len(mismatches) == 0
            results.append({"id": case["id"], "passed": passed, "mismatches": mismatches})

        passed_count = sum(1 for r in results if r["passed"])
        total = len(results)
        pass_rate = passed_count / total if total else 0.0

        # Print per-case report
        print(f"\n[extraction_eval] Risk weight exact-match: {passed_count}/{total} passed ({pass_rate:.0%})")
        for r in results:
            status = "✓" if r["passed"] else "✗"
            detail = "" if r["passed"] else f" → {r.get('mismatches') or r.get('reason', '')}"
            print(f"  [{status}] {r['id']}{detail}")

        # Require ≥ 80% pass rate (lenient for now — tighten once golden set is calibrated)
        assert pass_rate >= 0.80, (
            f"Extraction accuracy {pass_rate:.0%} is below the 80% target. "
            f"Failing cases: {[r['id'] for r in results if not r['passed']]}"
        )

    @pytest.mark.eval
    def test_completeness_flag_accuracy(self, golden, llm):
        """is_complete must match expected_is_complete for every golden case."""
        if not llm:
            pytest.skip("No LLM configured")

        mismatches = []
        for case in golden:
            try:
                payload = _invoke_extraction(llm, case["risk_class"], case["clause_text"])
                payload["parameters"] = [CalculationParameter(**p) for p in payload.get("parameters", [])]
                logic = ExtractedLogic(**payload)
            except Exception:
                continue  # extraction failure is caught by fallback rate test

            if logic.is_complete != case["expected_is_complete"]:
                mismatches.append(
                    f"{case['id']}: got is_complete={logic.is_complete}, "
                    f"expected {case['expected_is_complete']}"
                )

        assert not mismatches, "is_complete flag mismatches:\n" + "\n".join(mismatches)


# ── Fallback Rate Eval ────────────────────────────────────────────────────────

class TestFallbackRate:
    """Eval: Static Annex fallback must not trigger for most standard clauses."""

    @pytest.mark.eval
    def test_fallback_rate_below_limit(self, golden, llm):
        """
        Counts how many cases fail LLM extraction and fall back to static tables.
        A high fallback rate signals a broken LLM config, model change, or prompt drift.
        """
        if not llm:
            pytest.skip("No LLM configured")

        # Exclude cases intentionally designed to trigger fallback
        standard_cases = [g for g in golden if "FALLBACK" not in g["id"] and "INCOMPLETE" not in g["id"]]
        fallback_count = 0

        for case in standard_cases:
            try:
                payload = _invoke_extraction(llm, case["risk_class"], case["clause_text"])
                payload["parameters"] = [CalculationParameter(**p) for p in payload.get("parameters", [])]
                ExtractedLogic(**payload)
            except Exception:
                # Any parse/validation failure in production triggers _static_fallback
                fallback_count += 1

        rate = fallback_count / len(standard_cases) if standard_cases else 0.0
        print(f"\n[extraction_eval] Fallback rate: {fallback_count}/{len(standard_cases)} ({rate:.0%}), limit={FALLBACK_RATE_LIMIT:.0%}")

        assert rate <= FALLBACK_RATE_LIMIT, (
            f"Fallback rate {rate:.0%} exceeds {FALLBACK_RATE_LIMIT:.0%}. "
            f"The LLM is failing too often — check API key, model name, or prompt."
        )

    def test_static_fallback_is_complete_for_all_known_risk_classes(self):
        """
        Static fallback must return is_complete=True for every risk class in the
        Basel Annex tables — otherwise the quant engine will receive incomplete parameters.
        """
        from src.quant.risk_weights import RISK_WEIGHTS_BY_CLASS
        for rc in RISK_WEIGHTS_BY_CLASS:
            logic = _static_fallback(rc)
            assert logic.is_complete, f"Static fallback for {rc} returned is_complete=False"
            assert logic.risk_weights, f"Static fallback for {rc} has empty risk_weights"


# ── Retrieval Hit Rate Eval ───────────────────────────────────────────────────

class TestRetrievalHitRate:
    """Eval: ChromaDB must return a clause mentioning the expected MAR reference."""

    @pytest.mark.eval
    def test_retrieval_recall_at_k(self, golden):
        """
        For each golden case with an expected_mar_clause, query the vector store
        and check whether any of the top-K results contain the expected clause reference.
        Hit@3 target: RETRIEVAL_RECALL_TARGET.
        """
        cases_with_clause = [g for g in golden if g.get("expected_mar_clause")]

        hits = 0
        misses = []

        for case in cases_with_clause:
            # Build minimal AgentState with one position to trigger retrieval
            state: AgentState = {
                "portfolio_inputs": [
                    PortfolioPosition(
                        instrument_id="eval",
                        risk_class=case["risk_class"],
                        bucket="default",
                        risk_factor="default",
                        sensitivity=1.0,
                    )
                ],
                "retrieved_regulatory_nodes": [],
            }
            result_state = asyncio.get_event_loop().run_until_complete(retriever_node(state))
            retrieved = result_state.get("retrieved_regulatory_nodes", [])

            # Check if any retrieved clause text contains the expected MAR reference
            mar_ref = case["expected_mar_clause"]
            hit = any(mar_ref.lower() in node.text.lower() for node in retrieved)
            if hit:
                hits += 1
            else:
                misses.append(case["id"])

        total = len(cases_with_clause)
        recall = hits / total if total else 0.0

        print(f"\n[retrieval_eval] Recall@3: {hits}/{total} ({recall:.0%}), target={RETRIEVAL_RECALL_TARGET:.0%}")
        if misses:
            print(f"  Missed cases: {misses}")

        # Skip instead of fail if the vector store is empty (not yet populated)
        from src.ingestion.vector_store import RegulatoryStore
        store = RegulatoryStore()
        if store.count() == 0:
            pytest.skip("ChromaDB vector store is empty — run ingestion first: python src/ingestion/ingest_basel_pdf.py")

        assert recall >= RETRIEVAL_RECALL_TARGET, (
            f"Retrieval Recall@3 is {recall:.0%}, below the {RETRIEVAL_RECALL_TARGET:.0%} target. "
            f"Missed: {misses}. Re-index ChromaDB with a fresh ingestion run."
        )


# ── Cross-check: Bind & Correct function ─────────────────────────────────────

class TestBindAndCrossCheck:
    """
    Unit tests for _bind_and_cross_check_parameters in isolation.
    These do NOT require a live LLM — they verify the cross-check logic itself.
    """

    def test_diverging_risk_weight_gets_corrected(self):
        logic = ExtractedLogic(
            risk_class="FX",
            formula_ref="test",
            risk_weights={"default": 0.20},   # wrong: should be 0.15
            correlations={},
            is_complete=True,
        )
        errors: list[ValidationError] = []
        _bind_and_cross_check_parameters(logic, errors)

        assert logic.risk_weights["default"] == pytest.approx(0.15)
        assert len(errors) == 1
        assert "corrected" in errors[0].message.lower()

    def test_missing_statutory_weights_are_backfilled(self):
        logic = ExtractedLogic(
            risk_class="FX",
            formula_ref="test",
            risk_weights={},   # empty — all weights should be backfilled
            correlations={},
            is_complete=False,
        )
        errors: list[ValidationError] = []
        _bind_and_cross_check_parameters(logic, errors)

        assert "default" in logic.risk_weights
        assert logic.is_complete is True
        assert len(errors) == 0   # no divergence, just backfill

    def test_correct_weight_passes_without_error(self):
        logic = ExtractedLogic(
            risk_class="GIRR",
            formula_ref="test",
            risk_weights={"5Y": 0.011},
            correlations={},
            is_complete=True,
        )
        errors: list[ValidationError] = []
        _bind_and_cross_check_parameters(logic, errors)
        assert logic.risk_weights["5Y"] == pytest.approx(0.011)
        assert not any("corrected" in e.message.lower() for e in errors)

    def test_diverging_correlation_gets_corrected(self):
        logic = ExtractedLogic(
            risk_class="FX",
            formula_ref="test",
            risk_weights={"default": 0.15},
            correlations={"gamma_bc": 0.99},   # wrong: should be 0.60
            is_complete=True,
        )
        errors: list[ValidationError] = []
        _bind_and_cross_check_parameters(logic, errors)
        assert logic.correlations["gamma_bc"] == pytest.approx(0.60)
        assert len(errors) >= 1


# ── Summary Reporter ──────────────────────────────────────────────────────────

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Print a concise eval summary table after the test run."""
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    skipped = len(terminalreporter.stats.get("skipped", []))
    print(
        f"\n{'='*60}\n"
        f"  EVAL SUMMARY\n"
        f"  ✓ passed: {passed}  ✗ failed: {failed}  ⊘ skipped: {skipped}\n"
        f"{'='*60}"
    )

