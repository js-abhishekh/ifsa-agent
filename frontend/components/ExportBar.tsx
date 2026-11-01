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
      const url  = URL.createObjectURL(blob);
      const a    = document.createElement("a");
      a.href     = url;
      a.download = `frtb_run_${runId}.json`;
      a.click();
      URL.revokeObjectURL(url);
    } catch {
      showToast("Failed to export JSON");
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(complianceSummary);
    showToast("Copied compliance statement to clipboard!");
  };

  const handlePdf = () => showToast("PDF export generation queued");

  return (
    <div className="mt-6 flex flex-wrap items-center gap-3 border-t border-[#dddddd] pt-5 pb-8 relative">
      {/* Primary action — button-primary: near-black, white text, rounded-lg (12px) */}
      <button
        onClick={handlePdf}
        className="flex cursor-pointer items-center gap-2 rounded-[12px] bg-[#181d26] px-5 py-3 text-[14px] font-[500] text-white transition-colors active:bg-[#0d1218]"
      >
        <Download className="h-4 w-4" />
        Download IFSA Executive Summary PDF
      </button>

      {/* Secondary actions — button-secondary: white canvas, hairline border, ink text, rounded-lg */}
      <button
        onClick={handleExportJson}
        className="flex cursor-pointer items-center gap-2 rounded-[12px] border border-[#dddddd] bg-white px-5 py-3 text-[14px] font-[500] text-[#181d26] transition-colors active:bg-[#e0e2e6]"
      >
        <FileJson className="h-4 w-4 text-[#41454d]" />
        Export Audit Run JSON
      </button>

      <button
        onClick={handleCopy}
        className="flex cursor-pointer items-center gap-2 rounded-[12px] border border-[#dddddd] bg-white px-5 py-3 text-[14px] font-[500] text-[#181d26] transition-colors active:bg-[#e0e2e6]"
      >
        <Copy className="h-4 w-4 text-[#41454d]" />
        Copy Compliance Statement
      </button>

      {/* Toast — forest signature card */}
      {toastMsg && (
        <div className="absolute left-0 top-20 flex items-center gap-2 rounded-[10px] bg-[#0a2e0e] px-4 py-2.5 text-[13px] font-[500] text-white">
          <Check className="h-3.5 w-3.5 text-[#39bf45]" />
          {toastMsg}
        </div>
      )}
    </div>
  );
}
