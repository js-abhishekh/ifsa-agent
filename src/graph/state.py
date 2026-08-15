"""
src/graph/state.py

Pydantic-based state schema for the FRTB-SA LangGraph pipeline.

Using Pydantic (rather than bare TypedDict) ensures that malformed LLM
output raises a ValidationError immediately instead of silently propagating
bad numbers into the deterministic quant engine.
"""
from typing import Literal, Optional
from pydantic import BaseModel, Field
from typing_extensions import TypedDict


# ── Domain types ──────────────────────────────────────────────────────────────
RiskClass = Literal["GIRR", "CSR_NonSec", "CSR_Sec", "Equity", "Commodity", "FX"]
MetricName = Literal[
    "delta_charge", "vega_charge", "curvature_charge", "drc_charge", "rrao_charge"
]
Severity = Literal["blocking", "warning"]


# ── Portfolio inputs ───────────────────────────────────────────────────────────
class PortfolioPosition(BaseModel):
    """A single risk-factor sensitivity position from the trading book."""
    instrument_id: str
    risk_class: RiskClass
    bucket: str
    risk_factor: str            # e.g. tenor "5Y", equity name, commodity type
    sensitivity: float          # PV01 (delta), vega sensitivity, etc.
    notional: Optional[float] = None
    currency: str = "USD"
    # Curvature: up/down shock scenario values (optional, set for curvature calc)
    cvr_up: Optional[float] = None
    cvr_down: Optional[float] = None


# ── Retrieved regulatory content ───────────────────────────────────────────────
class RegulatoryNode(BaseModel):
    """A retrieved chunk from the ChromaDB vector store."""
    clause_id: str
    chapter: str
    risk_type: str
    text: str
    relevance_score: float


# ── Extracted parameters ───────────────────────────────────────────────────────
class CalculationParameter(BaseModel):
    """A single numeric parameter extracted from regulatory text by the LLM."""
    param_name: str             # e.g. "risk_weight_GIRR_5Y"
    value: float
    source_clause_id: str
    confidence: float = Field(ge=0.0, le=1.0)


class ExtractedLogic(BaseModel):
    """Structured regulatory logic for a single risk class, produced by the LLM."""
    risk_class: RiskClass
    formula_ref: str            # e.g. "Kb aggregation, para 21.3"
    risk_weights: dict[str, float] = Field(default_factory=dict)
    correlations: dict[str, float] = Field(default_factory=dict)   # "rho_kl" keys
    parameters: list[CalculationParameter] = Field(default_factory=list)
    is_complete: bool = False
    missing_fields: list[str] = Field(default_factory=list)


# ── Calculated results ─────────────────────────────────────────────────────────
class CalculatedMetric(BaseModel):
    """Capital charge computed by the deterministic quant engine."""
    risk_class: RiskClass
    metric_name: MetricName
    bucket_level: dict[str, float] = Field(default_factory=dict)
    aggregated_value: float
    formula_used: str


# ── Validation / audit ─────────────────────────────────────────────────────────
class ValidationError(BaseModel):
    """An error or warning surfaced by the validator node."""
    severity: Severity
    node: str
    message: str


# ── Top-level graph state ──────────────────────────────────────────────────────
class AgentState(TypedDict, total=False):
    """The shared mutable state threaded through every LangGraph node."""
    user_query: str
    document_path: Optional[str]
    audit_flags: list[str]
    portfolio_inputs: list[PortfolioPosition]
    retrieved_regulatory_nodes: list[RegulatoryNode]
    extracted_calculation_logic: list[ExtractedLogic]
    calculated_metrics: list[CalculatedMetric]
    validation_errors: list[ValidationError]
    final_compliance_summary: Optional[str]
    retry_count: int
    max_retries: int
