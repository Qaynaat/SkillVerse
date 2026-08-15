from src.core.memory import Memory
from src.core.productivity_analyzer import ProductivityAnalyzer


print("=" * 60)
print("MISSION 055 - PRODUCTIVITY ANALYZER TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate productive learning activity
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


analyzer = ProductivityAnalyzer()

report = analyzer.analyze(memory)


print("\n📊 Productivity Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print(f"⚡ Productivity Score: {report['productivity_score']}")
print(f"📈 Productivity Status: {report['productivity_status']}")

print(f"\n💡 {report['observation']}")


assert report["learning_streak"] == 3
assert report["completed_daily_goals"] == 2
assert report["completed_missions"] == 5
assert report["completed_lessons"] == 2
assert report["modules_read"] == 2
assert report["retries"] == 3

assert report["productivity_score"] == 17
assert report["productivity_status"] == "Productive"


print("\n" + "=" * 60)
print("✅ Productivity Analyzer Test Completed Successfully!")
print("=" * 60)