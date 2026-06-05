# 🚀 AI Resume Analyzer

## 📌 Overview

AI Resume Analyzer is an intelligent resume screening application that helps job seekers evaluate their resumes against specific job descriptions. The system extracts information from resumes, identifies relevant skills, calculates an ATS (Applicant Tracking System) compatibility score, highlights missing skills, and provides personalized suggestions to improve job-fit.

This project simulates how modern recruitment systems analyze resumes and helps candidates optimize their applications before applying for jobs.

---

## 🎯 Problem Statement

Many candidates submit resumes without knowing whether their profiles match the requirements of a job description. As a result, resumes are often filtered out by ATS systems before reaching recruiters.

The AI Resume Analyzer solves this problem by:

* Comparing resumes with job descriptions
* Calculating ATS compatibility scores
* Identifying missing skills
* Suggesting improvements for better job alignment

---

## ✨ Features

### 📄 Resume Parsing

* Upload resume in PDF format
* Extracts text automatically from resumes

### 🔍 Skill Extraction

* Detects technical and non-technical skills
* Matches resume skills with job requirements

### 📊 ATS Score Calculation

* Calculates resume-job similarity score
* Uses Natural Language Processing techniques

### ⚠️ Missing Skill Detection

* Identifies skills present in the job description but missing from the resume

### 💡 Resume Improvement Suggestions

* Provides actionable recommendations
* Helps improve ATS compatibility

### 🎨 Interactive User Interface

* Modern Gradio-based interface
* User-friendly and responsive design

---

## 🛠️ Technologies Used

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Python         | Core Development       |
| Gradio         | Web Interface          |
| PDFPlumber     | Resume Text Extraction |
| Pandas         | Data Processing        |
| Scikit-Learn   | ATS Score Calculation  |
| NLP Techniques | Skill Matching         |
| Git & GitHub   | Version Control        |

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app/
│   └── app.py
│
├── src/
│   ├── __init__.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── ats_score.py
│   └── utils.py
│
├── data/
│   └── skills.csv
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
```

```bash
cd AI-Resume-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python app/app.py
```

The application will launch locally in your browser.

---

## 📈 Workflow

1. User uploads resume PDF.
2. Resume text is extracted using PDFPlumber.
3. Job description is provided by the user.
4. Skills are extracted from both resume and job description.
5. ATS score is calculated using text similarity.
6. Missing skills are identified.
7. Personalized recommendations are generated.
8. Results are displayed through the Gradio interface.

---

## 📸 Sample Output

### ATS Score

```
72.5%
```

### Skills Found

```
Python, Machine Learning, SQL, Pandas
```

### Missing Skills

```
Docker, AWS, FastAPI
```

### Suggestions

```
Add Docker and AWS experience.
Include more project details.
Improve keyword matching with job description.
```

---

## 🔮 Future Enhancements

* AI-powered resume rewriting
* Resume ranking system
* Multi-resume comparison
* LinkedIn profile analysis
* Interview question generation
* LLM-based career recommendations
* Downloadable ATS report in PDF format
* Support for DOCX resumes

---

## 🎓 Learning Outcomes

This project demonstrates:

* Natural Language Processing (NLP)
* Information Retrieval
* Text Similarity Analysis
* PDF Processing
* Web Application Development
* Machine Learning Fundamentals
* Git and GitHub Workflow

---

## 👩‍💻 Author

**Jui Prabhukhot**

Bachelor of Information Technology

AI/ML Enthusiast | Python Developer | Aspiring Machine Learning Engineer

---

## ⭐ If you found this project useful

Please consider giving it a star on GitHub!
