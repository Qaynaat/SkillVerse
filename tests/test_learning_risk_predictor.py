from src.core.memory import Memory
from src.core.learning_risk_predictor import LearningRiskPredictor


print("=" * 60)
print("MISSION 064 - LEARNING RISK PREDICTOR TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate learner activity
# ==================================================

for _ in range(3):
    memory.increment_learning_streak()

for _ in range(2):
    memory.increment_completed_daily_goals()

for _ in range(5):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

for _ in range(2):
    memory.increment_modules_read()

for _ in range(5):
    memory.increment_retries_completed()


# ==================================================
# Analyze
# ==================================================

predictor = LearningRiskPredictor()

report = predictor.analyze(memory)


# ==================================================
# Display
# ==================================================

print("\n🚨 Learning Risk Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print("\n⚠️ Risk Signals:")

for signal in report["risk_signals"]:
    print(f"• {signal}")

print(f"\n🟢 Positive Signals: {report['positive_signals']}")
print(f"📊 Risk Score: {report['risk_score']}")
print(f"📈 Risk Status: {report['risk_status']}")

print(f"\n💡 {report['observation']}")


# ==================================================
# Assertions
# ==================================================

assert report["learning_streak"] == 3
assert report["completed_daily_goals"] == 2
assert report["completed_missions"] == 5
assert report["completed_lessons"] == 2
assert report["modules_read"] == 2
assert report["retries"] == 5

assert "Repeated Difficulty" in report["risk_signals"]
assert "High Retry Load" in report["risk_signals"]

assert report["positive_signals"] == 5

assert report["risk_score"] == -3
assert report["risk_status"] == "Low Risk"


print("\n" + "=" * 60)
print("✅ Learning Risk Predictor Test Completed Successfully!")
print("=" * 60)