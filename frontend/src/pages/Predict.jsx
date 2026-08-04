import { useState } from "react";
import api from "../api/api";

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

      console.error("FULL ERROR:", err);

      if (err.response) {
        console.log("Response:", err.response.data);
        console.log("Status:", err.response.status);
      }
      
      alert("Prediction failed");

    }

    setLoading(false);
  };

  return (
    <div>

      <h1>Shipment Prediction</h1>

      <form onSubmit={handleSubmit}>

        <input
          name="shipment_date"
          type="date"
          onChange={handleChange}
        />

        <input
          name="origin_port"
          placeholder="Origin Port"
          onChange={handleChange}
        />

        <input
          name="destination_port"
          placeholder="Destination Port"
          onChange={handleChange}
        />

        <input
          name="transport_mode"
          placeholder="Transport Mode"
          onChange={handleChange}
        />

        <input
          name="product_category"
          placeholder="Product Category"
          onChange={handleChange}
        />

        <input
          name="distance_km"
          placeholder="Distance KM"
          onChange={handleChange}
        />

        <input
          name="weight_mt"
          placeholder="Weight MT"
          onChange={handleChange}
        />

        <input
          name="fuel_price_index"
          placeholder="Fuel Price Index"
          onChange={handleChange}
        />

        <input
          name="geopolitical_risk_score"
          placeholder="Risk Score"
          onChange={handleChange}
        />

        <input
          name="weather_condition"
          placeholder="Weather"
          onChange={handleChange}
        />

        <input
          name="carrier_reliability_score"
          placeholder="Reliability Score"
          onChange={handleChange}
        />

        <button type="submit">

          {loading ? "Predicting..." : "Predict"}

        </button>

      </form>

      {result && (

        <div>

          <h2>Prediction Result</h2>

          <pre>
            {JSON.stringify(result, null, 2)}
          </pre>

        </div>

      )}

    </div>
  );
}