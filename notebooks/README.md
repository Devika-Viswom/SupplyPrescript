# Notebooks

This folder contains the complete analytical and machine learning workflow for the SupplyPrescript project.

The notebooks follow a structured pipeline beginning with raw data exploration and ending with production-ready machine learning models used by the FastAPI application.

Dataset Overview:

- Records: 5,000 shipments
- Time Period: January 2024 – December 2025
- Original Features: 14
- Engineered Features: 20
- Final Encoded Features: 87

---

## Notebook Workflow

### 1_data_understanding.ipynb

Purpose:
Perform initial exploration of the raw dataset and understand feature distributions.

Key Activities:
- Loaded raw shipment data
- Reviewed data types and structure
- Checked class balance
- Identified categorical feature cardinality

Dataset Characteristics:

| Metric | Value |
|----------|---------|
| Rows | 5,000 |
| Columns | 14 |
| Numeric Features | 7 |
| Categorical Features | 7 |
| Missing Values | 0 |

Target Distribution:

| Disruption Status | Count |
|-------------------|---------|
| Disrupted (1) | 3,063 |
| Not Disrupted (0) | 1,937 |

Categorical Feature Cardinality:

| Feature | Unique Values |
|----------|--------------|
| Origin_Port | 8 |
| Destination_Port | 9 |
| Transport_Mode | 4 |
| Product_Category | 5 |
| Weather_Condition | 5 |

---

### 2_data_cleaning.ipynb

Purpose:
Prepare data for analysis and model development.

Feature Engineering Performed:

Date Features:
- Year
- Month
- Quarter

Route Engineering:
- Origin_Port + Destination_Port

Reliability Categorization:

| Score Range | Category |
|------------|----------|
| < 0.65 | Low |
| 0.65 – 0.85 | Medium |
| > 0.85 | High |

Geopolitical Risk Categorization:

| Risk Score | Category |
|-----------|----------|
| 0 – 3 | Low |
| 3 – 7 | Medium |
| 7 – 10 | High |

Output:
- df_model.pkl

Result:
Dataset expanded from 14 features to 20 features.

---

### 3_eda.ipynb

Purpose:
Perform exploratory data analysis and identify operational patterns.

Key Findings:

#### Transport Mode vs Disruption Rate

| Mode | Disruption Rate |
|--------|--------------|
| Air | 61.74% |
| Rail | 61.18% |
| Road | 61.04% |
| Sea | 61.05% |

#### Weather vs Disruption Rate

| Weather | Disruption Rate |
|----------|---------------|
| Clear | 36.98% |
| Fog | 48.07% |
| Rain | 41.97% |
| Storm | 79.54% |
| Hurricane | 100.00% |

#### Average Lead Time by Weather

| Weather | Lead Time (Days) |
|----------|----------------|
| Clear | 6.70 |
| Rain | 7.74 |
| Fog | 9.89 |
| Storm | 19.30 |
| Hurricane | 53.50 |

#### Average Lead Time by Transport Mode

| Mode | Lead Time (Days) |
|--------|----------------|
| Air | 1.64 |
| Road | 16.45 |
| Rail | 19.95 |
| Sea | 39.80 |

Key Observation:
Weather conditions have a significantly stronger impact on lead time and disruption risk than transport mode.

---

### 4_feature_selection.ipynb

Purpose:
Prepare datasets for machine learning models.

Activities:
- Correlation analysis
- Categorical encoding
- Model-specific dataset creation

Important Correlations:

| Feature | Correlation with Disruption |
|----------|-------------------------|
| Lead_Time_Days | 0.265 |
| Geopolitical_Risk_Score | 0.225 |
| Carrier_Reliability_Score | -0.079 |

Categorical Encoding:

Features Encoded:
- Transport_Mode
- Product_Category
- Weather_Condition
- Route
- Risk_Level
- Reliability_Level

Generated Datasets:

| Dataset | Shape |
|----------|---------|
| df_classification_encoded.pkl | (5000, 87) |
| df_regression_encoded.pkl | (5000, 87) |

Outputs:
- df_final.pkl
- df_classification_encoded.pkl
- df_regression_encoded.pkl

---

### 5_disruption_classifier_model.ipynb

Purpose:
Develop disruption prediction model.

Model:
Random Forest Classifier

Performance:

| Metric | Value |
|----------|---------|
| Accuracy | 71.7% |
| Precision (Disruption) | 75% |
| Recall (Disruption) | 80% |
| F1 Score (Disruption) | 78% |

Most Important Predictors:

1. Weather_Condition_Hurricane
2. Geopolitical_Risk_Score
3. Carrier_Reliability_Score
4. Distance_km
5. Fuel_Price_Index

Risk Scoring:
Prediction probabilities converted into operational risk categories:

| Probability | Risk Level |
|-------------|------------|
| < 40% | Low |
| 40%-70% | Medium |
| > 70% | High |

Risk Distribution:

- Low Risk: 206
- Medium Risk: 431
- High Risk: 363

---

### 6_lead_days_regressor_model.ipynb

Purpose:
Predict shipment lead time.

Model:
Random Forest Regressor

Performance:

| Metric | Value |
|----------|---------|
| MAE | 0.954 |
| RMSE | 1.777 |
| R2 Score | 0.996 |

Most Important Predictors:

1. Weather_Condition_Hurricane
2. Distance_km
3. Transport_Mode_Sea
4. Transport_Mode_Road
5. Transport_Mode_Rail

---

### 7_business_analysis.ipynb

Purpose:
Convert analytical findings into operational business insights.

Key Business Findings:

#### Weather Impact

Hurricanes are the most critical disruption driver:

- 100% disruption occurrence
- Average lead time: 53.5 days

Storm conditions create substantial operational risk:

- 79.5% disruption rate
- Average lead time: 19.3 days

#### Geopolitical Risk Impact

Disruption likelihood increases with geopolitical risk:

| Risk Level | Disruption Rate |
|------------|----------------|
| Low | 47.69% |
| Medium | 61.71% |
| High | 73.67% |

#### Carrier Reliability Impact

Higher carrier reliability reduces disruption probability:

| Reliability Level | Disruption Rate |
|------------------|----------------|
| Low | 65.31% |
| Medium | 62.31% |
| High | 56.08% |

#### Transport Mode Analysis

Fastest:
- Air Transport (1.64 days)

Slowest:
- Sea Transport (39.80 days)

Strategic Insight:
Weather and geopolitical conditions have greater influence on disruptions than transport mode alone.

---

### 8_model_pipeline.ipynb

Purpose:
Create production-ready machine learning pipelines.

Pipeline Components:

1. One-Hot Encoding
2. Feature Transformation
3. Model Training
4. Serialization

Classifier:

RandomForestClassifier
- Trees: 500
- Max Depth: 15
- Min Samples Leaf: 5

Performance:
- Accuracy: 72.6%

Regression:

RandomForestRegressor
- Trees: 200

Performance:

| Metric | Value |
|----------|---------|
| MAE | 0.98 |
| RMSE | 1.85 |
| R² | 0.9962 |

Artifacts Produced:

- disruption_pipeline.pkl
- leadtime_pipeline.pkl

These models are used directly by the FastAPI prediction API.