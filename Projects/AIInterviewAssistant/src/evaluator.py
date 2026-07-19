#Evaluator  - evaluates answer quality
from src.models import InterviewResponse, Feedback


class Evaluator:

    def __init__(self):

        # Expected keywords for each question
        self.answer_key = {
            "What is Machine Learning?": [
                "machine",
                "learning",
                "data",
                "algorithm",
                "prediction"
            ],

            "What is Python?": [
                "python",
                "programming",
                "language"
            ],

            "What is OOP?": [
                "object",
                "class",
                "inheritance",
                "polymorphism",
                "encapsulation"
            ]
        }

    def evaluate(self, response: InterviewResponse) -> Feedback:

        strengths = []
        weaknesses = []
        suggestions = []

        answer = response.answer.lower()

        expected_keywords = self.answer_key.get(
            response.question,
            []
        )

        for keyword in expected_keywords:

            if keyword in answer:

                strengths.append(
                    f"Mentioned '{keyword}'."
                )

            else:

                weaknesses.append(
                    f"Missing '{keyword}'."
                )

                suggestions.append(
                    f"Explain the concept of '{keyword}'."
                )

        return Feedback(
            strengths=strengths,
            weaknesses=weaknesses,
            suggestions=suggestions
        )