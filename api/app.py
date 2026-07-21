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

    shipment_date = pd.to_datetime(data.shipment_date)

    year = shipment_date.year
    month = shipment_date.month
    quarter = shipment_date.quarter

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

def get_prediction_results(data):

    input_df = build_input_df(data)

    disruption_prediction = int(
        clf_model.predict(input_df)[0]
    )

    risk_probability = float(
        clf_model.predict_proba(input_df)[0][1]
    )

    lead_time = float(
        reg_model.predict(input_df)[0]
    )

    return {
        "disruption_prediction": disruption_prediction,
        "risk_probability": round(risk_probability * 100, 2),
        "predicted_lead_time": round(lead_time, 2)
    }

def estimate_shipping_cost(distance_km, weight_mt, transport_mode):

        mode_factor = {
            "Air": 5.0,
            "Road": 2.0,
            "Rail": 1.5,
            "Sea": 1.0
        }

        cost = (
            distance_km *
            weight_mt *
            mode_factor[transport_mode]
        ) / 1000

        return round(cost, 2)

def get_mode_comparison(data):

    modes = ["Air", "Road", "Rail", "Sea"]

    comparison = []

    for mode in modes:

        mode_data = ShipmentInput(
            shipment_date=data.shipment_date,

            origin_port=data.origin_port,
            destination_port=data.destination_port,

            transport_mode=mode,

            product_category=data.product_category,

            distance_km=data.distance_km,
            weight_mt=data.weight_mt,

            fuel_price_index=data.fuel_price_index,

            geopolitical_risk_score=data.geopolitical_risk_score,

            weather_condition=data.weather_condition,

            carrier_reliability_score=data.carrier_reliability_score
        )

        result = get_prediction_results(mode_data)

        estimated_cost = estimate_shipping_cost(data.distance_km, data.weight_mt, mode)

        comparison.append({

            "mode": mode,

            "risk_probability":
                result["risk_probability"],

            "predicted_lead_time":
                result["predicted_lead_time"],

            "estimated_cost":
                estimated_cost
        })

    return comparison

@app.post("/predict")
def predict(data: ShipmentInput):

    results = get_prediction_results(data)

    risk_probability = results["risk_probability"]
    lead_time = results["predicted_lead_time"]
    disruption_prediction = results["disruption_prediction"]

    confidence_score = round(abs(risk_probability - 50) * 2, 2)

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

    comparison = get_mode_comparison(data)

    max_risk = max(row["risk_probability"] for row in comparison)

    max_time = max(row["predicted_lead_time"] for row in comparison)

    max_cost = max(row["estimated_cost"] for row in comparison)

    for row in comparison:

        risk_score = (row["risk_probability"] / max_risk)
        time_score = (row["predicted_lead_time"] / max_time)
        cost_score = (row["estimated_cost"] / max_cost)

        row["score"] = round(
            (
                risk_score * 0.25
                +
                time_score * 0.45
                +
                cost_score * 0.3
            ),
            3
        )
    
    best_option = min(
        comparison,
        key=lambda x: x["score"]
    )

    if best_option["mode"] == "Air":

        air_time = next(
            x["predicted_lead_time"]
            for x in comparison
            if x["mode"] == "Air"
        )

        time_saved = round(lead_time - air_time, 1)

        recommendation_reason = (
            f"Fastest delivery option. "
            f"Can reduce lead time by "
            f"approximately {time_saved} days "
            f"compared to {data.transport_mode} transport."
        )

    elif best_option["mode"] == "Road":

        recommendation_reason = (
            "Balanced option with moderate lead time, risk, and cost."
        )

    elif best_option["mode"] == "Rail":

        recommendation_reason = (
            "Suitable for cost-conscious shipments with acceptable lead times."
        )

    else:

        recommendation_reason = (
            "Preferred when delivery speed is not a priority. "
            "Offers the lowest cost option for bulk shipments."
        )
    
    fastest_mode = min(
        comparison,
        key=lambda x:
            x["predicted_lead_time"]
    )

    cheapest_mode = min(
        comparison,
        key=lambda x:
            x["estimated_cost"]
    )

    lowest_risk_mode = min(
        comparison,
        key=lambda x:
            x["risk_probability"]
    )

    return {

    "prediction": {

        "disruption_prediction":
            disruption_prediction,

        "risk_probability":
            risk_probability,

        "risk_level":
            risk_level,
        
        "confidence_score":
            confidence_score,

        "predicted_lead_time":
            lead_time,

        "delay_category":
            delay_category,

        "recommendations":
            recommendations
    },

    "comparison": {

        "recommended_mode":
            best_option["mode"],

        "recommendation_reason":
            recommendation_reason,
        
        "fastest_mode":
            fastest_mode["mode"],

        "cheapest_mode":
            cheapest_mode["mode"],

        "lowest_risk_mode":
            lowest_risk_mode["mode"],

        "modes":
            comparison
    }
}

@app.post("/compare_modes")
def compare_modes(data: ShipmentInput):

    modes = [
        "Air",
        "Road",
        "Rail",
        "Sea"
    ]

    comparison = []

    for mode in modes:

        mode_data = ShipmentInput(
            shipment_date=data.shipment_date,

            origin_port=data.origin_port,
            destination_port=data.destination_port,

            transport_mode=mode,

            product_category=data.product_category,

            distance_km=data.distance_km,
            weight_mt=data.weight_mt,

            fuel_price_index=data.fuel_price_index,

            geopolitical_risk_score=
                data.geopolitical_risk_score,

            weather_condition=
                data.weather_condition,

            carrier_reliability_score=
                data.carrier_reliability_score
        )

        result = get_prediction_results(mode_data)

        comparison.append({
            "mode": mode,
            "risk_probability":
                result["risk_probability"],
            "predicted_lead_time":
                result["predicted_lead_time"]
        })

    best_option = min(
        comparison,
        key=lambda x: (
            x["risk_probability"],
            x["predicted_lead_time"]
        )
    )

    return {
        "recommended_mode":
            best_option["mode"],

        "comparison":
            comparison
    }