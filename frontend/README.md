# Frontend

The frontend folder contains the React-based user interface for SupplyPrescript.

It provides an interactive platform for users to predict shipment risks, analyze supply chain performance, review historical predictions, and explore business insights through dashboards and visualizations.

---

## Technology Stack

### Core Framework

- React.js
- Vite

### Styling

- Tailwind CSS

### Routing

- React Router DOM

### API Communication

- Axios

### Data Visualization

- Recharts

---

## Folder Structure

```text
frontend/
│
├── public/
│
├── src/
│   ├── api/
│   │   └── api.js
│   │
│   ├── components/
│   │   ├── Navbar.jsx
│   │   └── PredictionResult.jsx
│   │
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   ├── Predict.jsx
│   │   ├── History.jsx
│   │   └── Insights.jsx
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── index.html
├── package.json
├── vite.config.js
└── README.md
```

---

## Application Pages

### Dashboard

Route:

```text
/
```

Purpose:

Provides a high-level overview of supply chain operations.

Features:

- KPI Cards
- Shipment Trends
- Risk Distribution
- Lead Time Analysis
- Weather Impact Analysis
- Transport Performance Metrics

---

### Predict

Route:

```text
/predict
```

Purpose:

Allows users to predict shipment disruptions and lead times.

Input Fields:

- Shipment Date
- Origin Port
- Destination Port
- Transport Mode
- Product Category
- Distance
- Weight
- Fuel Price Index
- Geopolitical Risk Score
- Weather Condition
- Carrier Reliability Score

Outputs:

- Risk Prediction
- Risk Probability
- Lead Time Prediction
- Delay Category
- Recommendations

---

### History

Route:

```text
/history
```

Purpose:

Displays previously generated predictions stored in the database.

Features:

- Historical Records
- Shipment Details
- Risk Analysis
- Prediction Tracking

---

### Insights

Route:

```text
/insights
```

Purpose:

Provides business and model performance insights.

Features:

- Dataset Statistics
- Classification Metrics
- Regression Metrics
- Feature Importance
- Business Recommendations

---

## Components

### Navbar.jsx

Provides application navigation.

Navigation Links:

- Dashboard
- Predict
- History
- Insights

---

### PredictionResult.jsx

Displays prediction outputs.

Shows:

- Risk Probability
- Risk Level
- Lead Time
- Delay Category
- Recommendations

---

## API Integration

### api/api.js

Centralized API service layer.

Communicates with:

```text
/api/predict
/api/dashboard/*
/api/insights/*
/api/history
```

Uses Axios for HTTP requests.

---

## User Workflow

```text
User
 │
 ▼
Dashboard
 │
 ▼
Prediction Form
 │
 ▼
API Request
 │
 ▼
Prediction Results
 │
 ▼
Database Storage
 │
 ▼
History & Insights
```

---

## Build & Run

### Install Dependencies

```bash
npm install
```

### Start Development Server

```bash
npm run dev
```

Application URL:

```text
http://localhost:5173
```

---

### Production Build

```bash
npm run build
```

Output Folder:

```text
dist/
```

---

## Purpose

The frontend serves as the presentation layer of SupplyPrescript, transforming complex machine learning outputs into intuitive dashboards, predictions, insights, and actionable supply chain intelligence.