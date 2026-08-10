from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte

print("=" * 60)
print("MISSION 050 - BYTE WEAKNESS ANALYSIS TEST")
print("=" * 60)

memory = Memory()

# Simulate learning weaknesses
memory.increment_retries_completed()
memory.increment_retries_completed()
memory.increment_retries_completed()

brain = create_test_byte(memory)

response = brain.get_weakness_analysis()

print()
print(response)

assert "Consistency" in response
assert "Goal Completion" in response
assert "Learning Activity" in response
assert "Repeated Difficulty" in response
assert "Mission Progress" in response
assert "Weakness Status: Needs Attention" in response

print("\n" + "=" * 60)
print("✅ Byte Weakness Analysis Test Completed Successfully!")
print("=" * 60)