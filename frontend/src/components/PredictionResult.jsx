export default function PredictionResult({ result }) {
  if (!result) return null;

  const prediction = result.prediction;
  const comparison = result.comparison;

  const riskConfig = {
    High: {
      text: "text-red-700",
      bg: "bg-red-50",
      border: "border-red-300",
      badge: "bg-red-600",
    },
    Medium: {
      text: "text-yellow-700",
      bg: "bg-yellow-50",
      border: "border-yellow-300",
      badge: "bg-yellow-500",
    },
    Low: {
      text: "text-green-700",
      bg: "bg-green-50",
      border: "border-green-300",
      badge: "bg-green-600",
    },
  };

  const currentRisk = riskConfig[prediction.risk_level];

  return (
    <div className="space-y-6">

      {/* Risk Banner */}

      <div
        className={`rounded-2xl border p-6 shadow-sm ${currentRisk.bg} ${currentRisk.border}`}
      >
        <div className="flex flex-col md:flex-row justify-between items-center">

          <div>

            <p className="text-gray-500 text-sm uppercase tracking-wide">
              Shipment Risk Assessment
            </p>

            <h2
              className={`text-3xl md:text-4xl font-bold mt-2 ${currentRisk.text}`}
            >
              {prediction.risk_level} Risk Shipment
            </h2>

            <p className="text-gray-700 mt-2">
              Estimated disruption probability:
              <span className="font-bold ml-1">
                {prediction.risk_probability}%
              </span>
            </p>

          </div>

          <div
            className={`mt-4 md:mt-0 px-6 py-3 rounded-full text-white font-bold text-lg ${currentRisk.badge}`}
          >
            {prediction.risk_level}
          </div>

        </div>
      </div>

      {/* KPI Cards */}

      <div className="grid grid-cols-2 md:grid-cols-4 gap-5">

        <div className="bg-white rounded-2xl border shadow-sm p-5 text-center">

          <p className="text-gray-500 text-sm">
            Risk Probability
          </p>

          <p className="text-3xl font-bold text-red-600 mt-2">
            {prediction.risk_probability}%
          </p>

        </div>

        <div className="bg-white rounded-2xl border shadow-sm p-5 text-center">

          <p className="text-gray-500 text-sm">
            Confidence
          </p>

          <p className="text-3xl font-bold text-blue-600 mt-2">
            {prediction.confidence_score}%
          </p>

        </div>

        <div className="bg-white rounded-2xl border shadow-sm p-5 text-center">

          <p className="text-gray-500 text-sm">
            Lead Time
          </p>

          <p className="text-3xl font-bold text-purple-600 mt-2">
            {prediction.predicted_lead_time}
          </p>

          <p className="text-xs text-gray-500 mt-1">
            Days
          </p>

        </div>

        <div className="bg-white rounded-2xl border shadow-sm p-5 text-center">

          <p className="text-gray-500 text-sm">
            Delay Category
          </p>

          <p className="text-3xl font-bold text-orange-500 mt-2">
            {prediction.delay_category}
          </p>

        </div>

      </div>

      {/* Recommendations */}

      <div className="bg-white rounded-2xl border shadow-sm p-6">

        <h3 className="text-xl font-bold mb-4">
          Recommended Actions
        </h3>

        {prediction.recommendations.length > 0 ? (

          <div className="grid md:grid-cols-2 gap-3">

            {prediction.recommendations.map((item, index) => (

              <div
                key={index}
                className="bg-blue-50 border border-blue-200 rounded-xl p-4 text-gray-700"
              >
                ✓ {item}
              </div>

            ))}

          </div>

        ) : (

          <div className="bg-green-50 border border-green-200 rounded-xl p-4 text-green-700">
            No immediate action required.
          </div>

        )}

      </div>

      {/* Mode Summary Cards */}

      <div className="grid md:grid-cols-4 gap-4">

        <div className="bg-green-50 border border-green-200 rounded-2xl p-5">

          <p className="text-green-700 font-medium">
            Fastest Mode
          </p>

          <p className="text-2xl font-bold mt-2">
            {comparison.fastest_mode}
          </p>

        </div>

        <div className="bg-yellow-50 border border-yellow-200 rounded-2xl p-5">

          <p className="text-yellow-700 font-medium">
            Cheapest Mode
          </p>

          <p className="text-2xl font-bold mt-2">
            {comparison.cheapest_mode}
          </p>

        </div>

        <div className="bg-red-50 border border-red-200 rounded-2xl p-5">

          <p className="text-red-700 font-medium">
            Lowest Risk
          </p>

          <p className="text-2xl font-bold mt-2">
            {comparison.lowest_risk_mode}
          </p>

        </div>

        <div className="bg-blue-50 border border-blue-200 rounded-2xl p-5">

          <p className="text-blue-700 font-medium">
            Recommended
          </p>

          <p className="text-2xl font-bold mt-2">
            {comparison.recommended_mode}
          </p>

        </div>

      </div>

      {/* Mode Comparison Table */}

      <div className="bg-white rounded-2xl border shadow-sm p-6">

        <h3 className="text-xl font-bold mb-4">
          Transport Mode Comparison
        </h3>

        <div className="overflow-x-auto">

          <table className="w-full text-center">

            <thead>

              <tr className="bg-slate-100">

                <th className="p-3 font-semibold">
                  Mode
                </th>

                <th className="p-3 font-semibold">
                  Risk %
                </th>

                <th className="p-3 font-semibold">
                  Lead Time
                </th>

                <th className="p-3 font-semibold">
                  Cost
                </th>

              </tr>

            </thead>

            <tbody>

              {comparison.modes.map((mode, index) => (

                <tr
                  key={index}
                  className="border-b hover:bg-blue-50 transition"
                >

                  <td className="p-3 font-medium">
                    {mode.mode}
                  </td>

                  <td className="p-3">
                    {mode.risk_probability}%
                  </td>

                  <td className="p-3">
                    {mode.predicted_lead_time} Days
                  </td>

                  <td className="p-3">
                    ${mode.estimated_cost}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

      {/* Recommendation Banner */}

      <div className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-2xl p-6 shadow-lg">

        <p className="uppercase tracking-wide text-sm opacity-80">
          Best Recommendation
        </p>

        <h2 className="text-4xl font-bold mt-2">
          {comparison.recommended_mode}
        </h2>

        <p className="mt-4 text-blue-100 leading-relaxed">
          {comparison.recommendation_reason}
        </p>

      </div>

    </div>
  );
}