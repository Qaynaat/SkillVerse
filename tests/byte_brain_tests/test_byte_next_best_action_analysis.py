from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 061 - BYTE NEXT BEST ACTION ANALYSIS TEST")
print("=" * 60)

memory = Memory()

memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

memory.increment_completed_daily_goals()

for _ in range(5):
    memory.increment_retries_completed()

byte = create_test_byte(memory)

print("\n🎯 Your Next Best Learning Action\n")

result = byte.get_next_best_action_analysis()

print(result)

assert "Review a difficult concept before starting new work." in result
assert "Priority: High" in result

print("\n" + "=" * 60)
print("✅ Byte Next Best Action Analysis Test Completed Successfully!")
print("=" * 60)