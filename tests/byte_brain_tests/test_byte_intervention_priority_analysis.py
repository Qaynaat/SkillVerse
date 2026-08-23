from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 067 - BYTE INTERVENTION PRIORITY ANALYSIS TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate Learner
# ==================================================

for _ in range(2):
    memory.increment_learning_streak()

memory.increment_completed_daily_goals()

for _ in range(2):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")

memory.increment_modules_read()

for _ in range(5):
    memory.increment_retries_completed()


# ==================================================
# Create Byte
# ==================================================

byte = create_test_byte(memory)


print("\n🎯 Your Intervention Priority Analysis\n")

result = byte.get_intervention_priority_analysis()

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

assert "Targeted Revision (Critical)" in result
assert "Difficulty Reduction (High)" in result
assert "Goal Reduction (High)" in result
assert "Consistency Reset (High)" in result
assert "Mission Simplification (High)" in result

assert "Primary Intervention" in result
assert "🎯 Targeted Revision" in result
assert "📈 Priority: Critical" in result


print("\n" + "=" * 60)
print(
    "✅ Byte Intervention Priority Analysis Test "
    "Completed Successfully!"
)
print("=" * 60)