from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 059 - BYTE MISSION RECOMMENDATION TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate repeated difficulty
# ==================================================

memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

for _ in range(5):
    memory.increment_retries_completed()

memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()


byte = create_test_byte(memory)

response = byte.get_mission_recommendation()


print("\n🎯 Your Mission Recommendation\n")
print(response)


assert "Mission Recommendation" in response
assert "Review a previously difficult concept." in response
assert "Priority: High" in response


print("\n" + "=" * 60)
print("✅ Byte Mission Recommendation Test Completed Successfully!")
print("=" * 60)