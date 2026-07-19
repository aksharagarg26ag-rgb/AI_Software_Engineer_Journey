import re


class SkillAnalyzer:

    SKILLS = [

        "python",
        "java",
        "c++",
        "sql",
        "mysql",

        "machine learning",
        "deep learning",
        "artificial intelligence",

        "fastapi",
        "streamlit",
        "flask",

        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",

        "scikit-learn",
        "tensorflow",
        "keras",
        "pytorch",

        "git",
        "github",
        "docker"
    ]

    def extract_skills(self, text):

        text = text.lower()

        extracted = []

        for skill in self.SKILLS:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):
                extracted.append(skill)

        return extracted

    def analyze(self, resume_text, job_text):

        resume_skills = self.extract_skills(resume_text)

        job_skills = self.extract_skills(job_text)

        matched = sorted(list(set(resume_skills) & set(job_skills)))

        missing = sorted(list(set(job_skills) - set(resume_skills)))

        if len(job_skills) == 0:
            ats_score = 0
        else:
            ats_score = (len(matched) / len(job_skills)) * 100

        return {

            "resume_skills": resume_skills,

            "job_skills": job_skills,

            "matched": matched,

            "missing": missing,

            "ats_score": ats_score

        }