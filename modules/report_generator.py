from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_report(filename, ats_score, matched_skills, missing_skills):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))
    elements.append(Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["BodyText"]))

    elements.append(Paragraph("<b>Matched Skills:</b>", styles["Heading2"]))
    if matched_skills:
        for skill in matched_skills:
            elements.append(Paragraph(f"• {skill}", styles["BodyText"]))
    else:
        elements.append(Paragraph("No matched skills found.", styles["BodyText"]))

    elements.append(Paragraph("<b>Missing Skills:</b>", styles["Heading2"]))
    if missing_skills:
        for skill in missing_skills:
            elements.append(Paragraph(f"• {skill}", styles["BodyText"]))
    else:
        elements.append(Paragraph("No missing skills.", styles["BodyText"]))

    doc.build(elements)