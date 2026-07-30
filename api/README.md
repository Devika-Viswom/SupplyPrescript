# API

This folder contains the FastAPI backend for SupplyPrescript.

The API provides shipment risk prediction, lead time estimation, transport mode recommendations, dashboard analytics, insights, prediction history management, and PDF report generation.

---

## Architecture

Input Shipment Data → Prediction Engine → ML Models → Risk Assessment → Recommendations → Mode Comparison → History Storage → Dashboard / Insights / Reports

---

## Files

### app.py

Main FastAPI application.

Exposes all API endpoints:

#### Prediction
- POST `/predict`
  - Predict disruption risk
  - Predict lead time
  - Generate recommendations
  - Compare transport modes

#### Dashboard
- GET `/dashboard/summary`
- GET `/dashboard/charts`
- GET `/dashboard/shipments`

#### Insights
- GET `/insights/weather_risks`
- GET `/insights/dataset`
- GET `/insights/disruption_classifier`
- GET `/insights/leadtime_regressor`

#### History
- GET `/history`

#### Reports
- GET `/report/{prediction_id}`

---

### schemas.py

Defines request schemas using Pydantic.

#### ShipmentInput

Required shipment fields:

- shipment_date
- origin_port
- destination_port
- transport_mode
- product_category
- distance_km
- weight_mt
- fuel_price_index
- geopolitical_risk_score
- weather_condition
- carrier_reliability_score

---

### prediction.py

Core prediction engine.

Responsibilities:

- Build model input features
- Generate disruption predictions
- Generate lead time predictions
- Calculate confidence scores
- Compare transport modes
- Estimate shipping costs
- Select recommended transport mode
- Save prediction history

Uses:
- disruption_pipeline.pkl
- leadtime_pipeline.pkl

---

### recommendation_engine.py

Generates prescriptive recommendations.

Calculates:

#### Risk Levels

| Probability | Level |
|------------|---------|
| < 40% | Low |
| 40–70% | Medium |
| 70–95% | High |
| > 95% | Critical |

#### Delay Categories

| Lead Time | Category |
|------------|------------|
| < 8 Days | Short |
| 8–21 Days | Moderate |
| 21–40 Days | Long |
| > 40 Days | Severe |

Produces operational recommendations based on:

- Weather conditions
- Geopolitical risk
- Carrier reliability
- Lead time
- Transport mode

---

### dashboard.py

Provides dashboard analytics from the processed dataset.

Available Metrics:

#### Summary KPIs
- Total Shipments
- Average Lead Time
- Disruption Rate
- Average Risk Score

#### Charts
- Lead Time by Transport Mode
- Disruption Rate by Weather
- Monthly Shipment Volume
- Route Distribution

#### Tables
- Recent Shipments

---

### insights.py

Provides analytical and model-performance insights.

Available Insights:

#### Dataset Insights
- Total shipments
- Average lead time
- Disruption rate

#### Weather Risk Analysis
- Disruption percentage by weather condition

#### Disruption Model Metrics
- Accuracy
- Precision
- Recall
- F1 Score

#### Lead Time Model Metrics
- MAE
- RMSE
- R² Score

---

### db.py

Database connection module.

Database:
- PostgreSQL

Responsibilities:
- Load environment variables
- Establish database connection
- Manage prediction history storage

Table:
- prediction_history

---

### history.py

Stores prediction results.

Responsibilities:

- Save shipment inputs
- Save prediction outputs
- Save recommendations
- Save transport comparisons

Target Table:
- prediction_history

---

### history_service.py

Retrieves prediction history from the database.

Features:

- Paginated history retrieval
- Fetch prediction by ID
- Return full prediction details

Default Page Size:
- 50 records

---

### report.py

Generates PDF reports for saved predictions.

Report Sections:

1. Shipment Information
2. Risk Assessment
3. Lead Time Analysis
4. Recommendations
5. Transport Mode Comparison
6. Mode Recommendation

Output:
- Downloadable PDF report

---

## Dependencies

Key Libraries:

- FastAPI
- Pydantic
- Pandas
- Scikit-Learn
- Joblib
- PostgreSQL (psycopg2)
- ReportLab

---

## API Purpose

The API serves as the operational layer of SupplyPrescript by transforming shipment information into actionable supply chain decisions through machine learning predictions, risk analysis, transport recommendations, and reporting.