from src.core.engine.career_matching_engine import CareerMatchingEngine
from src.core.student_profile import StudentProfile

class FakeCareer:
    def __init__(self):
        self.required_traits = {
            "logical_thinking": 5,
            "analytical_thinking": 5,
            "communication": 3
        }
student = StudentProfile()

student.set_scores({
    "logical_thinking": 5,
    "analytical_thinking": 4,
    "communication": 3
})

engine = CareerMatchingEngine()

score = engine.calculate_match(student, FakeCareer())

print("=" * 60)
print("MISSION 022 - CAREER MATCHING ENGINE TEST")
print("=" * 60)

match_score = engine.calculate_match(student, FakeCareer())

print()
print("Student Traits")
print("-" * 40)

for trait, score in student.get_scores().items():
    print(f"{trait}: {score}")

print()
print("Career")
print("-" * 40)

print("Cybersecurity")



print()
print(f"Career Match: {match_score}%")

print()
print("=" * 60)
print("TEST FINISHED")
print("=" * 60)