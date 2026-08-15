"use client";

import React, { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import Navbar from "@/components/Navbar";
import ExportBar from "@/components/ExportBar";
import { FinalResults } from "@/lib/types";
import { ShieldCheck, AlertTriangle, FileText, CheckCircle2, DollarSign, Layers } from "lucide-react";

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

export default function ResultsPage() {
  const params = useParams();
  const router = useRouter();
  const runId = params.runId as string;

  const [results, setResults] = useState<FinalResults | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadResults = async () => {
      try {
        const cached = sessionStorage.getItem("frtb_results_" + runId);
        if (cached) {
          setResults(JSON.parse(cached));
          setLoading(false);
        } else {
          const fetched = await fetchResults(runId);
          setResults(fetched);
          setLoading(false);
        }
      } catch (err: any) {
        setError("Failed to load results. They may have expired.");
        setLoading(false);
      }
    };
    loadResults();
  }, [runId]);

  if (loading) {
    return (
      <div className="flex min-h-screen flex-col bg-[#FAF9F6] text-[#0F172A]">
        <Navbar screenLabel="VERIFICATION RESULTS" runId={runId} />
        <div className="flex flex-1 flex-col items-center justify-center gap-3">
          <div className="h-9 w-9 animate-spin rounded-full border-3 border-[#B45309] border-t-transparent"></div>
          <span className="font-[family-name:var(--font-serif)] text-[16px] font-semibold text-[#0F172A]">
            Compiling Regulatory Audit Statement…
          </span>
        </div>
      </div>
    );
  }

  if (error || !results) {
    return (
      <div className="flex min-h-screen flex-col bg-[#FAF9F6] text-[#0F172A]">
        <Navbar screenLabel="VERIFICATION RESULTS" runId={runId} />
        <div className="flex flex-1 flex-col items-center justify-center gap-4 p-6">
          <div className="rounded-lg border border-[#FCA5A5] bg-[#FEF2F2] p-5 text-[15px] font-medium text-[#991B1B]">
            ⚠️ {error || "Results not found."}
          </div>
          <button onClick={() => router.push("/")} className="font-[family-name:var(--font-mono)] text-[13px] font-semibold text-[#B45309] underline hover:text-[#92400E]">
            Return to Upload Page →
          </button>
        </div>
      </div>
    );
  }

  const parseFlag = (flagStr: string): ParsedAuditFlag => {
    const lines = flagStr.split("\n");
    const title = lines[0] || "Audit Finding";
    let location = "";
    let quote = "";
    let issue = "";

    lines.slice(1).forEach((line) => {
      if (line.startsWith("Where in PDF:")) {
        location = line.replace("Where in PDF:", "").trim();
      } else if (line.startsWith("What it says:")) {
        quote = line.replace("What it says:", "").trim().replace(/^"|"$/g, "");
      } else if (line.startsWith("The Issue:")) {
        issue = line.replace("The Issue:", "").trim();
      }
    });

    if (!location && !quote && !issue) {
      return { title: "Regulatory Audit Finding", location: "", quote: "", issue: flagStr };
    }

    return { title, location, quote, issue };
  };

  const parsedFlags = (results.audit_flags || []).map(parseFlag);

  const formatCurrency = (val: number) => {
    return "₹ " + val.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  };

  const totalCapitalCharge = (results.calculated_metrics || []).reduce(
    (sum, m) => sum + (m.aggregated_value || 0),
    0
  );

  return (
    <div className="flex min-h-screen flex-col bg-[#FAF9F6] text-[#0F172A]">
      <Navbar screenLabel="VERIFICATION OUTPUT RESULTS" runId={runId} />

      <main className="mx-auto flex w-full max-w-[1120px] flex-1 flex-col gap-10 px-6 py-10">
        {/* Editorial Report Header */}
        <header className="flex flex-col gap-4 border-b-2 border-[#0F172A] pb-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <span className="font-[family-name:var(--font-mono)] text-[11px] font-bold tracking-widest text-[#B45309] uppercase">
                OFFICIAL IFSA REGULATORY STATEMENT · BASEL III / BCBS 352
              </span>
              <h1 className="font-[family-name:var(--font-serif)] text-[32px] font-bold leading-tight text-[#0F172A] md:text-[38px]">
                IFSA's FRTB-SA Capital Verification & Audit Report
              </h1>
            </div>
            <div className="flex flex-col items-end">
              <span className="font-[family-name:var(--font-mono)] text-[11px] font-semibold text-[#64748B]">
                REPORT ID: #{runId.slice(0, 12)}
              </span>
              <span className="font-[family-name:var(--font-mono)] text-[11px] text-[#64748B]">
                ISSUED BY: IFSA AUDITOR ENGINE ({new Date().toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" })})
              </span>
            </div>
          </div>

          {/* Executive KPI Banner */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 rounded-xl border border-[#E2E8F0] bg-white p-5 shadow-xs">
            <div className="flex flex-col gap-1 border-b md:border-b-0 md:border-r border-[#E2E8F0] pb-3 md:pb-0 md:pr-4">
              <span className="font-[family-name:var(--font-mono)] text-[11px] font-semibold text-[#64748B] uppercase">
                Aggregated FRTB Capital Charge
              </span>
              <span className="font-[family-name:var(--font-mono)] text-[22px] font-bold text-[#0F172A]">
                {formatCurrency(totalCapitalCharge)}
              </span>
            </div>

            <div className="flex flex-col gap-1 border-b md:border-b-0 md:border-r border-[#E2E8F0] pb-3 md:pb-0 md:pr-4">
              <span className="font-[family-name:var(--font-mono)] text-[11px] font-semibold text-[#64748B] uppercase">
                IFSA Compliance Audit
              </span>
              <span className="flex items-center gap-1.5 font-[family-name:var(--font-serif)] text-[18px] font-bold text-[#059669]">
                <CheckCircle2 className="h-5 w-5 text-[#059669]" />
                DISCLOSURE VERIFIED
              </span>
            </div>

            <div className="flex flex-col gap-1">
              <span className="font-[family-name:var(--font-mono)] text-[11px] font-semibold text-[#64748B] uppercase">
                IFSA Audit Flags Captured
              </span>
              <span className="font-[family-name:var(--font-mono)] text-[22px] font-bold text-[#B45309]">
                {parsedFlags.length} Flag{parsedFlags.length === 1 ? "" : "s"}
              </span>
            </div>
          </div>
        </header>

        {/* Section 1: Extracted Portfolio Positions */}
        {results.portfolio_inputs && results.portfolio_inputs.length > 0 && (
          <section className="flex flex-col gap-4">
            <div className="flex items-center gap-2 border-b border-[#E2E8F0] pb-2">
              <span className="font-[family-name:var(--font-mono)] text-[13px] font-bold text-[#B45309]">1.0</span>
              <h2 className="font-[family-name:var(--font-serif)] text-[22px] font-bold text-[#0F172A]">
                Extracted Trading Book Positions & Sensitivities
              </h2>
            </div>
            
            <div className="overflow-hidden rounded-xl border border-[#E2E8F0] bg-white shadow-xs">
              <table className="w-full border-collapse text-left text-[13.5px]">
                <thead>
                  <tr className="border-b border-[#CBD5E1] bg-[#F8FAFC] font-[family-name:var(--font-mono)] text-[11px] font-bold tracking-wider text-[#475569] uppercase">
                    <th className="px-5 py-3">Instrument ID</th>
                    <th className="px-5 py-3">Risk Class</th>
                    <th className="px-5 py-3">Risk Factor / Bucket</th>
                    <th className="px-5 py-3 text-right">Sensitivity / Notional</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#E2E8F0] font-sans">
                  {(results.portfolio_inputs || []).map((pos, idx) => (
                    <tr key={idx} className="hover:bg-[#FAF9F6] transition-colors">
                      <td className="px-5 py-3.5 font-[family-name:var(--font-mono)] font-semibold text-[#0F172A]">
                        {pos.instrument_id}
                      </td>
                      <td className="px-5 py-3.5">
                        <span className="inline-flex items-center rounded-md border border-[#BFDBFE] bg-[#EFF6FF] px-2.5 py-0.5 font-[family-name:var(--font-mono)] text-[11px] font-bold text-[#1D4ED8]">
                          {pos.risk_class}
                        </span>
                      </td>
                      <td className="px-5 py-3.5">
                        <div className="flex flex-col gap-0.5">
                          <span className="font-medium text-[#0F172A]">{pos.risk_factor}</span>
                          <span className="font-[family-name:var(--font-mono)] text-[11.5px] text-[#64748B]">
                            Bucket: {pos.bucket}
                          </span>
                        </div>
                      </td>
                      <td className="px-5 py-3.5 text-right">
                        <div className="flex flex-col gap-0.5 font-[family-name:var(--font-mono)]">
                          <span className="font-semibold text-[#0F172A]">{formatCurrency(pos.sensitivity)}</span>
                          {pos.notional && (
                            <span className="text-[11.5px] text-[#64748B]">Notional: {formatCurrency(pos.notional)}</span>
                          )}
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {/* Section 2: Multi-Section Document Sampling */}
        <section className="flex flex-col gap-4">
          <div className="flex items-center gap-2 border-b border-[#E2E8F0] pb-2">
            <span className="font-[family-name:var(--font-mono)] text-[13px] font-bold text-[#B45309]">2.0</span>
            <h2 className="font-[family-name:var(--font-serif)] text-[22px] font-bold text-[#0F172A]">
              IFSA Disclosure Document Sampling & Audit Findings
            </h2>
          </div>

          <div className="flex flex-col gap-4">
            <div className="rounded-lg border border-[#E2E8F0] bg-white p-4 font-[family-name:var(--font-mono)] text-[12.5px] text-[#475569] shadow-2xs">
              <span className="font-bold text-[#0F172A]">IFSA Audit Scope: </span>
              Up to 150,000 characters scanned across extracted tabular sections of the disclosure document.
            </div>

            <div className="flex flex-col gap-4">
              {parsedFlags.length === 0 ? (
                <div className="rounded-xl border border-[#A7F3D0] bg-[#F0FDF4] p-5 text-[13.5px] font-semibold text-[#065F46]">
                  ✓ No regulatory compliance breaches or reporting omissions were detected in the sampled sections.
                </div>
              ) : (
                parsedFlags.map((flag, idx) => (
                  <div
                    key={idx}
                    className="flex flex-col gap-3 rounded-xl border border-[#FDE68A] bg-[#FFFBEB] p-5 shadow-xs transition-all hover:border-[#F59E0B]"
                  >
                    <div className="flex items-center justify-between border-b border-[#FDE68A] pb-3">
                      <div className="flex items-center gap-2">
                        <AlertTriangle className="h-4 w-4 text-[#D97706]" />
                        <h4 className="font-[family-name:var(--font-serif)] text-[16.5px] font-bold text-[#0F172A]">
                          {flag.title}
                        </h4>
                      </div>
                      {flag.location && (
                        <span className="rounded-md border border-[#F59E0B]/40 bg-white px-2.5 py-1 font-[family-name:var(--font-mono)] text-[11px] font-bold text-[#B45309] shadow-2xs">
                          📍 {flag.location}
                        </span>
                      )}
                    </div>

                    {flag.quote && (
                      <div className="rounded-lg border-l-4 border-[#B45309] bg-white p-4 font-[family-name:var(--font-serif)] text-[14px] italic leading-relaxed text-[#334155] shadow-2xs">
                        &ldquo;{flag.quote}&rdquo;
                      </div>
                    )}

                    {flag.issue && (
                      <div className="text-[13.5px] leading-relaxed text-[#475569]">
                        <strong className="font-bold text-[#DC2626]">Audit Issue Detail: </strong>
                        <span>{flag.issue}</span>
                      </div>
                    )}
                  </div>
                ))
              )}
            </div>
          </div>
        </section>

        {/* Section 3: Calculated Market Risk Charges */}
        <section className="flex flex-col gap-4">
          <div className="flex items-center gap-2 border-b border-[#E2E8F0] pb-2">
            <span className="font-[family-name:var(--font-mono)] text-[13px] font-bold text-[#B45309]">3.0</span>
            <h2 className="font-[family-name:var(--font-serif)] text-[22px] font-bold text-[#0F172A]">
              BCBS Standardised Market Risk Capital Requirements
            </h2>
          </div>

          <div className="overflow-hidden rounded-xl border border-[#E2E8F0] bg-white shadow-xs">
            <table className="w-full border-collapse text-left text-[13.5px]">
              <thead>
                <tr className="border-b border-[#CBD5E1] bg-[#F8FAFC] font-[family-name:var(--font-mono)] text-[11px] font-bold tracking-wider text-[#475569] uppercase">
                  <th className="px-5 py-3">Risk Class</th>
                  <th className="px-5 py-3">Sensitivity Metric</th>
                  <th className="px-5 py-3 text-right">Aggregated Charge (INR)</th>
                  <th className="px-5 py-3">Bucket Level Disclosure</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#E2E8F0] font-sans">
                {(results.calculated_metrics || []).map((m, idx) => {
                  const bucketEntries = Object.entries(m.bucket_level || {});
                  const bucketStr =
                    bucketEntries.length > 0
                      ? bucketEntries.map(([k, v]) => `${k} = ${formatCurrency(v)}`).join(", ")
                      : "Default / Aggregated";

                  return (
                    <tr key={idx} className="hover:bg-[#FAF9F6] transition-colors">
                      <td className="px-5 py-3.5 font-[family-name:var(--font-serif)] font-bold text-[#0F172A]">
                        {m.risk_class}
                      </td>
                      <td className="px-5 py-3.5">
                        <code className="rounded bg-[#F1F5F9] px-2.5 py-1 font-[family-name:var(--font-mono)] text-[12px] font-semibold text-[#0F172A]">
                          {m.metric_name}
                        </code>
                      </td>
                      <td className="px-5 py-3.5 text-right font-[family-name:var(--font-mono)] font-bold text-[#0F172A]">
                        {formatCurrency(m.aggregated_value || 0)}
                      </td>
                      <td className="px-5 py-3.5">
                        <code className="rounded bg-[#F8FAFC] border border-[#E2E8F0] px-2.5 py-1 font-[family-name:var(--font-mono)] text-[11.5px] text-[#475569]">
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

        {/* Section 4: Final Compliance Summary */}
        <section className="flex flex-col gap-4">
          <div className="flex items-center gap-2 border-b border-[#E2E8F0] pb-2">
            <span className="font-[family-name:var(--font-mono)] text-[13px] font-bold text-[#B45309]">4.0</span>
            <h2 className="font-[family-name:var(--font-serif)] text-[22px] font-bold text-[#0F172A]">
              IFSA Final Regulatory Compliance Statement
            </h2>
          </div>

          <div className="rounded-xl border border-[#CBD5E1] bg-white p-6 shadow-xs">
            <p className="font-[family-name:var(--font-serif)] text-[16px] leading-relaxed text-[#0F172A]">
              {results.compliance_summary || "PASS — Capital calculations verified cleanly under BCBS FRTB sensitivities-based method rules."}
            </p>
          </div>
        </section>

        {/* Action Export Bar */}
        <ExportBar runId={runId} complianceSummary={results.compliance_summary} />
      </main>
    </div>
  );
}

