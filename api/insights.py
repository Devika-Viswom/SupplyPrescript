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

df = pd.read_pickle("../data/df_final.pkl")

def get_insights():

    # ==========================
    # CLASSIFIER
    # ==========================

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

    # ==========================
    # REGRESSOR
    # ==========================

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

    # ==========================
    # DATASET INSIGHTS
    # ==========================

    disruption_rate = round(
        df["Disruption_Occurred"].mean() * 100,
        2
    )

    avg_lead_time = round(
        df["Lead_Time_Days"].mean(),
        2
    )

    total_shipments = len(df)

    # ==========================
    # TOP RISKS
    # ==========================

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

    # ==========================
    # RESPONSE
    # ==========================

    return {

        "dataset": {

            "total_shipments":
                total_shipments,

            "avg_lead_time":
                avg_lead_time,

            "disruption_rate":
                disruption_rate
        },

        "classifier": {

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
        },

        "regressor": {

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
        },

        "top_weather_risks":
            weather_risk.to_dict()
    }