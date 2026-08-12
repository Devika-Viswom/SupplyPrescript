# API

The API folder contains the FastAPI backend for SupplyPrescript.

It serves as the core processing layer of the application, handling shipment predictions, recommendation generation, dashboard analytics, historical records, business insights, and report generation.

---

## Backend Architecture

```text
Frontend (React)
        │
        ▼
 FastAPI Backend
        │
 ┌──────┼──────┐
 │      │      │
 ▼      ▼      ▼
Prediction Dashboard History
 Engine    APIs    APIs
 │
 ▼
ML Models
 │
 ▼
Recommendation Engine
 │
 ▼
PostgreSQL Database
 │
 ▼
Reports & Insights
```

---

## Folder Contents

```text
api/
│
├── app.py
├── prediction.py
├── dashboard.py
├── insights.py
├── history.py
├── history_service.py
├── recommendation_engine.py
├── report.py
├── schemas.py
└── connection.py
```

---

## Core Components

### app.py

Main FastAPI application.

Responsibilities:

- API routing
- Request validation
- Response generation
- CORS configuration
- Service integration

### Available Endpoints

#### Prediction

| Method | Endpoint |
|----------|----------|
| POST | `/api/predict` |

Returns:

- Disruption Prediction
- Risk Probability
- Risk Level
- Predicted Lead Time
- Delay Category
- Recommendations

---

#### Dashboard

| Method | Endpoint |
|----------|----------|
| GET | `/api/dashboard/kpi` |
| GET | `/api/dashboard/charts` |
| GET | `/api/dashboard/shipments` |

Provides:

- KPI metrics
- Chart visualizations
- Recent shipment records

---

#### Insights

| Method | Endpoint |
|----------|----------|
| GET | `/api/insights/dataset` |
| GET | `/api/insights/disruption_classifier` |
| GET | `/api/insights/leadtime_regressor` |
| GET | `/api/insights/feature_importance` |
| GET | `/api/insights/business_insights` |

Provides:

- Dataset statistics
- Model evaluation metrics
- Feature importance analysis
- Business recommendations

---

#### History

| Method | Endpoint |
|----------|----------|
| GET | `/api/history` |

Provides:

- Historical predictions
- Shipment details
- Risk assessments

---

#### Reports

| Method | Endpoint |
|----------|----------|
| GET | `/api/report/{prediction_id}` |

Generates:

- Downloadable PDF reports

---

## schemas.py

Contains all Pydantic request and response schemas.

### ShipmentInput

Validates incoming shipment information.

Required Fields:

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

Purpose:

- Input validation
- Type checking
- API documentation generation

---

## prediction.py

Core machine learning inference engine.

Responsibilities:

- Feature preparation
- Input transformation
- Classification prediction
- Regression prediction
- Risk probability calculation
- Lead time estimation
- Recommendation integration
- Prediction history storage

Models Used:

### Classification Model

```text
models/disruption_pipeline.pkl
```

Predicts:

- Shipment Disruption
- Risk Probability

---

### Regression Model

```text
models/leadtime_pipeline.pkl
```

Predicts:

- Lead Time (Days)

---

### Outputs

Returns:

- disruption_prediction
- risk_probability
- risk_level
- predicted_lead_time
- delay_category
- recommendations

---

## recommendation_engine.py

Generates actionable supply chain recommendations based on prediction outcomes.

### Risk Levels

| Probability | Risk Level |
|------------|------------|
| 0 – 40% | Low |
| 40 – 70% | Medium |
| 70 – 90% | High |
| > 90% | Critical |

---

### Delay Categories

| Lead Time | Category |
|------------|------------|
| < 8 Days | Short |
| 8 – 21 Days | Moderate |
| 21 – 40 Days | Long |
| > 40 Days | Severe |

---

### Recommendation Factors

Recommendations are generated using:

- Weather Conditions
- Geopolitical Risk
- Carrier Reliability
- Predicted Lead Time
- Risk Probability
- Transport Mode

Example Recommendations:

- Select alternative carriers
- Increase safety stock
- Add delivery buffer
- Avoid severe weather routes
- Review high-risk regions

---

## dashboard.py

Provides dashboard metrics and chart data.

Data Source:

```text
data/processed/df_model.pkl
```

---

### KPI Metrics

Returns:

- Total Shipments
- Average Lead Time
- Disruption Rate
- Average Risk Score
- High Risk Shipments
- Average Reliability Score

---

### Dashboard Charts

Provides:

#### Shipment Trends

- Monthly Shipment Volume

#### Lead Time Analysis

- Average Lead Time by Transport Mode

#### Risk Analysis

- Risk Distribution

#### Weather Analysis

- Weather Impact on Disruptions

#### Transport Analysis

- Transport Mode Performance

---

### Shipment Records

Provides:

- Recent shipment history
- Latest operational records

---

## insights.py

Provides analytical and model evaluation insights.

### Dataset Insights

Returns:

- Dataset size
- Feature count
- Date range
- Lead time statistics
- Disruption statistics

---

### Disruption Classifier Insights

Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

---

### Lead Time Regressor Insights

Metrics:

- MAE
- RMSE
- R² Score

---

### Feature Importance

Returns:

- Most influential disruption factors
- Most influential lead time factors

Examples:

- Weather Condition
- Distance
- Geopolitical Risk Score
- Carrier Reliability Score

---

### Business Insights

Provides:

- Operational findings
- Risk observations
- Logistics recommendations

---

## connection.py

Database connection module.

Database:

```text
PostgreSQL (Supabase)
```

Responsibilities:

- Load environment variables
- Establish database connection
- Execute database operations

Environment Variable:

```env
DATABASE_URL=
```

---

## history.py

Stores prediction records in PostgreSQL.

Stored Information:

### Shipment Inputs

- Route Details
- Shipment Characteristics

### Prediction Outputs

- Risk Probability
- Lead Time Prediction
- Risk Level

### Recommendations

- Generated Actions

Purpose:

- Historical tracking
- Auditability
- Reporting

---

## history_service.py

Retrieves prediction history from the database.

Features:

- Fetch prediction history
- Pagination support
- Record retrieval
- Historical analysis

---

## report.py

Generates PDF reports using ReportLab.

### Report Sections

1. Shipment Information
2. Risk Assessment
3. Lead Time Prediction
4. Delay Category
5. Recommendations

Output:

- PDF Document
- Downloadable Report

---

## Dependencies

Major Backend Libraries

### API Framework

- FastAPI
- Uvicorn
- Pydantic

### Machine Learning

- Scikit-Learn
- XGBoost
- Joblib

### Data Processing

- Pandas
- NumPy

### Database

- PostgreSQL
- psycopg2

### Reporting

- ReportLab

---

## API Workflow

```text
User Input
     │
     ▼
Request Validation
     │
     ▼
Feature Engineering
     │
     ▼
ML Models
     │
     ▼
Risk Assessment
     │
     ▼
Recommendation Engine
     │
     ▼
Database Storage
     │
     ▼
Response Returned
```

---

## Purpose

The API transforms shipment information into actionable logistics intelligence through machine learning predictions, operational recommendations, historical tracking, business analytics, and reporting.