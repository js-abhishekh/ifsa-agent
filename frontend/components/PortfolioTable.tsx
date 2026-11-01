"use client";

import React from "react";
import { PortfolioPosition } from "@/lib/types";

export interface PortfolioTableProps {
  positions: PortfolioPosition[];
  onPositionsChange: (positions: PortfolioPosition[]) => void;
}

// Airtable demo-grid-card palette for risk class badges
const RISK_BADGES: Record<string, { bg: string; text: string; border: string }> = {
  GIRR:       { bg: "#f8fafc",  text: "#254fad",  border: "#dddddd" },  // surface-soft + info
  Equity:     { bg: "#a8d8c4",  text: "#0a2e0e",  border: "#a8d8c4" },  // signature mint + forest
  FX:         { bg: "#fcab79",  text: "#181d26",  border: "#fcab79" },  // signature peach
  CSR_NonSec: { bg: "#f5e9d4",  text: "#181d26",  border: "#dddddd" },  // signature cream
  CSR_Sec:    { bg: "#f5e9d4",  text: "#181d26",  border: "#dddddd" },
  Commodity:  { bg: "#f4d35e",  text: "#181d26",  border: "#d9a441" },  // signature yellow/mustard
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
    // demo-grid-card: white canvas, rounded-md (10px), hairline border, flat
    <div className="w-full overflow-hidden rounded-[10px] border border-[#dddddd] bg-white">
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-left text-[13px]">
          <thead>
            <tr className="border-b border-[#dddddd] bg-[#f8fafc] font-[family-name:var(--font-mono)] text-[11px] font-[600] tracking-wider text-[#41454d] uppercase">
              <th className="px-4 py-3">Instrument ID</th>
              <th className="px-4 py-3">Risk Class</th>
              <th className="px-4 py-3">Bucket</th>
              <th className="px-4 py-3">Risk Factor</th>
              <th className="px-4 py-3 text-right">Sensitivity (INR)</th>
              <th className="px-4 py-3 text-right">Notional (INR)</th>
              <th className="px-4 py-3 text-center">Ccy</th>
            </tr>
          </thead>

          <tbody className="divide-y divide-[#dddddd]">
            {positions.map((pos, idx) => {
              const badge = RISK_BADGES[pos.risk_class] || {
                bg: "#f8fafc",
                text: "#333840",
                border: "#dddddd",
              };

              return (
                <tr key={`${pos.instrument_id}-${idx}`} className="transition-colors">
                  <td className="px-4 py-3 font-[family-name:var(--font-mono)] text-[12.5px] font-[500] text-[#181d26]">
                    {pos.instrument_id}
                  </td>
                  <td className="px-4 py-3">
                    <span
                      className="inline-flex items-center rounded-[6px] border px-2.5 py-0.5 font-[family-name:var(--font-mono)] text-[11px] font-[600] uppercase"
                      style={{
                        backgroundColor: badge.bg,
                        color: badge.text,
                        borderColor: badge.border,
                      }}
                    >
                      {pos.risk_class}
                    </span>
                  </td>
                  <td className="px-4 py-3 text-[#333840]">{pos.bucket}</td>
                  <td className="px-4 py-3 text-[#333840]">{pos.risk_factor}</td>
                  <td className="px-4 py-3 text-right">
                    <input
                      type="number"
                      value={pos.sensitivity}
                      onChange={(e) => handleChange(idx, "sensitivity", e.target.value)}
                      className="w-[120px] rounded-[6px] border border-[#dddddd] bg-[#f8fafc] px-2.5 py-1 text-right font-[family-name:var(--font-mono)] text-[12px] font-[500] text-[#181d26] transition-colors focus:border-[#458fff] focus:bg-white focus:outline-none"
                    />
                  </td>
                  <td className="px-4 py-3 text-right">
                    <input
                      type="number"
                      value={pos.notional ?? ""}
                      onChange={(e) => handleChange(idx, "notional", e.target.value)}
                      className="w-[120px] rounded-[6px] border border-[#dddddd] bg-[#f8fafc] px-2.5 py-1 text-right font-[family-name:var(--font-mono)] text-[12px] font-[500] text-[#181d26] transition-colors focus:border-[#458fff] focus:bg-white focus:outline-none"
                    />
                  </td>
                  <td className="px-4 py-3 text-center font-[family-name:var(--font-mono)] text-[12px] font-[500] text-[#41454d]">
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
