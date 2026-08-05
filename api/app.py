from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from schemas import ShipmentInput

from prediction import predict_shipment

from dashboard import (
    get_summary,
    get_monthly_disruptions,
    get_monthly_leadtime,
    get_riskiest_routes,
    get_risk_distribution,
    get_reliability_distribution,
    get_leadtime_by_weather,
    get_distance_mode_analysis,
    get_top_routes,
    get_disruption_by_weather,
    get_recent_shipments
)
from insights import (
    get_top_weather_risks,
    get_dataset_insights,
    get_disruption_classifier_insights,
    get_leadtime_regressor_insights
)

from history_service import (
    get_prediction_history,
    get_prediction_by_id
)

from report import generate_pdf_report

app = FastAPI(title="SupplyPrescript API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/predict")
def predict(data: ShipmentInput):

    return predict_shipment(data)


@app.get("/api/dashboard/kpi")
def dashboard_kpi():

    return get_summary()


@app.get("/api/dashboard/charts")
def dashboard_charts():

    return {
        "monthly_disruptions":
            get_monthly_disruptions(),

        "monthly_leadtime":
            get_monthly_leadtime(),

        "riskiest_routes":
            get_riskiest_routes(),

        "risk_distribution":
            get_risk_distribution(),

        "reliability_distribution":
            get_reliability_distribution(),

        "leadtime_by_weather":
            get_leadtime_by_weather(),

        "distance_mode_analysis":
            get_distance_mode_analysis(),

        "top_routes":
            get_top_routes(),

        "disruption_by_weather":
            get_disruption_by_weather()
    }


@app.get("/api/dashboard/shipments")
def dashboard_shipments():

    return get_recent_shipments()


@app.get("/api/insights/weather_risks")
def insights_weather_risks():

    return {
        "top_weather_risks": get_top_weather_risks()
    }


@app.get("/api/insights/dataset")
def insights_dataset():

    return {
        "dataset_insights": get_dataset_insights()
    }


@app.get("/api/insights/disruption_classifier")
def insights_disruption_classifier():

    return {
        "disruption_classifier_insights":
            get_disruption_classifier_insights()
    }


@app.get("/api/insights/leadtime_regressor")
def insights_leadtime_regressor():

    return {
        "leadtime_regressor_insights":
            get_leadtime_regressor_insights()
    }

@app.get("/api/history")
def get_history(page: int = 1):

    data=get_prediction_history(page=page)

    return {
        "page": page,
        "page_size": len(data),
        "records": data
    }

@app.get("/api/report/{prediction_id}")
def get_report(prediction_id: int):

    record = get_prediction_by_id(prediction_id)

    if not record:
        return {"error": "Prediction not found"}

    pdf_buffer = generate_pdf_report(record)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            f"attachment; filename=SupplyPrescript_Report_{prediction_id}.pdf"
        }
    )