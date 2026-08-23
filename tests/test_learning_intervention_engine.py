from src.core.memory import Memory
from src.core.learning_intervention_engine import LearningInterventionEngine


print("=" * 60)
print("MISSION 066 - LEARNING INTERVENTION ENGINE TEST")
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

engine = LearningInterventionEngine()

report = engine.analyze(memory)


# ==================================================
# Display
# ==================================================

print("\n🎯 Learning Intervention Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print("\n⚠️ Intervention Signals:")

for signal in report["signals"]:
    print(f"• {signal}")

print(f"\n🛠 Intervention: {report['intervention_type']}")
print(f"📈 Priority: {report['priority']}")

print("\n🔎 Reason:")
print(report["reason"])

print("\n🎯 Action:")
print(report["action"])

print("\n🌱 Expected Outcome:")
print(report["expected_outcome"])


# ==================================================
# Assertions
# ==================================================

assert report["learning_streak"] == 2
assert report["completed_daily_goals"] == 1
assert report["completed_missions"] == 2
assert report["completed_lessons"] == 1
assert report["modules_read"] == 1
assert report["retries"] == 5

assert "Repeated Difficulty" in report["signals"]
assert "High Retry Load" in report["signals"]
assert "Low Daily Goal Completion" in report["signals"]
assert "Weak Consistency" in report["signals"]
assert "Low Mission Completion" in report["signals"]

assert report["intervention_type"] == "Targeted Revision"
assert report["priority"] == "Critical"

assert "Repeated attempts" in report["reason"]

assert (
    "Review difficult concepts"
    in report["action"]
)

assert (
    "Improved understanding"
    in report["expected_outcome"]
)


print("\n" + "=" * 60)
print("✅ Learning Intervention Engine Test Completed Successfully!")
print("=" * 60)