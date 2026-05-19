from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_report(target, results, risk_score):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = "reports/vulnspecter_report.pdf"

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("VulnSpecter Security Report", styles["Title"]))
    elements.append(Spacer(1,20))

    elements.append(Paragraph(f"Target: {target}", styles["Normal"]))
    elements.append(Paragraph(f"Risk Score: {risk_score}", styles["Normal"]))
    elements.append(Spacer(1,20))

    for category in results:

        elements.append(Paragraph(category, styles["Heading2"]))

        if results[category]:

            for issue in results[category]:
                elements.append(Paragraph(f"- {issue}", styles["Normal"]))

        else:

            elements.append(Paragraph("No issues detected", styles["Normal"]))

        elements.append(Spacer(1,10))

    doc = SimpleDocTemplate(filename)

    doc.build(elements)

    return filename
