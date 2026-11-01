"use client";

import React from "react";
import { useRouter, usePathname } from "next/navigation";
import { ArrowLeft, ArrowRight, ShieldCheck, Home, FileText, BarChart3 } from "lucide-react";

export interface NavbarProps {
  screenLabel: string;
  runId?: string;
}

// Airtable top-nav: 64px white bar, ink type, hairline bottom border
export default function Navbar({ screenLabel, runId }: NavbarProps) {
  const router = useRouter();
  const pathname = usePathname();

  return (
    <header className="relative sticky top-0 z-30 flex h-[64px] w-full items-center justify-between border-b border-[#dddddd] bg-white px-6">
      {/* Left: Nav Controls & Brand */}
      <div className="flex items-center gap-4">
        {/* Back / Forward controls — button-icon-circular style */}
        <div className="flex items-center gap-1 rounded-full border border-[#dddddd] bg-white p-1">
          <button
            onClick={() => router.back()}
            title="Go Back"
            className="flex h-8 w-8 items-center justify-center rounded-full text-[#41454d] transition-colors active:bg-[#e0e2e6]"
          >
            <ArrowLeft className="h-4 w-4" />
          </button>
          <div className="h-4 w-[1px] bg-[#dddddd]" />
          <button
            onClick={() => router.forward()}
            title="Go Forward"
            className="flex h-8 w-8 items-center justify-center rounded-full text-[#41454d] transition-colors active:bg-[#e0e2e6]"
          >
            <ArrowRight className="h-4 w-4" />
          </button>
        </div>

        {/* Brand wordmark */}
        <div
          onClick={() => router.push("/")}
          className="flex cursor-pointer items-center gap-2.5 transition-opacity active:opacity-70"
        >
          <div className="flex h-7 w-7 items-center justify-center rounded-full bg-[#181d26] text-white">
            <ShieldCheck className="h-4 w-4" />
          </div>
          <div className="flex flex-col">
            <span className="font-milligram text-[15px] font-bold leading-tight tracking-tight text-[#181d26]">
              IFSA's FRTB-SA Auditor
            </span>
            <span className="font-[family-name:var(--font-mono)] text-[9.5px] font-semibold tracking-widest text-[#41454d] uppercase">
              Regulatory Capital Engine
            </span>
          </div>
        </div>
      </div>

      {/* Middle: Breadcrumb perfectly centered */}
      <div className="absolute left-1/2 -translate-x-1/2 hidden md:flex items-center gap-2 text-[14px] text-[#333840]">
        <button
          onClick={() => router.push("/")}
          className={`flex items-center gap-1.5 transition-colors active:text-[#181d26] ${
            pathname === "/" ? "text-[#181d26] font-[500]" : "text-[#41454d]"
          }`}
        >
          <Home className="h-3.5 w-3.5" />
          Upload
        </button>
        {runId && (
          <>
            <span className="text-[#dddddd]">/</span>
            <button
              onClick={() => router.push(`/run/${runId}`)}
              className={`flex items-center gap-1.5 transition-colors active:text-[#181d26] ${
                pathname.includes(`/run/${runId}`) && !pathname.includes("/results")
                  ? "text-[#181d26] font-[500]"
                  : "text-[#41454d]"
              }`}
            >
              <FileText className="h-3.5 w-3.5" />
              Workspace
            </button>
            <span className="text-[#dddddd]">/</span>
            <button
              onClick={() => router.push(`/run/${runId}/results`)}
              className={`flex items-center gap-1.5 transition-colors active:text-[#181d26] ${
                pathname.includes("/results") ? "text-[#181d26] font-[500]" : "text-[#41454d]"
              }`}
            >
              <BarChart3 className="h-3.5 w-3.5" />
              Results
            </button>
          </>
        )}
      </div>

      {/* Right: Screen tag — hairline border badge */}
      <div className="flex items-center gap-2">
        <span className="rounded-[6px] border border-[#dddddd] bg-white px-3 py-1.5 text-[12px] font-[500] text-[#181d26]">
          <span className="mr-1.5 inline-block h-2 w-2 rounded-full bg-[#aa2d00]" />
          {screenLabel}
          {runId && (
            <span className="ml-1.5 text-[#41454d]">#{runId.slice(0, 8)}</span>
          )}
        </span>
      </div>
    </header>
  );
}
