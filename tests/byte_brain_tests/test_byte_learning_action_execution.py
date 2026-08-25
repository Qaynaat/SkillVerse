from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.save_system import SaveSystem


services = BrainServices.default()
memory = Memory()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=SaveSystem(),
)


print("=" * 60)
print("MISSION 074 - BYTE LEARNING ACTION EXECUTION TEST")
print("=" * 60)

print()

response = byte.get_learning_action_execution()

print(response)

assert response
assert "Learning Action Execution" in response
assert "Start Here" in response
assert "Completion Rule" in response

print()
print("=" * 60)
print(
    "✅ Byte Learning Action Execution Test Completed Successfully!"
)
print("=" * 60)