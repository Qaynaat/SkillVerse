from src.core.memory import Memory
from src.core.burnout_detector import BurnoutDetector


print("=" * 60)
print("MISSION 053 - BURNOUT DETECTOR TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate learning pressure
# ==================================================

memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

# No completed daily goals

for _ in range(5):
    memory.increment_completed_missions()

for _ in range(5):
    memory.increment_modules_read()

for _ in range(3):
    memory.increment_retries_completed()


detector = BurnoutDetector()

report = detector.analyze(memory)


print("\n🔥 Burnout Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print(f"⚠️ Burnout Signals: {report['burnout_signals']}")
print(f"📈 Burnout Status: {report['burnout_status']}")

print(f"\n💡 {report['observation']}")


assert report["learning_streak"] == 3
assert report["completed_daily_goals"] == 0
assert report["completed_missions"] == 5
assert report["modules_read"] == 5
assert report["retries"] == 3

assert "Repeated Difficulty" in report["burnout_signals"]
assert "High Mission Load" in report["burnout_signals"]
assert "High Study Load" in report["burnout_signals"]
assert "Goal Imbalance" in report["burnout_signals"]

assert report["burnout_status"] == "High Risk"


print("\n" + "=" * 60)
print("✅ Burnout Detector Test Completed Successfully!")
print("=" * 60)