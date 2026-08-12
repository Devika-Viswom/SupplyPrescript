from fastapi import FastAPI
from src.api.schemas import ShipmentData
from src.api.predictor import predict
import pandas as pd

app = FastAPI(
    title="SupplyPrescript API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "SupplyPrescript API Running Successfully!"
    }


@app.post("/predict")
def predict_disruption(shipment: ShipmentData):

    # Convert request to DataFrame
    df = pd.DataFrame([shipment.model_dump()])

    # ============================
    # Feature Engineering
    # ============================

    today = pd.Timestamp.today()

    df["Year"] = today.year
    df["Month"] = today.month
    df["Day"] = today.day
    df["DayOfWeek"] = today.dayofweek

    df["Cost_Per_KM"] = (
        df["Fuel_Price_Index"] /
        df["Distance_km"]
    )

    df["Risk_LeadTime"] = (
        df["Geopolitical_Risk_Score"] *
        df["Lead_Time_Days"]
    )

    df["Weight_Per_KM"] = (
        df["Weight_MT"] /
        df["Distance_km"]
    )

    df["Risk_Reliability"] = (
        df["Geopolitical_Risk_Score"] *
        df["Carrier_Reliability_Score"]
    )

    # ============================
    # Convert categorical columns
    # ============================

    categorical_cols = [
        "Origin_Port",
        "Destination_Port",
        "Transport_Mode",
        "Product_Category",
        "Weather_Condition"
    ]

    for col in categorical_cols:
        df[col] = df[col].astype("category")

    # ============================
    # Prediction
    # ============================

    prediction, probability = predict(df)

    recommendation = (
        "Use alternate supplier"
        if prediction == 1
        else "Shipment is safe"
    )

    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 3),
        "recommendation": recommendation
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SupplyPrescript API",
        "model": "XGBoost",
        "version": "1.0"
    }
