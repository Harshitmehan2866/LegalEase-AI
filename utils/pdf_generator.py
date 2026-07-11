from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(summary):

    filename = "legal_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>LegalEase AI Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            summary.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename