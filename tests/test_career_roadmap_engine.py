from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 081 - CAREER ROADMAP ENGINE TEST")
print("=" * 60)

services = BrainServices.default()

engine = services.career_roadmap_engine

report = engine.analyze("Software Engineering")

print("\n🗺️ Career Roadmap\n")

print(f"🎯 Career: {report['career']}")

print("\n📚 Skills:")
for skill in report["skills"]:
    print(f"• {skill}")

print("\n🛣️ Career Paths:")
for path in report["career_paths"]:
    print(f"• {path}")

print("\n📍 Roadmap Stages:")

for stage in report["stages"]:
    print(
        f"\n🟢 Stage {stage['stage']} — "
        f"{stage['title']}"
    )

    for focus in stage["focus"]:
        print(f"• {focus}")

print("\n📊 Roadmap Summary:")
print(report["roadmap_summary"])

assert report["career"] == "Software Engineering"
assert report["total_skills"] == 7
assert report["total_stages"] == 5
assert len(report["career_paths"]) == 8
assert len(report["stages"]) == 5

print("\n" + "=" * 60)
print("✅ Career Roadmap Engine Test Completed Successfully!")
print("=" * 60)