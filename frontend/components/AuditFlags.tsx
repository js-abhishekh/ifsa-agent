"use client";

import React from "react";
import { ValidationError } from "@/lib/types";

export interface AuditFlagsProps {
  flags: string[];
  validationErrors?: ValidationError[];
}

export default function AuditFlags({ flags, validationErrors = [] }: AuditFlagsProps) {
  const blockingErrors = validationErrors.filter((e) => e.severity === "blocking");
  const totalCount = flags.length + blockingErrors.length;

  const parseFlag = (flag: string) => {
    const lines = flag.split("\n");
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
      return { title: "Regulatory Audit Finding", location: "", quote: "", issue: flag };
    }

    return { title, location, quote, issue };
  };

  return (
    <div className="flex flex-col gap-4">
      <div className="flex items-center justify-between border-b border-[#E2E8F0] pb-2">
        <h3 className="font-[family-name:var(--font-mono)] text-[11px] font-bold tracking-wider text-[#B45309] uppercase">
          📋 IFSA REGULATORY AUDIT FINDINGS ({totalCount})
        </h3>
      </div>
      
      <div className="flex flex-col gap-4">
        {blockingErrors.map((err, idx) => (
          <div key={`err-${idx}`} className="rounded-xl border border-[#FCA5A5] bg-[#FEF2F2] p-5 shadow-xs">
            <div className="mb-2 flex items-center gap-2">
              <div className="h-2.5 w-2.5 rounded-full bg-[#DC2626]" />
              <div className="font-[family-name:var(--font-serif)] text-[15px] font-bold text-[#991B1B]">
                IFSA Audit Validation Error: {err.node}
              </div>
            </div>
            <div className="mt-2 text-[13px] text-[#7F1D1D] leading-relaxed">{err.message}</div>
          </div>
        ))}

        {flags.length === 0 && blockingErrors.length === 0 ? (
          <div className="rounded-xl border border-[#E2E8F0] bg-white p-6 text-center text-[13.5px] font-medium text-[#059669]">
            ✓ No regulatory compliance breaches detected by IFSA Auditor in the disclosure text.
          </div>
        ) : (
          flags.map((flagStr, idx) => {
            const parsed = parseFlag(flagStr);
            return (
              <div
                key={`flag-${idx}`}
                className="flex flex-col gap-3.5 rounded-xl border border-[#FDE68A] bg-[#FFFBEB] p-5 shadow-xs transition-all hover:border-[#F59E0B]"
              >
                {/* Header */}
                <div className="flex flex-wrap items-center justify-between gap-2 border-b border-[#FDE68A] pb-3">
                  <div className="flex items-center gap-2">
                    <span className="text-base">🚩</span>
                    <h4 className="font-[family-name:var(--font-serif)] text-[16px] font-bold text-[#0F172A]">{parsed.title}</h4>
                  </div>
                  {parsed.location && (
                    <span className="rounded-md border border-[#F59E0B]/40 bg-white px-2.5 py-1 font-[family-name:var(--font-mono)] text-[11px] font-bold text-[#B45309] shadow-2xs">
                      📍 {parsed.location}
                    </span>
                  )}
                </div>

                {/* Quote */}
                {parsed.quote && (
                  <div className="rounded-lg border-l-4 border-[#B45309] bg-white p-3.5 font-[family-name:var(--font-serif)] text-[13.5px] italic leading-relaxed text-[#334155] shadow-2xs">
                    &ldquo;{parsed.quote}&rdquo;
                  </div>
                )}

                {/* Issue Explanation */}
                {parsed.issue && (
                  <div className="text-[13px] leading-relaxed text-[#475569]">
                    <span className="font-semibold text-[#DC2626]">The Issue: </span>
                    {parsed.issue}
                  </div>
                )}
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}

