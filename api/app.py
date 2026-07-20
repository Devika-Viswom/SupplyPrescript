from fastapi import FastAPI
import joblib
import pandas as pd
from datetime import datetime

from schemas import ShipmentInput
from recommendation_engine import generate_recommendations

clf_model = joblib.load(
    "../models/disruption_pipeline.pkl"
)

reg_model = joblib.load(
    "../models/leadtime_pipeline.pkl"
)

app = FastAPI(
    title="SupplyPrescript API"
)

def build_input_df(data):

    route = (
        f"{data.origin_port}_to_{data.destination_port}"
    )

    today = datetime.today()

    month = today.month

    quarter = (month - 1) // 3 + 1

    year = today.year

    risk_level = "Low"

    if data.geopolitical_risk_score >= 7:
        risk_level = "High"

    elif data.geopolitical_risk_score >= 3:
        risk_level = "Medium"

    reliability_level = "High"

    if data.carrier_reliability_score < 0.65:
        reliability_level = "Low"

    elif data.carrier_reliability_score < 0.85:
        reliability_level = "Medium"

    return pd.DataFrame([{
        "Origin_Port": data.origin_port,
        "Destination_Port": data.destination_port,
        "Transport_Mode": data.transport_mode,
        "Product_Category": data.product_category,
        "Distance_km": data.distance_km,
        "Weight_MT": data.weight_mt,
        "Fuel_Price_Index": data.fuel_price_index,
        "Geopolitical_Risk_Score":
            data.geopolitical_risk_score,
        "Weather_Condition":
            data.weather_condition,
        "Carrier_Reliability_Score":
            data.carrier_reliability_score,
        "Year": year,
        "Month": month,
        "Quarter": quarter,
        "Route": route,
        "Risk_Level": risk_level,
        "Reliability_Level": reliability_level
    }])

@app.post("/predict")
def predict(data: ShipmentInput):

    input_df = build_input_df(data)

    risk_probability = float(
        clf_model.predict_proba(input_df)[0][1]
    )

    lead_time = float(
        reg_model.predict(input_df)[0]
    )

    risk_level, delay_category, recommendations = (
        generate_recommendations(
            risk_probability,
            lead_time,
            data.weather_condition,
            data.geopolitical_risk_score,
            data.carrier_reliability_score,
            data.transport_mode
        )
    )

    return {
        "risk_probability":
            round(risk_probability * 100, 2),

        "risk_level":
            risk_level,

        "predicted_lead_time":
            round(lead_time, 2),

        "delay_category":
            delay_category,

        "recommendations":
            recommendations
    }