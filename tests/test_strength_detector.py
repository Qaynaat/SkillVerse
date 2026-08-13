from src.core.memory import Memory
from src.core.strength_detector import StrengthDetector

print("=" * 60)
print("MISSION 051 - STRENGTH DETECTOR TEST")
print("=" * 60)

memory = Memory()

# Simulate strong learning behavior

memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.increment_completed_missions()
memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

memory.increment_retries_completed()
memory.increment_retries_completed()
memory.increment_retries_completed()

analyzer = StrengthDetector()

report = analyzer.analyze(memory)

print("\n💪 Strength Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries_completed']}")
print(f"💪 Strengths: {report['strengths']}")
print(f"📈 Strength Status: {report['strength_status']}")
print(f"\n💡 {report['advice']}")

assert "Consistency" in report["strengths"]
assert "Goal Achievement" in report["strengths"]
assert "Mission Completion" in report["strengths"]
assert "Learning Activity" in report["strengths"]
assert "Persistence" in report["strengths"]

assert report["strength_status"] == "Excellent"

print("\n" + "=" * 60)
print("✅ Strength Detector Test Completed Successfully!")
print("=" * 60)