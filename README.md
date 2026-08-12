## Commands before starting of work 
git pull origin main

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

## Before daily work
git pull origin main

`if any modification in dependencies`

pip install -r requirements.txt

## After Installing/deleting any dependency
pip freeze > requirements.txt

## For undo back to last commit
git restore .

## After important modification
git add .

git commit -m "message"

git push origin main

---

# SupplyPrescript: AI-Powered Supply Chain Risk Prediction & Prescriptive Analytics

## Project Overview

SupplyPrescript is an end-to-end AI-powered Supply Chain Analytics platform designed to predict shipment disruptions, estimate delivery lead times, and generate actionable recommendations to support operational decision-making.

The project combines Machine Learning, Business Analytics, FastAPI, and Dashboarding to help organizations proactively manage supply chain risks caused by weather conditions, geopolitical instability, carrier reliability issues, and transportation delays.

By transforming raw logistics data into predictive insights and prescriptive actions, SupplyPrescript enables more resilient and efficient supply chain operations.

---

## Problem Statement

Supply chains face frequent disruptions due to:

- Extreme weather events
- Geopolitical conflicts
- Unreliable carriers
- Transportation delays
- Increasing fuel costs

Traditional systems often react after disruptions occur.

SupplyPrescript helps organizations:

✅ Predict disruptions before they occur

✅ Estimate shipment lead times

✅ Identify major risk drivers

✅ Generate mitigation strategies

✅ Improve operational planning

---

## Key Features

### 1. Disruption Risk Prediction

Predicts whether a shipment is likely to experience a disruption.

**Outputs**

- Disruption Prediction (Yes/No)
- Risk Probability (%)
- Risk Level (Low / Medium / High)

---

### 2. Lead Time Forecasting

Estimates expected shipment delivery duration.

**Outputs**

- Predicted Lead Time (Days)
- Delay Category
  - On Time
  - Moderate Delay
  - Severe Delay

---

### 3. Prescriptive Recommendation Engine

Generates business recommendations based on shipment characteristics and model predictions.

Examples:

- Use alternative carrier
- Switch transport mode
- Increase safety stock
- Monitor weather risks
- Monitor geopolitical risks
- Re-route shipments

---

### 4. Business Analytics Dashboard

Interactive dashboard for supply chain monitoring and analysis.

Dashboard Modules:

- Dashboard Page
- Analyze Page
- Insights Page

Capabilities:

- KPI Monitoring
- Prediction Interface
- Model Insights
- Risk Analysis
- Performance Tracking
- Shipment Analytics

---

## System Architecture

```text
                    User Input
                         │
                         ▼
                FastAPI Backend
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
      ▼                  ▼                  ▼
Disruption Model   Lead Time Model   Recommendation Engine
      │                  │                  │
      └──────────────────┼──────────────────┘
                         ▼
                 Dashboard Services
                         │
                         ▼
                  Retool Dashboard
                         │
                         ▼
                Business Decisions
```

---

## Project Structure

```text
SupplyPrescript
│
├── api/
│   ├── app.py
│   ├── prediction.py
│   ├── dashboard.py
│   ├── insights.py
│   ├── history.py
│   ├── history_service.py
│   ├── recommendation_engine.py
│   ├── report.py
│   ├── schemas.py
│   └── db.py
│
├── data/
│   ├── raw/
│   │   └── raw1.csv
│   │
│   └── processed/
│       ├── df_model.pkl
│       ├── df_final.pkl
│       ├── df_classification_encoded.pkl
│       └── df_regression_encoded.pkl
│
├── models/
│   ├── disruption_pipeline.pkl
│   └── leadtime_pipeline.pkl
│
├── notebooks/
│   ├── 1_data_understanding.ipynb
│   ├── 2_data_cleaning.ipynb
│   ├── 3_eda.ipynb
│   ├── 4_feature_selection.ipynb
│   ├── 5_disruption_classifier_model.ipynb
│   ├── 6_lead_days_regressor_model.ipynb
│   ├── 7_business_analysis.ipynb
│   └── 8_model_pipeline.ipynb
│
├── requirements.txt
│
└── README.md
```

---

### Dataset Information

### Dataset Size

- Records: 5,000 shipments
- Original Features: 14
- Engineered Features: 16
- Encoded Features: 87
- Date Range: 2024-01-01 to 2025-12-31

### Original Features

