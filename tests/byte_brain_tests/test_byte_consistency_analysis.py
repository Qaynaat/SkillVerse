from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 049 - BYTE CONSISTENCY ANALYSIS TEST")
print("=" * 60)

memory = Memory()

# Simulate consistent learning activity
memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.add_streak_day("2026-08-01")
memory.add_streak_day("2026-08-02")
memory.add_streak_day("2026-08-03")

brain = create_test_byte(memory)

response = brain.get_consistency_analysis()

print("\n📈 Your Learning Consistency Analysis\n")
print(response)

assert "Learning Streak: 3" in response
assert "Daily Goals: 2" in response
assert "Streak Days Recorded: 3" in response
assert "Consistency Status: Consistent" in response

print("\n" + "=" * 60)
print("✅ Byte Consistency Analysis Test Completed Successfully!")
print("=" * 60)