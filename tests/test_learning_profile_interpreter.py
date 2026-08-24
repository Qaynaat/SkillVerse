from src.core.learning_profile_interpreter import LearningProfileInterpreter


snapshot = {
    "learning_state": "Recovering",
    "state_priority": "Critical",
    "risk_status": "Moderate Risk",
    "risk_score": 2,
    "recovery_level": "Intensive Recovery",
    "intervention": "Targeted Revision",
    "intervention_priority": "Critical",
    "primary_intervention": "Targeted Revision",
    "primary_intervention_priority": "Critical",
    "learning_decision": "Recovery Mode",
    "decision_priority": "Critical",
    "velocity_score": 15,
    "velocity_status": "High Velocity",
    "performance_score": 2,
    "trend_status": "Declining",
    "next_best_action": (
        "Review a difficult concept before starting new work."
    ),
    "overall_priority": "Critical",
}


interpreter = LearningProfileInterpreter()

report = interpreter.analyze(snapshot)


print("=" * 60)
print("MISSION 071 - LEARNING PROFILE INTERPRETER TEST")
print("=" * 60)

print()
print("🧠 Learning Profile Interpretation")
print()

print(f"📍 Profile Type: {report['profile_type']}")
print(f"🎯 Dominant Pattern: {report['dominant_pattern']}")
print()
print(f"🛠 Primary Need: {report['primary_need']}")
print()
print("🧭 Recommended Direction:")
print(report["recommended_direction"])
print()
print("💡 Profile Summary:")
print(report["profile_summary"])

assert report["profile_type"] == "Recovering Learner"
assert report["dominant_pattern"] == "Difficulty Dominant"
assert report["primary_need"] == "Targeted Revision"
assert (
    report["recommended_direction"]
    == "Recover → Stabilize → Build Momentum"
)

print()
print("=" * 60)
print("✅ Learning Profile Interpreter Test Completed Successfully!")
print("=" * 60)