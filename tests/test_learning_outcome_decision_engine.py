from src.core.learning_outcome_decision_engine import (
    LearningOutcomeDecisionEngine
)


print("=" * 60)
print("MISSION 078 - LEARNING OUTCOME DECISION ENGINE TEST")
print("=" * 60)

engine = LearningOutcomeDecisionEngine()

outcome_report = {
    "outcome": "Difficult"
}

interpretation_report = {
    "impact": "Learning Difficulty"
}

report = engine.analyze(
    outcome_report,
    interpretation_report
)

print("\n🧭 Learning Outcome Decision\n")

print(f"📊 Outcome: {report['outcome']}")
print(f"📈 Impact: {report['impact']}")
print(f"🎯 Decision: {report['decision']}")
print(f"📌 Priority: {report['priority']}")

print("\n🔎 Reason:")
print(report["reason"])

print("\n🛠 Action:")
print(report["action"])

print("\n➡️ Next Step:")
print(report["next_step"])

assert report["decision"] == "Targeted Revision"
assert report["priority"] == "Critical"
assert "Review" in report["action"]
assert "revision" in report["next_step"].lower()

print("\n" + "=" * 60)
print("✅ Learning Outcome Decision Engine Test Completed Successfully!")
print("=" * 60)