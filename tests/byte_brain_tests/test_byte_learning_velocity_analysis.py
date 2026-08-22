from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 062 - BYTE LEARNING VELOCITY ANALYSIS TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate learner activity
# ==================================================

for _ in range(3):
    memory.increment_learning_streak()

for _ in range(2):
    memory.increment_completed_daily_goals()

for _ in range(5):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

for _ in range(2):
    memory.increment_modules_read()

for _ in range(2):
    memory.increment_retries_completed()


# ==================================================
# Create Byte
# ==================================================

byte = create_test_byte(memory)


# ==================================================
# Run Byte Analysis
# ==================================================

print("\n📈 Your Learning Velocity Analysis\n")

result = byte.get_learning_velocity_analysis()

print(result)


# ==================================================
# Assertions
# ==================================================

assert "Learning Streak: 3" in result
assert "Daily Goals: 2" in result
assert "Missions: 5" in result
assert "Lessons: 2" in result
assert "Modules Read: 2" in result
assert "Retries: 2" in result

assert "Velocity Score: 23" in result
assert "Velocity Status: High Velocity" in result


print("\n" + "=" * 60)
print("✅ Byte Learning Velocity Analysis Test Completed Successfully!")
print("=" * 60)
