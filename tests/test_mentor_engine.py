from src.core.mentor_engine import MentorEngine
from src.core.career_database import CareerDatabase

database = CareerDatabase()
mentor = MentorEngine()

career = database.get_career("Software Engineering")

print("=" * 60)
print("LEARNING MISSIONS ")
print("=" * 60)
print()

print(mentor.get_first_step(career))