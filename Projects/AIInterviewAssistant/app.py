from src.models import InterviewResponse
from src.evaluator import Evaluator
from src.feedback import FeedbackGenerator
from src.report  import ReportGenerator


response = InterviewResponse(
    question="What is Machine Learning?",
    answer="Machine Learning is a technique where computers learn from data."
)

print(response)
print(response.question)

# Create Evaluator
evaluator = Evaluator()

# Inject Evaluator into FeedbackGenerator
generator = FeedbackGenerator(evaluator)

#Generate Feedback
feedback = generator.generate_feedback(response)

#Display REport
report = ReportGenerator()
report.display(feedback)