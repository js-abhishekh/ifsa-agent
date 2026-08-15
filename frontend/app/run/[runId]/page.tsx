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

export default function WorkspacePage() {
  const params = useParams();
  const searchParams = useSearchParams();
  const router = useRouter();
  
  const runId = params.runId as string;
  const positionsParam = searchParams.get("positions");

  const [positions, setPositions] = useState<PortfolioPosition[]>([]);
  const [activeTab, setActiveTab] = useState<"feed" | "portfolio" | "pdf">("feed");
  const [fileUrl, setFileUrl] = useState<string | null>(null);
  const [extractionMsg, setExtractionMsg] = useState<string | null>(null);

  const { nodes, logs, finalResults, pipelineDone, error } = usePipelineSSE(runId);
  const runStarted = useRef(false);

  useEffect(() => {
    setFileUrl(`/data/uploads/${runId}.pdf`);
    const msg = sessionStorage.getItem(`frtb_msg_${runId}`);
    if (msg) setExtractionMsg(msg);

    // Guard: only start the pipeline once, even if the effect re-runs
    if (runStarted.current) return;
    runStarted.current = true;

    try {
      const parsed = positionsParam
        ? JSON.parse(decodeURIComponent(positionsParam))
        : [];
      setPositions(parsed);
      startRun(runId, parsed, 3).catch(console.error);
    } catch (e) {
      console.error("Failed to parse positions from URL");
      startRun(runId, [], 3).catch(console.error);
    }
  }, [runId, positionsParam]);

  useEffect(() => {
    if (pipelineDone && finalResults) {
      sessionStorage.setItem("frtb_results_" + runId, JSON.stringify(finalResults));
    }
  }, [pipelineDone, finalResults, runId]);

  const activeNode = [...nodes].reverse().find(n => n.status === "active") || 
                     [...nodes].reverse().find(n => n.status === "done");

  return (
    <div className="flex h-screen flex-col bg-[#FAF9F6] text-[#0F172A]">
      <Navbar screenLabel="LIVE WORKSPACE" runId={runId} />
      
      <div className="flex flex-1 min-h-0 flex-row">
        <PipelineRail nodes={nodes} />
        
        <div className="flex flex-1 flex-col relative bg-white">
          <div className="flex h-[48px] items-center gap-6 border-b border-[#E2E8F0] bg-[#FAF9F6] px-6">
            {(["feed", "portfolio", "pdf"] as const).map((tab) => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                className={`flex h-full items-center gap-2 border-b-2 text-[13px] font-semibold transition-colors ${
                  activeTab === tab 
                    ? "border-[#B45309] text-[#0F172A]" 
                    : "border-transparent text-[#64748B] hover:text-[#0F172A]"
                }`}
              >
                {tab === "feed" && <Activity className="h-3.5 w-3.5 text-[#B45309]" />}
                {tab === "portfolio" && <Table className="h-3.5 w-3.5 text-[#B45309]" />}
                {tab === "pdf" && <FileText className="h-3.5 w-3.5 text-[#B45309]" />}
                {tab === "feed" ? "Live Agent Feed" : tab === "portfolio" ? "Portfolio Review & Edit" : "PDF Disclosure Document"}
              </button>
            ))}
          </div>
          
          {extractionMsg && (
            <div className="mx-6 mt-4 flex items-center justify-between rounded-lg border border-[#FDE68A] bg-[#FFFBEB] p-3 text-[13px] font-medium text-[#92400E] shadow-xs">
              <span>⚠️ Partial Extraction Warning: {extractionMsg}</span>
              <button onClick={() => setExtractionMsg(null)} className="underline hover:text-[#B45309]">Dismiss</button>
            </div>
          )}

          <div className="flex-1 overflow-y-auto p-5 px-6">
            {activeTab === "feed" && <LiveFeed logs={logs} error={error} />}
            {activeTab === "portfolio" && (
              <PortfolioTable positions={positions} onPositionsChange={setPositions} />
            )}
            {activeTab === "pdf" && (
              <div className="h-full w-full rounded-lg border border-[#E2E8F0] bg-[#FAF9F6] flex items-center justify-center p-4">
                {fileUrl ? (
                  <iframe src={fileUrl} className="h-full w-full rounded border border-[#E2E8F0]" />
                ) : (
                  <div className="text-[14px] text-[#64748B] text-center border border-dashed border-[#CBD5E1] p-12 w-full h-full flex items-center justify-center font-[family-name:var(--font-mono)]">
                    PDF Document viewer placeholder.
                  </div>
                )}
              </div>
            )}
          </div>

          {pipelineDone && (
            <div className="animate-fade-slide-up absolute bottom-6 left-1/2 -translate-x-1/2 rounded-full shadow-lg">
              <button
                onClick={() => router.push(`/run/${runId}/results`)}
                className="flex items-center gap-2 rounded-full border border-[#B45309]/40 bg-[#0F172A] px-7 py-3 font-[family-name:var(--font-mono)] text-[14px] font-bold text-white shadow-md transition-all hover:bg-[#1E293B] hover:shadow-lg"
              >
                <span>View Full Regulatory Verification Results</span>
                <ArrowRight className="h-4 w-4 text-[#F59E0B]" />
              </button>
            </div>
          )}
        </div>
        
        <Inspector 
          activeNodeLabel={activeNode?.label ?? "—"} 
          dataSlice={activeNode?.dataSlice} 
        />
      </div>
    </div>
  );
}

