from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 056 - BYTE SMART GOAL ANALYSIS TEST")
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


byte = create_test_byte(memory)

response = byte.get_smart_goal()

print("\n" + response)


assert "Your Smart Learning Goal" in response
assert "Complete 2 learning missions today." in response
assert "Priority: High" in response
assert "Learning Streak: 3" in response
assert "Daily Goals: 2" in response
assert "Missions: 3" in response
assert "Lessons: 2" in response
assert "Modules Read: 2" in response
assert "Retries: 3" in response


print("\n" + "=" * 60)
print("✅ Byte Smart Goal Analysis Test Completed Successfully!")
print("=" * 60)