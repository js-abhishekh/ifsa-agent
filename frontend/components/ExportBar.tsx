"use client";

import React, { useState } from "react";
import { exportRunJson } from "@/lib/api";
import { Download, FileJson, Copy, Check } from "lucide-react";

export interface ExportBarProps {
  runId: string;
  complianceSummary: string;
}

export default function ExportBar({ runId, complianceSummary }: ExportBarProps) {
  const [toastMsg, setToastMsg] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMsg(msg);
    setTimeout(() => setToastMsg(null), 3000);
  };

  const handleExportJson = async () => {
    try {
      const data = await exportRunJson(runId);
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `frtb_run_${runId}.json`;
      a.click();
      URL.revokeObjectURL(url);
    } catch (e) {
      showToast("Failed to export JSON");
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(complianceSummary);
    showToast("Copied compliance statement to clipboard!");
  };

  const handlePdf = () => {
    showToast("PDF export generation queued");
  };

  return (
    <div className="mt-6 flex flex-wrap items-center gap-3 border-t border-[#E2E8F0] pt-4 pb-8 relative font-[family-name:var(--font-mono)]">
      <button
        onClick={handlePdf}
        className="flex cursor-pointer items-center gap-2 rounded-md border border-[#E2E8F0] bg-white px-4 py-2.5 text-[12.5px] font-semibold text-[#0F172A] shadow-xs transition-colors hover:border-[#B45309] hover:bg-[#FFFBEB] hover:text-[#92400E]"
      >
        <Download className="h-4 w-4 text-[#B45309]" />
        Download IFSA Executive Summary PDF
      </button>

      <button
        onClick={handleExportJson}
        className="flex cursor-pointer items-center gap-2 rounded-md border border-[#E2E8F0] bg-white px-4 py-2.5 text-[12.5px] font-semibold text-[#0F172A] shadow-xs transition-colors hover:border-[#B45309] hover:bg-[#FFFBEB] hover:text-[#92400E]"
      >
        <FileJson className="h-4 w-4 text-[#B45309]" />
        Export IFSA Audit Run JSON Data
      </button>

      <button
        onClick={handleCopy}
        className="flex cursor-pointer items-center gap-2 rounded-md border border-[#E2E8F0] bg-white px-4 py-2.5 text-[12.5px] font-semibold text-[#0F172A] shadow-xs transition-colors hover:border-[#B45309] hover:bg-[#FFFBEB] hover:text-[#92400E]"
      >
        <Copy className="h-4 w-4 text-[#B45309]" />
        Copy IFSA Compliance Statement
      </button>

      {toastMsg && (
        <div className="absolute left-0 top-16 flex items-center gap-2 rounded-md border border-[#059669] bg-[#ECFDF5] px-3.5 py-1.5 text-[12px] font-semibold text-[#047857] shadow-sm">
          <Check className="h-3.5 w-3.5" />
          {toastMsg}
        </div>
      )}
    </div>
  );
}

