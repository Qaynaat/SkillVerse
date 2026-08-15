from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 054 - BYTE CONFIDENCE ANALYSIS TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate strong learning confidence
# ==================================================

for _ in range(3):
    memory.increment_learning_streak()

for _ in range(2):
    memory.increment_completed_daily_goals()

for _ in range(5):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

for _ in range(3):
    memory.increment_retries_completed()

memory.increment_categories_explored()
memory.increment_categories_explored()


brain = create_test_byte(memory)

response = brain.get_confidence_analysis()


print("\n🎯 Your Learning Confidence Analysis\n")
print(response)


assert "Learning Streak: 3" in response
assert "Daily Goals: 2" in response
assert "Missions: 5" in response
assert "Lessons: 2" in response
assert "Modules Read: 2" in response
assert "Retries: 3" in response
assert "Categories Explored: 2" in response

assert "Confidence Score: 10" in response
assert "Confidence Level: High" in response


print("\n" + "=" * 60)
print("✅ Byte Confidence Analysis Test Completed Successfully!")
print("=" * 60)