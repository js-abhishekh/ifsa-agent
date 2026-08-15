"use client";

import React from "react";

export interface InspectorProps {
  activeNodeLabel: string;
  dataSlice?: Record<string, unknown>;
}

export default function Inspector({ activeNodeLabel, dataSlice }: InspectorProps) {
  return (
    <div className="w-[320px] flex-shrink-0 border-l border-[#E2E8F0] bg-[#FAF9F6] p-5 overflow-y-auto">
      <div className="mb-[14px] border-b border-[#E2E8F0] pb-2 font-[family-name:var(--font-mono)] text-[10.5px] font-bold tracking-widest text-[#B45309] uppercase">
        AGENT STATE INSPECTOR
      </div>
      <div className="mb-3 font-[family-name:var(--font-serif)] text-[15px] font-bold text-[#0F172A]">
        {activeNodeLabel}
      </div>
      <pre className="overflow-x-auto rounded-lg border border-[#E2E8F0] bg-white p-3.5 font-[family-name:var(--font-mono)] text-[11px] leading-[1.6] text-[#334155] shadow-xs">
        {dataSlice ? JSON.stringify(dataSlice, null, 2) : "Awaiting pipeline start…"}
      </pre>
    </div>
  );
}

