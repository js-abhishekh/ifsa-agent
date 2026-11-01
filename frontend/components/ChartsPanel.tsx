"use client";

import React from "react";
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  PieChart, Pie, Cell,
} from "recharts";

export interface ChartsPanelProps {
  barData: Array<{ name: string; delta: number; vega: number; curvature: number }>;
  donutData: Array<{ name: string; value: number; color: string }>;
}

// Airtable chart colors — signature + semantic palette
const CHART_COLORS = {
  delta:     "#254fad",  // info blue
  vega:      "#006400",  // success green
  curvature: "#aa2d00",  // signature coral
};

export default function ChartsPanel({ barData, donutData }: ChartsPanelProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-[1.4fr_1fr] gap-5">
      {/* Stacked bar — feature-card-tabbed: white canvas, rounded-lg (12px), hairline border, flat */}
      <div className="rounded-[12px] border border-[#dddddd] bg-white p-5">
        <h3 className="mb-3 font-[family-name:var(--font-mono)] text-[11px] font-[600] tracking-wider text-[#181d26] uppercase">
          Charge by Risk Class &amp; Sensitivity Metric
        </h3>
        <div className="h-[320px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={barData} margin={{ top: 20, right: 20, left: 0, bottom: 0 }}>
              {/* Airtable grid: hairline #dddddd */}
              <CartesianGrid stroke="#dddddd" vertical={false} />
              <XAxis
                dataKey="name"
                tick={{ fill: "#333840", fontSize: 12, fontFamily: "var(--font-mono)", fontWeight: 500 }}
                axisLine={{ stroke: "#dddddd" }}
                tickLine={false}
              />
              <YAxis
                tick={{ fill: "#9297a0", fontSize: 11, fontFamily: "var(--font-mono)" }}
                axisLine={false}
                tickLine={false}
                tickFormatter={(val) => `₹${(val / 1000).toFixed(0)}k`}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#ffffff",
                  borderColor: "#dddddd",
                  borderRadius: "10px",
                  color: "#181d26",
                  fontFamily: "var(--font-mono)",
                  fontSize: "12px",
                }}
              />
              <Legend
                wrapperStyle={{
                  fontFamily: "var(--font-mono)",
                  fontSize: "11.5px",
                  color: "#41454d",
                  paddingTop: "10px",
                }}
              />
              <Bar dataKey="delta"     stackId="a" fill={CHART_COLORS.delta}     name="Delta Charge"     radius={[0,0,0,0]} />
              <Bar dataKey="vega"      stackId="a" fill={CHART_COLORS.vega}      name="Vega Charge"      radius={[0,0,0,0]} />
              <Bar dataKey="curvature" stackId="a" fill={CHART_COLORS.curvature} name="Curvature Charge" radius={[4,4,0,0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Donut chart */}
      <div className="rounded-[12px] border border-[#dddddd] bg-white p-5">
        <h3 className="mb-3 font-[family-name:var(--font-mono)] text-[11px] font-[600] tracking-wider text-[#181d26] uppercase">
          Risk Class Capital Allocation
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
                stroke="#ffffff"
                strokeWidth={2}
              >
                {donutData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip
                contentStyle={{
                  backgroundColor: "#ffffff",
                  borderColor: "#dddddd",
                  borderRadius: "10px",
                  color: "#181d26",
                  fontFamily: "var(--font-mono)",
                  fontSize: "12px",
                }}
              />
              <Legend
                wrapperStyle={{
                  fontFamily: "var(--font-mono)",
                  fontSize: "11.5px",
                  color: "#41454d",
                }}
              />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
