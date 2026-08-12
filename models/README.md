# Models

## Overview

This folder contains trained machine learning pipelines used by the FastAPI backend.

The models are serialized using Joblib and loaded during API execution.

## Files

### disruption_pipeline.pkl

Classification pipeline used to predict supply chain disruptions.

#### Outputs

- Disruption Prediction
- Risk Probability
- Risk Level

#### Performance

- Accuracy: 72.6%
- Precision: 75%
- Recall: 82%
- F1 Score: 79%

---

### leadtime_pipeline.pkl

Regression pipeline used to predict shipment lead time.

#### Outputs

- Predicted Lead Time
- Delay Category

#### Performance

- MAE: 0.977
- RMSE: 1.848
- R² Score: 0.996

## Usage

Loaded by the FastAPI application during prediction requests.

## Notes

Retrain models using the notebooks and replace these files when updating the system.