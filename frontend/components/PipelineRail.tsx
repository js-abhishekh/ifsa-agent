"use client";

import React from "react";
import { NodeState } from "@/lib/types";

export interface PipelineRailProps {
  nodes: NodeState[];
}

export default function PipelineRail({ nodes }: PipelineRailProps) {
  return (
    <div className="w-[280px] flex-shrink-0 border-r border-[#E2E8F0] bg-[#FAF9F6] px-4 py-5 overflow-y-auto">
      <div className="mb-[16px] border-b border-[#E2E8F0] pb-2 font-[family-name:var(--font-mono)] text-[10.5px] font-bold tracking-widest text-[#B45309] uppercase">
        IFSA AUDIT PIPELINE AGENTS
      </div>
      <div className="flex flex-col gap-2">
        {nodes.map((node) => {
          const isActive = node.status === "active";
          const isDone = node.status === "done";
          const isError = node.status === "error";
          const isPending = node.status === "pending";

          let dotColor = "#CBD5E1";
          let borderClass = "border-transparent";
          let bgClass = "bg-transparent";
          let labelColor = "#64748B";

          if (isActive) {
            dotColor = "#D97706";
            borderClass = "border-[#F59E0B]/40";
            bgClass = "bg-[#FFFBEB]";
            labelColor = "#0F172A";
          } else if (isDone) {
            dotColor = "#059669";
            borderClass = "border-transparent";
            bgClass = "bg-white/60";
            labelColor = "#1E293B";
          } else if (isError) {
            dotColor = "#DC2626";
            borderClass = "border-[#FCA5A5]";
            bgClass = "bg-[#FEF2F2]";
            labelColor = "#991B1B";
          }

          return (
            <div
              key={node.id}
              className={`flex flex-row items-start gap-[12px] rounded-lg border p-2.5 transition-all shadow-2xs ${borderClass} ${bgClass} ${
                isActive ? "animate-pulse-glow" : ""
              }`}
            >
              <div className="flex w-[20px] flex-shrink-0 justify-center pt-[5px]">
                <div
                  className={`h-[8px] w-[8px] rounded-full ${isActive ? "animate-pulse-dot" : ""}`}
                  style={{ backgroundColor: dotColor }}
                />
              </div>
              <div className="flex flex-col">
                <span className={`text-[13px] font-semibold ${isActive ? "font-bold" : ""}`} style={{ color: labelColor }}>
                  {node.label}
                </span>
                <span className="text-[11.5px] leading-snug text-[#64748B] mt-0.5">
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

