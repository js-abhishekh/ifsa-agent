"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import {
  LogEntry,
  NodeState,
  FinalResults,
  PipelineNode,
  ComplianceStatus,
  CalculatedMetric,
} from "@/lib/types";
import { getStreamUrl } from "@/lib/api";

const NODE_ORDER: PipelineNode[] = [
  "audit_document",
  "retrieve",
  "extract_logic",
  "execute_quant",
  "validate",
  "retry_bump",
  "request_missing_inputs"
];

const NODE_META: Record<PipelineNode, { label: string; desc: string }> = {
  audit_document: { label: "Audit Document", desc: "Scanning PDF for regulatory disclosure breaches" },
  retrieve: { label: "Retrieve Rules", desc: "Fetching Basel MAR rules from ChromaDB vector store" },
  extract_logic: { label: "Extract Logic", desc: "Extracting risk weights & correlation matrices via LLM" },
  execute_quant: { label: "Execute Quant Core", desc: "Executing SBM bucket aggregation formulas" },
  validate: { label: "Validate", desc: "Validating mathematical consistency & output thresholds" },
  retry_bump: { label: "Retry Needed", desc: "Missing inputs detected, triggering pipeline retry" },
  request_missing_inputs: { label: "Manual Input Req.", desc: "Pipeline blocked, manual intervention required" }
};

function makeId() {
  return Math.random().toString(36).slice(2, 10);
}

function nodeDataToLogs(node: string, data: Record<string, unknown>): LogEntry[] {
  const ts = new Date().toISOString();
  const entries: LogEntry[] = [];

  if (node === "audit_document") {
    const flags = data.audit_flags as string[] | undefined;
    if (flags && flags.length > 0) {
      entries.push({
        id: makeId(), type: "flag",
        text: `Audit scan complete — ${flags.length} regulatory flag${flags.length > 1 ? "s" : ""} raised`,
        node: "Audit Document", meta: `${flags.length} issue(s) found`, timestamp: ts,
      });
      flags.forEach((f) => {
        const firstLine = f.split("\n")[0];
        entries.push({ id: makeId(), type: "flag", text: firstLine, node: "Audit Document", timestamp: ts });
      });
    } else {
      entries.push({ id: makeId(), type: "success", text: "Audit scan complete — no compliance flags raised", node: "Audit Document", timestamp: ts });
    }
  }

  if (node === "retrieve") {
    const count = (data.retrieved_count as number) ?? 0;
    entries.push({ id: makeId(), type: "success", text: `Retrieved ${count} regulatory clauses from vector store`, node: "Retrieve Rules", timestamp: ts });
  }

  if (node === "extract_logic") {
    const count = (data.extracted_count as number) ?? 0;
    const complete = data.is_complete as boolean;
    entries.push({
      id: makeId(), type: complete ? "success" : "flag",
      text: complete
        ? `Risk weights & correlations resolved for ${count} risk class(es)`
        : `Partial extraction — ${count} risk class(es) incomplete, triggering retry`,
      node: "Extract Logic", timestamp: ts,
    });
  }

  if (node === "execute_quant") {
    const metrics = (data.metrics as CalculatedMetric[]) ?? [];
    metrics.forEach((m) => {
      entries.push({
        id: makeId(), type: "metric",
        text: `${m.risk_class} ${m.metric_name.replace("_", " ")} = $${m.aggregated_value.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`,
        node: "Execute Quant Core", timestamp: ts,
      });
    });
    if (metrics.length === 0) {
      entries.push({ id: makeId(), type: "info", text: "Executing SBM bucket aggregation formulas…", node: "Execute Quant Core", timestamp: ts });
    }
  }

  if (node === "validate") {
    const errors = (data.validation_errors as number) ?? 0;
    const warnings = (data.warnings as number) ?? 0;
    if (errors === 0) {
      entries.push({ id: makeId(), type: "success", text: `Validation complete — ${warnings} warning${warnings !== 1 ? "s" : ""}`, node: "Validate", timestamp: ts });
    } else {
      entries.push({ id: makeId(), type: "error", text: `Validation found ${errors} blocking error${errors !== 1 ? "s" : ""}`, node: "Validate", timestamp: ts });
    }
  }

  return entries;
}

