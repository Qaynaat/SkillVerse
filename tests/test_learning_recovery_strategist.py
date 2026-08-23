from src.core.memory import Memory
from src.core.learning_recovery_strategist import LearningRecoveryStrategist


print("=" * 60)
print("MISSION 065 - LEARNING RECOVERY STRATEGIST TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate Learner Activity
# ==================================================

for _ in range(2):
    memory.increment_learning_streak()

for _ in range(1):
    memory.increment_completed_daily_goals()

for _ in range(2):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")

for _ in range(1):
    memory.increment_modules_read()

for _ in range(5):
    memory.increment_retries_completed()


# ==================================================
# Analyze
# ==================================================

strategist = LearningRecoveryStrategist()

report = strategist.analyze(memory)


# ==================================================
# Display
# ==================================================

print("\n🛟 Learning Recovery Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print("\n⚠️ Recovery Signals:")

for signal in report["recovery_signals"]:
    print(f"• {signal}")

print(f"\n📊 Recovery Score: {report['recovery_score']}")
print(f"📈 Recovery Level: {report['recovery_level']}")

print("\n🛟 Recovery Plan:")

for index, step in enumerate(report["recovery_plan"], start=1):
    print(f"{index}. {step}")

print(f"\n🎯 Primary Strategy:")
print(report["primary_strategy"])

print(f"\n💡 {report['observation']}")


# ==================================================
# Assertions
# ==================================================

assert report["learning_streak"] == 2
assert report["completed_daily_goals"] == 1
assert report["completed_missions"] == 2
assert report["completed_lessons"] == 1
assert report["modules_read"] == 1
assert report["retries"] == 5

assert "Repeated Difficulty" in report["recovery_signals"]
assert "Repeated Attempts" in report["recovery_signals"]
assert "Weak Daily Goal Completion" in report["recovery_signals"]
assert "Weak Learning Consistency" in report["recovery_signals"]
assert "Low Mission Completion" in report["recovery_signals"]

assert report["recovery_score"] == 5
assert report["recovery_level"] == "Intensive Recovery"

assert len(report["recovery_plan"]) == 5

assert (
    "Reduce workload"
    in report["primary_strategy"]
)

assert (
    "recovery should take priority"
    in report["observation"]
)


print("\n" + "=" * 60)
print("✅ Learning Recovery Strategist Test Completed Successfully!")
print("=" * 60)