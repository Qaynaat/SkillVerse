from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 048 - BYTE HABIT ANALYSIS TEST")
print("=" * 60)

memory = Memory()

brain = create_test_byte(memory)

# Simulate learning activity AFTER ByteBrain loads saved data
brain.memory.increment_learning_streak()
brain.memory.increment_learning_streak()
brain.memory.increment_learning_streak()

brain.memory.increment_completed_missions()
brain.memory.increment_completed_missions()

brain.memory.increment_completed_daily_goals()
brain.memory.increment_completed_daily_goals()

brain.memory.complete_lesson("Python Basics")
brain.memory.complete_lesson("OOP Basics")

response = brain.get_habit_analysis()

print("\n" + response)

assert "Learning Streak: 3" in response
assert "Missions: 2" in response
assert "Daily Goals: 2" in response
assert "Lessons: 2" in response
assert "Habit Status: Consistent" in response

print("\n" + "=" * 60)
print("✅ Byte Habit Analysis Test Completed Successfully!")
print("=" * 60)