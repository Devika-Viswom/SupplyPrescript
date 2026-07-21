def generate_recommendations(
    risk_probability,
    predicted_lead_time,
    weather,
    geopolitical_risk,
    carrier_reliability,
    transport_mode
):

    recommendations = []

    # Risk Level
    if risk_probability < 40:
        risk_level = "Low"

    elif risk_probability < 70:
        risk_level = "Medium"

    elif risk_probability < 95:
        risk_level = "High"

    else:
        risk_level = "Critical"

    # Delay Category
    if predicted_lead_time < 8:
        delay_category = "Short"

    elif predicted_lead_time < 21:
        delay_category = "Moderate"

    elif predicted_lead_time < 40:
        delay_category = "Long"

    else:
        delay_category = "Severe"

    # Weather
    if weather == "Hurricane":

        recommendations.extend([
            "Activate contingency plan",
            "Increase safety stock",
            "Prepare backup supplier",
            "Escalate shipment monitoring"
        ])

    elif weather == "Storm":

        recommendations.extend([
            "Increase inventory buffer",
            "Monitor shipment daily",
            "Prepare alternate route"
        ])

    # Risk
    if geopolitical_risk > 7:

        recommendations.extend([
            "Review alternative routes",
            "Diversify sourcing options"
        ])

    # Carrier
    if carrier_reliability < 0.65:

        recommendations.extend([
            "Consider higher reliability carrier",
            "Request priority handling"
        ])

    # Delay
    if predicted_lead_time > 30:

        recommendations.append(
            "Increase safety stock"
        )

        if transport_mode == "Sea":

            recommendations.append(
                "Evaluate Air transport for urgent shipments"
            )

        elif transport_mode in ["Road", "Rail"]:

            recommendations.append(
                "Evaluate faster transport alternatives"
            )

    # Critical
    if risk_probability > 0.95:

        recommendations.append(
            "Immediate management review required"
        )

    recommendations = list(set(recommendations))

    return risk_level, delay_category, recommendations