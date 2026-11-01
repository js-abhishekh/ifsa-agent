"use client";

import React, { useEffect, useRef } from "react";
import { LogEntry } from "@/lib/types";

export interface LiveFeedProps {
  logs: LogEntry[];
  error?: string | null;
}

// Color map using Airtable semantic + signature palette
const getLogStyle = (type: LogEntry["type"]) => {
  switch (type) {
    case "success":
      return {
        border: "#39bf45",
        bg: "#ffffff",
        dot: "#006400",
        text: "#181d26",
        nodeMeta: "#41454d",
      };
    case "flag":
      return {
        border: "#aa2d00",
        bg: "#f5e9d4",        // signature cream
        dot: "#aa2d00",       // signature coral
        text: "#181d26",
        nodeMeta: "#41454d",
      };
    case "metric":
      return {
        border: "#458fff",
        bg: "#ffffff",
        dot: "#254fad",       // info
        text: "#181d26",
        nodeMeta: "#41454d",
      };
    case "error":
      return {
        border: "#aa2d00",
        bg: "#aa2d00",        // coral signature card
        dot: "#ffffff",
        text: "#ffffff",      // on-dark
        nodeMeta: "#f5e9d4",
      };
    case "retry":
      return {
        border: "#dddddd",
        bg: "#f5e9d4",
        dot: "#d9a441",       // mustard
        text: "#181d26",
        nodeMeta: "#41454d",
      };
    case "info":
    default:
      return {
        border: "#dddddd",
        bg: "#ffffff",
        dot: "#9297a0",
        text: "#333840",
        nodeMeta: "#9297a0",
      };
  }
};

export default function LiveFeed({ logs, error }: LiveFeedProps) {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [logs]);

  return (
    <div className="flex h-full flex-col">
      {/* Error — dark surface card (hero-card-dark treatment) */}
      {error && (
        <div className="sticky top-0 z-10 mb-4 rounded-[12px] bg-[#181d26] p-3.5 text-[13px] font-[500] text-white">
          ⚠ {error}
        </div>
      )}

      <div className="flex flex-col gap-2 pb-4">
        {logs.map((log) => {
          const s = getLogStyle(log.type);
          return (
            <div
              key={log.id}
              className="animate-fade-slide-up flex flex-row items-start gap-3 rounded-[10px] border p-3.5 transition-all"
              style={{ borderColor: s.border, backgroundColor: s.bg }}
            >
              {/* Status dot */}
              <div
                className="mt-[5px] h-2 w-2 flex-none rounded-full"
                style={{ backgroundColor: s.dot }}
              />

              {/* Content */}
              <div className="flex flex-1 flex-col">
                <span
                  className="text-[13.5px] leading-relaxed"
                  style={{ color: s.text, fontWeight: 400 }}
                >
                  {log.text}
                </span>
                <div className="mt-1.5 flex items-center justify-between">
                  <span
                    className="font-[family-name:var(--font-mono)] text-[10.5px] tracking-wide uppercase"
                    style={{ color: s.nodeMeta }}
                  >
                    Agent: {log.node}
                  </span>
                </div>
                {log.meta && (
                  <pre
                    className="mt-2 overflow-x-auto rounded-[6px] border border-[#dddddd] bg-white p-2.5 font-[family-name:var(--font-mono)] text-[11px] leading-relaxed text-[#333840]"
                  >
                    {typeof log.meta === "string"
                      ? log.meta
                      : JSON.stringify(log.meta, null, 2)}
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
