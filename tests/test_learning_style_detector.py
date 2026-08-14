from src.core.memory import Memory
from src.core.learning_style_detector import LearningStyleDetector


print("=" * 60)
print("MISSION 052 - LEARNING STYLE DETECTOR TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate practice-oriented learning
# ==================================================

memory.increment_completed_missions()
memory.increment_completed_missions()

memory.increment_retries_completed()
memory.increment_retries_completed()
memory.increment_retries_completed()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_completed_daily_goals()

memory.increment_categories_explored()

memory.add_message(
    "user",
    "I want to practice this concept again."
)


detector = LearningStyleDetector()

report = detector.analyze(memory)


print("\n🧠 Learning Style Report\n")

print(f"📚 Learning Style: {report['learning_style']}")

print(f"📖 Reading Score: {report['reading_score']}")
print(f"💻 Practice Score: {report['practice_score']}")
print(f"🎯 Goal Score: {report['goal_score']}")
print(f"🔎 Exploration Score: {report['exploration_score']}")
print(f"💬 Interactive Score: {report['interactive_score']}")

print(f"\n💡 {report['observation']}")


assert report["learning_style"] == "Practice-Oriented"

assert report["practice_score"] == 5
assert report["reading_score"] == 2


print("\n" + "=" * 60)
print("✅ Learning Style Detector Test Completed Successfully!")
print("=" * 60)