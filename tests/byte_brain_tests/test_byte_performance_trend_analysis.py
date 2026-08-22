from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 063 - BYTE PERFORMANCE TREND ANALYSIS TEST")
print("=" * 60)


# ==================================================
# Create Memory
# ==================================================

memory = Memory()


# ==================================================
# Simulate Learning Activity
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
# Run Performance Trend Analysis
# ==================================================

print("\n📊 Your Performance Trend Analysis\n")

result = byte.get_performance_trend_analysis()

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

assert "Positive Signals: 14" in result
assert "Difficulty Signals: 2" in result
assert "Performance Score: 12" in result
assert "Trend Status: Improving" in result

assert (
    "Your recent learning activity shows positive performance growth."
    in result
)


# ==================================================
# Success
# ==================================================

print("\n" + "=" * 60)
print("✅ Byte Performance Trend Analysis Test Completed Successfully!")
print("=" * 60)