from src.core.services.brain_services import BrainServices
from src.core.byte_brain import ByteBrain
from src.core.memory import Memory
from src.core.save_system import SaveSystem


print("=" * 60)
print("MISSION 084 - BYTE INTERNSHIP RECOMMENDATION TEST")
print("=" * 60)

services = BrainServices.default()

memory = Memory()

save_system = SaveSystem(
    "data/test_byte_internship_recommendation.json"
)

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system
)

response = byte.get_internship_recommendation(
    "Software Engineering"
)

print(response)

assert "Internship Recommendation" in response
assert "Software Engineering" in response
assert "Intern" in response
assert "Preparation Skills" in response

print("=" * 60)
print("✅ Byte Internship Recommendation Test Completed Successfully!")
print("=" * 60)