from src.core.services.brain_services import BrainServices


print("=" * 60)
print(
    "MISSION 085 - CERTIFICATION RECOMMENDATION ENGINE TEST"
)
print("=" * 60)

services = BrainServices.default()

report = (
    services.certification_recommendation_engine
    .analyze("Software Engineering")
)

response = (
    services.certification_recommendation_engine
    .format_report(report)
)

print(response)

assert report["career"] == "Software Engineering"

assert len(
    report["recommended_certifications"]
) > 0

assert len(
    report["skills"]
) > 0

assert report["priority"] in [
    "High",
    "Medium",
    "Foundational"
]

assert "recommendation" in report

print("=" * 60)
print(
    "✅ Certification Recommendation Engine "
    "Test Completed Successfully!"
)
print("=" * 60)