from src.core.memory import Memory
from src.core.adaptive_difficulty import AdaptiveDifficulty


print("=" * 60)
print("MISSION 058 - ADAPTIVE DIFFICULTY TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate a strong learner
# ==================================================

memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_retries_completed()
memory.increment_retries_completed()


engine = AdaptiveDifficulty()

report = engine.analyze(memory)


print("\n⚙️ Adaptive Difficulty Report\n")

print(f"🎚 Difficulty: {report['difficulty']}")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"🔁 Retries: {report['retries']}")

print(f"\n📊 Positive Signals: {report['positive_signals']}")
print(f"⚠️ Difficulty Signals: {report['difficulty_signals']}")

print(f"\n💡 {report['reason']}")


assert report["difficulty"] == "Harder"

assert report["learning_streak"] == 3

assert report["completed_daily_goals"] == 2

assert report["completed_missions"] == 5

assert report["completed_lessons"] == 2

assert report["retries"] == 2

assert report["positive_signals"] == 12

assert report["difficulty_signals"] == 2


print("\n" + "=" * 60)
print("✅ Adaptive Difficulty Test Completed Successfully!")
print("=" * 60)