| Feature |
|----------|
| Shipment_ID |
| Date |
| Origin_Port |
| Destination_Port |
| Transport_Mode |
| Product_Category |
| Distance_km |
| Weight_MT |
| Fuel_Price_Index |
| Geopolitical_Risk_Score |
| Weather_Condition |
| Carrier_Reliability_Score |
| Lead_Time_Days |
| Disruption_Occurred |

---

## Data Processing Pipeline

### Data Understanding

- Dataset exploration
- Data type validation
- Statistical summaries

### Data Cleaning

- Date conversion and parsing
- Temporal feature generation (Year, Month, Quarter)
- Route creation (Origin → Destination)
- Risk categorization
- Carrier reliability categorization

### Exploratory Data Analysis

- Univariate Analysis
- Bivariate Analysis
- Correlation Analysis
- Trend Analysis

### Feature Engineering

Generated Features:

#### Date Features

- Year
- Month
- Quarter

#### Route Features

- Routes = Origin_Port → Destination_Port
- 64 Unique Routes

#### Risk Categories

- Low (0–3)
- Medium (3–7)
- High (7–10)

#### Reliability Categories

- Low (<0.65)
- Medium (0.65–0.85)
- High (>0.85)

#### Encodings

- One-Hot Encoding
- Label Encoding

---

## Machine Learning Models

### Model 1: Disruption Prediction

#### Objective

Predict whether a shipment will experience disruption.

##### Algorithms Evaluated

- Random Forest Classifier
- XGBoost Classifier

#### Final Production Model

##### Pipeline:

- OneHotEncoder
- ColumnTransformer
- RandomForestClassifier

##### Hyperparameters:

- n_estimators = 500
- max_depth = 15
- min_samples_leaf = 5

#### Performance

| Metric | Score |
|----------|---------|
| Accuracy | 72.6% |
| Precision | 75% |
| Recall | 82% |
| F1 Score | 79% |

---

### Model 2: Lead Time Prediction

#### Objective

Predict shipment lead time.

#### Final Model

##### Pipeline:

- OneHotEncoder
- ColumnTransformer
- RandomForestRegressor

##### Hyperparameters:

- n_estimators = 200

#### Performance

| Metric | Score |
|----------|---------|
| MAE | 0.98 |
| RMSE | 1.85 |
| R² Score | 0.996 |

---

## Key Business Insights

### Disruption Rate by Weather Condition

| Weather Condition | Disruption Rate |
|------------------|----------------|
| Hurricane | 100.00% |
| Storm | 79.54% |
| Fog | 48.07% |
| Rain | 41.97% |
| Clear | 36.98% |

### Average Lead Time by Weather Condition

| Weather Condition | Average Lead Time (Days) |
|------------------|--------------------------|
| Hurricane | 53.50 |
| Storm | 19.30 |
| Fog | 9.89 |
| Rain | 7.74 |
| Clear | 6.70 |

### Average Lead Time by Transport Mode

| Transport Mode | Average Lead Time (Days) |
|---------------|--------------------------|
| Air | 1.64 |
| Road | 16.45 |
| Rail | 19.95 |
| Sea | 39.80 |

### Disruption Rate by Geopolitical Risk Level

| Risk Level | Disruption Rate |
|-----------|----------------|
| Low | 47.69% |
| Medium | 61.71% |
| High | 73.67% |

### Disruption Rate by Carrier Reliability

| Reliability Level | Disruption Rate |
|------------------|----------------|
| High | 56.08% |
| Medium | 62.31% |
| Low | 65.31% |

### Key Findings

- Hurricane conditions resulted in a 100% disruption rate and the highest average lead time of 53.5 days.
- Storm conditions increased disruption probability to nearly 80%.
- Sea transport recorded the highest average lead time (39.8 days), while Air transport was the fastest (1.64 days).
- Higher geopolitical risk scores were associated with substantially higher disruption rates.
- Shipments handled by lower reliability carriers experienced more disruptions than those managed by highly reliable carriers.

---

## Notebook Workflow

| Notebook | Purpose |
|-----------|----------|
| 1_data_understanding | Dataset exploration |
| 2_data_cleaning | Data preprocessing |
| 3_eda | Exploratory analysis |
| 4_feature_selection | Feature engineering |
| 5_disruption_classifier_model | Classification model |
| 6_lead_days_regressor_model | Regression model |
| 7_business_analysis | Business insights |
| 8_model_pipeline | Final pipeline creation |

---

## API Endpoints


### Prediction

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/predict` | Predict disruption risk, lead time, recommendations, and transport mode comparison |

### Dashboard

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/dashboard/summary` | Dashboard KPI summary |
| GET | `/dashboard/charts` | Chart data for dashboard visualizations |
| GET | `/dashboard/shipments` | Latest 50 shipment records |

