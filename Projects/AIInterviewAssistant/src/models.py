# Python provides a special feature called dataclass.
# It automatically creates:
# constructor (__init__)
# string representation (__repr__)
# comparisons (optional)
# Instead of writing all of that manually.

from dataclasses import dataclass
from typing import List

#it automatically creates -
# class InterviewResponse:
#     def __init__(self, question, answer):
#         self.question = question
#         self.answer = answer
@dataclass
class InterviewResponse:

    question: str
    answer: str


@dataclass
class Feedback:
    
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]