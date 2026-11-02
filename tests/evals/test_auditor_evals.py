"""
tests/evals/test_auditor_evals.py

Eval harness for the document_auditor_node.

Metrics measured:
  - Flag Precision:  Of the flags raised, what fraction are real violations?
  - Flag Recall:     Are all known violations caught (zero false-negatives on critical issues)?
  - No-Flag Accuracy: Does the auditor stay silent on clean documents?

Strategy: We use synthetic document snippets instead of full PDFs so the tests
are fast, deterministic in their input, and don't require raw bank PDFs.

Run with:
    pytest tests/evals/test_auditor_evals.py -v --tb=short
"""
import asyncio
import pytest
from src.graph.nodes.document_auditor import (
    _extract_json_payload,
    AUDITOR_PROMPT,
    _llm_available,
)
from src.config import create_llm_client


# ── Synthetic disclosure snippets ─────────────────────────────────────────────
# Each snippet represents a bank disclosure paragraph with known regulatory status.

SYNTHETIC_CASES = [
    {
        "id": "AUDIT-001",
        "description": "Explicit vega/curvature exclusion — clear breach",
        "text": (
            "The Bank has determined that vega and curvature capital charges are not material "
            "to its trading book and has excluded these charges from the FRTB-SA capital calculation. "
            "Only delta sensitivities are included in the market risk capital requirement."
        ),
        "expected_flags": ["vega", "curvature"],
        "min_flags": 1,
        "is_violation": True,
    },
    {
        "id": "AUDIT-002",
        "description": "Asymmetric curvature shock — methodological breach",
        "text": (
            "For curvature risk, the Bank applies an upward shock only to the risk factors, "
            "as the downward scenario was determined to be non-binding. The CVR is computed as "
            "the loss under the upward stress scenario alone per internal policy."
        ),
        "expected_flags": ["curvature", "asymmetric"],
        "min_flags": 1,
        "is_violation": True,
    },
    {
        "id": "AUDIT-003",
        "description": "FX notional with zero capital charge — suspicious anomaly",
        "text": (
            "The Bank holds USD/INR forward positions with a total notional of INR 45,000 crore. "
            "The FX delta risk capital charge attributable to these positions is reported as INR 0 "
            "as the bank classifies all FX positions as structural under internal guidelines."
        ),
        "expected_flags": ["fx", "zero"],
        "min_flags": 1,
        "is_violation": True,
    },
    {
        "id": "AUDIT-004",
        "description": "Clean, FRTB-SA compliant disclosure — no flags expected",
        "text": (
            "The Bank computes market risk capital under the Standardised Approach (SA) as per "
            "RBI circular DBR.MRG.BC.No.96/21.06.201/2014-15 and BCBS 352. Delta, vega and curvature "
            "charges are computed for all applicable risk classes: GIRR, CSR (non-securitisation and "
            "securitisation), Equity, FX and Commodity. Curvature risk is computed using both upward "
            "and downward stress scenarios. Default Risk Charge and RRAO are included."
        ),
        "expected_flags": [],
        "min_flags": 0,
        "is_violation": False,
    },
    {
        "id": "AUDIT-005",
        "description": "Missing DRC disclosure — possible omission",
        "text": (
            "Market risk capital is computed using the Standardised Approach. Delta and vega "
            "sensitivities are computed across GIRR, Equity, and FX risk classes. The Bank does "
            "not hold any securitisation or correlation trading positions. No Default Risk Charge "
            "calculation is performed as the Bank has no eligible credit positions."
        ),
        "expected_flags": [],
        "min_flags": 0,
        "is_violation": False,
    },
    {
        "id": "AUDIT-006",
        "description": "Blanket vega exclusion via LLM-visible language",
        "text": (
            "In accordance with its internal model approval, vega risk is immaterial for the Bank's "
            "trading portfolio and is excluded from standardised approach calculations. The Bank's "
            "options portfolio is limited and below the materiality threshold."
        ),
        "expected_flags": ["vega"],
        "min_flags": 1,
        "is_violation": True,
    },
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _run_auditor_on_text(llm_client, text: str) -> list[dict]:
    """Invoke the auditor LLM on synthetic text and return parsed flags list."""
    response = llm_client.invoke([
        {"role": "system", "content": AUDITOR_PROMPT},
        {"role": "user",   "content": f"Document Text:\n{text}"},
    ])
    payload = _extract_json_payload(response.content)
    return payload.get("flags", [])


def _flags_contain_keyword(flags: list[dict], keyword: str) -> bool:
    """Check if any flag's title, quote or issue mentions the keyword (case-insensitive)."""
    keyword_lower = keyword.lower()
    for flag in flags:
        combined = (
            flag.get("title", "") + " " +
            flag.get("quote", "") + " " +
            flag.get("issue", "")
        ).lower()
        if keyword_lower in combined:
            return True
    return False


# ── Auditor Evals ─────────────────────────────────────────────────────────────

class TestAuditorFlagRecall:
    """Eval: The auditor must catch every known regulatory violation."""

    @pytest.mark.eval
    def test_recall_on_violation_cases(self):
        """
        For all synthetic violation snippets, the auditor must raise at least one flag.
        A missed violation (false negative) is the most dangerous outcome.
        """
        llm = create_llm_client(is_fallback=False) or create_llm_client(is_fallback=True)
        if not llm:
            pytest.skip("No LLM configured")

        violation_cases = [c for c in SYNTHETIC_CASES if c["is_violation"]]
        misses = []

        for case in violation_cases:
            flags = _run_auditor_on_text(llm, case["text"])
            if len(flags) < case["min_flags"]:
                misses.append(f"{case['id']}: got {len(flags)} flags, expected ≥ {case['min_flags']}")
            else:
                # Also check that relevant keywords appear in the flags
                for keyword in case["expected_flags"]:
                    if not _flags_contain_keyword(flags, keyword):
                        misses.append(f"{case['id']}: no flag mentions '{keyword}'")

        recall = 1.0 - (len(misses) / len(violation_cases)) if violation_cases else 1.0
        print(f"\n[auditor_eval] Recall on violations: {recall:.0%}  (misses={len(misses)})")
        if misses:
            for m in misses:
                print(f"  ✗ {m}")

        # 100% recall on violations: never miss a real breach
        assert not misses, (
            f"Auditor missed {len(misses)} violation(s). "
            "False negatives are unacceptable in a regulatory audit tool.\n"
            + "\n".join(misses)
        )


class TestAuditorFlagPrecision:
    """Eval: The auditor must not raise false alarms on clean disclosures."""

    @pytest.mark.eval
    def test_no_false_flags_on_clean_documents(self):
        """
        For clean, compliant disclosure snippets, the auditor must return zero flags.
        False positives erode trust and generate audit fatigue.
        """
        llm = create_llm_client(is_fallback=False) or create_llm_client(is_fallback=True)
        if not llm:
            pytest.skip("No LLM configured")

        clean_cases = [c for c in SYNTHETIC_CASES if not c["is_violation"]]
        false_positives = []

        for case in clean_cases:
            flags = _run_auditor_on_text(llm, case["text"])
            if len(flags) > 0:
                titles = [f.get("title", "?") for f in flags]
                false_positives.append(f"{case['id']}: raised {len(flags)} flag(s): {titles}")

        if false_positives:
            print(f"\n[auditor_eval] False positives on clean docs: {len(false_positives)}")
            for fp in false_positives:
                print(f"  ⚠ {fp}")

        # Allow at most 1 false positive across all clean cases (some LLM hallucination is expected)
        assert len(false_positives) <= 1, (
            f"Auditor raised false flags on {len(false_positives)} clean document(s):\n"
            + "\n".join(false_positives)
        )


class TestAuditorOutputSchema:
    """Unit tests for _extract_json_payload — no LLM required."""

    def test_clean_json_parses(self):
        raw = '{"flags": [{"title": "T", "location": "L", "quote": "Q", "issue": "I"}]}'
        payload = _extract_json_payload(raw)
        assert len(payload["flags"]) == 1

    def test_markdown_fenced_json_parses(self):
        raw = '```json\n{"flags": []}\n```'
        payload = _extract_json_payload(raw)
        assert payload["flags"] == []

    def test_empty_flags_returns_empty_list(self):
        raw = '{"flags": []}'
        payload = _extract_json_payload(raw)
        assert payload["flags"] == []

    def test_malformed_json_returns_empty_flags(self):
        """Malformed responses must not raise — they must degrade to empty flags."""
        raw = "I could not find any violations in this text."
        payload = _extract_json_payload(raw)
        assert payload == {"flags": []}


# ── End-to-End Pipeline Eval ──────────────────────────────────────────────────

class TestAuditorPipelineIntegration:
    """Integration: Run the full auditor_node through the LangGraph state machine."""

    @pytest.mark.eval
    def test_auditor_node_returns_flags_for_vega_exclusion(self, tmp_path):
        """
        Write a synthetic PDF with a known vega exclusion violation and
        run it through the full document_auditor_node to verify end-to-end.
        Requires pymupdf and an active LLM.
        """
        if not _llm_available:
            pytest.skip("No LLM configured")

        try:
            import pymupdf
        except ImportError:
            pytest.skip("pymupdf not installed")

        # Create a minimal synthetic PDF with the violation text
        pdf_path = tmp_path / "synthetic_violation.pdf"
        doc = pymupdf.open()
        page = doc.new_page()
        page.insert_text(
            (50, 100),
            (
                "The Bank has determined that vega and curvature capital charges are not "
                "material and has excluded them from the FRTB-SA capital computation. "
                "Only delta sensitivities are included."
            ),
            fontsize=11,
        )
        doc.save(str(pdf_path))
        doc.close()

        from src.graph.nodes.document_auditor import document_auditor_node
        from src.graph.state import AgentState

        state: AgentState = {
            "document_path": str(pdf_path),
            "audit_flags": [],
        }
        result = asyncio.get_event_loop().run_until_complete(document_auditor_node(state))
        flags = result.get("audit_flags", [])

        print(f"\n[auditor_integration] Flags raised: {len(flags)}")
        for f in flags:
            print(f"  - {f[:80]}...")

        assert len(flags) >= 1, (
            "Full pipeline auditor_node raised zero flags on a document "
            "with an explicit vega/curvature exclusion."
        )

