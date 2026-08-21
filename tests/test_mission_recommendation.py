from src.core.memory import Memory
from src.core.mission_recommendation import MissionRecommendation


print("=" * 60)
print("MISSION 059 - MISSION RECOMMENDATION TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate a learner with repeated difficulty
# ==================================================

memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

memory.increment_retries_completed()
memory.increment_retries_completed()
memory.increment_retries_completed()
memory.increment_retries_completed()
memory.increment_retries_completed()


engine = MissionRecommendation()

report = engine.analyze(memory)


print("\n🎯 Mission Recommendation Report\n")

print(f"🎯 Recommendation: {report['recommendation']}")
print(f"📈 Priority: {report['priority']}")

print(f"\n🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print(f"\n💡 {report['reason']}")


assert report["recommendation"] == (
    "Review a previously difficult concept."
)

assert report["priority"] == "High"

assert report["learning_streak"] == 3
assert report["completed_daily_goals"] == 2
assert report["completed_missions"] == 3
assert report["completed_lessons"] == 2
assert report["modules_read"] == 2
assert report["retries"] == 5


print("\n" + "=" * 60)
print("✅ Mission Recommendation Test Completed Successfully!")
print("=" * 60)