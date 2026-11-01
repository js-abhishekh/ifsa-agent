"use client";

import React from "react";
import { CalculatedMetric } from "@/lib/types";

export interface RiskClassCardsProps {
  metrics: CalculatedMetric[];
}

// Airtable signature + demo-grid palette mapped to FRTB risk classes
const RISK_ACCENTS: Record<string, { dot: string; badge: string; badgeText: string; total: string }> = {
  GIRR:       { dot: "#254fad",  badge: "#f8fafc",  badgeText: "#254fad",  total: "#254fad" },  // info blue
  Equity:     { dot: "#0a2e0e",  badge: "#a8d8c4",  badgeText: "#0a2e0e",  total: "#006400" },  // forest + mint
  FX:         { dot: "#aa2d00",  badge: "#f5e9d4",  badgeText: "#aa2d00",  total: "#aa2d00" },  // coral signature
  CSR_NonSec: { dot: "#181d26",  badge: "#f8fafc",  badgeText: "#181d26",  total: "#181d26" },  // near-black ink
  CSR_Sec:    { dot: "#181d26",  badge: "#f8fafc",  badgeText: "#181d26",  total: "#181d26" },
  Commodity:  { dot: "#d9a441",  badge: "#f4d35e",  badgeText: "#181d26",  total: "#d9a441" },  // mustard
};

const METRIC_LABELS: Record<string, string> = {
  delta_charge:    "Delta Sensitivity Charge",
  vega_charge:     "Vega Volatility Charge",
  curvature_charge:"Curvature Non-linear Charge",
  drc_charge:      "Default Risk Charge (DRC)",
  rrao_charge:     "Residual Risk Add-on (RRAO)",
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
        const accent = RISK_ACCENTS[riskClass] || {
          dot: "#41454d", badge: "#f8fafc", badgeText: "#333840", total: "#181d26",
        };
        const total = classMetrics.reduce((sum, m) => sum + (m.aggregated_value || 0), 0);

        return (
          // feature-card-tabbed: rounded-lg (12px), flat, white canvas
          <div
            key={riskClass}
            className="rounded-[12px] border border-[#dddddd] bg-white p-5 flex flex-col justify-between"
          >
            <div>
              {/* Card header */}
              <div className="mb-4 flex items-center justify-between border-b border-[#dddddd] pb-3">
                <div className="flex items-center gap-2.5">
                  <div
                    className="h-2.5 w-2.5 rounded-full"
                    style={{ backgroundColor: accent.dot }}
                  />
                  {/* title-sm 18px/bold */}
                  <div className="font-milligram text-[16px] font-bold text-[#181d26]">{riskClass}</div>
                </div>
                <span
                  className="rounded-[6px] border border-[#dddddd] px-2.5 py-0.5 font-[family-name:var(--font-mono)] text-[10px] font-[600] uppercase tracking-wider"
                  style={{ backgroundColor: accent.badge, color: accent.badgeText }}
                >
                  SBM Risk Class
                </span>
              </div>

              {/* Metric rows */}
              <div className="flex flex-col gap-3">
                {classMetrics.map((m, idx) => (
                  <div key={idx} className="flex flex-col gap-1 text-[12.5px]">
                    <div className="flex justify-between">
                      <span className="text-[#41454d]">
                        {METRIC_LABELS[m.metric_name] || m.metric_name}
                      </span>
                      <span className="font-[family-name:var(--font-mono)] font-[500] text-[#181d26]">
                        {formatMoney(m.aggregated_value || 0)}
                      </span>
                    </div>

                    {/* Bucket-level breakdown */}
                    {m.bucket_level && Object.keys(m.bucket_level).length > 0 && (
                      <div className="flex flex-col gap-0.5 rounded-[6px] border border-[#dddddd] bg-[#f8fafc] p-2 text-[11px] text-[#41454d]">
                        {Object.entries(m.bucket_level).map(([bKey, bVal]) => (
                          <div key={bKey} className="flex justify-between font-[family-name:var(--font-mono)]">
                            <span>Bucket [{bKey}]</span>
                            <span className="font-[500] text-[#333840]">{formatMoney(bVal)}</span>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>

            {/* Total row */}
            <div className="mt-5 flex items-center justify-between border-t border-[#dddddd] pt-3.5">
              <span className="text-[14px] text-[#41454d]">Aggregated Risk Charge</span>
              <span
                className="font-[family-name:var(--font-mono)] text-[15px] font-[600]"
                style={{ color: accent.total }}
              >
                {formatMoney(total)}
              </span>
            </div>
          </div>
        );
      })}
    </div>
  );
}
