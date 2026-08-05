import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR.parent / "data" / "processed" / "df_model.pkl"

df = pd.read_pickle(DB_PATH)

def get_summary():

    return {
        "total_shipments": int(len(df)),
        "avg_lead_time": round(
            df["Lead_Time_Days"].mean(),
            2
        ),
        "disruption_rate": round(
            df["Disruption_Occurred"].mean(),
            4
        ),
        "avg_risk_score": round(
            df["Geopolitical_Risk_Score"].mean(),
            2
        ),
        "high_risk_shipments": int(
            len(
                df[
                    df["Risk_Level"] == "High"
                ]
            )
        ),
        "avg_reliability_score": round(
            df["Carrier_Reliability_Score"].mean(),
            2
        )
    }


def get_monthly_disruptions():

    monthly = (
        df.groupby(
            ["Year", "Month"]
        )['Disruption_Occurred']
        .sum()
        .reset_index()
    )

    monthly["Period"] = (
        monthly["Year"].astype(str)
        + "-"
        + monthly["Month"].astype(str)
    )

    return monthly[
        ["Period", "Disruption_Occurred"]
    ].to_dict(orient="records")


def get_monthly_leadtime():

    monthly = (
        df.groupby(
            ["Year", "Month"]
        )["Lead_Time_Days"]
        .mean()
        .round(2)
        .reset_index()
    )

    monthly["Period"] = (
        monthly["Year"].astype(str)
        + "-"
        + monthly["Month"].astype(str)
    )

    return monthly[
        ["Period", "Lead_Time_Days"]
    ].to_dict(orient="records")


def get_riskiest_routes():

    routes = (
        df.groupby("Route")
        ["Disruption_Occurred"]
        .mean()
        .reset_index()
    )

    routes["Risk"] = (
        routes["Disruption_Occurred"]
        * 100
    )

    routes = routes.sort_values(
        "Risk",
        ascending=False
    ).head(10)

    return routes[
        ["Route", "Risk"]
    ].to_dict(orient="records")


def get_risk_distribution():

    result = (
        df["Risk_Level"]
        .value_counts()
        .reset_index()
    )

    result.columns = [
        "Risk_Level",
        "Count"
    ]

    return result.to_dict(
        orient="records"
    )


def get_reliability_distribution():

    result = (
        df["Reliability_Level"]
        .value_counts()
        .reset_index()
    )

    result.columns = [
        "Reliability_Level",
        "Count"
    ]

    return result.to_dict(
        orient="records"
    )


def get_leadtime_by_weather():

    result = (
        df.groupby(
            "Weather_Condition"
        )["Lead_Time_Days"]
        .mean()
        .round(2)
        .reset_index()
    )

    result = result.sort_values(
        "Lead_Time_Days",
        ascending=False
    )

    return result.to_dict(
        orient="records"
    )


def get_distance_mode_analysis():

    df["Distance_Range"] = pd.cut(
        df["Distance_km"],
        bins=[0, 4000, 7000, 10000, 20000],
        labels=[
            "Short",
            "Medium",
            "Long",
            "Very Long"
        ]
    )

    result = (
        df.groupby(
            ["Distance_Range", "Transport_Mode"]
        )["Lead_Time_Days"]
        .mean()
        .round(2)
        .reset_index()
    )

    pivot = (
        result.pivot(
            index="Distance_Range",
            columns="Transport_Mode",
            values="Lead_Time_Days"
        )
        .reset_index()
        .fillna(0)
    )

    return pivot.to_dict(orient="records")


def get_top_routes():

    routes = (
        df["Route"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    routes.columns = [
        "Route",
        "Shipments"
    ]

    return routes.to_dict(
        orient="records"
    )


def get_disruption_by_weather():

    result = (
        df.groupby("Weather_Condition")
        ["Disruption_Occurred"]
        .mean()
        .round(2)
        .reset_index()
    )

    result["Disruption_Occurred"] *= 100

    result = result.sort_values(
        "Disruption_Occurred",
        ascending=False
    )

    return result.to_dict(orient="records")


def get_recent_shipments():

    cols = [
        "Date",
        "Origin_Port",
        "Destination_Port",
        "Transport_Mode",
        "Lead_Time_Days",
        "Disruption_Occurred"
    ]

    recent = (
        df[cols]
        .sort_values(
            "Date",
            ascending=False
        )
        .head(20)
    )

    return recent.to_dict(
        orient="records"
    )