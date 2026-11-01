"use client";

import React from "react";

export interface InspectorProps {
  activeNodeLabel: string;
  dataSlice?: Record<string, unknown>;
}

// Airtable: surface-soft side panel, hairline left border
export default function Inspector({ activeNodeLabel, dataSlice }: InspectorProps) {
  return (
    <div className="w-[300px] flex-shrink-0 border-l border-[#dddddd] bg-[#f8fafc] p-5 overflow-y-auto">
      {/* Section label — caption 14px/500 */}
      <div className="mb-3 border-b border-[#dddddd] pb-3 font-[family-name:var(--font-mono)] text-[11px] font-[600] tracking-widest text-[#41454d] uppercase">
        Agent Inspector
      </div>

      {/* Active node label — title-sm 18px/500 */}
      <div className="mb-3 text-[15px] font-[500] text-[#181d26] leading-snug">
        {activeNodeLabel}
      </div>

      {/* Data pre — white canvas, hairline border, body text */}
      <pre className="overflow-x-auto rounded-[6px] border border-[#dddddd] bg-white p-3.5 font-[family-name:var(--font-mono)] text-[11px] leading-[1.6] text-[#333840]">
        {dataSlice
          ? JSON.stringify(dataSlice, null, 2)
          : "Awaiting pipeline start…"}
      </pre>
    </div>
  );
}
