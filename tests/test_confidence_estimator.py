from src.core.memory import Memory
from src.core.confidence_estimator import ConfidenceEstimator


print("=" * 60)
print("MISSION 054 - CONFIDENCE ESTIMATOR TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate strong learning confidence
# ==================================================

for _ in range(3):
    memory.increment_learning_streak()

for _ in range(2):
    memory.increment_completed_daily_goals()

for _ in range(5):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

for _ in range(3):
    memory.increment_retries_completed()

memory.increment_categories_explored()
memory.increment_categories_explored()


estimator = ConfidenceEstimator()

report = estimator.analyze(memory)


print("\n🎯 Confidence Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")
print(f"🔎 Categories Explored: {report['categories_explored']}")

print(f"⭐ Confidence Score: {report['confidence_score']}")
print(f"📈 Confidence Level: {report['confidence_level']}")

print(f"\n💡 {report['observation']}")


assert report["learning_streak"] == 3
assert report["completed_daily_goals"] == 2
assert report["completed_missions"] == 5
assert report["completed_lessons"] == 2
assert report["modules_read"] == 2
assert report["retries"] == 3
assert report["categories_explored"] == 2

assert report["confidence_score"] == 10
assert report["confidence_level"] == "High"


print("\n" + "=" * 60)
print("✅ Confidence Estimator Test Completed Successfully!")
print("=" * 60)