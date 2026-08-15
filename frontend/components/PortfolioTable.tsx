"use client";

import React from "react";
import { PortfolioPosition } from "@/lib/types";

export interface PortfolioTableProps {
  positions: PortfolioPosition[];
  onPositionsChange: (positions: PortfolioPosition[]) => void;
}

const RISK_BADGES: Record<string, { bg: string; text: string; border: string }> = {
  GIRR: { bg: "#EFF6FF", text: "#1D4ED8", border: "#BFDBFE" },
  Equity: { bg: "#ECFDF5", text: "#047857", border: "#A7F3D0" },
  FX: { bg: "#FFFBEB", text: "#B45309", border: "#FDE68A" },
  CSR_NonSec: { bg: "#F3E8FF", text: "#6D28D9", border: "#DDD6FE" },
  CSR_Sec: { bg: "#F3E8FF", text: "#6D28D9", border: "#DDD6FE" },
  Commodity: { bg: "#FEF2F2", text: "#B91C1C", border: "#FECACA" },
};

export default function PortfolioTable({ positions, onPositionsChange }: PortfolioTableProps) {
  const handleChange = (index: number, field: keyof PortfolioPosition, value: string) => {
    const numValue = parseFloat(value);
    const newPositions = [...positions];
    newPositions[index] = {
      ...newPositions[index],
      [field]: isNaN(numValue) ? 0 : numValue,
    };
    onPositionsChange(newPositions);
  };

  return (
    <div className="w-full overflow-hidden rounded-lg border border-[#E2E8F0] bg-white shadow-xs">
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-left text-[13px]">
          <thead>
            <tr className="border-b border-[#CBD5E1] bg-[#F8FAFC] font-[family-name:var(--font-mono)] text-[11px] font-bold tracking-wider text-[#475569] uppercase">
              <th className="px-4 py-3">Instrument ID</th>
              <th className="px-4 py-3">Risk Class</th>
              <th className="px-4 py-3">Bucket</th>
              <th className="px-4 py-3">Risk Factor</th>
              <th className="px-4 py-3 text-right">Sensitivity (INR)</th>
              <th className="px-4 py-3 text-right">Notional (INR)</th>
              <th className="px-4 py-3 text-center">Ccy</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-[#E2E8F0] font-sans">
            {positions.map((pos, idx) => {
              const badge = RISK_BADGES[pos.risk_class] || { bg: "#F1F5F9", text: "#475569", border: "#CBD5E1" };

              return (
                <tr key={`${pos.instrument_id}-${idx}`} className="hover:bg-[#FAF9F6] transition-colors">
                  <td className="px-4 py-3 font-[family-name:var(--font-mono)] text-[12.5px] font-semibold text-[#0F172A]">
                    {pos.instrument_id}
                  </td>
                  <td className="px-4 py-3">
                    <span
                      className="inline-flex items-center rounded-md border px-2.5 py-0.5 font-[family-name:var(--font-mono)] text-[11px] font-bold uppercase shadow-2xs"
                      style={{
                        backgroundColor: badge.bg,
                        color: badge.text,
                        borderColor: badge.border,
                      }}
                    >
                      {pos.risk_class}
                    </span>
                  </td>
                  <td className="px-4 py-3 text-[#334155] font-medium">{pos.bucket}</td>
                  <td className="px-4 py-3 text-[#334155]">{pos.risk_factor}</td>
                  <td className="px-4 py-3 text-right">
                    <input
                      type="number"
                      value={pos.sensitivity}
                      onChange={(e) => handleChange(idx, "sensitivity", e.target.value)}
                      className="w-[120px] rounded border border-[#CBD5E1] bg-[#F8FAFC] px-2.5 py-1 text-right font-[family-name:var(--font-mono)] text-[12px] font-medium text-[#0F172A] shadow-2xs transition-colors focus:border-[#B45309] focus:bg-white focus:outline-none"
                    />
                  </td>
                  <td className="px-4 py-3 text-right">
                    <input
                      type="number"
                      value={pos.notional ?? ""}
                      onChange={(e) => handleChange(idx, "notional", e.target.value)}
                      className="w-[120px] rounded border border-[#CBD5E1] bg-[#F8FAFC] px-2.5 py-1 text-right font-[family-name:var(--font-mono)] text-[12px] font-medium text-[#0F172A] shadow-2xs transition-colors focus:border-[#B45309] focus:bg-white focus:outline-none"
                    />
                  </td>
                  <td className="px-4 py-3 text-center font-[family-name:var(--font-mono)] text-[12px] font-semibold text-[#64748B]">
                    {pos.currency}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

