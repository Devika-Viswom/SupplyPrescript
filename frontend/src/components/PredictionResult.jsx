export default function PredictionResult({ result }) {

  const prediction = result.prediction;

  return (
    <div className="grid grid-cols-2 gap-4 mt-6">

      <div className="bg-white p-4 rounded shadow">
        <h3>Risk Probability</h3>
        <p className="text-2xl font-bold">
          {prediction.risk_probability}%
        </p>
      </div>

      <div className="bg-white p-4 rounded shadow">
        <h3>Risk Level</h3>
        <p className="text-2xl font-bold">
          {prediction.risk_level}
        </p>
      </div>

      <div className="bg-white p-4 rounded shadow">
        <h3>Lead Time</h3>
        <p className="text-2xl font-bold">
          {prediction.predicted_lead_time} Days
        </p>
      </div>

      <div className="bg-white p-4 rounded shadow">
        <h3>Delay Category</h3>
        <p className="text-2xl font-bold">
          {prediction.delay_category}
        </p>
      </div>

    </div>
  );
}