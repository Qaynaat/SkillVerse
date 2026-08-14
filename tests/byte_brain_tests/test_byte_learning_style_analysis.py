from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte

print("=" * 60)
print("MISSION 052 - BYTE LEARNING STYLE ANALYSIS TEST")
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

brain = create_test_byte(memory)

response = brain.get_learning_style_analysis()

print("\n🧠 Your Learning Style Analysis\n")
print(response)

assert "Learning Style: Practice-Oriented" in response
assert "Reading Score: 2" in response
assert "Practice Score: 5" in response
assert "Goal Score: 3" in response
assert "Exploration Score: 1" in response
assert "Interactive Score: 1" in response

print("\n" + "=" * 60)
print("✅ Byte Learning Style Analysis Test Completed Successfully!")
print("=" * 60)