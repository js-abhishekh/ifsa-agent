"use client";

import React from "react";
import { CalculatedMetric } from "@/lib/types";

export interface RiskClassCardsProps {
  metrics: CalculatedMetric[];
}

const RISK_ACCENTS: Record<string, { color: string; badgeBg: string; text: string }> = {
  GIRR: { color: "#1D4ED8", badgeBg: "#EFF6FF", text: "#1E40AF" },
  Equity: { color: "#047857", badgeBg: "#ECFDF5", text: "#065F46" },
  FX: { color: "#B45309", badgeBg: "#FFFBEB", text: "#92400E" },
  CSR_NonSec: { color: "#6D28D9", badgeBg: "#F3E8FF", text: "#5B21B6" },
  CSR_Sec: { color: "#6D28D9", badgeBg: "#F3E8FF", text: "#5B21B6" },
  Commodity: { color: "#B91C1C", badgeBg: "#FEF2F2", text: "#991B1B" },
};

const METRIC_LABELS: Record<string, string> = {
  delta_charge: "Delta Sensitivity Charge",
  vega_charge: "Vega Volatility Charge",
  curvature_charge: "Curvature Non-linear Charge",
  drc_charge: "Default Risk Charge (DRC)",
  rrao_charge: "Residual Risk Add-on (RRAO)",
};

export default function RiskClassCards({ metrics }: RiskClassCardsProps) {
  const grouped = metrics.reduce((acc, m) => {
    if (!acc[m.risk_class]) acc[m.risk_class] = [];
    acc[m.risk_class].push(m);
    return acc;
  }, {} as Record<string, CalculatedMetric[]>);

  const formatMoney = (n: number) =>
    "₹ " + n.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  return (
    <div className="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-5">
      {Object.entries(grouped).map(([riskClass, classMetrics]) => {
        const accent = RISK_ACCENTS[riskClass] || { color: "#B45309", badgeBg: "#FFFBEB", text: "#92400E" };
        const total = classMetrics.reduce((sum, m) => sum + (m.aggregated_value || 0), 0);

        return (
          <div key={riskClass} className="rounded-xl border border-[#E2E8F0] bg-white p-5 shadow-xs flex flex-col justify-between transition-shadow hover:shadow-md">
            <div>
              <div className="mb-4 flex items-center justify-between border-b border-[#E2E8F0] pb-3">
                <div className="flex items-center gap-2.5">
                  <div className="h-3 w-3 rounded-full shadow-2xs" style={{ backgroundColor: accent.color }} />
                  <div className="font-[family-name:var(--font-serif)] text-[16px] font-bold text-[#0F172A]">{riskClass}</div>
                </div>
                <span
                  className="rounded-md px-2.5 py-0.5 font-[family-name:var(--font-mono)] text-[10px] font-bold uppercase tracking-wider shadow-2xs"
                  style={{ backgroundColor: accent.badgeBg, color: accent.text }}
                >
                  SBM RISK CLASS
                </span>
              </div>
              <div className="flex flex-col gap-3">
                {classMetrics.map((m, idx) => (
                  <div key={idx} className="flex flex-col gap-1 text-[12.5px]">
                    <div className="flex justify-between font-medium">
                      <span className="text-[#475569]">{METRIC_LABELS[m.metric_name] || m.metric_name}</span>
                      <span className="font-[family-name:var(--font-mono)] font-semibold text-[#0F172A]">
                        {formatMoney(m.aggregated_value || 0)}
                      </span>
                    </div>
                    {/* Bucket level disclosure if present */}
                    {m.bucket_level && Object.keys(m.bucket_level).length > 0 && (
                      <div className="flex flex-col gap-0.5 rounded border border-[#F1F5F9] bg-[#F8FAFC] p-2 text-[11px] text-[#64748B]">
                        {Object.entries(m.bucket_level).map(([bKey, bVal]) => (
                          <div key={bKey} className="flex justify-between font-[family-name:var(--font-mono)]">
                            <span>Bucket [{bKey}]</span>
                            <span className="font-semibold text-[#334155]">{formatMoney(bVal)}</span>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>

            <div className="mt-5 flex items-center justify-between border-t border-[#E2E8F0] pt-3.5">
              <span className="font-[family-name:var(--font-serif)] text-[14px] font-bold text-[#475569]">Aggregated Risk Charge</span>
              <span className="font-[family-name:var(--font-mono)] text-[15px] font-bold" style={{ color: accent.color }}>
                {formatMoney(total)}
              </span>
            </div>
          </div>
        );
      })}
    </div>
  );
}

