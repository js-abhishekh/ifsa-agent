"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import Navbar from "@/components/Navbar";
import { uploadPdf, loadSamplePortfolio } from "@/lib/api";
import { UploadCloud, FileText, ArrowRight, ShieldCheck, PieChart, Sparkles } from "lucide-react";

export default function Home() {
  const router = useRouter();
  const [dragOver, setDragOver]   = useState(false);
  const [loading, setLoading]     = useState(false);
  const [errorMsg, setErrorMsg]   = useState<string | null>(null);

  const handleFile = async (file: File) => {
    if (file.type !== "application/pdf") {
      setErrorMsg("Please upload a valid PDF file.");
      return;
    }
    setErrorMsg(null);
    setLoading(true);
    try {
      const res = await uploadPdf(file);
      if (res.extraction_message) {
        sessionStorage.setItem(`frtb_msg_${res.run_id}`, res.extraction_message);
      }
      const positionsParam = encodeURIComponent(JSON.stringify(res.extracted_positions || []));
      router.push(`/run/${res.run_id}?positions=${positionsParam}`);
    } catch (e: any) {
      setErrorMsg(e.message || "An error occurred during upload.");
      setLoading(false);
    }
  };

  const handleDrop       = (e: React.DragEvent) => { e.preventDefault(); setDragOver(false); const f = e.dataTransfer.files[0]; if (f) handleFile(f); };
  const handleDragOver   = (e: React.DragEvent) => { e.preventDefault(); setDragOver(true); };
  const handleDragLeave  = () => setDragOver(false);
  const openFilePicker   = () => document.getElementById("pdf-upload")?.click();
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => { const f = e.target.files?.[0]; if (f) handleFile(f); };

  const startDemo = async () => {
    setErrorMsg(null);
    setLoading(true);
    try {
      const res = await loadSamplePortfolio();
      const positionsParam = encodeURIComponent(JSON.stringify(res.extracted_positions || []));
      router.push(`/run/${res.run_id}?positions=${positionsParam}`);
    } catch (e: any) {
      setErrorMsg(e.message || "Failed to load sample portfolio.");
      setLoading(false);
    }
  };

  return (
    <div className="flex min-h-screen flex-col bg-white text-[#181d26]">
      <Navbar screenLabel="PORTFOLIO UPLOAD" />

      {/* ── Hero Band — white canvas, 96px vertical padding ─────────────────── */}
      <main className="flex flex-1 flex-col items-center px-6 py-24 gap-10">

        {/* Hero copy */}
        <div className="w-full max-w-[800px] text-center">
          {/* Hairline badge */}
          <div className="mx-auto mb-6 inline-flex items-center gap-2 rounded-full border border-[#dddddd] bg-white px-4 py-1.5 font-[family-name:var(--font-mono)] text-[11px] font-[500] tracking-wider text-[#41454d] uppercase">
            <span className="inline-block h-2 w-2 rounded-full bg-[#aa2d00]" />
            IFSA · FRTB-SA Regulatory Audit Engine · BCBS 352
          </div>

          {/* display-lg: 40px / weight 700 — Milligram Bold */}
          <h1 className="font-milligram text-[40px] font-bold leading-[1.2] text-[#181d26]">
            IFSA's FRTB-SA Auditor
          </h1>
          <p className="font-milligram mt-2 text-[32px] font-bold leading-[1.2] text-[#333840]">
            Capital Calculation &amp; Compliance Audit
          </p>

          {/* body-md: 14px/400 */}
          <p className="mx-auto mt-6 max-w-[600px] text-[14px] leading-[1.6] text-[#41454d]">
            Submit any institutional Bank Disclosure or Trading Book PDF. IFSA's autonomous
            agent extracts sensitivity risk vectors, computes BCBS capital charges, and validates
            disclosures against Basel&nbsp;III regulatory mandates.
          </p>
        </div>

        {/* Error — cream callout */}
        {errorMsg && (
          <div className="w-full max-w-[600px] rounded-[10px] border border-[#dddddd] bg-[#f5e9d4] p-4 text-[13.5px] text-[#181d26]">
            ⚠ {errorMsg}
          </div>
        )}

        {/* ── Dropzone — text-input + demo-grid-card style ─────────────────── */}
        <div
          onClick={openFilePicker}
          onDrop={handleDrop}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          className={`group flex h-[220px] w-full max-w-[600px] cursor-pointer flex-col items-center justify-center gap-4 rounded-[10px] border-2 border-dashed p-6 transition-all ${
            dragOver
              ? "border-[#181d26] bg-[#f8fafc]"
              : "border-[#dddddd] bg-white"
          }`}
        >
          <input
            id="pdf-upload"
            type="file"
            accept=".pdf"
            className="hidden"
            onChange={handleFileChange}
          />

          {loading ? (
            <div className="flex flex-col items-center gap-3">
              {/* Spinner — coral accent */}
              <div className="h-8 w-8 animate-spin rounded-full border-2 border-[#aa2d00] border-t-transparent" />
              <span className="text-[16px] font-[400] text-[#181d26]">
                Extracting trading book sensitivities…
              </span>
              <span className="font-[family-name:var(--font-mono)] text-[12px] text-[#9297a0]">
                Parsing GIRR, Equity, FX, and Credit Spread Risk vectors
              </span>
            </div>
          ) : (
            <>
              {/* Upload icon — circular button */}
              <div className="flex h-10 w-10 items-center justify-center rounded-full border border-[#dddddd] bg-[#f8fafc] text-[#9297a0] transition-colors group-active:border-[#181d26] group-active:text-[#181d26]">
                <UploadCloud className="h-5 w-5" />
              </div>
              <div className="text-center">
                {/* label-md: 16px/500 */}
                <span className="text-[16px] font-[500] text-[#181d26]">
                  Drag &amp; drop a Bank PDF, or{" "}
                  <span className="underline underline-offset-4 decoration-[#181d26]/30">browse files</span>
                </span>
                <p className="mt-1.5 font-[family-name:var(--font-mono)] text-[11.5px] text-[#9297a0]">
                  Bank Disclosures · Trading Book Annexes · Regulatory Circulars
                </p>
              </div>
            </>
          )}
        </div>

        {/* ── Demo CTA — button-secondary style ────────────────────────────── */}
        <button
          onClick={(e) => { e.stopPropagation(); startDemo(); }}
          disabled={loading}
          className="inline-flex items-center gap-2 rounded-[12px] border border-[#dddddd] bg-white px-5 py-3 text-[14px] font-[500] text-[#181d26] transition-colors active:bg-[#e0e2e6] disabled:opacity-40"
        >
          <FileText className="h-4 w-4 text-[#9297a0]" />
          Execute Sample Analysis (Punjab National Bank Trading Book)
          <ArrowRight className="h-3.5 w-3.5 text-[#9297a0]" />
        </button>

        {/* ── Signature Coral Band — brand voltage separator ───────────────── */}
        <div className="w-full max-w-[920px] rounded-[12px] bg-[#aa2d00] px-12 py-10">
          <p className="text-[13px] font-[family-name:var(--font-mono)] font-[500] uppercase tracking-widest text-white/70 mb-3">
            What IFSA Auditor does
          </p>
          <p className="font-milligram text-[32px] font-bold leading-[1.2] text-white">
            Production-grade FRTB capital verification at prototype speed.
          </p>
        </div>

        {/* ── Feature grid — demo-grid-card style ─────────────────────────── */}
        <div className="w-full max-w-[920px]">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">

            {/* Card 1 — surface-soft */}
            <div className="flex flex-col gap-3 rounded-[10px] border border-[#dddddd] bg-[#f8fafc] p-5">
              <div className="flex items-center gap-2">
                <span className="font-[family-name:var(--font-mono)] text-[12px] font-[600] text-[#aa2d00]">01</span>
                <ShieldCheck className="h-4 w-4 text-[#181d26]" />
              </div>
              {/* label-md 16px/bold */}
              <h3 className="text-[16px] font-bold text-[#181d26]">
                Automated Position Extraction
              </h3>
              {/* body-md 14px/400 */}
              <p className="text-[14px] leading-[1.6] text-[#41454d]">
                Extracts non-contiguous disclosure text into structured Delta, Vega, and Curvature sensitivity tables.
              </p>
            </div>

            {/* Card 2 — signature mint surface */}
            <div className="flex flex-col gap-3 rounded-[10px] border border-[#a8d8c4] bg-[#a8d8c4] p-5">
              <div className="flex items-center gap-2">
                <span className="font-[family-name:var(--font-mono)] text-[12px] font-[600] text-[#0a2e0e]">02</span>
                <PieChart className="h-4 w-4 text-[#0a2e0e]" />
              </div>
              <h3 className="text-[16px] font-bold text-[#0a2e0e]">
                Standardised Capital Math
              </h3>
              <p className="text-[14px] leading-[1.6] text-[#0a2e0e]/80">
                Computes aggregated capital charges across GIRR, Equity, FX, CSR Non-Sec, and Commodity risk classes.
              </p>
            </div>

            {/* Card 3 — signature cream */}
            <div className="flex flex-col gap-3 rounded-[10px] border border-[#dddddd] bg-[#f5e9d4] p-5">
              <div className="flex items-center gap-2">
                <span className="font-[family-name:var(--font-mono)] text-[12px] font-[600] text-[#aa2d00]">03</span>
                <Sparkles className="h-4 w-4 text-[#181d26]" />
              </div>
              <h3 className="text-[16px] font-bold text-[#181d26]">
                IFSA Regulatory Audit Flagging
              </h3>
              <p className="text-[14px] leading-[1.6] text-[#41454d]">
                Flags reporting discrepancies, missing risk buckets, and regulatory breaches with exact citation quotes under IFSA audit rules.
              </p>
            </div>

          </div>
        </div>

        {/* ── CTA Band Light — surface-strong near footer ───────────────────── */}
        <div className="w-full max-w-[920px] rounded-[12px] bg-[#e0e2e6] px-12 py-10 flex flex-col md:flex-row items-center justify-between gap-6">
          <p className="font-milligram text-[32px] font-bold leading-[1.2] text-[#181d26]">
            Start your FRTB-SA audit now.
          </p>
          {/* button-primary: near-black, white text, rounded-lg */}
          <button
            onClick={openFilePicker}
            disabled={loading}
            className="flex-shrink-0 rounded-[12px] bg-[#181d26] px-6 py-3.5 text-[16px] font-[500] text-white transition-colors active:bg-[#0d1218] disabled:opacity-40"
          >
            Upload Bank PDF
          </button>
        </div>

      </main>
    </div>
  );
}
