from src.core.memory import Memory
from src.core.habit_analyzer import HabitAnalyzer


print("=" * 60)
print("MISSION 048 - HABIT ANALYZER TEST")
print("=" * 60)

memory = Memory()

# Simulate learning activity
memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

memory.increment_completed_missions()
memory.increment_completed_missions()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.complete_lesson("Python Basics")
memory.complete_lesson("OOP Basics")

analyzer = HabitAnalyzer()

report = analyzer.analyze(memory)

print("\n📊 Habit Report")
print("-" * 40)

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📅 Streak Days Recorded: {report['streak_days_recorded']}")
print(f"📈 Habit Status: {report['habit_status']}")
print(f"\n💡 {report['observation']}")

assert report["learning_streak"] == 3
assert report["completed_missions"] == 2
assert report["completed_daily_goals"] == 2
assert report["completed_lessons"] == 2
assert report["habit_status"] == "Consistent"

print("\n" + "=" * 60)
print("✅ Habit Analyzer Test Completed Successfully!")
print("=" * 60)