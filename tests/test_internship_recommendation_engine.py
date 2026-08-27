from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 084 - INTERNSHIP RECOMMENDATION ENGINE TEST")
print("=" * 60)

services = BrainServices.default()

report = services.internship_recommendation_engine.analyze(
    "Software Engineering"
)

response = (
    services.internship_recommendation_engine
    .format_report(report)
)

print(response)

assert report["career"] == "Software Engineering"
assert len(report["recommended_internships"]) > 0
assert len(report["preparation_skills"]) > 0
assert report["priority"] in [
    "High",
    "Medium",
    "Foundational"
]

print("=" * 60)
print("✅ Internship Recommendation Engine Test Completed Successfully!")
print("=" * 60)