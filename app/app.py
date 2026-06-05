import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import gradio as gr
from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.ats_score import calculate_ats_score


custom_css = """
body {
    background: linear-gradient(135deg, #f5f7fa, #e4ecff);
}

.gradio-container {
    max-width: 1200px !important;
    margin: auto;
}

.submit-btn {
    background: linear-gradient(90deg, #ff7a18, #ffb347) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}

textarea, input {
    border-radius: 12px !important;
}
"""


def analyze_resume(resume_file, job_description):
    if resume_file is None:
        return "Please upload a resume PDF.", "", "", ""

    if not job_description.strip():
        return "Please enter a job description.", "", "", ""

    resume_text = extract_text_from_pdf(resume_file)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    missing_skills = list(set(job_skills) - set(resume_skills))

    ats_score = calculate_ats_score(resume_text, job_description)

    suggestions = []

    if ats_score < 50:
        suggestions.append("Improve keyword matching with the job description.")

    if missing_skills:
        suggestions.append("Add or learn missing skills: " + ", ".join(missing_skills))

    if len(resume_text.split()) < 200:
        suggestions.append("Your resume seems short. Add more project and experience details.")

    if not suggestions:
        suggestions.append("Your resume matches the job description well.")

    return (
        f"{ats_score}%",
        ", ".join(resume_skills) if resume_skills else "No matching skills found.",
        ", ".join(missing_skills) if missing_skills else "No major missing skills found.",
        "\n".join(suggestions)
    )


with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:

    gr.HTML("""
    <div style="text-align:center; padding:25px;">
        <h1 style="font-size:40px; margin-bottom:10px;">
            🚀 AI Resume Analyzer
        </h1>
        <p style="font-size:18px; color:#555;">
            Upload your resume and compare it with a job description to get ATS score,
            missing skills, and smart improvement suggestions.
        </p>
    </div>
    """)

    with gr.Row():

        with gr.Column():

            resume_input = gr.File(
                label="📄 Upload Resume PDF",
                file_types=[".pdf"]
            )

            job_input = gr.Textbox(
                label="📝 Paste Job Description",
                lines=10,
                placeholder="Paste the full job description here..."
            )

            submit_btn = gr.Button(
                "Analyze Resume",
                elem_classes="submit-btn"
            )

        with gr.Column():

            ats_output = gr.Textbox(
                label="📊 ATS Score"
            )

            skills_output = gr.Textbox(
                label="✅ Skills Found in Resume"
            )

            missing_output = gr.Textbox(
                label="⚠️ Missing Skills"
            )

            suggestions_output = gr.Textbox(
                label="💡 Suggestions",
                lines=5
            )

    submit_btn.click(
        fn=analyze_resume,
        inputs=[resume_input, job_input],
        outputs=[
            ats_output,
            skills_output,
            missing_output,
            suggestions_output
        ]
    )


if __name__ == "__main__":
    demo.launch()