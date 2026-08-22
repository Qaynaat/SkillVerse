from src.core.memory import Memory
from src.core.learning_velocity_tracker import LearningVelocityTracker


print("=" * 60)
print("MISSION 062 - LEARNING VELOCITY TRACKER TEST")
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

for _ in range(2):
    memory.increment_retries_completed()


tracker = LearningVelocityTracker()

report = tracker.analyze(memory)


print("\n📈 Learning Velocity Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print(f"📊 Velocity Score: {report['velocity_score']}")
print(f"📈 Velocity Status: {report['velocity_status']}")

print(f"\n💡 {report['observation']}")


assert report["learning_streak"] == 3
assert report["completed_daily_goals"] == 2
assert report["completed_missions"] == 5
assert report["completed_lessons"] == 2
assert report["modules_read"] == 2
assert report["retries"] == 2

assert report["velocity_score"] == 23
assert report["velocity_status"] == "High Velocity"


print("\n" + "=" * 60)
print("✅ Learning Velocity Tracker Test Completed Successfully!")
print("=" * 60)