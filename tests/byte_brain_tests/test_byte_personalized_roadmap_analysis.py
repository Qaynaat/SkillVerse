from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 057 - BYTE PERSONALIZED ROADMAP ANALYSIS TEST")
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

response = byte.get_personalized_roadmap()

print("\n" + response)


assert "Your Personalized Learning Roadmap" in response

assert "Current Stage: Building Momentum" in response

assert "Strengthen your learning routine through consistent practice." in response

assert "Complete 2 learning missions." in response

assert "Finish 1 learning lesson." in response

assert "Review a previously difficult concept." in response

assert "Maintain your daily learning goal." in response

assert "Priority: High" in response


print("\n" + "=" * 60)
print("✅ Byte Personalized Roadmap Analysis Test Completed Successfully!")
print("=" * 60)
