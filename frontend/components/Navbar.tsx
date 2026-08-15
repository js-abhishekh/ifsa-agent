"use client";

import React from "react";
import { useRouter, usePathname } from "next/navigation";
import { ArrowLeft, ArrowRight, ShieldCheck, Home, FileText, BarChart3 } from "lucide-react";

export interface NavbarProps {
  screenLabel: string;
  runId?: string;
}

export default function Navbar({ screenLabel, runId }: NavbarProps) {
  const router = useRouter();
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-30 flex h-[60px] w-full items-center justify-between border-b border-[#E2E8F0] bg-[#FAF9F6]/95 px-6 backdrop-blur-md">
      {/* Left: Navigation Controls & Brand */}
      <div className="flex items-center gap-4">
        {/* Back and Forward Navigation Controls */}
        <div className="flex items-center gap-1 rounded-md border border-[#E2E8F0] bg-white p-1 shadow-xs">
          <button
            onClick={() => router.back()}
            title="Go Back"
            className="flex h-7 w-7 items-center justify-center rounded text-[#475569] transition-colors hover:bg-[#F1F5F9] hover:text-[#0F172A] active:bg-[#E2E8F0]"
          >
            <ArrowLeft className="h-4 w-4" />
          </button>
          <div className="h-4 w-[1px] bg-[#E2E8F0]" />
          <button
            onClick={() => router.forward()}
            title="Go Forward"
            className="flex h-7 w-7 items-center justify-center rounded text-[#475569] transition-colors hover:bg-[#F1F5F9] hover:text-[#0F172A] active:bg-[#E2E8F0]"
          >
            <ArrowRight className="h-4 w-4" />
          </button>
        </div>

        {/* Financial Editorial Crest / Brand */}
        <div 
          onClick={() => router.push("/")}
          className="flex cursor-pointer items-center gap-2.5 transition-opacity hover:opacity-85"
        >
          <div className="flex h-7 w-7 items-center justify-center rounded border border-[#B45309]/30 bg-[#FFFBEB] text-[#B45309] shadow-2xs">
            <ShieldCheck className="h-4 w-4" />
          </div>
          <div className="flex flex-col">
            <span className="font-[family-name:var(--font-serif)] text-[15px] font-bold tracking-tight text-[#0F172A]">
              IFSA'S FRTB-SA AUDITOR
            </span>
            <span className="font-[family-name:var(--font-mono)] text-[9.5px] font-semibold tracking-widest text-[#B45309] uppercase">
              IFSA REGULATORY CAPITAL ENGINE
            </span>
          </div>
        </div>
      </div>

      {/* Middle: Breadcrumb Quick Jump */}
      <div className="hidden md:flex items-center gap-2 font-[family-name:var(--font-mono)] text-[11.5px] font-medium text-[#64748B]">
        <button 
          onClick={() => router.push("/")}
          className={`flex items-center gap-1 transition-colors hover:text-[#0F172A] ${pathname === "/" ? "text-[#0F172A] font-bold" : ""}`}
        >
          <Home className="h-3.5 w-3.5" />
          Upload
        </button>
        {runId && (
          <>
            <span className="text-[#CBD5E1]">/</span>
            <button 
              onClick={() => router.push(`/run/${runId}`)}
              className={`flex items-center gap-1 transition-colors hover:text-[#0F172A] ${pathname.includes(`/run/${runId}`) && !pathname.includes('/results') ? "text-[#0F172A] font-bold" : ""}`}
            >
              <FileText className="h-3.5 w-3.5" />
              Workspace
            </button>
            <span className="text-[#CBD5E1]">/</span>
            <button 
              onClick={() => router.push(`/run/${runId}/results`)}
              className={`flex items-center gap-1 transition-colors hover:text-[#0F172A] ${pathname.includes('/results') ? "text-[#0F172A] font-bold" : ""}`}
            >
              <BarChart3 className="h-3.5 w-3.5" />
              Results
            </button>
          </>
        )}
      </div>

      {/* Right: Screen Tag & Run ID */}
      <div className="flex items-center gap-2">
        <span className="rounded-full border border-[#E2E8F0] bg-white px-3 py-1 font-[family-name:var(--font-mono)] text-[11px] font-semibold text-[#0F172A] shadow-2xs">
          <span className="text-[#B45309] font-bold mr-1.5">[IFSA AUDIT]</span> {screenLabel} {runId && <span className="text-[#B45309]">| #{runId.slice(0, 8)}</span>}
        </span>
      </div>
    </header>
  );
}

