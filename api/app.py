from fastapi import FastAPI

from schemas import ShipmentInput

from prediction import predict_shipment

from dashboard import (
    get_summary,
    get_leadtime_by_mode,
    get_disruption_by_weather,
    get_monthly_shipments,
    get_route_distribution,
    get_recent_shipments
)
from insights import (
    get_top_weather_risks,
    get_dataset_insights,
    get_disruption_classifier_insights,
    get_leadtime_regressor_insights
)

app = FastAPI(
    title="SupplyPrescript API"
)

@app.post("/predict")
def predict(data: ShipmentInput):

    return predict_shipment(data)


@app.get("/dashboard/summary")
def dashboard_summary():

    return get_summary()


@app.get("/dashboard/charts")
def dashboard_charts():

    return {
        "lead_time_by_mode":
            get_leadtime_by_mode(),

        "disruption_by_weather":
            get_disruption_by_weather(),

        "monthly_shipments":
            get_monthly_shipments(),

        "route_distribution":
            get_route_distribution()
    }


@app.get("/dashboard/shipments")
def dashboard_shipments():

    return get_recent_shipments()


@app.get("/insights/weather_risks")
def insights_weather_risks():

    return {
        "top_weather_risks": get_top_weather_risks()
    }


@app.get("/insights/dataset")
def insights_dataset():

    return {
        "dataset_insights": get_dataset_insights()
    }


@app.get("/insights/disruption_classifier")
def insights_disruption_classifier():

    return {
        "disruption_classifier_insights":
            get_disruption_classifier_insights()
    }


@app.get("/insights/leadtime_regressor")
def insights_leadtime_regressor():

    return {
        "leadtime_regressor_insights":
            get_leadtime_regressor_insights()
    }