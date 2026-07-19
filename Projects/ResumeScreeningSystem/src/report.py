class ReportGenerator:

    def generate_report(self, analysis):

        report = {
            "ATS Score": f"{analysis['ats_score']:.2f}%",
            "Resume Skills": analysis["resume_skills"],
            "Job Skills": analysis["job_skills"],
            "Matched Skills": analysis["matched"],
            "Missing Skills": analysis["missing"]
        }

        return report