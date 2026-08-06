import pandas as pd
import numpy as np
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

BASE_DIR = Path(__file__).resolve().parent

clf_model = joblib.load(BASE_DIR.parent / "models" / "disruption_pipeline.pkl")

reg_model = joblib.load(BASE_DIR.parent / "models" / "leadtime_pipeline.pkl")

df = pd.read_pickle(BASE_DIR.parent / "data" / "processed" / "df_final.pkl")

def get_business_insights():

    weather = (
        df.groupby("Weather_Condition")
        ["Disruption_Occurred"]
        .mean()
        .mul(100)
        .idxmax()
    )

    mode = (
        df.groupby("Transport_Mode")
        ["Lead_Time_Days"]
        .mean()
        .idxmax()
    )

    best_mode = (
        df.groupby("Transport_Mode")
        ["Lead_Time_Days"]
        .mean()
        .idxmin()
    )

    return [
        f"{weather} weather causes the highest disruption risk.",
        f"{mode} transport has the longest average lead time.",
        f"{best_mode} transport has the shortest average lead time.",
        "Carrier reliability significantly impacts disruptions."
    ]


def get_disruption_classifier_insights():

    X_clf = df.drop(
        [
            "Disruption_Occurred",
            "Lead_Time_Days"
        ],
        axis=1
    )

    y_clf = df["Disruption_Occurred"]

    X_train,X_test,y_train,y_test = train_test_split(
        X_clf,
        y_clf,
        test_size=0.20,
        random_state=42
    )

    y_pred = clf_model.predict(X_test)

    probs = clf_model.predict_proba(X_test)[:, 1]

    confidence = (probs.max() * 100).round(2)

    bins = pd.cut(
        confidence,
        bins=[0, 70, 80, 90, 100],
        labels=["0-70", "70-80", "80-90", "90-100"]
    )

    tn, fp, fn, tp = confusion_matrix(
        y_test,
        y_pred
    ).ravel()

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    precision = precision_score(
        y_test,
        y_pred
    )

    recall = recall_score(
        y_test,
        y_pred
    )

    f1 = f1_score(
        y_test,
        y_pred
    )

    feature_importance = pd.DataFrame({
        "Feature": X_train.columns,
        "Importance": clf_model.named_steps["model"].feature_importances_
    })
    
    feature_importance = feature_importance.sort_values(
        by="Importance",
        ascending=False
    )
    
    feature_importance = feature_importance.head(10)
    
    feature_importance["Importance"] = (
        feature_importance["Importance"] * 100
    ).round(2)

    return {

        "model":
            type(
                clf_model.named_steps["model"]
            ).__name__,

        "accuracy":
            round(
                accuracy * 100,
                2
            ),

        "precision":
            round(
                precision * 100,
                2
            ),

        "recall":
            round(
                recall * 100,
                2
            ),

        "f1_score":
            round(
                f1 * 100,
                2
            ),

        "confusion_matrix":
            {
                "true_negatives": int(tn),
                "false_positives": int(fp),
                "false_negatives": int(fn),
                "true_positives": int(tp)
            },

        "confidence_distribution":
            (
                pd.Series(bins)
                    .value_counts()
                    .sort_index()
                    .to_dict()
            ),

        "top_features":
            feature_importance.to_dict(
                orient="records"
            )
    }


def get_leadtime_regressor_insights():

    X_reg = df.drop(
        [
            "Lead_Time_Days",
            "Disruption_Occurred"
        ],
        axis=1
    )

    y_reg = df["Lead_Time_Days"]

    X_train_r,X_test_r,y_train_r,y_test_r = train_test_split(
        X_reg,
        y_reg,
        test_size=0.20,
        random_state=42
    )

    lead_pred = reg_model.predict(
        X_test_r
    )

    mae = mean_absolute_error(
        y_test_r,
        lead_pred
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test_r,
            lead_pred
        )
    )

    r2 = r2_score(
        y_test_r,
        lead_pred
    )

    feature_importance = pd.DataFrame({
        "Feature": X_train_r.columns,
        "Importance": reg_model.named_steps["model"].feature_importances_
    })

    feature_importance = feature_importance.sort_values(
        by="Importance",
        ascending=False
    )

    feature_importance = feature_importance.head(10)

    feature_importance["Importance"] = (
        feature_importance["Importance"] * 100
    ).round(2)

    return {

        "model":
            type(
                reg_model.named_steps["model"]
            ).__name__,

        "mae":
            round(
                mae,
                3
            ),

        "rmse":
            round(
                rmse,
                3
            ),

        "r2":
            round(
                r2,
                4
            ),

        "top_features":
            feature_importance.to_dict(
                orient="records"
            )
    }


def get_recommendation_insights():

    recommendations = [
        "Use Air transport for high-priority shipments.",
        "Avoid Sea transport during severe weather conditions.",
        "Prefer high reliability carriers for long routes.",
        "Monitor geopolitical risk scores above 7 carefully.",
        "Consider alternate routes when disruption probability is high."
    ]

    return recommendations