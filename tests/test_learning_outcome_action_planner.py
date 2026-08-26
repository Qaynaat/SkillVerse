from src.core.learning_outcome_action_planner import (
    LearningOutcomeActionPlanner
)


print("=" * 60)
print("MISSION 079 - LEARNING OUTCOME ACTION PLANNER TEST")
print("=" * 60)

planner = LearningOutcomeActionPlanner()

decision_report = {
    "outcome": "Difficult",
    "decision": "Targeted Revision",
    "priority": "Critical"
}

report = planner.analyze(decision_report)

print("\n🧭 Learning Outcome Action Plan\n")

print(f"📊 Outcome: {report['outcome']}")
print(f"🎯 Decision: {report['decision']}")
print(f"📈 Priority: {report['priority']}")
print(f"⏱ Duration: {report['duration']}")

print(f"\n🛠 Plan: {report['plan_type']}")

print("\n📝 Action Steps:")

for index, step in enumerate(
    report["steps"],
    start=1
):
    print(f"{index}. {step}")

print("\n✅ Completion Rule:")
print(report["completion_rule"])

print("\n➡️ Next Action:")
print(report["next_action"])

print("\n" + "=" * 60)
print("✅ Learning Outcome Action Planner Test Completed Successfully!")
print("=" * 60)