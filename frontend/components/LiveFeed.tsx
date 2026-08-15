"use client";

import React, { useEffect, useRef } from "react";
import { LogEntry } from "@/lib/types";

export interface LiveFeedProps {
  logs: LogEntry[];
  error?: string | null;
}

export default function LiveFeed({ logs, error }: LiveFeedProps) {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [logs]);

  const getLogStyle = (type: LogEntry["type"]) => {
    switch (type) {
      case "success":
        return { border: "#A7F3D0", bg: "#F0FDF4", dot: "#059669", text: "#065F46" };
      case "flag":
        return { border: "#FDE68A", bg: "#FFFBEB", dot: "#D97706", text: "#92400E" };
      case "metric":
        return { border: "#BFDBFE", bg: "#EFF6FF", dot: "#2563EB", text: "#1E40AF" };
      case "error":
        return { border: "#FECACA", bg: "#FEF2F2", dot: "#DC2626", text: "#991B1B" };
      case "retry":
        return { border: "#FED7AA", bg: "#FFF7ED", dot: "#EA580C", text: "#9A3412" };
      case "info":
      default:
        return { border: "#E2E8F0", bg: "#FFFFFF", dot: "#64748B", text: "#0F172A" };
    }
  };

  return (
    <div className="flex h-full flex-col">
      {error && (
        <div className="sticky top-0 z-10 mb-4 rounded-lg border border-[#F59E0B]/40 bg-[#FFFBEB] p-3 text-[13px] font-semibold text-[#92400E] shadow-2xs">
          ⚠️ {error}
        </div>
      )}
      <div className="flex flex-col gap-2.5 pb-4">
        {logs.map((log) => {
          const style = getLogStyle(log.type);
          return (
            <div
              key={log.id}
              className="animate-fade-slide-up flex flex-row items-start gap-3 rounded-lg border p-3.5 shadow-2xs transition-all"
              style={{ borderColor: style.border, backgroundColor: style.bg }}
            >
              <div
                className="mt-1.5 h-[8px] w-[8px] flex-none rounded-full"
                style={{ backgroundColor: style.dot }}
              />
              <div className="flex flex-col flex-1">
                <span className="text-[13.5px] font-medium leading-relaxed" style={{ color: style.text }}>
                  {log.text}
                </span>
                <div className="mt-1.5 flex items-center justify-between">
                  <span className="font-[family-name:var(--font-mono)] text-[10.5px] font-semibold tracking-wide text-[#64748B] uppercase">
                    Agent: {log.node}
                  </span>
                </div>
                {log.meta && (
                  <pre className="mt-2 overflow-x-auto rounded border border-[#E2E8F0] bg-[#F8FAFC] p-2.5 font-[family-name:var(--font-mono)] text-[11px] leading-relaxed text-[#334155]">
                    {typeof log.meta === "string" ? log.meta : JSON.stringify(log.meta, null, 2)}
                  </pre>
                )}
              </div>
            </div>
          );
        })}
        <div ref={bottomRef} />
      </div>
    </div>
  );
}

