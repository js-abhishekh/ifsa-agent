"use client";

import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from "recharts";

export interface ChartsPanelProps {
  barData: Array<{ name: string; delta: number; vega: number; curvature: number }>;
  donutData: Array<{ name: string; value: number; color: string }>;
}

export default function ChartsPanel({ barData, donutData }: ChartsPanelProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-[1.4fr_1fr] gap-5">
      {/* Stacked Bar Chart */}
      <div className="rounded-xl border border-[#E2E8F0] bg-white p-5 shadow-xs">
        <h3 className="mb-3 font-[family-name:var(--font-mono)] text-[11px] font-bold tracking-wider text-[#B45309] uppercase">
          CHARGE BY RISK CLASS & SENSITIVITY METRIC
        </h3>
        <div className="h-[320px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={barData} margin={{ top: 20, right: 20, left: 0, bottom: 0 }}>
              <CartesianGrid stroke="#F1F5F9" vertical={false} />
              <XAxis
                dataKey="name"
                tick={{ fill: "#475569", fontSize: 12, fontFamily: "var(--font-mono)", fontWeight: 600 }}
                axisLine={{ stroke: "#CBD5E1" }}
                tickLine={false}
              />
              <YAxis
                tick={{ fill: "#64748B", fontSize: 11, fontFamily: "var(--font-mono)" }}
                axisLine={false}
                tickLine={false}
                tickFormatter={(val) => `₹${(val / 1000).toFixed(0)}k`}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#FFFFFF",
                  borderColor: "#E2E8F0",
                  borderRadius: "8px",
                  color: "#0F172A",
                  boxShadow: "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
                  fontFamily: "var(--font-mono)",
                  fontSize: "12px",
                }}
              />
              <Legend wrapperStyle={{ fontFamily: "var(--font-mono)", fontSize: "11.5px", color: "#475569", paddingTop: "10px" }} />
              <Bar dataKey="delta" stackId="a" fill="#1E3A8A" name="Delta Charge" />
              <Bar dataKey="vega" stackId="a" fill="#059669" name="Vega Charge" />
              <Bar dataKey="curvature" stackId="a" fill="#D97706" name="Curvature Charge" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Donut Chart */}
      <div className="rounded-xl border border-[#E2E8F0] bg-white p-5 shadow-xs">
        <h3 className="mb-3 font-[family-name:var(--font-mono)] text-[11px] font-bold tracking-wider text-[#B45309] uppercase">
          RISK CLASS CAPITAL ALLOCATION
        </h3>
        <div className="h-[280px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={donutData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                innerRadius={65}
                outerRadius={95}
                paddingAngle={3}
                stroke="#FFFFFF"
                strokeWidth={2}
              >
                {donutData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip
                contentStyle={{
                  backgroundColor: "#FFFFFF",
                  borderColor: "#E2E8F0",
                  borderRadius: "8px",
                  color: "#0F172A",
                  boxShadow: "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
                  fontFamily: "var(--font-mono)",
                  fontSize: "12px",
                }}
              />
              <Legend wrapperStyle={{ fontFamily: "var(--font-mono)", fontSize: "11.5px", color: "#475569" }} />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