### Insights

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/insights/weather_risks` | Weather-related disruption analysis |
| GET | `/insights/dataset` | Dataset summary statistics |
| GET | `/insights/disruption_classifier` | Classification model metrics |
| GET | `/insights/leadtime_regressor` | Regression model metrics |

### History & Reports

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/history?page=1` | Paginated prediction history |
| GET | `/report/{prediction_id}` | Generate PDF report for a prediction |

---

## Prediction Endpoint

```http
POST /predict
```

### Input

```json
{
  "shipment_date": "2025-07-20",
  "origin_port": "Mumbai",
  "destination_port": "Singapore",
  "transport_mode": "Sea",
  "product_category": "Electronics",
  "distance_km": 5000,
  "weight_mt": 20,
  "fuel_price_index": 110,
  "geopolitical_risk_score": 6.5,
  "weather_condition": "Storm",
  "carrier_reliability_score": 0.75
}
```

### Output

```json
{
  "disruption_prediction": 1,
  "risk_probability": 78.5,
  "risk_level": "High",
  "predicted_lead_time": 42.3,
  "delay_category": "Severe Delay",
  "recommendations": [
    "Use alternate carrier",
    "Increase safety stock",
    "Monitor weather conditions"
  ]
}
```

---

## Dashboard Components

### Dashboard Page

Provides:

- Total Shipments
- Average Lead Time
- Disruption Statistics
- Shipment Trends
- Weather Analysis

### Analyze Page

Allows users to:

- Enter shipment details
- Generate predictions
- View risk scores
- Receive recommendations

### Insights Page

Displays:

- Model Information
- Dataset Information
- Feature Importance
- Performance Metrics
- Business Insights

---

## Prediction History

All shipment predictions generated through the API are automatically stored in PostgreSQL for auditability and future analysis.

Stored Information:

- Shipment details
- Risk prediction results
- Lead time predictions
- Confidence score
- Generated recommendations
- Transport mode comparison
- Recommended transport strategy

Features:

- Paginated history retrieval
- Historical shipment analysis
- Report generation from saved predictions
- Persistent storage of prediction outcomes

Endpoint:

```http
GET /history?page=1
```

---

## Transport Mode Comparison Engine

For every shipment request, SupplyPrescript evaluates all available transport modes:

- Air
- Road
- Rail
- Sea

For each mode, the system predicts:

- Disruption Risk Probability
- Lead Time
- Estimated Transportation Cost

A weighted scoring model is used to determine the optimal transport strategy.

Scoring Weights:

| Factor | Weight |
|----------|---------|
| Lead Time | 45% |
| Cost | 30% |
| Risk Probability | 25% |

Outputs:

- Recommended Transport Mode
- Fastest Mode
- Cheapest Mode
- Lowest Risk Mode
- Recommendation Explanation

This enables users to compare transportation options and make data-driven logistics decisions.

---

## Automated PDF Reporting

SupplyPrescript can generate professional PDF reports for previously saved shipment predictions.

Report Contents:

- Shipment Information
- Risk Assessment
- Lead Time Analysis
- AI Recommendations
- Transport Mode Comparison
- Recommended Transport Strategy

Benefits:

- Easy sharing with stakeholders
- Operational documentation
- Decision support records
- Historical shipment reporting

Endpoint:

```http
GET /report/{prediction_id}
```

---

## Technology Stack

### Programming

- Python

### Backend

- FastAPI
- Uvicorn

### Machine Learning

- Scikit-Learn
- Random Forest Classifier
- Random Forest Regressor
- Joblib

### Data Processing

- Pandas
- NumPy

### Visualization & Analysis

- Matplotlib
- Seaborn

### Dashboard

- Retool

### Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

### Database

- PostgreSQL

### Reporting

- ReportLab

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/SupplyPrescript.git
cd SupplyPrescript
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

```bash
cd api
uvicorn app:app
```

API Documentation:

```text
http://localhost:8000/docs
```

---

## Business Value

SupplyPrescript helps organizations:

- Reduce supply chain risk
- Improve shipment planning
- Increase delivery reliability
- Enhance operational visibility
- Support proactive decision-making
- Improve customer satisfaction

---

## Future Enhancements

- Real-Time Weather API Integration
- Live Geopolitical Risk Monitoring
- Cost Optimization Engine
- Supplier Risk Assessment
- Route Optimization
- Explainable AI (SHAP)
- Real-Time Dashboard Updates
- Cloud Deployment (AWS/Azure)
