"use client";

import React, { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import Navbar from "@/components/Navbar";
import ExportBar from "@/components/ExportBar";
import { FinalResults } from "@/lib/types";
import { CheckCircle2, AlertTriangle, DollarSign, Flag } from "lucide-react";

const fetchResults = async (runId: string): Promise<FinalResults> => {
  const res = await fetch(`/api/result/${runId}`);
  if (!res.ok) throw new Error("Failed to fetch results");
  return res.json();
};

interface ParsedAuditFlag {
  title: string;
  location: string;
  quote: string;
  issue: string;
}

const parseFlag = (flagStr: string): ParsedAuditFlag => {
  const lines = flagStr.split("\n");
  const title = lines[0] || "Audit Finding";
  let location = "", quote = "", issue = "";
  lines.slice(1).forEach((line) => {
    if (line.startsWith("Where in PDF:"))   location = line.replace("Where in PDF:", "").trim();
    else if (line.startsWith("What it says:")) quote   = line.replace("What it says:", "").trim().replace(/^"|"$/g, "");
    else if (line.startsWith("The Issue:"))   issue   = line.replace("The Issue:", "").trim();
  });
  if (!location && !quote && !issue) return { title: "Regulatory Audit Finding", location: "", quote: "", issue: flagStr };
  return { title, location, quote, issue };
};

// Risk badge palette — Airtable demo-grid surfaces
const RISK_BADGE: Record<string, { bg: string; text: string; border: string }> = {
  GIRR:       { bg: "#f8fafc", text: "#254fad", border: "#dddddd" },
  Equity:     { bg: "#a8d8c4", text: "#0a2e0e", border: "#a8d8c4" },
  FX:         { bg: "#f5e9d4", text: "#aa2d00", border: "#dddddd" },
  CSR_NonSec: { bg: "#f8fafc", text: "#181d26", border: "#dddddd" },
  CSR_Sec:    { bg: "#f8fafc", text: "#181d26", border: "#dddddd" },
  Commodity:  { bg: "#f4d35e", text: "#181d26", border: "#d9a441" },
};

export default function ResultsPage() {
  const params   = useParams();
  const router   = useRouter();
  const runId    = params.runId as string;

  const [results, setResults] = useState<FinalResults | null>(null);
  const [loading, setLoading] = useState(true);
  const [error,   setError]   = useState<string | null>(null);

  useEffect(() => {
    (async () => {
      try {
        const cached = sessionStorage.getItem("frtb_results_" + runId);
        if (cached) { setResults(JSON.parse(cached)); setLoading(false); return; }
        const fetched = await fetchResults(runId);
        setResults(fetched);
        setLoading(false);
      } catch {
        setError("Failed to load results. They may have expired.");
        setLoading(false);
      }
    })();
  }, [runId]);

  /* ── Loading ──────────────────────────────────────────────────────────────*/
  if (loading) {
    return (
      <div className="flex min-h-screen flex-col bg-white text-[#181d26]">
        <Navbar screenLabel="VERIFICATION RESULTS" runId={runId} />
        <div className="flex flex-1 flex-col items-center justify-center gap-3">
          <div className="h-8 w-8 animate-spin rounded-full border-2 border-[#aa2d00] border-t-transparent" />
          <span className="text-[16px] font-[400] text-[#181d26]">
            Compiling Regulatory Audit Statement…
          </span>
        </div>
      </div>
    );
  }

  /* ── Error ────────────────────────────────────────────────────────────────*/
  if (error || !results) {
    return (
      <div className="flex min-h-screen flex-col bg-white text-[#181d26]">
        <Navbar screenLabel="VERIFICATION RESULTS" runId={runId} />
        <div className="flex flex-1 flex-col items-center justify-center gap-4 p-6">
          {/* coral signature card for error */}
          <div className="rounded-[12px] bg-[#aa2d00] px-6 py-5 text-[15px] text-white">
            ⚠ {error || "Results not found."}
          </div>
          <button
            onClick={() => router.push("/")}
            className="text-[14px] font-[500] text-[#181d26] underline underline-offset-4 decoration-[#dddddd]"
          >
            Return to Upload →
          </button>
        </div>
      </div>
    );
  }

  const parsedFlags       = (results.audit_flags || []).map(parseFlag);
  const formatCurrency    = (val: number) =>
    "₹ " + val.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const totalCapitalCharge = (results.calculated_metrics || []).reduce(
    (sum, m) => sum + (m.aggregated_value || 0), 0
  );

  return (
    <div className="flex min-h-screen flex-col bg-white text-[#181d26]">
      <Navbar screenLabel="VERIFICATION RESULTS" runId={runId} />

      <main className="mx-auto flex w-full max-w-[1120px] flex-1 flex-col gap-12 px-6 py-12">

        {/* ── Report Header — editorial rule ──────────────────────────────── */}
        <header className="flex flex-col gap-5 border-b-2 border-[#181d26] pb-8">
          <div>
            {/* display-md: 32px/bold */}
            <h1 className="text-[32px] font-bold leading-[1.2] text-[#181d26] md:text-[38px]">
              Capital Verification &amp; Audit Report
            </h1>
          </div>

          {/* KPI Banner — white canvas card, hairline border, rounded-lg */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-0 rounded-[12px] border border-[#dddddd] bg-white overflow-hidden">
            {/* KPI 1 */}
            <div className="flex flex-col gap-1 p-6 border-b md:border-b-0 md:border-r border-[#dddddd]">
              <span className="font-[family-name:var(--font-mono)] text-[11px] font-[500] text-[#9297a0] uppercase tracking-wider">
                Aggregated FRTB Capital Charge
              </span>
              <span className="font-[family-name:var(--font-mono)] text-[22px] font-[600] text-[#181d26]">
                {formatCurrency(totalCapitalCharge)}
              </span>
            </div>
            {/* KPI 2 */}
            <div className="flex flex-col gap-1 p-6 border-b md:border-b-0 md:border-r border-[#dddddd]">
              <span className="font-[family-name:var(--font-mono)] text-[11px] font-[500] text-[#9297a0] uppercase tracking-wider">
                IFSA Compliance Audit
              </span>
              {parsedFlags.length > 0 ? (
                <span className="flex items-center gap-2 text-[18px] font-[600] text-[#aa2d00]">
                  <AlertTriangle className="h-5 w-5 text-[#aa2d00]" />
                  Non-Compliant
                </span>
              ) : (
                <span className="flex items-center gap-2 text-[18px] font-[500] text-[#006400]">
                  <CheckCircle2 className="h-5 w-5" />
                  Disclosure Verified
                </span>
              )}
            </div>
            {/* KPI 3 */}
            <div className="flex flex-col gap-1 p-6">
              <span className="font-[family-name:var(--font-mono)] text-[11px] font-[500] text-[#9297a0] uppercase tracking-wider">
                Audit Flags Captured
              </span>
              <span className="flex items-center gap-2 font-[family-name:var(--font-mono)] text-[22px] font-[600] text-[#aa2d00]">
                <Flag className="h-5 w-5" />
                {parsedFlags.length} Flag{parsedFlags.length === 1 ? "" : "s"}
              </span>
            </div>
          </div>
        </header>

        {/* ── Section 1: Portfolio Positions ───────────────────────────────── */}
        {results.portfolio_inputs && results.portfolio_inputs.length > 0 && (
          <section className="flex flex-col gap-5">
            <div className="flex items-center gap-3 border-b border-[#dddddd] pb-3">
              {/* coral section number */}
              <span className="font-[family-name:var(--font-mono)] text-[13px] font-[600] text-[#aa2d00]">1.0</span>
              {/* title-lg: 24px/bold */}
              <h2 className="text-[22px] font-bold text-[#181d26]">
                Extracted Trading Book Positions &amp; Sensitivities
              </h2>
            </div>

            <div className="overflow-hidden rounded-[10px] border border-[#dddddd] bg-white">
              <table className="w-full border-collapse text-left text-[13.5px]">
                <thead>
                  <tr className="border-b border-[#dddddd] bg-[#f8fafc] font-[family-name:var(--font-mono)] text-[11px] font-[600] tracking-wider text-[#41454d] uppercase">
                    <th className="px-5 py-3">Instrument ID</th>
                    <th className="px-5 py-3">Risk Class</th>
                    <th className="px-5 py-3">Risk Factor / Bucket</th>
                    <th className="px-5 py-3 text-right">Sensitivity / Notional</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#dddddd]">
                  {results.portfolio_inputs.map((pos, idx) => {
                    const badge = RISK_BADGE[pos.risk_class] || { bg: "#f8fafc", text: "#333840", border: "#dddddd" };
                    return (
                      <tr key={idx} className="transition-colors">
                        <td className="px-5 py-3.5 font-[family-name:var(--font-mono)] font-[500] text-[#181d26]">
                          {pos.instrument_id}
                        </td>
                        <td className="px-5 py-3.5">
                          <span
                            className="inline-flex items-center rounded-[6px] border px-2.5 py-0.5 font-[family-name:var(--font-mono)] text-[11px] font-[600] uppercase"
                            style={{ backgroundColor: badge.bg, color: badge.text, borderColor: badge.border }}
                          >
                            {pos.risk_class}
                          </span>
                        </td>
                        <td className="px-5 py-3.5">
                          <div className="flex flex-col gap-0.5">
                            <span className="font-[400] text-[#181d26]">{pos.risk_factor}</span>
                            <span className="font-[family-name:var(--font-mono)] text-[11.5px] text-[#9297a0]">
                              Bucket: {pos.bucket}
                            </span>
                          </div>
                        </td>
                        <td className="px-5 py-3.5 text-right">
                          <div className="flex flex-col gap-0.5 font-[family-name:var(--font-mono)]">
                            <span className="font-[500] text-[#181d26]">{formatCurrency(pos.sensitivity)}</span>
                            {pos.notional && (
                              <span className="text-[11.5px] text-[#9297a0]">Notional: {formatCurrency(pos.notional)}</span>
                            )}
                          </div>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {/* ── Section 2: Audit Flags ───────────────────────────────────────── */}
        <section className="flex flex-col gap-5">
          <div className="flex items-center gap-3 border-b border-[#dddddd] pb-3">
            <span className="font-[family-name:var(--font-mono)] text-[13px] font-[600] text-[#aa2d00]">2.0</span>
            <h2 className="text-[22px] font-bold text-[#181d26]">
              IFSA Disclosure Document Sampling &amp; Audit Findings
            </h2>
          </div>

          {parsedFlags.length === 0 ? (
            /* Success — forest signature card */
            <div className="rounded-[12px] bg-[#0a2e0e] p-6 text-[14px] text-white">
              ✓ No regulatory compliance breaches or reporting omissions were detected in the sampled sections.
            </div>
          ) : (
            <div className="flex flex-col gap-4">
              {parsedFlags.map((flag, idx) => (
                // cream-callout-card per DESIGN.md
                <div
                  key={idx}
                  className="flex flex-col gap-3.5 rounded-[10px] border border-[#dddddd] bg-[#f5e9d4] p-5"
                >
                  {/* Flag header */}
                  <div className="flex flex-wrap items-center justify-between gap-2 border-b border-[#dddddd] pb-3">
                    <div className="flex items-center gap-2">
                      <AlertTriangle className="h-4 w-4 text-[#aa2d00]" />
                      <h4 className="text-[16px] font-bold text-[#181d26]">{flag.title}</h4>
                    </div>
                    {flag.location && (
                      <span className="rounded-[6px] border border-[#dddddd] bg-white px-2.5 py-1 font-[family-name:var(--font-mono)] text-[11px] font-[500] text-[#41454d]">
                        📍 {flag.location}
                      </span>
                    )}
                  </div>
                  {/* Quote — white inset with coral left border */}
                  {flag.quote && (
                    <div className="rounded-[6px] border-l-4 border-[#aa2d00] bg-white p-4 text-[14px] italic leading-relaxed text-[#333840]">
                      &ldquo;{flag.quote}&rdquo;
                    </div>
                  )}
                  {/* Issue */}
                  {flag.issue && (
                    <div className="text-[13.5px] leading-relaxed text-[#333840]">
                      <strong className="font-[500] text-[#aa2d00]">Audit Issue: </strong>
                      {flag.issue}
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </section>

        {/* ── Section 3: Capital Charges Table ────────────────────────────── */}
        <section className="flex flex-col gap-5">
          <div className="flex items-center gap-3 border-b border-[#dddddd] pb-3">
            <span className="font-[family-name:var(--font-mono)] text-[13px] font-[600] text-[#aa2d00]">3.0</span>
            <h2 className="text-[22px] font-bold text-[#181d26]">
              BCBS Standardised Market Risk Capital Requirements
            </h2>
          </div>

          <div className="overflow-hidden rounded-[10px] border border-[#dddddd] bg-white">
            <table className="w-full border-collapse text-left text-[13.5px]">
              <thead>
                <tr className="border-b border-[#dddddd] bg-[#f8fafc] font-[family-name:var(--font-mono)] text-[11px] font-[600] tracking-wider text-[#41454d] uppercase">
                  <th className="px-5 py-3">Risk Class</th>
                  <th className="px-5 py-3">Sensitivity Metric</th>
                  <th className="px-5 py-3 text-right">Aggregated Charge (INR)</th>
                  <th className="px-5 py-3">Bucket Level Disclosure</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#dddddd]">
                {(results.calculated_metrics || []).map((m, idx) => {
                  const bucketEntries = Object.entries(m.bucket_level || {});
                  const bucketStr     = bucketEntries.length > 0
                    ? bucketEntries.map(([k, v]) => `${k} = ${formatCurrency(v)}`).join(", ")
                    : "Default / Aggregated";
                  return (
                    <tr key={idx} className="transition-colors">
                      <td className="px-5 py-3.5 text-[14px] font-[500] text-[#181d26]">
                        {m.risk_class}
                      </td>
                      <td className="px-5 py-3.5">
                        <code className="rounded-[4px] border border-[#dddddd] bg-[#f8fafc] px-2.5 py-1 font-[family-name:var(--font-mono)] text-[12px] font-[500] text-[#181d26]">
                          {m.metric_name}
                        </code>
                      </td>
                      <td className="px-5 py-3.5 text-right font-[family-name:var(--font-mono)] font-[600] text-[#181d26]">
                        {formatCurrency(m.aggregated_value || 0)}
                      </td>
                      <td className="px-5 py-3.5">
                        <code className="rounded-[4px] border border-[#dddddd] bg-[#f8fafc] px-2.5 py-1 font-[family-name:var(--font-mono)] text-[11.5px] text-[#41454d]">
                          {bucketStr}
                        </code>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </section>

        {/* ── Section 4: Compliance Summary — dark signature card ──────────── */}
        <section className="flex flex-col gap-5">
          <div className="flex items-center gap-3 border-b border-[#dddddd] pb-3">
            <span className="font-[family-name:var(--font-mono)] text-[13px] font-[600] text-[#aa2d00]">4.0</span>
            <h2 className="text-[22px] font-bold text-[#181d26]">
              IFSA Final Regulatory Compliance Statement
            </h2>
          </div>

          {/* hero-card: dark with coral highlight when non-compliant */}
          <div className={`rounded-[12px] px-10 py-8 ${parsedFlags.length > 0 ? "bg-[#280c05] border-2 border-[#aa2d00]" : "bg-[#181d26]"}`}>
            <p className="text-[16px] font-[400] leading-relaxed text-white">
              {results.compliance_summary ||
                "PASS — Capital calculations verified cleanly under BCBS FRTB sensitivities-based method rules."}
            </p>
          </div>
        </section>

        {/* ── Export Bar ───────────────────────────────────────────────────── */}
        <ExportBar runId={runId} complianceSummary={results.compliance_summary} />

      </main>
    </div>
  );
}
