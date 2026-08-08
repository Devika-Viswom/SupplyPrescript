import { useState } from "react";
import api from "../api/api";
import PredictionResult from "../components/PredictionResult";

export default function Predict() {
  const [formData, setFormData] = useState({
    shipment_date: "",
    origin_port: "",
    destination_port: "",
    transport_mode: "",
    product_category: "",
    distance_km: "",
    weight_mt: "",
    fuel_price_index: "",
    geopolitical_risk_score: "",
    weather_condition: "",
    carrier_reliability_score: ""
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const isFormValid = Object.values(formData).every(
    value => value !== ""
  );

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);

    try {
      const response = await api.post(
        "/predict",
        formData
      );

      setResult(response.data);

    } catch (err) {
      console.error(err);
      alert("Prediction failed");
    }

    setLoading(false);
  };

  return (
    <div className="flex justify-center py-10 px-4">

      <div className="bg-slate-50 shadow-2xl rounded-3xl p-10 w-full max-w-6xl border">

        <div className="text-center mb-8">

          <h1 className="text-4xl font-bold">
            Supply Chain Risk Prediction
          </h1>

          <p className="text-gray-500 mt-2">
            Predict disruption risk, lead time and recommended transport mode
          </p>

        </div>

        <form
          onSubmit={handleSubmit}
          className="space-y-4"
        >

          <input
            type="date"
            name="shipment_date"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />

          <select
            name="origin_port"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          >
            <option value="">Origin Port</option>
            <option>Singapore</option>
            <option>Rotterdam</option>
            <option>Busan</option>
            <option>Shanghai</option>
            <option>Dubai</option>
            <option>Los Angeles</option>
            <option>Hamburg</option>
            <option>Antwerp</option>
          </select>

          <select
            name="destination_port"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          >
            <option value="">Destination Port</option>
            <option>Singapore</option>
            <option>Rotterdam</option>
            <option>Busan</option>
            <option>Shanghai</option>
            <option>Dubai</option>
            <option>Los Angeles</option>
            <option>Hamburg</option>
            <option>Antwerp</option>
            <option>Marseille</option>
          </select>

          <select
            name="transport_mode"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          >
            <option value="">Transport Mode</option>
            <option>Air</option>
            <option>Road</option>
            <option>Rail</option>
            <option>Sea</option>
          </select>

          <select
            name="product_category"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          >
            <option value="">Product Category</option>
            <option>Electronics</option>
            <option>Automotive</option>
            <option>Pharmaceuticals</option>
            <option>Food</option>
            <option>Industrial Equipment</option>
          </select>

          <input
            type="number"
            name="distance_km"
            placeholder="Distance (KM)"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />

          <input
            type="number"
            name="weight_mt"
            placeholder="Weight (MT)"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />

          <input
            type="number"
            step="0.01"
            name="fuel_price_index"
            placeholder="Fuel Price Index"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />

          <input
            type="number"
            step="0.01"
            name="geopolitical_risk_score"
            placeholder="Geopolitical Risk Score"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />

          <select
            name="weather_condition"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          >
            <option value="">Weather Condition</option>
            <option>Clear</option>
            <option>Rain</option>
            <option>Fog</option>
            <option>Storm</option>
            <option>Hurricane</option>
          </select>

          <input
            type="number"
            step="0.01"
            name="carrier_reliability_score"
            placeholder="Carrier Reliability Score"
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />

          <button
            type="submit"
            disabled={!isFormValid || loading}
            className={`w-full p-3 rounded-lg font-semibold transition-all duration-300
              ${
                isFormValid
                  ? "bg-blue-600 text-white hover:bg-blue-700 shadow-lg shadow-blue-300"
                  : "bg-gray-300 text-gray-500 cursor-not-allowed"
              }
            `}
          >
            {loading ? "Predicting..." : "Predict Shipment"}
          </button>

        </form>

        {result && (
          <div className="mt-8">
            <PredictionResult result={result} />
          </div>
        )}

      </div>

    </div>
  );
}