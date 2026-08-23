from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 065 - BYTE LEARNING RECOVERY ANALYSIS TEST")
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

print("\n🛟 Your Learning Recovery Analysis\n")

result = byte.get_learning_recovery_analysis()

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
assert "Repeated Attempts" in result
assert "Weak Daily Goal Completion" in result
assert "Weak Learning Consistency" in result
assert "Low Mission Completion" in result

assert "Recovery Score: 5" in result
assert "Recovery Level: Intensive Recovery" in result

assert "Review concepts that required repeated attempts." in result
assert "Practice difficult concepts before starting new work." in result
assert "Set a smaller and achievable daily learning goal." in result
assert "Rebuild consistency with short daily learning sessions." in result
assert "Complete a manageable learning mission to rebuild momentum." in result

assert "Reduce workload" in result
assert "recovery should take priority" in result


print("\n" + "=" * 60)
print("✅ Byte Learning Recovery Analysis Test Completed Successfully!")
print("=" * 60)