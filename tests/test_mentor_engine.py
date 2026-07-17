from src.core.mentor_engine import MentorEngine
from src.core.career_database import CareerDatabase

database = CareerDatabase()
mentor = MentorEngine()

career = database.get_career("Software Engineering")

print("=" * 60)
print("BYTE FIRST LEARNING STEP")
print("=" * 60)
print()

print(mentor.get_first_step(career))