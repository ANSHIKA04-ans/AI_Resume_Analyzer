import streamlit as st
import matplotlib.pyplot as plt
from modules.pdf_parser import extract_text_from_pdf
from modules.skill_match import extract_skills
from modules.ats_score import calculate_ats_score
from modules.report_generator import generate_report

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- Title ----------------
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a Job Description.")

# ---------------- Sidebar ----------------
st.sidebar.header("Navigation")
st.sidebar.success("✅ Resume Upload")
st.sidebar.success("✅ Job Description")
st.sidebar.success("✅ ATS Score")
st.sidebar.success("✅ Skill Matching")
st.sidebar.success("✅ AI Suggestions")
st.sidebar.info("📈 Resume Statistics")

# ---------------- Resume Upload ----------------
st.header("📂 Upload Resume")

resume = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

# ---------------- Job Description ----------------
st.header("📝 Job Description")

job_description = st.text_area(
    "Paste the Job Description here",
    height=200
)

# ---------------- Analyze ----------------
if st.button("🔍 Analyze Resume"):

    if resume is None:
        st.error("Please upload your resume.")

    elif job_description.strip() == "":
        st.error("Please enter the Job Description.")

    else:

        st.success("Resume uploaded successfully!")

        # Extract Resume Text
        resume_text = extract_text_from_pdf(resume)

        st.subheader("📄 Extracted Resume")
        st.text_area(
            "Resume Content",
            resume_text,
            height=250
        )

        # Extract Skills
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        # ATS Score
        ats_score, matched_skills, missing_skills = calculate_ats_score(
            resume_skills,
            jd_skills
        )

        # ---------------- Matched Skills ----------------
        st.subheader("✅ Matched Skills")

        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.warning("No matching skills found.")

        # ---------------- Missing Skills ----------------
        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("Excellent! No missing skills.")

        # ---------------- ATS Score ----------------
        st.subheader("📊 ATS Score")

        st.progress(ats_score / 100)

        st.metric(
            label="ATS Match",
            value=f"{ats_score}%"
        )

        if ats_score >= 80:
            st.success("🎉 Excellent Match!")

        elif ats_score >= 60:
            st.info("👍 Good Match")

        else:
            st.warning("⚠️ Resume needs improvement.")

        # ---------------- AI Suggestions ----------------
        st.subheader("💡 AI Resume Suggestions")

        if missing_skills:
            st.write("Add the following skills to improve your ATS score:")
            for skill in missing_skills:
                st.write(f"• {skill}")
        else:
            st.success("Your resume already covers all required skills!")

        # ---------------- Resume Statistics ----------------
        st.subheader("📈 Resume Statistics")

        word_count = len(resume_text.split())
        skill_count = len(resume_skills)
        matched_count = len(matched_skills)
        missing_count = len(missing_skills)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Words", word_count)

        with col2:
            st.metric("Skills Found", skill_count)

        with col3:
            st.metric("Matched Skills", matched_count)

        with col4:
            st.metric("Missing Skills", missing_count)
           
                   # ---------------- Skill Match Chart ----------------

        st.subheader("📊 Skill Match Visualization")

        labels = ["Matched Skills", "Missing Skills"]
        sizes = [matched_count, missing_count]

        if matched_count == 0 and missing_count == 0:
            st.info("No skills available to visualize.")
        else:
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.pie(
                sizes,
                labels=labels,
                autopct="%1.1f%%",
                startangle=90
            )
            ax.axis("equal")
            st.pyplot(fig)

        # ---------------- PDF Report ----------------

        st.subheader("📄 Download Analysis Report")

        report_file = "Resume_Analysis_Report.pdf"

        generate_report(
            report_file,
            ats_score,
            matched_skills,
            missing_skills
        )

        with open(report_file, "rb") as pdf_file:
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="Resume_Analysis_Report.pdf",
                mime="application/pdf"
            )