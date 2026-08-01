from src.core.engine.explanation_engine import ExplanationEngine
from src.core.student_profile import StudentProfile


class FakeCareer:

    def __init__(self):
        

        self.name = "Cybersecurity"

        self.recommendation_reason = (
            "You enjoy solving logical problems and protecting digital systems."
        )

student = StudentProfile()

student.set_strongest_trait({
    "id": "logical_thinking",
    "name": "Logical Thinking",
    "category": "thinking_style",
    "description": "Enjoys analysing problems and finding logical solutions.",
    "why_it_matters": "Logical thinkers solve complex problems step by step.",
    "careers": [
        "Software Engineering",
        "Cybersecurity",
        "Data Science",
        "Artificial Intelligence"
    ]
})


engine = ExplanationEngine()

career = FakeCareer()

print("=" * 60)
print("MISSION 024 - EXPLANATION ENGINE TEST")
print("=" * 60)

print()

print("Career")
print("-" * 40)
print(career.name)

print()

print("Explanation")
print("-" * 40)
print(engine.explain_career(student, career))

print()

print("=" * 60)
print("TEST FINISHED")
print("=" * 60)