export function usePipelineSSE(runId: string | null) {
  const [nodes, setNodes] = useState<NodeState[]>(() =>
    NODE_ORDER.map((id) => ({ id, ...NODE_META[id], status: "pending" as const }))
  );
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [finalResults, setFinalResults] = useState<FinalResults | null>(null);
  const [pipelineDone, setPipelineDone] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const appendLogs = useCallback((entries: LogEntry[]) => {
    setLogs((prev) => [...prev, ...entries]);
  }, []);

  const setNodeStatus = useCallback((node: string, status: NodeState["status"], dataSlice?: Record<string, unknown>) => {
    setNodes((prev) =>
      prev.map((n) => (n.id === node ? { ...n, status, dataSlice: dataSlice ?? n.dataSlice } : n))
    );
  }, []);

  useEffect(() => {
    if (!runId) return;

    // Mark first node as active
    setNodeStatus("audit_document", "active");
    appendLogs([{ id: makeId(), type: "info", text: "Pipeline started — scanning PDF structure…", node: "System", timestamp: new Date().toISOString() }]);

    const es = new EventSource(getStreamUrl(runId));
    
    let isInitialWait = true;
    let lastEventTime = Date.now();

    // Allow up to 5 minutes for LLM calls on free-tier models
    const timeoutId = setInterval(() => {
      const elapsed = Date.now() - lastEventTime;
      if (isInitialWait && elapsed > 300000) {
        setError("Pipeline timed out after 5 minutes. The LLM may be overloaded — please try again.");
        es.close();
        clearInterval(timeoutId);
      }
    }, 10000);

    // Keepalive pings from backend reset our last-event timer
    es.addEventListener("ping", () => {
      lastEventTime = Date.now();
      isInitialWait = false;
    });

    es.addEventListener("node_complete", (e: MessageEvent) => {
      isInitialWait = false;
      lastEventTime = Date.now();
      const payload = JSON.parse(e.data) as { node: string; data: Record<string, unknown> };
      const { node, data } = payload;

      // Mark current node done, next active
      setNodeStatus(node, "done", data);
      const currentIdx = NODE_ORDER.indexOf(node as PipelineNode);
      if (currentIdx >= 0 && currentIdx < NODE_ORDER.length - 1) {
        setNodeStatus(NODE_ORDER[currentIdx + 1], "active");
      }

      appendLogs(nodeDataToLogs(node, data));
    });

    es.addEventListener("error_event", (e: MessageEvent) => {
      const payload = JSON.parse(e.data) as { message: string; node?: string };
      setError(payload.message);
      appendLogs([{
        id: makeId(), type: "error",
        text: `⚠ ${payload.node ? `[${payload.node}] ` : ""}${payload.message}`,
        node: payload.node ?? "System", timestamp: new Date().toISOString(),
      }]);
      // Don't mark as fatal — keep going if possible
    });

    es.addEventListener("done", (e: MessageEvent) => {
      const payload = JSON.parse(e.data);
      const summary: string = payload.final_compliance_summary ?? "";
      const auditFlags: string[] = payload.audit_flags ?? [];
      const metrics = payload.calculated_metrics ?? [];
      const valErrors = payload.validation_errors ?? [];
      const portfolioInputs = payload.portfolio_inputs ?? [];

      let status: ComplianceStatus = "PASS";
      if (valErrors.some((v: { severity: string }) => v.severity === "blocking")) status = "INCOMPLETE";
      else if (auditFlags.length > 0 || valErrors.some((v: { severity: string }) => v.severity === "warning")) status = "WARNING";

      setFinalResults({ compliance_status: status, compliance_summary: summary, calculated_metrics: metrics, audit_flags: auditFlags, validation_errors: valErrors, portfolio_inputs: portfolioInputs });
      setPipelineDone(true);
      // Mark last node done
      setNodeStatus("validate", "done");
      es.close();
    });

    es.onerror = () => {
      setError("Connection to pipeline stream lost. The pipeline may still be running.");
      es.close();
    };

    return () => {
      clearInterval(timeoutId);
      es.close();
    };
  }, [runId, appendLogs, setNodeStatus]);

  return { nodes, logs, finalResults, pipelineDone, error };
}
