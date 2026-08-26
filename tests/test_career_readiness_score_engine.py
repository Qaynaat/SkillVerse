from src.core.career_database import CareerDatabase
from src.core.career_readiness_score_engine import (
    CareerReadinessScoreEngine
)


print("=" * 60)
print("MISSION 082 - CAREER READINESS SCORE ENGINE TEST")
print("=" * 60)

database = CareerDatabase()

engine = CareerReadinessScoreEngine(
    database
)

report = engine.analyze(
    "Software Engineering",
    [
        "Problem Solving",
        "Programming",
        "Communication"
    ]
)

print(engine.format_report(report))

assert report["career"] == "Software Engineering"
assert report["readiness_score"] == 43
assert report["readiness_level"] == "Developing"

assert "Problem Solving" in report["matched_skills"]
assert "Programming" in report["matched_skills"]

assert "Teamwork" in report["missing_skills"]
assert "Debugging" in report["missing_skills"]

print("=" * 60)
print("✅ Career Readiness Score Engine Test Completed Successfully!")
print("=" * 60)