from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 058 - BYTE ADAPTIVE DIFFICULTY ANALYSIS TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate a strong learner
# ==================================================

memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_retries_completed()
memory.increment_retries_completed()


byte = create_test_byte(memory)

response = byte.get_adaptive_difficulty()

print("\n" + response)


assert "Your Adaptive Difficulty Analysis" in response

assert "Difficulty: Harder" in response

assert "Learning Streak: 3" in response

assert "Daily Goals: 2" in response

assert "Missions: 5" in response

assert "Lessons: 2" in response

assert "Retries: 2" in response

assert "Positive Signals: 12" in response

assert "Difficulty Signals: 2" in response

assert "greater challenge" in response


print("\n" + "=" * 60)
print("✅ Byte Adaptive Difficulty Analysis Test Completed Successfully!")
print("=" * 60)