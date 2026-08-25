from src.core.learning_profile_action_planner import (
    LearningProfileActionPlanner
)


advice = {
    "profile_type": "Recovering Learner",
    "focus": "Revision",
    "urgency": "Immediate",
    "primary_need": "Targeted Revision",
    "action": "Review difficult concepts before starting new work.",
    "next_step": (
        "Choose one difficult concept and complete "
        "a revision-focused task."
    ),
}


planner = LearningProfileActionPlanner()

report = planner.analyze(advice)


print("=" * 60)
print("MISSION 073 - LEARNING PROFILE ACTION PLANNER TEST")
print("=" * 60)

print()
print("🧭 Learning Action Plan")
print()

print(f"📍 Profile: {report['profile_type']}")
print(f"🎯 Focus: {report['focus']}")
print(f"📈 Priority: {report['priority']}")
print(f"⏱ Duration: {report['duration']}")

print()
print(f"🛠 Plan: {report['plan_type']}")

print()
print("📝 Action Steps:")

for index, step in enumerate(report["steps"], start=1):
    print(f"{index}. {step}")

print()
print(f"💡 {report['summary']}")

assert report["profile_type"] == "Recovering Learner"
assert report["focus"] == "Revision"
assert report["priority"] == "Critical"
assert report["plan_type"] == "Focused Recovery Plan"
assert len(report["steps"]) == 5

print()
print("=" * 60)
print("✅ Learning Profile Action Planner Test Completed Successfully!")
print("=" * 60)