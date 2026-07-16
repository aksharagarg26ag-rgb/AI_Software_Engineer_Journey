from dataclasses import dataclass
from typing import List


@dataclass
class InterviewResponse:
    """
    Stores the user's interview response.
    """

    question: str
    answer: str


@dataclass
class Feedback:
    """
    Stores the generated feedback.
    """

    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]