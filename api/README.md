# API

## Overview

This folder contains the FastAPI backend powering the SupplyPrescript application.

The API handles:

- Input validation
- Feature preparation
- Prediction generation
- Recommendation generation
- Dashboard data services

---

## Files

### app.py

Main prediction API.

Responsibilities:

- Load models
- Receive requests
- Generate predictions
- Return recommendations

---

### schemas.py

Pydantic request schemas.

Responsibilities:

- Input validation
- Data type enforcement

---

### recommendation_engine.py

Business rule engine.

Responsibilities:

- Generate mitigation strategies
- Create actionable recommendations

---

### dashboard.py

Dashboard data provider.

Responsibilities:

- KPI calculations
- Summary statistics
- Dashboard visualizations

---

### insights.py

Insights generation module.

Responsibilities:

- Model insights
- Feature importance reporting
- Dataset statistics

---

## Main Endpoint

### POST /predict

Returns:

- Disruption Prediction
- Risk Probability
- Risk Level
- Predicted Lead Time
- Delay Category
- Recommendations

---

## Run API

```bash
cd .\api\
python -m uvicorn app:app --reload