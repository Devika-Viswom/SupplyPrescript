from connection import conn

def get_prediction_history(page):

    page_size = 50

    offset = (page - 1) * page_size

    cursor = conn.cursor()

    try:

        cursor.execute("""
            SELECT *
            FROM prediction_history
            ORDER BY id ASC
            LIMIT %s
            OFFSET %s
        """, (page_size, offset))

        rows = cursor.fetchall()

        history = []

        for row in rows:

            history.append({
                "id": row[0],
                "created_at": row[1],
                "shipment_date": row[2],
                "origin_port": row[3],
                "destination_port": row[4],
                "transport_mode": row[5],
                "product_category": row[6],
                "distance_km": row[7],
                "weight_mt": row[8],
                "fuel_price_index": row[9],
                "geopolitical_risk_score": row[10],
                "weather_condition": row[11],
                "carrier_reliability_score": row[12],
                "disruption_prediction": row[13],
                "risk_probability": row[14],
                "risk_level": row[15],
                "confidence_score": row[16],
                "predicted_lead_time": row[17],
                "delay_category": row[18],
                "recommendations": row[19],
                "recommended_mode": row[20],
                "recommendation_reason": row[21],
                "fastest_mode": row[22],
                "cheapest_mode": row[23],
                "lowest_risk_mode": row[24],
                "comparison_json": row[25]
            })

        return history

    finally:

        cursor.close()

def get_prediction_by_id(prediction_id):

    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT *
            FROM prediction_history
            WHERE id = %s
            """,
            (prediction_id,)
        )

        row = cursor.fetchone()

        if not row:
            return None

        return {
            "id": row[0],
            "created_at": row[1],
            "shipment_date": row[2],
            "origin_port": row[3],
            "destination_port": row[4],
            "transport_mode": row[5],
            "product_category": row[6],
            "distance_km": row[7],
            "weight_mt": row[8],
            "fuel_price_index": row[9],
            "geopolitical_risk_score": row[10],
            "weather_condition": row[11],
            "carrier_reliability_score": row[12],
            "disruption_prediction": row[13],
            "risk_probability": row[14],
            "risk_level": row[15],
            "confidence_score": row[16],
            "predicted_lead_time": row[17],
            "delay_category": row[18],
            "recommendations": row[19],
            "recommended_mode": row[20],
            "recommendation_reason": row[21],
            "fastest_mode": row[22],
            "cheapest_mode": row[23],
            "lowest_risk_mode": row[24],
            "comparison_json": row[25]
        }

    finally:
        
        cursor.close()