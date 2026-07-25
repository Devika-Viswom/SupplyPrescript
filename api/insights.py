import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

clf_model = joblib.load("../models/disruption_pipeline.pkl")

reg_model = joblib.load("../models/leadtime_pipeline.pkl")

df = pd.read_pickle("../data/processed/df_final.pkl")

def get_top_weather_risks():

    weather_risk = (
        df.groupby(
            "Weather_Condition"
        )["Disruption_Occurred"]
        .mean()
        .sort_values(
            ascending=False
        )
        * 100
    ).round(2)

    return weather_risk.to_dict()

def get_dataset_insights():

    disruption_rate = round(
        df["Disruption_Occurred"].mean() * 100,
        2
    )

    avg_lead_time = round(
        df["Lead_Time_Days"].mean(),
        2
    )

    total_shipments = len(df)

    return {

        "total_shipments":
            total_shipments,

        "avg_lead_time":
            avg_lead_time,

        "disruption_rate":
            disruption_rate
    }

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
            )
    }