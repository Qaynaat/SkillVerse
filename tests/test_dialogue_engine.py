from src.core.dialogue_engine import DialogueEngine

engine = DialogueEngine()

print("=" * 60)
print("MISSION 025 - DIALOGUE ENGINE TEST")
print("=" * 60)

print()
print(engine.greeting())

from src.core.student_profile import StudentProfile


class FakeCareer:
    def __init__(self):
        self.name = "Cybersecurity"


student = StudentProfile()

student.set_strongest_trait({
    "id": "logical_thinking",
    "name": "Logical Thinking"
})

career = FakeCareer()

print()
print("Recommendation")
print("-" * 40)

print(engine.career_recommendation(student, career))

print()
print("=" * 60)
print("TEST FINISHED")
print("=" * 60)

