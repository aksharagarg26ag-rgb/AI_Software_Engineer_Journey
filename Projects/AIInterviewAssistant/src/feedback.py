#feedback - genERATE FEEDBACK   on basis of evaluator output
#Its job is NOT to evaluate.
#Its job is to decide
#"Who will generate the feedback?"

from src.evaluator import Evaluator
from src.models import InterviewResponse, Feedback


class FeedbackGenerator:

    def __init__(self,evaluator):
        self.evaluator = evaluator

    def generate_feedback(
        self,
        response: InterviewResponse
    ) -> Feedback:

        feedback = self.evaluator.evaluate(response)

        return feedback
    