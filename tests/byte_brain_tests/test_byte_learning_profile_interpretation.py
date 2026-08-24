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
print("MISSION 071 - BYTE LEARNING PROFILE INTERPRETATION TEST")
print("=" * 60)

print()

response = byte.get_learning_profile_interpretation()

print(response)

print()
print("=" * 60)
print("✅ Byte Learning Profile Interpretation Test Completed Successfully!")
print("=" * 60)