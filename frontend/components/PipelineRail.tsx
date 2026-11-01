"use client";

import React from "react";
import { NodeState } from "@/lib/types";

export interface PipelineRailProps {
  nodes: NodeState[];
}

// Airtable topic-filter-rail: 240px surface-soft bg, editorial hierarchy
export default function PipelineRail({ nodes }: PipelineRailProps) {
  return (
    <div className="w-[260px] flex-shrink-0 border-r border-[#dddddd] bg-[#f8fafc] px-4 py-5 overflow-y-auto">
      {/* Section header — label-md 16px/500 */}
      <div className="mb-4 border-b border-[#dddddd] pb-3 text-[11px] font-[600] tracking-widest text-[#41454d] uppercase font-[family-name:var(--font-mono)]">
        Pipeline Agents
      </div>

      <div className="flex flex-col gap-1.5">
        {nodes.map((node) => {
          const isActive  = node.status === "active";
          const isDone    = node.status === "done";
          const isError   = node.status === "error";

          // Airtable signature surface color mapping
          let dotColor   = "#dddddd";        // pending — hairline
          let rowBg      = "bg-transparent";
          let rowBorder  = "border-transparent";
          let labelColor = "#9297a0";        // muted

          if (isActive) {
            dotColor   = "#aa2d00";          // signature coral — brand voltage
            rowBg      = "bg-[#f5e9d4]";     // cream callout surface
            rowBorder  = "border-[#aa2d00]/30";
            labelColor = "#181d26";          // ink
          } else if (isDone) {
            dotColor   = "#006400";          // success
            rowBg      = "bg-white";
            rowBorder  = "border-[#dddddd]";
            labelColor = "#333840";          // body
          } else if (isError) {
            dotColor   = "#aa2d00";
            rowBg      = "bg-[#aa2d00]";     // coral signature card
            rowBorder  = "border-[#aa2d00]";
            labelColor = "#ffffff";          // on-dark
          }

          return (
            <div
              key={node.id}
              className={`flex flex-row items-start gap-3 rounded-[10px] border p-2.5 transition-all ${rowBorder} ${rowBg} ${
                isActive ? "animate-pulse-glow" : ""
              }`}
            >
              {/* Status dot */}
              <div className="flex w-5 flex-shrink-0 justify-center pt-[6px]">
                <div
                  className={`h-2 w-2 rounded-full ${isActive ? "animate-pulse-dot" : ""}`}
                  style={{ backgroundColor: dotColor }}
                />
              </div>

              {/* Label + description */}
              <div className="flex flex-col">
                <span
                  className="font-milligram text-[13px] leading-snug"
                  style={{ color: labelColor, fontWeight: isActive ? 500 : 400 }}
                >
                  {node.label}
                </span>
                <span className="mt-0.5 text-[11.5px] leading-snug text-[#9297a0]">
                  {node.desc}
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
