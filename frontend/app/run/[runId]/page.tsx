"use client";

import React, { useEffect, useRef, useState } from "react";
import { useParams, useSearchParams, useRouter } from "next/navigation";
import Navbar from "@/components/Navbar";
import PipelineRail from "@/components/PipelineRail";
import LiveFeed from "@/components/LiveFeed";
import PortfolioTable from "@/components/PortfolioTable";
import Inspector from "@/components/Inspector";
import { startRun } from "@/lib/api";
import { usePipelineSSE } from "@/hooks/usePipelineSSE";
import { PortfolioPosition } from "@/lib/types";
import { ArrowRight, Activity, Table, FileText } from "lucide-react";

const TABS = [
  { id: "feed",      label: "Live Agent Feed",           Icon: Activity  },
  { id: "portfolio", label: "Portfolio Review & Edit",   Icon: Table     },
  { id: "pdf",       label: "PDF Disclosure Document",   Icon: FileText  },
] as const;
type TabId = (typeof TABS)[number]["id"];

export default function WorkspacePage() {
  const params       = useParams();
  const searchParams = useSearchParams();
  const router       = useRouter();

  const runId          = params.runId as string;
  const positionsParam = searchParams.get("positions");

  const [positions,    setPositions]    = useState<PortfolioPosition[]>([]);
  const [activeTab,    setActiveTab]    = useState<TabId>("feed");
  const [fileUrl,      setFileUrl]      = useState<string | null>(null);
  const [extractionMsg, setExtractionMsg] = useState<string | null>(null);

  const { nodes, logs, finalResults, pipelineDone, error } = usePipelineSSE(runId);
  const runStarted = useRef(false);

  useEffect(() => {
    setFileUrl(`/data/uploads/${runId}.pdf`);
    const msg = sessionStorage.getItem(`frtb_msg_${runId}`);
    if (msg) setExtractionMsg(msg);

    if (runStarted.current) return;
    runStarted.current = true;

    try {
      const parsed = positionsParam ? JSON.parse(decodeURIComponent(positionsParam)) : [];
      setPositions(parsed);
      startRun(runId, parsed, 3).catch(console.error);
    } catch {
      console.error("Failed to parse positions from URL");
      startRun(runId, [], 3).catch(console.error);
    }
  }, [runId, positionsParam]);

  useEffect(() => {
    if (pipelineDone && finalResults) {
      sessionStorage.setItem("frtb_results_" + runId, JSON.stringify(finalResults));
    }
  }, [pipelineDone, finalResults, runId]);

  const activeNode =
    [...nodes].reverse().find((n) => n.status === "active") ||
    [...nodes].reverse().find((n) => n.status === "done");

  return (
    <div className="flex h-screen flex-col bg-white text-[#181d26]">
      <Navbar screenLabel="LIVE WORKSPACE" runId={runId} />

      <div className="flex flex-1 min-h-0 flex-row">
        {/* Left rail */}
        <PipelineRail nodes={nodes} />

        {/* Main content */}
        <div className="flex flex-1 flex-col relative bg-white">

          {/* Tab bar — Airtable top-nav variant, 48px, hairline bottom */}
          <div className="flex h-[48px] items-center gap-6 border-b border-[#dddddd] bg-white px-6">
            {TABS.map(({ id, label, Icon }) => (
              <button
                key={id}
                onClick={() => setActiveTab(id)}
                className={`flex h-full items-center gap-2 border-b-2 text-[13px] font-[500] transition-colors ${
                  activeTab === id
                    ? "border-[#181d26] text-[#181d26]"
                    : "border-transparent text-[#9297a0]"
                }`}
              >
                {/* Coral dot accent on active tab icon */}
                <Icon className={`h-3.5 w-3.5 ${activeTab === id ? "text-[#aa2d00]" : ""}`} />
                {label}
              </button>
            ))}
          </div>

          {/* Extraction warning — cream-callout-card */}
          {extractionMsg && (
            <div className="mx-6 mt-4 flex items-center justify-between rounded-[10px] border border-[#dddddd] bg-[#f5e9d4] p-3.5 text-[13px] text-[#181d26]">
              <span>⚠ Partial Extraction Warning: {extractionMsg}</span>
              <button
                onClick={() => setExtractionMsg(null)}
                className="ml-4 rounded-[6px] border border-[#dddddd] bg-white px-2.5 py-1 text-[12px] font-[500] text-[#181d26] transition-colors active:bg-[#e0e2e6]"
              >
                Dismiss
              </button>
            </div>
          )}

          {/* Tab content */}
          <div className="flex-1 overflow-y-auto p-5 px-6">
            {activeTab === "feed" && <LiveFeed logs={logs} error={error} />}

            {activeTab === "portfolio" && (
              <PortfolioTable positions={positions} onPositionsChange={setPositions} />
            )}

            {activeTab === "pdf" && (
              <div className="h-full w-full rounded-[10px] border border-[#dddddd] bg-[#f8fafc] flex items-center justify-center p-4">
                {fileUrl ? (
                  <iframe src={fileUrl} className="h-full w-full rounded-[6px] border border-[#dddddd]" />
                ) : (
                  <div className="text-[14px] text-[#9297a0] text-center border border-dashed border-[#dddddd] p-12 w-full h-full flex items-center justify-center font-[family-name:var(--font-mono)]">
                    PDF Document viewer placeholder.
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Pipeline done CTA — button-primary floating pill */}
          {pipelineDone && (
            <div className="animate-fade-slide-up absolute bottom-6 left-1/2 -translate-x-1/2">
              <button
                onClick={() => router.push(`/run/${runId}/results`)}
                className="flex items-center gap-2.5 rounded-[12px] bg-[#181d26] px-7 py-3.5 text-[14px] font-[500] text-white transition-colors active:bg-[#0d1218]"
              >
                View Full Regulatory Verification Results
                <ArrowRight className="h-4 w-4 text-white/70" />
              </button>
            </div>
          )}
        </div>

        {/* Right inspector rail */}
        <Inspector
          activeNodeLabel={activeNode?.label ?? "—"}
          dataSlice={activeNode?.dataSlice}
        />
      </div>
    </div>
  );
}
