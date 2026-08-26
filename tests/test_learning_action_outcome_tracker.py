from src.core.learning_action_outcome_tracker import (
    LearningActionOutcomeTracker
)
from src.core.memory import Memory


print("=" * 60)
print("MISSION 076 - LEARNING ACTION OUTCOME TRACKER TEST")
print("=" * 60)

memory = Memory()

tracker = LearningActionOutcomeTracker()

report = tracker.analyze(memory)

print()
print("📊 Learning Action Outcome")
print()

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print()
print(f"📊 Outcome: {report['outcome']}")
print(f"📈 Status: {report['status']}")

print()
print("📌 Signals:")

for signal in report["signals"]:
    print(f"• {signal}")

print()
print("➡️ Recommendation:")
print(report["recommendation"])

assert "outcome" in report
assert "status" in report
assert "signals" in report
assert "recommendation" in report

print()
print("=" * 60)
print("✅ Learning Action Outcome Tracker Test Completed Successfully!")
print("=" * 60)