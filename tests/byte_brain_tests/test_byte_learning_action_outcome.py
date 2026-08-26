from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.byte_brain import ByteBrain
from src.core.save_system import SaveSystem


print("=" * 60)
print("MISSION 076 - BYTE LEARNING ACTION OUTCOME TEST")
print("=" * 60)

memory = Memory()

services = BrainServices.default()

save_system = SaveSystem(
    "data/test_byte_learning_action_outcome.json"
)

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system
)

response = byte.get_learning_action_outcome()

print()
print(response)
print()

assert "Your Learning Action Outcome" in response
assert "Outcome:" in response
assert "Status:" in response
assert "Recommendation:" in response
assert "Signals:" in response

print("=" * 60)
print("✅ Byte Learning Action Outcome Test Completed Successfully!")
print("=" * 60)