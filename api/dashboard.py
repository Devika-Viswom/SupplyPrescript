import pandas as pd

df = pd.read_pickle("../data/processed/df_model.pkl")

def get_summary():

    return {
        "total_shipments": int(len(df)),
        "avg_lead_time": round(df["Lead_Time_Days"].mean(), 2),
        "disruption_rate": round(
            df["Disruption_Occurred"].mean(),
            4
        ),
        "avg_risk_score": round(
            df["Geopolitical_Risk_Score"].mean(),
            2
        )
    }


def get_leadtime_by_mode():

    result = (
        df.groupby("Transport_Mode")
        ["Lead_Time_Days"]
        .mean()
        .reset_index()
    )

    return result.to_dict(orient="records")


def get_disruption_by_weather():

    result = (
        df.groupby("Weather_Condition")
        ["Disruption_Occurred"]
        .mean()
        .reset_index()
    )

    result["Disruption_Occurred"] *= 100

    return result.to_dict(orient="records")


def get_monthly_shipments():

    monthly = (
        df.groupby(
            ["Year", "Month"]
        )
        .size()
        .reset_index(name="Shipments")
    )

    monthly["Period"] = (
        monthly["Year"].astype(str)
        + "-"
        + monthly["Month"].astype(str)
    )

    return monthly[
        ["Period", "Shipments"]
    ].to_dict(orient="records")


def get_route_distribution():

    routes = (
        df["Route"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    routes.columns = [
        "Route",
        "Count"
    ]

    return routes.to_dict(orient="records")


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
        .head(50)
    )

    return recent.to_dict(
        orient="records"
    )