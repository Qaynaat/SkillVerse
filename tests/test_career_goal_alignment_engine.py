from src.core.engine.career_goal_alignment_engine import (
    CareerGoalAlignmentEngine
)
from src.core.student_profile import StudentProfile


class FakeCareer:

    def __init__(self):

        self.name = "Cybersecurity"

        self.required_traits = {
            "logical_thinking": 5,
            "curiosity": 4,
            "communication": 3
        }


print("=" * 60)
print("MISSION 107 - CAREER GOAL ALIGNMENT ENGINE")
print("=" * 60)


# --------------------------------------------------
# Create Student
# --------------------------------------------------

student = StudentProfile()

student.set_dream_career("Cybersecurity")

student.set_scores({
    "logical_thinking": 5,
    "curiosity": 5,
    "communication": 2
})


# --------------------------------------------------
# Run Engine
# --------------------------------------------------

engine = CareerGoalAlignmentEngine()

result = engine.calculate_alignment(
    student,
    FakeCareer()
)


# --------------------------------------------------
# Display Result
# --------------------------------------------------

print()
print("Career Goal")
print("-" * 40)

print(result["career"])

print()
print("Alignment")
print("-" * 40)

print(f'{result["alignment"]}%')

print()
print("Strong Traits")
print("-" * 40)

for trait in result["strong_traits"]:
    print(trait)

print()
print("Growth Areas")
print("-" * 40)

for trait in result["growth_areas"]:
    print(trait)


# --------------------------------------------------
# Tests
# --------------------------------------------------

assert result["career"] == "Cybersecurity"

assert isinstance(
    result["alignment"],
    (int, float)
)

assert 0 <= result["alignment"] <= 100

assert "logical_thinking" in result["strong_traits"]

assert "curiosity" in result["strong_traits"]

assert "communication" in result["growth_areas"]

assert isinstance(result["strong_traits"], list)

assert isinstance(result["growth_areas"], list)


# --------------------------------------------------
# Missing Trait Test
# --------------------------------------------------

student.set_scores({
    "logical_thinking": 5
})

result = engine.calculate_alignment(
    student,
    FakeCareer()
)

assert 0 <= result["alignment"] <= 100

assert "curiosity" in result["growth_areas"]

assert "communication" in result["growth_areas"]


print()
print("All Mission 107 Career Goal Alignment tests passed.")

print("=" * 60)