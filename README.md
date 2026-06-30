# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Python** and **Streamlit** that evaluates resumes against a given Job Description. The application extracts text from PDF resumes, identifies technical skills, calculates an ATS score, highlights matching and missing skills, and provides suggestions to improve resume quality.

---

## 🚀 Features

* 📄 Upload Resume (PDF)
* 📝 Paste Job Description
* 🔍 Extract text from resume
* 🛠️ Automatic skill extraction
* 📊 ATS Score calculation
* ✅ Matched Skills detection
* ❌ Missing Skills identification
* 💡 Resume improvement suggestions
* 📈 Resume statistics dashboard
* 🥧 Skill Match Visualization (Pie Chart)

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **PyMuPDF (fitz)**
* **Pandas**
* **Matplotlib**
* **ReportLab** (for future PDF report generation)

---

## 📂 Project Structure

```
AI_Resume_Analyzer/
│── app.py
│── requirements.txt
│── data/
│   └── skills.csv
│── modules/
│   ├── ats_score.py
│   ├── pdf_parser.py
│   ├── skill_match.py
│   └── report_generator.py
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/ANSHIKA04-ans/AI_Resume_Analyzer.git
```

2. Move into the project folder

```bash
cd AI_Resume_Analyzer
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots here after running the application.

* Home Page
* Resume Upload
* ATS Score
* Skill Match Chart

---

## 🎯 Future Improvements

* AI-powered resume feedback
* Better ATS scoring logic
* Download analysis report as PDF
* Resume ranking against multiple job descriptions
* Resume keyword optimization

---

## 👩‍💻 Author

Anshika

GitHub: https://github.com/ANSHIKA04-ans
## 🌐 Live Demo
https://ai-resume-analyzer-01z.streamlit.app/
