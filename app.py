import streamlit as st
from modules.pdf_parser import extract_text_from_pdf
from modules.skill_match import extract_skills
from modules.ats_score import calculate_ats_score

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
st.sidebar.write("✅ Resume Upload")
st.sidebar.write("✅ Job Description Upload")
st.sidebar.write("✅ ATS Score")
st.sidebar.write("✅ Skill Matching")
st.sidebar.write("🚧 AI Suggestions (Coming Soon)")

# ---------------- Resume Upload ----------------
st.header("Upload Resume")

resume = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

# ---------------- Job Description ----------------
st.header("Job Description")

job_description = st.text_area(
    "Paste the Job Description here",
    height=200
)

# ---------------- Analyze Button ----------------
if st.button("Analyze Resume"):

    if resume is None:
        st.error("Please upload your resume.")

    elif job_description.strip() == "":
        st.error("Please enter the Job Description.")

    else:

        st.success("Resume uploaded successfully!")

        # Extract Resume Text
        resume_text = extract_text_from_pdf(resume)

        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=250
        )

        # Extract Skills
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        # Calculate ATS Score
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
            st.success("No missing skills!")

        # ---------------- ATS Score ----------------
        st.subheader("📊 ATS Score")

        st.progress(ats_score / 100)

        st.metric(
            label="ATS Match",
            value=f"{ats_score}%"
        )

        if ats_score >= 80:
            st.success("Excellent Match! 🎉")

        elif ats_score >= 60:
            st.info("Good Match 👍")

        else:
            st.warning("Resume needs improvement.")