import { useEffect, useState } from "react";
import api from "../api/api";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  PieChart,
  Pie,
  Cell,
  Legend
} from "recharts";
export default function Insights() {

  const [classifier, setClassifier] = useState(null);
  const [regressor, setRegressor] = useState(null);
  const [business, setBusiness] = useState([]);
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    loadInsights();
  }, []);

  const loadInsights = async () => {

    try {

      const classifierRes = await api.get(
        "/insights/disruption_classifier"
      );

      const regressorRes = await api.get(
        "/insights/leadtime_regressor"
      );

      const businessRes = await api.get(
        "/insights/business"
      );

      const recommendationRes = await api.get(
        "/insights/recommendations"
      );

      setClassifier(
        classifierRes.data.disruption_classifier_insights
      );

      setRegressor(
        regressorRes.data.leadtime_regressor_insights
      );

      setBusiness(
        businessRes.data.business_insights
      );

      setRecommendations(
        recommendationRes.data.recommendation_insights
      );

    } catch (error) {
      console.error(error);
    }
  };

  if (!classifier || !regressor) {
    return <div className="p-10">Loading Insights...</div>;
  }

  const confidenceData = Object.entries(
    classifier.confidence_distribution
  ).map(([range, count]) => ({
    range,
    count
  }));

  const cm =
    classifier.confusion_matrix;

  return (
    <div className="max-w-7xl mx-auto p-8">

      <h1 className="text-4xl font-bold mb-8">
        Model & Business Insights
      </h1>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-2xl font-semibold mb-4">
            Disruption Classifier
          </h2>

          <div className="grid grid-cols-2 gap-4">

            <div>
              <p className="text-gray-500">Accuracy</p>
              <h3 className="text-3xl font-bold text-blue-600">
                {classifier.accuracy}%
              </h3>
            </div>

            <div>
              <p className="text-gray-500">Precision</p>
              <h3 className="text-3xl font-bold">
                {classifier.precision}%
              </h3>
            </div>

            <div>
              <p className="text-gray-500">Recall</p>
              <h3 className="text-3xl font-bold">
                {classifier.recall}%
              </h3>
            </div>

            <div>
              <p className="text-gray-500">F1 Score</p>
              <h3 className="text-3xl font-bold">
                {classifier.f1_score}%
              </h3>
            </div>

          </div>

        </div>

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-2xl font-semibold mb-4">
            Lead Time Regressor
          </h2>

          <div className="grid grid-cols-3 gap-4">

            <div>
              <p className="text-gray-500">MAE</p>
              <h3 className="text-3xl font-bold">
                {regressor.mae}
              </h3>
            </div>

            <div>
              <p className="text-gray-500">RMSE</p>
              <h3 className="text-3xl font-bold">
                {regressor.rmse}
              </h3>
            </div>

            <div>
              <p className="text-gray-500">R²</p>
              <h3 className="text-3xl font-bold text-green-600">
                {regressor.r2}
              </h3>
            </div>

          </div>

        </div>

      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

        {/* Confusion Matrix */}

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-2xl font-semibold mb-6">
            Disruption Prediction Performance
          </h2>

          <div className="overflow-auto">

            <table className="w-full text-center border-collapse">

              <thead>

                <tr>

                  <th className="border p-4 bg-slate-100">
                  </th>

                  <th className="border p-4 bg-slate-100">
                    Actual: No Disruption
                  </th>

                  <th className="border p-4 bg-slate-100">
                    Actual: Disruption
                  </th>

                </tr>

              </thead>

              <tbody>

                <tr>

                  <td className="border p-4 font-semibold bg-slate-50">
                    Predicted: No Disruption
                  </td>

                  <td className="border p-6 bg-green-100">

                    <div className="text-4xl font-bold text-green-700">
                      {cm.true_negatives}
                    </div>

                    <div className="text-sm text-gray-600 mt-2">
                      Correct
                    </div>

                  </td>

                  <td className="border p-6 bg-orange-100">

                    <div className="text-4xl font-bold text-orange-700">
                      {cm.false_negatives}
                    </div>

                    <div className="text-sm text-gray-600 mt-2">
                      Missed Disruptions
                    </div>

                  </td>

                </tr>

                <tr>

                  <td className="border p-4 font-semibold bg-slate-50">
                    Predicted: Disruption
                  </td>

                  <td className="border p-6 bg-red-100">

                    <div className="text-4xl font-bold text-red-700">
                      {cm.false_positives}
                    </div>

                    <div className="text-sm text-gray-600 mt-2">
                      False Alarms
                    </div>

                  </td>

                  <td className="border p-6 bg-green-100">

                    <div className="text-4xl font-bold text-green-700">
                      {cm.true_positives}
                    </div>

                    <div className="text-sm text-gray-600 mt-2">
                      Correct
                    </div>

                  </td>

                </tr>

              </tbody>

            </table>

          </div>

        </div>

        {/* Confidence Distribution */}

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-2xl font-semibold mb-4">
            Confidence Distribution
          </h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <BarChart data={confidenceData}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="range" />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="count"
                fill="#2563eb"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-xl font-semibold mb-4">
            Disruption Model Drivers
          </h2>

          <ResponsiveContainer width="100%" height={400}>

            <BarChart
              layout="vertical"
              data={classifier.top_features}
            >

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis type="number" />

              <YAxis
                dataKey="Feature"
                type="category"
                width={180}
              />

              <Tooltip />

              <Bar
                dataKey="Importance"
                fill="#ef4444"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-xl font-semibold mb-4">
            Lead Time Model Drivers
          </h2>

          <ResponsiveContainer width="100%" height={400}>

            <BarChart
              layout="vertical"
              data={regressor.top_features}
            >

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis type="number" />

              <YAxis
                dataKey="Feature"
                type="category"
                width={180}
              />

              <Tooltip />

              <Bar
                dataKey="Importance"
                fill="#2563eb"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

      </div>

      <div className="bg-white rounded-xl shadow p-6 mt-8">

        <h2 className="text-2xl font-semibold mb-4">
          Business Insights
        </h2>

        <div className="space-y-3">

          {business.map((item, index) => (

            <div
              key={index}
              className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded"
            >
              {item}
            </div>

          ))}

        </div>

      </div>

      <div className="bg-white rounded-xl shadow p-6 mt-8">

        <h2 className="text-2xl font-semibold mb-4">
          Operational Recommendations
        </h2>

        <div className="space-y-3">

          {recommendations.map((item, index) => (

            <div
              key={index}
              className="bg-green-50 border-l-4 border-green-500 p-4 rounded"
            >
              {item}
            </div>

          ))}

        </div>

      </div>

    </div>
  );
}