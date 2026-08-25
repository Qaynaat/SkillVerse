from src.core.learning_action_execution_engine import (
    LearningActionExecutionEngine
)


action_plan = {
    "profile_type": "Recovering Learner",
    "focus": "Revision",
    "priority": "Critical",
    "plan_type": "Focused Recovery Plan",
    "duration": "30–45 minutes",
    "steps": [
        "Choose one difficult concept.",
        "Review the concept for 20 minutes.",
        "Complete one small practice task.",
        "Check mistakes and retry once.",
        "Stop after the focused revision session.",
    ],
}


engine = LearningActionExecutionEngine()

report = engine.analyze(action_plan)


print("=" * 60)
print("MISSION 074 - LEARNING ACTION EXECUTION ENGINE TEST")
print("=" * 60)

print()
print("⚡ Learning Action Execution")
print()

print(f"📍 Profile: {report['profile_type']}")
print(f"🎯 Focus: {report['focus']}")
print(f"📈 Priority: {report['execution_priority']}")
print(f"🚦 State: {report['execution_state']}")
print(f"⏱ Duration: {report['duration']}")

print()
print("▶️ Start Here:")
print(report["first_action"])

print()
print("💡 Guidance:")
print(report["guidance"])

print()
print("✅ Completion Rule:")
print(report["expected_completion"])


assert report["profile_type"] == "Recovering Learner"
assert report["focus"] == "Revision"
assert report["execution_priority"] == "Critical"
assert report["execution_state"] == "Start Immediately"
assert (
    report["first_action"]
    == "Choose one difficult concept."
)
assert len(report["steps"]) == 5


print()
print("=" * 60)
print(
    "✅ Learning Action Execution Engine Test Completed Successfully!"
)
print("=" * 60)