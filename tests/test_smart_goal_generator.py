from src.core.memory import Memory
from src.core.smart_goal_generator import SmartGoalGenerator


print("=" * 60)
print("MISSION 056 - SMART GOAL GENERATOR TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate a productive learner
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


generator = SmartGoalGenerator()

report = generator.generate(memory)


print("\n🎯 Smart Goal Report\n")

print(f"🎯 Goal: {report['goal']}")
print(f"📈 Priority: {report['priority']}")

print(
    f"\n🔥 Learning Streak: {report['learning_streak']}"
)

print(
    f"🎯 Daily Goals: {report['completed_daily_goals']}"
)

print(
    f"✅ Missions: {report['completed_missions']}"
)

print(
    f"📚 Lessons: {report['completed_lessons']}"
)

print(
    f"📖 Modules Read: {report['modules_read']}"
)

print(
    f"🔁 Retries: {report['retries']}"
)

print(f"\n💡 {report['reason']}")


assert report["goal"] == "Complete 2 learning missions today."

assert report["priority"] == "High"

assert report["learning_streak"] == 3

assert report["completed_daily_goals"] == 2

assert report["completed_missions"] == 3

assert report["completed_lessons"] == 2

assert report["modules_read"] == 2

assert report["retries"] == 3



print("\n" + "=" * 60)
print("✅ Smart Goal Generator Test Completed Successfully!")
print("=" * 60)