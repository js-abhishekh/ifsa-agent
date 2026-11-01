"use client";

import React from "react";
import { ComplianceStatus } from "@/lib/types";

export interface ResultsBannerProps {
  status: ComplianceStatus;
  summary: string;
}

// Airtable signature-card system:
//   PASS    → signature-forest-card: deep green #0a2e0e, on-dark white text
//   WARNING → cream-callout-card: #f5e9d4, ink #181d26
//   FAIL    → signature-coral-card: #aa2d00, on-dark white text
export default function ResultsBanner({ status, summary }: ResultsBannerProps) {
  let bg        = "#aa2d00";   // coral — default FAIL
  let text      = "#ffffff";   // on-dark
  let dot       = "#ffffff";
  let label     = "IFSA Compliance Breach / Incomplete";
  let borderClr = "#aa2d00";

  if (status === "PASS") {
    bg        = "#0a2e0e";    // signature forest
    text      = "#ffffff";
    dot       = "#39bf45";   // success-border green
    label     = "IFSA Regulatory Audit — Pass";
    borderClr = "#0a2e0e";
  } else if (status === "WARNING") {
    bg        = "#f5e9d4";    // signature cream callout
    text      = "#181d26";   // ink
    dot       = "#aa2d00";   // coral dot
    label     = "IFSA Audit — Attention Required";
    borderClr = "#dddddd";
  }

  return (
    <div
      className="flex w-full flex-row items-center justify-between rounded-[12px] border p-5"
      style={{ backgroundColor: bg, borderColor: borderClr }}
    >
      <div className="flex flex-col gap-1">
        {/* title-sm: 18px/bold */}
        <div
          className="font-milligram text-[17px] font-bold tracking-tight leading-snug"
          style={{ color: text }}
        >
          {label}
        </div>
        {/* body-md: 14px/400 */}
        <div
          className="font-[family-name:var(--font-mono)] text-[12.5px]"
          style={{ color: text, opacity: 0.8 }}
        >
          {summary}
        </div>
      </div>
      <div
        className="h-3 w-3 flex-shrink-0 rounded-full"
        style={{ backgroundColor: dot }}
      />
    </div>
  );
}
