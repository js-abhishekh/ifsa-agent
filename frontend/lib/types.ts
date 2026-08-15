// TypeScript mirrors of the Python AgentState schema

export type RiskClass = "GIRR" | "CSR_NonSec" | "CSR_Sec" | "Equity" | "Commodity" | "FX";
export type MetricName = "delta_charge" | "vega_charge" | "curvature_charge" | "drc_charge" | "rrao_charge";
export type Severity = "blocking" | "warning";
export type ExtractionStatus = "success" | "partial" | "failed";

export interface PortfolioPosition {
  instrument_id: string;
  risk_class: RiskClass;
  bucket: string;
  risk_factor: string;
  sensitivity: number;
  notional?: number;
  currency: string;
  cvr_up?: number;
  cvr_down?: number;
}

export interface CalculatedMetric {
  risk_class: RiskClass;
  metric_name: MetricName;
  bucket_level: Record<string, number>;
  aggregated_value: number;
  formula_used: string;
}

export interface ValidationError {
  severity: Severity;
  node: string;
  message: string;
}

export interface UploadResponse {
  run_id: string;
  file_path: string;
  extracted_positions: PortfolioPosition[];
  extraction_status: ExtractionStatus;
  extraction_message: string;
  is_demo?: boolean;
}

export interface RunResponse {
  run_id: string;
  status: string;
}

// SSE event types
export type SSEEventType = "node_complete" | "error" | "done";

export interface SSENodeEvent {
  event: SSEEventType;
  node: string;
  timestamp: string;
  data: Record<string, unknown>;
}

export interface SSEDoneEvent {
  event: "done";
  final_compliance_summary: string | null;
  calculated_metrics: CalculatedMetric[];
  audit_flags: string[];
  validation_errors: ValidationError[];
}

export type PipelineNode =
  | "audit_document"
  | "retrieve"
  | "extract_logic"
  | "execute_quant"
  | "validate"
  | "retry_bump"
  | "request_missing_inputs";

export type NodeStatus = "pending" | "active" | "done" | "error";

export interface NodeState {
  id: PipelineNode;
  label: string;
  desc: string;
  status: NodeStatus;
  dataSlice?: Record<string, unknown>;
}

export interface LogEntry {
  id: string;
  type: "info" | "success" | "flag" | "metric" | "error" | "retry";
  text: string;
  node: string;
  meta?: string;
  timestamp: string;
}

// Compliance status derived from final state
export type ComplianceStatus = "PASS" | "WARNING" | "INCOMPLETE" | "ERROR";

export interface FinalResults {
  compliance_status: ComplianceStatus;
  compliance_summary: string;
  calculated_metrics: CalculatedMetric[];
  audit_flags: string[];
  validation_errors: ValidationError[];
  portfolio_inputs?: PortfolioPosition[];
}
