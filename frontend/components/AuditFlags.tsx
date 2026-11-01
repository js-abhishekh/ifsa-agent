"use client";

import React from "react";
import { ValidationError } from "@/lib/types";

export interface AuditFlagsProps {
  flags: string[];
  validationErrors?: ValidationError[];
}

const parseFlag = (flag: string) => {
  const lines = flag.split("\n");
  const title = lines[0] || "Audit Finding";
  let location = "", quote = "", issue = "";

  lines.slice(1).forEach((line) => {
    if (line.startsWith("Where in PDF:"))   location = line.replace("Where in PDF:", "").trim();
    else if (line.startsWith("What it says:")) quote   = line.replace("What it says:", "").trim().replace(/^"|"$/g, "");
    else if (line.startsWith("The Issue:"))   issue   = line.replace("The Issue:", "").trim();
  });

  if (!location && !quote && !issue) {
    return { title: "Regulatory Audit Finding", location: "", quote: "", issue: flag };
  }
  return { title, location, quote, issue };
};

export default function AuditFlags({ flags, validationErrors = [] }: AuditFlagsProps) {
  const blockingErrors = validationErrors.filter((e) => e.severity === "blocking");
  const totalCount     = flags.length + blockingErrors.length;

  return (
    <div className="flex flex-col gap-4">
      {/* Section header */}
      <div className="flex items-center justify-between border-b border-[#dddddd] pb-3">
        <div className="flex items-center gap-2">
          {/* coral dot — brand voltage accent */}
          <div className="h-2 w-2 rounded-full bg-[#aa2d00]" />
          <h3 className="font-[family-name:var(--font-mono)] text-[11px] font-[600] tracking-widest text-[#181d26] uppercase">
            IFSA Regulatory Audit Findings ({totalCount})
          </h3>
        </div>
      </div>

      <div className="flex flex-col gap-4">
        {/* Blocking validation errors — signature-coral-card treatment */}
        {blockingErrors.map((err, idx) => (
          <div
            key={`err-${idx}`}
            className="rounded-[12px] bg-[#aa2d00] p-5"  // coral signature card
          >
            <div className="mb-2 flex items-center gap-2">
              <div className="h-2.5 w-2.5 rounded-full bg-white" />
              <div className="text-[15px] font-[500] text-white">
                Validation Error: {err.node}
              </div>
            </div>
            <div className="text-[13px] leading-relaxed text-white/85">{err.message}</div>
          </div>
        ))}

        {/* Empty state — success */}
        {flags.length === 0 && blockingErrors.length === 0 ? (
          <div className="rounded-[12px] border border-[#39bf45] bg-white p-6 text-center text-[14px] text-[#006400]">
            ✓ No regulatory compliance breaches detected.
          </div>
        ) : (
          flags.map((flagStr, idx) => {
            const parsed = parseFlag(flagStr);
            return (
              // cream-callout-card: signature cream, rounded-md (10px), hairline border
              <div
                key={`flag-${idx}`}
                className="flex flex-col gap-3.5 rounded-[10px] border border-[#dddddd] bg-[#f5e9d4] p-5"
              >
                {/* Flag header */}
                <div className="flex flex-wrap items-center justify-between gap-2 border-b border-[#dddddd] pb-3">
                  <div className="flex items-center gap-2">
                    {/* coral accent dot */}
                    <div className="h-2 w-2 rounded-full bg-[#aa2d00]" />
                    <h4 className="text-[16px] font-[500] text-[#181d26]">{parsed.title}</h4>
                  </div>
                  {parsed.location && (
                    <span className="rounded-[6px] border border-[#dddddd] bg-white px-2.5 py-1 font-[family-name:var(--font-mono)] text-[11px] font-[500] text-[#41454d]">
                      📍 {parsed.location}
                    </span>
                  )}
                </div>

                {/* Quote block — white canvas inset, coral left border */}
                {parsed.quote && (
                  <div className="rounded-[6px] border-l-4 border-[#aa2d00] bg-white p-3.5 text-[13.5px] italic leading-relaxed text-[#333840]">
                    &ldquo;{parsed.quote}&rdquo;
                  </div>
                )}

                {/* Issue detail */}
                {parsed.issue && (
                  <div className="text-[13px] leading-relaxed text-[#333840]">
                    <span className="font-[500] text-[#aa2d00]">Audit Issue: </span>
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
