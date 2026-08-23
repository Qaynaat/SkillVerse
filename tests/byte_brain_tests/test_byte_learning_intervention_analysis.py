from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 066 - BYTE LEARNING INTERVENTION ANALYSIS TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate Learner Activity
# ==================================================

for _ in range(2):
    memory.increment_learning_streak()

for _ in range(1):
    memory.increment_completed_daily_goals()

for _ in range(2):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")

for _ in range(1):
    memory.increment_modules_read()

for _ in range(5):
    memory.increment_retries_completed()


# ==================================================
# Create Byte
# ==================================================

byte = create_test_byte(memory)


# ==================================================
# Run Byte Analysis
# ==================================================

print("\n🎯 Your Learning Intervention Analysis\n")

result = byte.get_learning_intervention_analysis()

print(result)


# ==================================================
# Assertions
# ==================================================

assert "Learning Streak: 2" in result
assert "Daily Goals: 1" in result
assert "Missions: 2" in result
assert "Lessons: 1" in result
assert "Modules Read: 1" in result
assert "Retries: 5" in result

assert "Repeated Difficulty" in result
assert "High Retry Load" in result
assert "Low Daily Goal Completion" in result
assert "Weak Consistency" in result
assert "Low Mission Completion" in result

assert "Intervention: Targeted Revision" in result
assert "Priority: Critical" in result

assert "Repeated attempts" in result
assert "Review difficult concepts" in result
assert "Improved understanding" in result


print("\n" + "=" * 60)
print("✅ Byte Learning Intervention Analysis Test Completed Successfully!")
print("=" * 60)