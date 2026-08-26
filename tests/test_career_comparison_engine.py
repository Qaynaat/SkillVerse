from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 080 - CAREER COMPARISON ENGINE TEST")
print("=" * 60)


services = BrainServices.default()

engine = services.career_comparison_engine


report = engine.analyze(
    "Software Engineering",
    "Cybersecurity"
)


print()
print("⚖️ Career Comparison")
print()

print(
    f"💻 Career 1: "
    f"{report['career_one']['name']}"
)

print(
    f"🛡️ Career 2: "
    f"{report['career_two']['name']}"
)

print()
print("📚 Shared Skills:")

for skill in report["shared_skills"]:
    print(f"• {skill}")


print()
print("🎯 Career 1 Skills:")

for skill in report["career_one"]["skills"]:
    print(f"• {skill}")


print()
print("🎯 Career 2 Skills:")

for skill in report["career_two"]["skills"]:
    print(f"• {skill}")


print()
print("💡 Comparison:")
print(report["comparison_summary"])


assert report["career_one"]["name"]
assert report["career_two"]["name"]
assert "shared_skills" in report
assert "career_one_unique_skills" in report
assert "career_two_unique_skills" in report
assert "comparison_summary" in report


print()
print("=" * 60)
print("✅ Career Comparison Engine Test Completed Successfully!")
print("=" * 60)