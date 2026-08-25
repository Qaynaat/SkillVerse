from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.byte_brain import ByteBrain
from src.core.save_system import SaveSystem


print("=" * 60)
print("MISSION 075 - BYTE LEARNING ACTION FOLLOW-UP TEST")
print("=" * 60)

# ==================================================
# Fresh learner state
# ==================================================

memory = Memory()

services = BrainServices.default()

save_system = SaveSystem(
    "data/test_byte_learning_action_followup.json"
)

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system
)

# ==================================================
# Generate Byte follow-up
# ==================================================

response = byte.get_learning_action_followup()

print()
print(response)
print()

# ==================================================
# Assertions
# ==================================================

assert "Your Learning Action Follow-Up" in response
assert "Stable Learner" in response
assert "Consistency" in response
assert "High" in response
assert "Record today's completed learning activity." in response
assert "Return tomorrow and complete another small learning goal." in response
assert "Completion Rule" in response

print("=" * 60)
print("✅ Byte Learning Action Follow-Up Test Completed Successfully!")
print("=" * 60)