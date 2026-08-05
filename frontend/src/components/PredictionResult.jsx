export default function PredictionResult({ result }) {
  const prediction = result.prediction;
  const comparison = result.comparison;

  const riskColor =
    prediction.risk_level === "High"
      ? "text-red-600"
      : prediction.risk_level === "Medium"
      ? "text-yellow-600"
      : "text-green-600";

  return (
    <div className="space-y-6">

      {/* KPI Cards */}

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">

        <div className="bg-white shadow rounded-xl p-4 text-center">
          <p className="text-gray-500">Risk %</p>
          <p className="text-2xl font-bold">
            {prediction.risk_probability}%
          </p>
        </div>

        <div className="bg-white shadow rounded-xl p-4 text-center">
          <p className="text-gray-500">Risk Level</p>
          <p className={`text-2xl font-bold ${riskColor}`}>
            {prediction.risk_level}
          </p>
        </div>

        <div className="bg-white shadow rounded-xl p-4 text-center">
          <p className="text-gray-500">Lead Time</p>
          <p className="text-2xl font-bold">
            {prediction.predicted_lead_time}
          </p>
        </div>

        <div className="bg-white shadow rounded-xl p-4 text-center">
          <p className="text-gray-500">Confidence</p>
          <p className="text-2xl font-bold">
            {prediction.confidence_score}%
          </p>
        </div>

      </div>

      {/* Delay */}

      <div className="bg-white shadow rounded-xl p-5">

        <h3 className="font-semibold mb-2">
          Delay Category
        </h3>

        <span className="px-4 py-2 rounded-full bg-red-100 text-red-700">
          {prediction.delay_category}
        </span>

      </div>

      {/* Recommendations */}

      <div className="bg-white shadow rounded-xl p-5">

        <h3 className="font-semibold mb-3">
          Recommendations
        </h3>

        <ul className="space-y-2">

          {prediction.recommendations.map((item, index) => (
            <li
              key={index}
              className="bg-slate-100 p-3 rounded-lg"
            >
              {item}
            </li>
          ))}

        </ul>

      </div>

      {/* Mode Comparison */}

      <div className="bg-white shadow rounded-xl p-5">

        <h3 className="font-semibold mb-4">
          Transport Mode Comparison
        </h3>

        <div className="overflow-x-auto">

          <table className="w-full">

            <thead>

              <tr className="border-b">

                <th className="text-left p-2">Mode</th>
                <th className="text-left p-2">Risk %</th>
                <th className="text-left p-2">Lead Time</th>
                <th className="text-left p-2">Cost</th>

              </tr>

            </thead>

            <tbody>

              {comparison.modes.map((mode, index) => (

                <tr
                  key={index}
                  className="border-b"
                >
                  <td className="p-2">
                    {mode.mode}
                  </td>

                  <td className="p-2">
                    {mode.risk_probability}
                  </td>

                  <td className="p-2">
                    {mode.predicted_lead_time}
                  </td>

                  <td className="p-2">
                    ${mode.estimated_cost}
                  </td>
                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

      {/* Best Recommendation */}

      <div className="bg-blue-50 border border-blue-200 rounded-xl p-5">

        <h3 className="font-semibold text-blue-700">
          Recommended Mode
        </h3>

        <p className="text-2xl font-bold mt-2">
          {comparison.recommended_mode}
        </p>

        <p className="mt-2 text-gray-700">
          {comparison.recommendation_reason}
        </p>

      </div>

    </div>
  );
}