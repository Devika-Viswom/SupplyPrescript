# Processed Data

This folder contains cleaned, engineered, and model-ready datasets generated during the data preparation phase.

The datasets represent different stages of the machine learning pipeline.

---

## Dataset Lineage

`raw1.csv` → Feature Engineering → `df_model.pkl` → Feature Selection → `df_final.pkl` → Encoding → (`df_classification_encoded.pkl`, `df_regression_encoded.pkl`)

---

## Files

### df_model.pkl

Purpose:
Cleaned dataset with engineered business features.

Additional Features Created:

- Year
- Month
- Quarter
- Route
- Reliability_Level
- Risk_Level

Total Features:
20 columns

Usage:
Exploratory analysis and business intelligence.

---

### df_final.pkl

Purpose:
Final analytical dataset used before encoding.

Contains:
- Original shipment variables
- Engineered temporal features
- Route information
- Risk categories
- Reliability categories

Usage:
Base dataset for all model pipelines.

---

### df_classification_encoded.pkl

Purpose:
Machine learning dataset for disruption prediction.

Target:
Disruption_Occurred

Encoding:
One-hot encoding with drop_first=True.

Shape:
5000 rows × 87 columns

Used By:
Disruption Classification Model

Output:
Probability of shipment disruption.

---

### df_regression_encoded.pkl

Purpose:
Machine learning dataset for lead time prediction.

Target:
Lead_Time_Days

Encoding:
One-hot encoding with drop_first=True.

Shape:
5000 rows × 87 columns

Used By:
Lead Time Regression Model

Output:
Predicted shipment lead time.

---

## Feature Categories

Numerical Features:
- Distance_km
- Weight_MT
- Fuel_Price_Index
- Geopolitical_Risk_Score
- Carrier_Reliability_Score
- Year
- Month
- Quarter

Categorical Features:
- Transport_Mode
- Product_Category
- Weather_Condition
- Route
- Risk_Level
- Reliability_Level

Route Variations:
64 unique routes

Risk Levels:
3 categories

Reliability Levels:
3 categories