from pydantic import BaseModel


class ShipmentInput(BaseModel):
    origin_port: str
    destination_port: str
    transport_mode: str
    product_category: str

    distance_km: float
    weight_mt: float
    fuel_price_index: float

    geopolitical_risk_score: float

    weather_condition: str

    carrier_reliability_score: float