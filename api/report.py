from io import BytesIO
import json

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(record):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = []

    # ==========================
    # Header
    # ==========================

    elements.append(
        Paragraph(
            "SupplyPrescript",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "AI-Powered Supply Chain Prescriptive Analytics",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph(
            f"Prediction ID: {record['id']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Generated On: {record['created_at']}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    # ==========================
    # Shipment Information
    # ==========================

    elements.append(
        Paragraph(
            "Shipment Information",
            styles["Heading1"]
        )
    )

    shipment_data = [

        ["Shipment Date",
         record["shipment_date"]],

        ["Origin Port",
         record["origin_port"]],

        ["Destination Port",
         record["destination_port"]],

        ["Transport Mode",
         record["transport_mode"]],

        ["Product Category",
         record["product_category"]],

        ["Distance (km)",
         str(record["distance_km"])],

        ["Weight (MT)",
         str(record["weight_mt"])],

        ["Fuel Price Index",
         str(record["fuel_price_index"])],

        ["Geopolitical Risk",
         str(record["geopolitical_risk_score"])],

        ["Weather",
         record["weather_condition"]],

        ["Carrier Reliability",
         str(record["carrier_reliability_score"])]
    ]

    shipment_table = Table(
        shipment_data,
        colWidths=[180, 250]
    )

    shipment_table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.black)
        ])
    )

    elements.append(shipment_table)

    elements.append(Spacer(1, 20))

    # ==========================
    # Risk Assessment
    # ==========================

    elements.append(
        Paragraph(
            "Risk Assessment",
            styles["Heading1"]
        )
    )

    risk_data = [

        ["Disruption Prediction",
         str(record["disruption_prediction"])],

        ["Risk Probability",
         f"{record['risk_probability']}%"],

        ["Risk Level",
         record["risk_level"]],

        ["Confidence Score",
         f"{record['confidence_score']}%"]
    ]

    risk_table = Table(
        risk_data,
        colWidths=[180, 250]
    )

    risk_table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.black)
        ])
    )

    elements.append(risk_table)

    elements.append(Spacer(1, 20))

    # ==========================
    # Lead Time
    # ==========================

    elements.append(
        Paragraph(
            "Lead Time Analysis",
            styles["Heading1"]
        )
    )

    lead_data = [

        ["Predicted Lead Time",
         f"{record['predicted_lead_time']} Days"],

        ["Delay Category",
         record["delay_category"]]
    ]

    lead_table = Table(
        lead_data,
        colWidths=[180,250]
    )

    lead_table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.black)
        ])
    )

    elements.append(lead_table)

    elements.append(Spacer(1, 20))

    # ==========================
    # Recommendations
    # ==========================

    elements.append(
        Paragraph(
            "Recommendations",
            styles["Heading1"]
        )
    )

    recommendations = json.loads(
        record["recommendations"]
    )

    for item in recommendations:

        elements.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 20))

    # ==========================
    # Mode Comparison
    # ==========================

    elements.append(
        Paragraph(
            "Transport Mode Comparison",
            styles["Heading1"]
        )
    )

    comparison = json.loads(
        record["comparison_json"]
    )

    comparison_rows = [[
        "Mode",
        "Risk(%)",
        "Lead Time",
        "Cost"
    ]]

    for row in comparison:

        comparison_rows.append([
            row["mode"],
            str(row["risk_probability"]),
            str(row["predicted_lead_time"]),
            f"${row['estimated_cost']:,.0f}"
        ])

    comparison_table = Table(
        comparison_rows
    )

    comparison_table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),1,colors.black),
            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey)
        ])
    )

    elements.append(comparison_table)

    elements.append(Spacer(1, 20))

    # ==========================
    # AI Recommendation
    # ==========================

    elements.append(
        Paragraph(
            "Mode Recommendation",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"Recommended Mode: "
            f"{record['recommended_mode']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            record["recommendation_reason"],
            styles["Normal"]
        )
    )

    doc.build(elements)

    buffer.seek(0)

    return buffer