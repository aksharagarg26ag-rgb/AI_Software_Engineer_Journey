#Report- display feedback
from src.models import Feedback


class ReportGenerator:

    def display(self, feedback: Feedback):

        print("=" * 50)
        print("INTERVIEW FEEDBACK REPORT")
        print("=" * 50)

        print("\n✅ Strengths")

        if feedback.strengths:

            for strength in feedback.strengths:
                print(f"- {strength}")

        else:

            print("No strengths found.")

        print("\n❌ Weaknesses")

        if feedback.weaknesses:

            for weakness in feedback.weaknesses:
                print(f"- {weakness}")

        else:

            print("No weaknesses found.")

        print("\n💡 Suggestions")

        if feedback.suggestions:

            for suggestion in feedback.suggestions:
                print(f"- {suggestion}")

        else:

            print("No suggestions.")

        print("\n" + "=" * 50)