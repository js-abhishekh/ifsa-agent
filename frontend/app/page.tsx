"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import Navbar from "@/components/Navbar";
import { uploadPdf, loadSamplePortfolio } from "@/lib/api";
import { UploadCloud, FileText, ArrowRight, ShieldCheck, PieChart, Sparkles } from "lucide-react";

export default function Home() {
  const router = useRouter();
  const [dragOver, setDragOver] = useState(false);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

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

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setDragOver(false);
    const file = e.dataTransfer.files[0];
    if (file) handleFile(file);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setDragOver(true);
  };

  const handleDragLeave = () => setDragOver(false);

  const openFilePicker = () => {
    document.getElementById("pdf-upload")?.click();
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) handleFile(file);
  };

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
    <div className="flex min-h-screen flex-col bg-[#FAF9F6] text-[#0F172A]">
      <Navbar screenLabel="PORTFOLIO UPLOAD" />
      
      <main className="flex flex-1 flex-col items-center justify-center gap-10 px-6 py-12">
        {/* Top Editorial Banner / Header */}
        <div className="w-full max-w-[840px] text-center">
          <div className="mx-auto mb-4 inline-flex items-center gap-2 rounded-full border border-[#B45309]/30 bg-[#FFFBEB] px-3.5 py-1 font-[family-name:var(--font-mono)] text-[11px] font-semibold tracking-wider text-[#B45309] uppercase shadow-2xs">
            <Sparkles className="h-3.5 w-3.5" />
            <span className="rounded bg-[#B45309] text-white px-1.5 py-0.5 font-bold">IFSA</span> REGULATORY INTELLIGENCE & AUDIT ENGINE
          </div>

          <h1 className="font-[family-name:var(--font-serif)] text-[42px] font-normal leading-[1.15] text-[#0F172A] md:text-[52px]">
            IFSA's FRTB-SA Auditor <br />
            <span className="italic font-light text-[#B45309]">Capital Calculation & Compliance Audit</span>
          </h1>

          <p className="mx-auto mt-4 max-w-[660px] text-[15.5px] leading-relaxed text-[#475569]">
            Submit any institutional Bank Disclosure or Trading Book PDF to IFSA's FRTB-SA Auditor. Our autonomous agent extracts sensitivity risk vectors, computes BCBS capital charges, and validates disclosures against Basel III regulatory mandates.
          </p>
        </div>

        {errorMsg && (
          <div className="w-full max-w-[620px] rounded-lg border border-[#F59E0B]/40 bg-[#FFFBEB] p-4 text-[13.5px] font-medium text-[#92400E] shadow-2xs">
            ⚠️ {errorMsg}
          </div>
        )}

        {/* Financial Dropzone Card */}
        <div
          onClick={openFilePicker}
          onDrop={handleDrop}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          className={`group flex h-[220px] w-full max-w-[640px] cursor-pointer flex-col items-center justify-center gap-3 rounded-xl border-2 border-dashed p-6 transition-all shadow-xs ${
            dragOver
              ? "border-[#B45309] bg-[#FFFBEB]"
              : "border-[#CBD5E1] bg-white hover:border-[#B45309] hover:bg-[#FFFBEB]/40 hover:shadow-md"
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
            <div className="flex flex-col items-center justify-center gap-3">
              <div className="h-9 w-9 animate-spin rounded-full border-3 border-[#B45309] border-t-transparent"></div>
              <span className="font-[family-name:var(--font-serif)] text-[16px] font-medium text-[#0F172A]">
                Extracting trading book sensitivities…
              </span>
              <span className="font-[family-name:var(--font-mono)] text-[12px] text-[#64748B]">
                Parsing GIRR, Equity, FX, and Credit Spread Risk vectors
              </span>
            </div>
          ) : (
            <>
              <div className="flex h-12 w-12 items-center justify-center rounded-full border border-[#E2E8F0] bg-[#F8FAFC] text-[#475569] transition-transform group-hover:scale-105 group-hover:border-[#B45309]/40 group-hover:text-[#B45309]">
                <UploadCloud className="h-6 w-6" />
              </div>
              <div className="text-center">
                <span className="font-[family-name:var(--font-serif)] text-[17px] font-semibold text-[#0F172A]">
                  Drag & drop a Bank PDF, or <span className="text-[#B45309] underline decoration-[#B45309]/40 underline-offset-4">browse files</span>
                </span>
                <p className="mt-1 font-[family-name:var(--font-mono)] text-[11.5px] text-[#64748B]">
                  Bank Disclosures · Trading Book Annexes · Regulatory Circulars
                </p>
              </div>
            </>
          )}
        </div>

        {/* Sample Execution Button */}
        <button
          onClick={(e) => { e.stopPropagation(); startDemo(); }}
          disabled={loading}
          className="group inline-flex items-center gap-2 rounded-full border border-[#E2E8F0] bg-white px-5 py-2.5 font-[family-name:var(--font-mono)] text-[13px] font-semibold text-[#0F172A] shadow-xs transition-all hover:border-[#B45309] hover:bg-[#FFFBEB] hover:text-[#92400E] disabled:opacity-50"
        >
          <FileText className="h-4 w-4 text-[#B45309]" />
          <span>Execute Sample Analysis (Punjab National Bank Trading Book)</span>
          <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" />
        </button>

        {/* Editorial Feature Grid with Fine Rule Lines */}
        <div className="mt-4 w-full max-w-[920px] border-t border-[#E2E8F0] pt-10">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="flex flex-col gap-2 rounded-lg border border-[#E2E8F0] bg-white p-5 shadow-2xs transition-shadow hover:shadow-xs">
              <div className="flex items-center gap-2">
                <span className="font-[family-name:var(--font-mono)] text-[12px] font-bold text-[#B45309]">01</span>
                <ShieldCheck className="h-4 w-4 text-[#0F172A]" />
              </div>
              <h3 className="font-[family-name:var(--font-serif)] text-[18px] font-bold text-[#0F172A]">
                Automated Position Extraction
              </h3>
              <p className="text-[13px] leading-relaxed text-[#475569]">
                Extracts non-contiguous disclosure text into structured Delta, Vega, and Curvature sensitivity tables.
              </p>
            </div>

            <div className="flex flex-col gap-2 rounded-lg border border-[#E2E8F0] bg-white p-5 shadow-2xs transition-shadow hover:shadow-xs">
              <div className="flex items-center gap-2">
                <span className="font-[family-name:var(--font-mono)] text-[12px] font-bold text-[#B45309]">02</span>
                <PieChart className="h-4 w-4 text-[#0F172A]" />
              </div>
              <h3 className="font-[family-name:var(--font-serif)] text-[18px] font-bold text-[#0F172A]">
                Standardised Capital Math
              </h3>
              <p className="text-[13px] leading-relaxed text-[#475569]">
                Computes aggregated capital charges across GIRR, Equity, FX, CSR Non-Sec, and Commodity risk classes.
              </p>
            </div>

            <div className="flex flex-col gap-2 rounded-lg border border-[#E2E8F0] bg-white p-5 shadow-2xs transition-shadow hover:shadow-xs">
              <div className="flex items-center gap-2">
                <span className="font-[family-name:var(--font-mono)] text-[12px] font-bold text-[#B45309]">03</span>
                <Sparkles className="h-4 w-4 text-[#0F172A]" />
              </div>
              <h3 className="font-[family-name:var(--font-serif)] text-[18px] font-bold text-[#0F172A]">
                IFSA Regulatory Audit Flagging
              </h3>
              <p className="text-[13px] leading-relaxed text-[#475569]">
                Flags reporting discrepancies, missing risk buckets, and regulatory breaches with exact citation quotes under IFSA audit rules.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

