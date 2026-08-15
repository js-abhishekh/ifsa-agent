const { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Legend, CartesianGrid, PieChart, Pie, Cell } = window.Recharts;

const axisStyle = { fontSize: 12, fontFamily: "'JetBrains Mono', monospace", fill: '#94A3B8' };
const tooltipStyle = { background: '#111827', border: '1px solid #1E293B', borderRadius: 6, fontFamily: "'JetBrains Mono', monospace", fontSize: 12, color: '#E2E8F0' };
const legendStyle = { fontFamily: "'JetBrains Mono', monospace", fontSize: 12, color: '#94A3B8' };

function StackedBarChart({ data }) {
  return React.createElement(ResponsiveContainer, { width: '100%', height: 320 },
    React.createElement(BarChart, { data, margin: { top: 10, right: 10, left: 0, bottom: 0 } },
      React.createElement(CartesianGrid, { stroke: '#1E293B', vertical: false }),
      React.createElement(XAxis, { dataKey: 'name', tick: axisStyle, axisLine: { stroke: '#1E293B' }, tickLine: false }),
      React.createElement(YAxis, { tick: axisStyle, axisLine: { stroke: '#1E293B' }, tickLine: false }),
      React.createElement(Tooltip, { contentStyle: tooltipStyle, itemStyle: { color: '#E2E8F0' }, cursor: { fill: '#1E293B' } }),
      React.createElement(Legend, { wrapperStyle: legendStyle }),
      React.createElement(Bar, { dataKey: 'delta', name: 'Delta', stackId: 'a', fill: '#3B82F6' }),
      React.createElement(Bar, { dataKey: 'vega', name: 'Vega', stackId: 'a', fill: '#10B981' }),
      React.createElement(Bar, { dataKey: 'curvature', name: 'Curvature', stackId: 'a', fill: '#F59E0B' })
    )
  );
}

function DonutChart({ data }) {
  return React.createElement(ResponsiveContainer, { width: '100%', height: 280 },
    React.createElement(PieChart, null,
      React.createElement(Pie, { data, dataKey: 'value', nameKey: 'name', innerRadius: 68, outerRadius: 98, paddingAngle: 3, stroke: '#0A0E1A', strokeWidth: 2 },
        data.map((d, i) => React.createElement(Cell, { key: i, fill: d.color }))
      ),
      React.createElement(Tooltip, { contentStyle: tooltipStyle, itemStyle: { color: '#E2E8F0' } }),
      React.createElement(Legend, { wrapperStyle: legendStyle })
    )
  );
}

module.exports = { StackedBarChart, DonutChart };
