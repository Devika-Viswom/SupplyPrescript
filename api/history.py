import json
from datetime import datetime

from connection import conn

def save_prediction(
    shipment,
    prediction,
    comparison
):

    cursor = conn.cursor()

    try:

        cursor.execute(
        """
        INSERT INTO prediction_history(

            created_at,
            shipment_date,
            origin_port,
            destination_port,
            transport_mode,
            product_category,
            distance_km,
            weight_mt,
            fuel_price_index,
            geopolitical_risk_score,
            weather_condition,
            carrier_reliability_score,
            disruption_prediction,
            risk_probability,
            risk_level,
            confidence,
            predicted_lead_time,
            delay_category,
            recommendations,
            recommended_mode,
            recommendation_reason,
            fastest_mode,
            cheapest_mode,
            lowest_risk_mode,
            comparison_json

        )

        VALUES(
            %s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,
            %s
        )
        """,

        (

            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            shipment.shipment_date,
            shipment.origin_port,
            shipment.destination_port,
            shipment.transport_mode,
            shipment.product_category,
            shipment.distance_km,
            shipment.weight_mt,
            shipment.fuel_price_index,
            shipment.geopolitical_risk_score,
            shipment.weather_condition,
            shipment.carrier_reliability_score,
            prediction["disruption_prediction"],
            prediction["risk_probability"],
            prediction["risk_level"],
            prediction["confidence_score"],
            prediction["predicted_lead_time"],
            prediction["delay_category"],
            json.dumps(prediction["recommendations"]),
            comparison["recommended_mode"],
            comparison["recommendation_reason"],
            comparison["fastest_mode"],
            comparison["cheapest_mode"],
            comparison["lowest_risk_mode"],
            json.dumps(comparison["modes"])

        ))

        conn.commit()

    except Exception as e:

        conn.rollback()
        print("Database Error:", e)
        raise
    
    finally:

        cursor.close()