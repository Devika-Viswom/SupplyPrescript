import { useEffect, useState } from "react";
import api from "../api/api";

export default function History() {

  const [records, setRecords] = useState([]);
  const [page, setPage] = useState(1);
  const [hasNextPage, setHasNextPage] = useState(false);
  const [selectedRecord, setSelectedRecord] = useState(null);

  useEffect(() => {
    loadHistory(page);
  }, [page]);

  const loadHistory = async (pageNo) => {

    try {

      const response = await api.get(
        `/history?page=${pageNo}`
      );

      setRecords(response.data.records);

      setHasNextPage(
        response.data.records.length === 50
      );

    } catch (error) {
      console.error(error);
    }
  };

  const getRiskColor = (risk) => {

    if (risk === "High")
      return "bg-red-100 text-red-700";

    if (risk === "Medium")
      return "bg-yellow-100 text-yellow-700";

    return "bg-green-100 text-green-700";
  };

  return (
    <div className="max-w-7xl mx-auto p-8">

      <h1 className="text-4xl font-bold mb-8">
        Prediction History
      </h1>

      {/* Table */}

      <div className="bg-white rounded-xl shadow overflow-auto">

        <table className="w-full">

          <thead className="bg-slate-100 sticky top-0">

            <tr>

              <th className="p-4 text-left">
                ID
              </th>
              
              <th className="p-4 text-left">
                Date
              </th>

              <th className="p-4 text-left">
                Product
              </th>

              <th className="p-4 text-left">
                Route
              </th>

              <th className="p-4 text-left">
                Mode
              </th>

              <th className="p-4 text-left">
                Risk
              </th>

              <th className="p-4 text-left">
                Lead Time
              </th>

              <th className="p-4 text-left">
                Details
              </th>

              <th className="p-4 text-left">
                PDF
              </th>

            </tr>

          </thead>

          <tbody>

            {records.length === 0 ? (

              <tr>
                <td className="text-center py-12 text-gray-500" colSpan="9">
                  No records found
                </td>
              </tr>

            ) : (

              records.map((record) => (

                <tr
                  key={record.id}
                  className="border-b hover:bg-slate-50"
                >

                  <td className="p-4">
                    {record.id}
                  </td>

                  <td className="p-4">
                    {record.shipment_date}
                  </td>

                  <td className="p-4">
                    {record.product_category}
                  </td>

                  <td className="p-4">
                    {record.origin_port}
                    {" → "}
                    {record.destination_port}
                  </td>

                  <td className="p-4">
                    {record.transport_mode}
                  </td>

                  <td className="p-4">

                    <span
                      className={`px-3 py-1 rounded-full text-sm font-semibold ${getRiskColor(record.risk_level)}`}
                    >
                      {record.risk_level}
                    </span>

                  </td>

                  <td className="p-4">
                    {record.predicted_lead_time} Days
                  </td>

                  <td className="p-4">

                    <div className="flex gap-2">

                      <button
                        onClick={() => setSelectedRecord(record)}
                        className="bg-indigo-600 text-white px-3 py-2 rounded"
                      >
                        View
                      </button>

                    </div>

                  </td>

                  <td className="p-4">

                    <a
                      href={`http://127.0.0.1:8000/api/report/${record.id}`}
                      target="_blank"
                      rel="noreferrer"
                      className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
                    >
                      Download
                    </a>

                  </td>

                </tr>

              ))
          
            )
            
            }

          </tbody>

        </table>

      </div>

      {/* Pagination */}

      <div className="flex justify-center gap-4 mt-8">

        <button
          onClick={() => setPage(page - 1)}
          disabled={page === 1}
          className="px-4 py-2 bg-slate-200 rounded disabled:opacity-40"
        >
          Previous
        </button>

        <div className="px-4 py-2 font-semibold">
          Page {page}
        </div>

        <button
          onClick={() => setPage(page + 1)}
          disabled={!hasNextPage}
          className="px-4 py-2 bg-slate-200 rounded disabled:opacity-40"
        >
          Next
        </button>

      </div>

      {/* Modal for Selected Record */}

      {
        selectedRecord && (

        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">

          <div className="bg-white rounded-xl w-[900px] max-h-[90vh] overflow-auto p-8">

            <div className="flex justify-between items-start mb-8">

              <div>

                <h2 className="text-3xl font-bold">
                Prediction Details
                </h2>

                <div className="text-gray-500 mt-2">

                  <div>
                    <b>ID:</b> {selectedRecord.id}
                  </div>

                  <div>
                    <b>Prediction Time:</b>{" "}
                    {new Date(selectedRecord.created_at).toLocaleString()}
                  </div>

                </div>

              </div>

              <button
                onClick={() => setSelectedRecord(null)}
                className="text-red-500 font-bold text-xl"
              >
                ✕
              </button>

            </div>

            <h3 className="text-xl font-bold mb-4 border-b pb-2">
              Shipment Details
            </h3>

            <div className="grid grid-cols-2 gap-4 mb-8">

              <div>
                <b>Shipment Date:</b>{" "}
                {selectedRecord.shipment_date}
              </div>

              <div>
                <b>Route:</b>
                {" "}
                {selectedRecord.origin_port}
                →
                {selectedRecord.destination_port}
              </div>

              <div>
                <b>Transport:</b>
                {" "}
                {selectedRecord.transport_mode}
              </div>

              <div>
                <b>Product Category:</b>{" "}
                {selectedRecord.product_category}
              </div>

              <div>
                <b>Distance:</b>{" "}
                {selectedRecord.distance_km} km
              </div>

              <div>
                <b>Weight:</b>{" "}
                {selectedRecord.weight_mt} MT
              </div>

              <div>
                <b>Fuel Price Index:</b>{" "}
                {selectedRecord.fuel_price_index}
              </div>

              <div>
                <b>Geopolitical Risk:</b>{" "}
                {selectedRecord.geopolitical_risk_score}
              </div>

              <div>
                <b>Carrier Reliability:</b>{" "}
                {selectedRecord.carrier_reliability_score}
              </div>

              <div>
                <b>Weather:</b>{" "}
                {selectedRecord.weather_condition}
              </div>
            
            </div>

            <h3 className="text-xl font-bold mb-4 border-b pb-2">
              Prediction
            </h3>

            <div className="grid grid-cols-2 gap-4 mb-8">

              <div>
                <b>Disruption Prediction:</b>{" "}
                {selectedRecord.disruption_prediction ? "Yes" : "No"}
              </div>

              <div>
                <b>Risk Level:</b>{" "}
                {selectedRecord.risk_level}
              </div>

              <div>
                <b>Confidence:</b>
                {" "}
                {selectedRecord.confidence_score}%
              </div>

              <div>
                <b>Predicted Lead Time:</b>
                {" "}
                {selectedRecord.predicted_lead_time}
                {" "}Days
              </div>

              <div>
                <b>Delay Category:</b>
                {" "}
                {selectedRecord.delay_category}
              </div>
              
            </div>

            <h3 className="text-xl font-bold mb-3 border-b pb-2">
            Recommendations
            </h3>

            <ul className="mb-6">

              {selectedRecord.recommendations.map((r,i) => (

                <li key={i}>
                ✓{" "}{r}
                </li>

              ))}

            </ul>

            <h3 className="text-xl font-bold mb-3 border-b pb-2">
            Mode Comparison
            </h3>

            <div className="grid grid-cols-4 gap-4 mb-6">

              <div className="bg-blue-50 p-4 rounded">
                Fastest
                <br/>
                <b>{selectedRecord.fastest_mode}</b>
              </div>

              <div className="bg-green-50 p-4 rounded">
                Cheapest
                <br/>
                <b>{selectedRecord.cheapest_mode}</b>
              </div>

              <div className="bg-red-50 p-4 rounded">
                Lowest Risk
                <br/>
                <b>{selectedRecord.lowest_risk_mode}</b>
              </div>

              <div className="bg-purple-50 p-4 rounded">
                Recommended
                <br/>
                <b>{selectedRecord.recommended_mode}</b>
              </div>

            </div>

            <table className="w-full border text-center">

              <thead>

                <tr className="bg-slate-100">

                  <th className="p-3">Mode</th>
                  <th className="p-3">Risk %</th>
                  <th className="p-3">Lead Time</th>
                  <th className="p-3">Cost</th>

                </tr>

              </thead>

              <tbody>

              {selectedRecord.comparison_json.map((mode) => (

                <tr key={mode.mode}
                  className="border-t hover:bg-slate-50">

                  <td className="p-3">{mode.mode}</td>

                  <td className="p-3">{mode.risk_probability}</td>

                  <td className="p-3">{mode.predicted_lead_time}</td>

                  <td className="p-3">${mode.estimated_cost}</td>

                </tr>

              ))}

              </tbody>

            </table>

          </div>
        
        </div>

      )}

    </div>

  );
}