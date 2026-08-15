"use client";

import React from "react";
import { ComplianceStatus } from "@/lib/types";

export interface ResultsBannerProps {
  status: ComplianceStatus;
  summary: string;
}

export default function ResultsBanner({ status, summary }: ResultsBannerProps) {
  let style = { dot: "#DC2626", bg: "#FEF2F2", border: "#FCA5A5", text: "#991B1B" };
  let label = "IFSA COMPLIANCE BREACH / INCOMPLETE";

  if (status === "PASS") {
    style = { dot: "#059669", bg: "#F0FDF4", border: "#A7F3D0", text: "#065F46" };
    label = "IFSA REGULATORY AUDIT PASS";
  } else if (status === "WARNING") {
    style = { dot: "#D97706", bg: "#FFFBEB", border: "#FDE68A", text: "#92400E" };
    label = "IFSA AUDIT ATTENTION REQUIRED";
  }

  return (
    <div
      className="flex w-full flex-row items-center justify-between rounded-xl border p-5 shadow-xs transition-all"
      style={{ backgroundColor: style.bg, borderColor: style.border }}
    >
      <div className="flex flex-col gap-1">
        <div className="font-[family-name:var(--font-serif)] text-[17px] font-bold tracking-tight" style={{ color: style.text }}>
          {label}
        </div>
        <div className="font-[family-name:var(--font-mono)] text-[12.5px] text-[#475569]">
          {summary}
        </div>
      </div>
      <div
        className="h-[12px] w-[12px] flex-shrink-0 rounded-full shadow-2xs"
        style={{ backgroundColor: style.dot }}
      />
    </div>
  );
}

