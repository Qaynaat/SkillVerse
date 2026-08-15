from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("MISSION 053 - BYTE BURNOUT ANALYSIS TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate learning pressure
# ==================================================

memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

for _ in range(5):
    memory.increment_completed_missions()

for _ in range(5):
    memory.increment_modules_read()

for _ in range(3):
    memory.increment_retries_completed()


brain = create_test_byte(memory)

response = brain.get_burnout_analysis()


print("\n🔥 Your Learning Burnout Analysis\n")
print(response)


assert "Learning Streak: 3" in response
assert "Daily Goals: 0" in response
assert "Missions: 5" in response
assert "Modules Read: 5" in response
assert "Retries: 3" in response

assert "Repeated Difficulty" in response
assert "High Mission Load" in response
assert "High Study Load" in response
assert "Goal Imbalance" in response

assert "Burnout Status: High Risk" in response


print("\n" + "=" * 60)
print("✅ Byte Burnout Analysis Test Completed Successfully!")
print("=" * 60)