from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 083 - FUTURE SKILLS RECOMMENDATION ENGINE TEST")
print("=" * 60)

services = BrainServices.default()

report = services.future_skills_recommendation_engine.analyze(
    "Software Engineering",
    [
        "Problem Solving",
        "Programming",
        "Communication"
    ]
)

print(
    services.future_skills_recommendation_engine.format_report(
        report
    )
)

assert report["career"] == "Software Engineering"
assert report["recommended_future_skills"]

print("=" * 60)
print("✅ Future Skills Recommendation Engine Test Completed Successfully!")
print("=" * 60)

