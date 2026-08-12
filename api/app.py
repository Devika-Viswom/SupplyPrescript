from fastapi import FastAPI
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from api.schemas import ShipmentInput

from api.prediction import predict_shipment

from api.dashboard import (
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
from api.insights import (
    get_business_insights,
    get_disruption_classifier_insights,
    get_leadtime_regressor_insights,
    get_recommendation_insights
)

from api.history_service import (
    get_prediction_history,
    get_prediction_by_id
)

from api.report import generate_pdf_report

app = FastAPI(title="SupplyPrescript API")

BASE_DIR = Path(__file__).resolve().parent.parent
frontend_dist = BASE_DIR / "frontend" / "dist"

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


@app.get("/api/insights/business")
def insights_business():

    return {
        "business_insights": get_business_insights()
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


@app.get("/api/insights/recommendations")
def insights_recommendations():

    return {
        "recommendation_insights":
            get_recommendation_insights()
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

if frontend_dist.exists():
    app.mount(
        "/assets",
        StaticFiles(directory=frontend_dist / "assets"),
        name="assets"
    )

    @app.get("/")
    async def serve_react():
        return FileResponse(frontend_dist / "index.html")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        if full_path.startswith("api"):
            return {"detail": "Not Found"}

        return FileResponse(frontend_dist / "index.html")