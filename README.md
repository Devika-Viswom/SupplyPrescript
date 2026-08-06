# SupplyPrescript
AI-powered Supply Chain Analytics Project

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

## Dataset Information

### Dataset Size

- Records: 5,000
- Features After Engineering: 87

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

- Missing value handling
- Duplicate checking
- Data consistency validation

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

- Origin_Port → Destination_Port

#### Risk Categories

- Low
- Medium
- High

#### Reliability Categories

- Low
- Medium
- High

#### Encodings

- One-Hot Encoding
- Label Encoding

---

## Machine Learning Models

### Model 1: Disruption Prediction

#### Objective

Predict whether a shipment will experience disruption.

#### Algorithms Evaluated

- Random Forest Classifier
- XGBoost Classifier

#### Final Model

Random Forest Classifier

#### Performance

| Metric | Score |
|----------|---------|
| Accuracy | 72.6% |
| Precision | 75% |
| Recall | 82% |
| F1 Score | 79% |

---

### Model 2: Lead Time Predictions

#### Objective

Predict shipment lead time.

#### Final Model

Random Forest Regressor

#### Performance

| Metric | Score |
|----------|---------|
| MAE | 0.98 |
| RMSE | 1.85 |
| R² Score | 0.996 |

---

## Key Business Insights

### Major Disruption Drivers

1. Hurricane Weather Conditions
2. Geopolitical Risk Score
3. Carrier Reliability Score
4. Shipment Distance

### Major Lead Time Drivers

1. Hurricane Weather
2. Distance
3. Sea Transport Mode

### Risk Trends

- Higher geopolitical risk increases disruption probability.
- Lower carrier reliability increases disruption likelihood.
- Extreme weather conditions significantly increase lead time.
- Sea transportation has the highest average lead time.

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

## API Services

### Prediction Endpoint

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

## Technology Stack

### Programming

- Python

### Backend

- FastAPI
- Uvicorn

### Machine Learning

- Scikit-Learn
- XGBoost
- Joblib

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn
- Plotly

### Dashboard

- Retool

### Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

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
uvicorn app:app --reload
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
