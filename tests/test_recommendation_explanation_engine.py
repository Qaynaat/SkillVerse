from src.core.engine.recommendation_explanation_engine import (
    RecommendationExplanationEngine
)
from src.core.student_profile import StudentProfile


class FakeCareer:

    def __init__(self):

        self.name = "Cybersecurity"

        self.ideal_profile = {
            "personality": {
                "curiosity": 5,
                "patience": 4
            },

            "thinking_style": {
                "logical_thinking": 5,
                "analytical_thinking": 5
            },

            "work_style": {
                "independent_work": 5
            },


        }


student = StudentProfile()

student.personality = {
    "curiosity": 5,
    "patience": 4
}

student.thinking_style = {
    "logical_thinking": 5,
    "analytical_thinking": 4
}

student.work_style = {
    "independent_work": 5
}



engine = RecommendationExplanationEngine()

explanation = engine.explain(
    student,
    FakeCareer(),
    92.5
)


print("=" * 60)
print("MISSION 100 - RECOMMENDATION EXPLANATION")
print("=" * 60)

print()
print(explanation)
print()

assert "Cybersecurity" in explanation
assert "92.5%" in explanation
assert "curiosity" in explanation
assert "logical thinking" in explanation

print("All Mission 100 Recommendation Explanation tests passed.")
print("=" * 60)