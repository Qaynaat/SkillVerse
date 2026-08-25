from src.core.learning_profile_advisor import LearningProfileAdvisor


interpretation = {
    "profile_type": "Recovering Learner",
    "dominant_pattern": "Difficulty Dominant",
    "primary_need": "Targeted Revision",
    "recommended_direction": (
        "Recover → Stabilize → Build Momentum"
    ),
    "overall_priority": "Critical",
}


advisor = LearningProfileAdvisor()

report = advisor.analyze(interpretation)


print("=" * 60)
print("MISSION 072 - LEARNING PROFILE ADVISOR TEST")
print("=" * 60)

print()
print("🧭 Learning Profile Advice")
print()

print(f"📍 Profile: {report['profile_type']}")
print(f"🎯 Focus: {report['focus']}")
print(f"📈 Urgency: {report['urgency']}")

print()
print("🛠 What You Should Do:")
print(report["action"])

print()
print("➡️ Next Step:")
print(report["next_step"])

print()
print(f"💡 {report['reason']}")

assert report["profile_type"] == "Recovering Learner"
assert report["focus"] == "Revision"
assert report["urgency"] == "Immediate"
assert (
    report["next_step"]
    == "Choose one difficult concept and complete a revision-focused task."
)

print()
print("=" * 60)
print("✅ Learning Profile Advisor Test Completed Successfully!")
print("=" * 60)