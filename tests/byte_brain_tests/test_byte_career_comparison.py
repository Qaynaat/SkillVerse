from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.byte_brain import ByteBrain
from src.core.save_system import SaveSystem


print("=" * 60)
print("MISSION 080 - BYTE CAREER COMPARISON TEST")
print("=" * 60)


services = BrainServices.default()
memory = Memory()

save_system = SaveSystem(
    "data/test_byte_career_comparison.json"
)


byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system
)


response = byte.compare_careers(
    "Software Engineering",
    "Cybersecurity"
)


print(response)


assert "Career Comparison" in response
assert "Software Engineering" in response
assert "Cybersecurity" in response


print()
print("=" * 60)
print("✅ Byte Career Comparison Test Completed Successfully!")
print("=" * 60)