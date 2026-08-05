from pydantic import BaseModel


class ShipmentData(BaseModel):

    Origin_Port: str
    Destination_Port: str
    Transport_Mode: str
    Product_Category: str

    Distance_km: float
    Weight_MT: float

    Fuel_Price_Index: float

    Geopolitical_Risk_Score: float

    Weather_Condition: str

    Carrier_Reliability_Score: float

    Lead_Time_Days: float