from api.connection import conn
'''
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prediction_history (

    id BIGSERIAL PRIMARY KEY,
    created_at TEXT,
    shipment_date TEXT,
    origin_port TEXT,
    destination_port TEXT,
    transport_mode TEXT,
    product_category TEXT,
    distance_km REAL,
    weight_mt REAL,
    fuel_price_index REAL,
    geopolitical_risk_score REAL,
    weather_condition TEXT,
    carrier_reliability_score REAL,
    disruption_prediction INTEGER,
    risk_probability REAL,
    risk_level TEXT,
    confidence REAL,
    predicted_lead_time REAL,
    delay_category TEXT,
    recommendations TEXT,
    recommended_mode TEXT,
    recommendation_reason TEXT,
    fastest_mode TEXT,
    cheapest_mode TEXT,
    lowest_risk_mode TEXT,
    comparison_json TEXT
)
""")

conn.commit()

print("Database Ready")

cursor.close()
'''