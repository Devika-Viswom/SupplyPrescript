import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  PieChart,
  Pie,
  Cell,
  Legend,
  BarChart,
  Bar
} from "recharts";
import api from "../api/api";

export default function Dashboard() {

  const [kpi, setKpi] = useState(null);
  const [charts, setCharts] = useState(null);
  const [shipments, setShipments] = useState([]);
  
  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
  try {

    const kpiResponse = await api.get(
      "/dashboard/kpi"
    );

    const chartResponse = await api.get(
      "/dashboard/charts"
    );

    const shipmentResponse = await api.get(
      "/dashboard/shipments"
    );

    setKpi(kpiResponse.data);
    setCharts(chartResponse.data);
    setShipments(shipmentResponse.data);

  } catch (error) {
    console.error(error);
  }
};

  if (!kpi || !charts) {
    return (
      <div className="p-10 text-center">
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto p-8">

      <div className="mb-10 bg-gradient-to-r from-slate-900 to-blue-900 rounded-2xl p-8 text-white shadow-xl">

        <h1 className="text-4xl font-bold mb-3">
          Supply Chain Intelligence Platform
        </h1>

        <p className="text-blue-100 text-lg max-w-3xl">
          Predict disruptions, estimate lead times, evaluate transport modes,
          and generate actionable recommendations to improve supply chain resilience.
        </p>

      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-4">

        <div className="bg-white rounded-xl shadow p-5 border-t-4 border-blue-600">
          <p className="text-gray-500">
            Total Shipments
          </p>

          <h2 className="text-3xl font-bold">
            {kpi.total_shipments}
          </h2>
        </div>

        <div className="bg-white rounded-xl shadow p-4 border-t-4 border-green-600">
          <p className="text-gray-500">
            Avg Lead Time
          </p>

          <h2 className="text-3xl font-bold">
            {kpi.avg_lead_time}
          </h2>
        </div>

        <div className="bg-white rounded-xl shadow p-4 border-t-4 border-red-600">
          <p className="text-gray-500">
            Disruption Rate
          </p>

          <h2 className="text-3xl font-bold text-red-600">
            {(kpi.disruption_rate * 100).toFixed(1)}%
          </h2>
        </div>

        <div className="bg-white rounded-xl shadow p-4 border-t-4 border-yellow-600">
          <p className="text-gray-500">
            Avg Geopolitical Risk
          </p>

          <h2 className="text-3xl font-bold text-orange-600">
            {kpi.avg_risk_score}
          </h2>
        </div>

        <div className="bg-white rounded-xl shadow p-4 border-t-4 border-red-600">
          <p className="text-gray-500">
            High Risk Shipments
          </p>

          <h2 className="text-3xl font-bold text-red-600">
            {kpi.high_risk_shipments}
          </h2>
        </div>

        <div className="bg-white rounded-xl shadow p-4 border-t-4 border-green-600">
          <p className="text-gray-500">
            Avg Carrier Reliability
          </p>

          <h2 className="text-3xl font-bold text-green-600">
            {(kpi.avg_reliability_score * 100).toFixed(0)}%
          </h2>
        </div>

      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

        {/* Monthly Disruptions */}

        <div className="bg-white rounded-2xl shadow-md p-6 border border-slate-200">

          <h2 className="text-xl font-semibold mb-4">
            Monthly Disruptions
          </h2>

          <ResponsiveContainer width="100%" height={350}>
            <LineChart data={charts.monthly_disruptions}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="Period" />

              <YAxis />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="Disruption_Occurred"
                stroke="#ef4444"
                strokeWidth={3}
              />

            </LineChart>
          </ResponsiveContainer>

        </div>

        {/* Monthly Lead Time */}

        <div className="bg-white rounded-2xl shadow p-6 border border-slate-200">

          <h2 className="text-xl font-semibold mb-4">
            Monthly Lead Time
          </h2>

          <ResponsiveContainer width="100%" height={350}>
            <LineChart data={charts.monthly_leadtime}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="Period" />

              <YAxis />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="Lead_Time_Days"
                stroke="#2563eb"
                strokeWidth={3}
              />

            </LineChart>

          </ResponsiveContainer>

        </div>

      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

        {/* Risk Distribution */}

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-xl font-semibold mb-4">
            Risk Distribution
          </h2>

          <ResponsiveContainer width="100%" height={350}>

            <PieChart>

              <Pie
                data={charts.risk_distribution}
                dataKey="Count"
                nameKey="Risk_Level"
                outerRadius={120}
                label
              >

                <Cell fill="#22c55e" />
                <Cell fill="#f59e0b" />
                <Cell fill="#ef4444" />

              </Pie>

              <Legend />

            </PieChart>

          </ResponsiveContainer>

        </div>

        {/* Reliability */}

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-xl font-semibold mb-4">
            Reliability Distribution
          </h2>

          <ResponsiveContainer width="100%" height={350}>

            <PieChart>

              <Pie
                data={charts.reliability_distribution}
                dataKey="Count"
                nameKey="Reliability_Level"
                outerRadius={120}
                label
              >

                <Cell fill="#ef4444" />
                <Cell fill="#f59e0b" />
                <Cell fill="#22c55e" />

              </Pie>

              <Legend />

            </PieChart>

          </ResponsiveContainer>

        </div>

      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

        <div className="bg-white rounded-xl shadow p-6 mt-8">

          <h2 className="text-xl font-semibold mb-4">
            Disruption Rate by Weather
          </h2>

          <ResponsiveContainer width="100%" height={350}>

            <BarChart data={charts.disruption_by_weather}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="Weather_Condition" />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="Disruption_Occurred"
                fill="#f97316"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

        <div className="bg-white rounded-xl shadow p-6 mt-8">

          <h2 className="text-xl font-semibold mb-4">
            Weather Impact on Lead Time
          </h2>

          <ResponsiveContainer width="100%" height={400}>

            <BarChart
              data={charts.leadtime_by_weather}
            >

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis
                dataKey="Weather_Condition"
              />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="Lead_Time_Days"
                fill="#2563eb"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>
      
      </div>

      <div className="bg-white rounded-xl shadow p-6 mt-8">

        <h2 className="text-xl font-semibold mb-4">
          Lead Time by Distance Range & Transport Mode
        </h2>

        <ResponsiveContainer
          width="100%"
          height={450}
        >

          <BarChart
            data={charts.distance_mode_analysis}
          >

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis
              dataKey="Distance_Range"
            />

            <YAxis />

            <Tooltip />

            <Legend />

            <Bar
              dataKey="Air"
              fill="#3b82f6"
            />

            <Bar
              dataKey="Road"
              fill="#22c55e"
            />

            <Bar
              dataKey="Rail"
              fill="#f59e0b"
            />

            <Bar
              dataKey="Sea"
              fill="#ef4444"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

      <div className="bg-white rounded-xl shadow p-6 mt-8">

        <div className="flex justify-between items-center mb-4">

          <h2 className="text-xl font-semibold">
            Recent Shipments
          </h2>

          <span className="text-sm text-gray-500">
            Latest 20 Records
          </span>

        </div>

        <div className="overflow-x-auto max-h-[500px]">

          <table className="w-full text-sm">

            <thead className="sticky top-0 bg-slate-100">

              <tr className="border-b bg-slate-50 hover:bg-slate-200 transition">

                <th className="p-3 text-left">Date</th>
                <th className="p-3 text-left">Origin</th>
                <th className="p-3 text-left">Destination</th>
                <th className="p-3 text-left">Mode</th>
                <th className="p-3 text-left">Lead Time</th>
                <th className="p-3 text-left">Status</th>

              </tr>

            </thead>

            <tbody>

              {shipments.map((shipment, index) => (

                <tr
                  key={index}
                  className="border-b hover:bg-slate-50 hover:bg-blue-50 transition"
                >

                  <td className="p-3">
                    {shipment.Date.slice(0, 10)}
                  </td>

                  <td className="p-3">
                    {shipment.Origin_Port}
                  </td>

                  <td className="p-3">
                    {shipment.Destination_Port}
                  </td>

                  <td className="p-3">
                    {shipment.Transport_Mode}
                  </td>

                  <td className="p-3">
                    {shipment.Lead_Time_Days}
                  </td>

                  <td className="p-3">

                    {shipment.Disruption_Occurred ? (

                      <span className="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm">
                        Disrupted
                      </span>

                    ) : (

                      <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">
                        Normal
                      </span>

                    )}

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

        {/* Top Routes */}

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-xl font-semibold mb-4">
            Top Routes
          </h2>

          <div className="overflow-auto max-h-[400px]">

            <table className="w-full">

              <thead className="sticky top-0 bg-slate-50">

                <tr>
                  <th className="text-left p-3">Route</th>
                  <th className="text-right p-3">Shipments</th>
                </tr>

              </thead>

              <tbody>

                {charts.top_routes.map((route,index)=>(

                  <tr key={index} className="border-b">

                    <td className="p-3">
                      {route.Route}
                    </td>

                    <td className="p-3 text-right font-semibold">
                      {route.Shipments}
                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        </div>

        {/* Riskiest Routes */}

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-xl font-semibold text-red-600 mb-4">
            Riskiest Routes
          </h2>

          <div className="overflow-auto max-h-[400px]">

            <table className="w-full">

              <thead className="sticky top-0 bg-slate-50">

                <tr>
                  <th className="text-left p-3">Route</th>
                  <th className="text-right p-3">Risk %</th>
                </tr>

              </thead>

              <tbody>

                {charts.riskiest_routes.map((route,index)=>(

                  <tr key={index} className="border-b">

                    <td className="p-3">
                      {route.Route}
                    </td>

                    <td className="p-3 text-right text-red-600 font-semibold">
                      {route.Risk.toFixed(1)}%
                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        </div>

      </div>

    </div>

  );
}