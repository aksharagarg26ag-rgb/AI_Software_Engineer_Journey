class ReportGenerator:

    def generate_report(self,
                        analysis,
                        llm_feedback):

        report = {

            "ATS Score":
                analysis["ats_score"],

            "Matched Skills":
                analysis["matched"],

            "Missing Skills":
                analysis["missing"],

            "LLM Feedback":
                llm_feedback

        }

        return report