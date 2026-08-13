from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte

print("=" * 60)
print("MISSION 051 - BYTE STRENGTH ANALYSIS TEST")
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

brain = create_test_byte(memory)

response = brain.get_strength_analysis()

print("\n💪 Your Learning Strength Analysis\n")
print(response)

assert "Learning Streak: 3" in response
assert "Daily Goals: 2" in response
assert "Missions: 2" in response
assert "Lessons: 2" in response
assert "Modules Read: 2" in response
assert "Retries: 3" in response

assert "Consistency" in response
assert "Goal Achievement" in response
assert "Mission Completion" in response
assert "Learning Activity" in response
assert "Persistence" in response

assert "Strength Status: Excellent" in response

print("\n" + "=" * 60)
print("✅ Byte Strength Analysis Test Completed Successfully!")
print("=" * 60)