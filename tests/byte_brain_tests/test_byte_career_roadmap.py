from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.byte_brain import ByteBrain



print("=" * 60)
print("MISSION 081 - BYTE CAREER ROADMAP TEST")
print("=" * 60)

services = BrainServices.default()
memory = Memory()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=None
)

response = byte.get_career_roadmap(
    "Software Engineering"
)

print(response)

assert "Career Roadmap" in response
assert "Software Engineering" in response
assert "Foundations" in response
assert "Core Skills" in response
assert "Career Preparation" in response
assert "Programming" in response
assert "Backend Developer" in response

print("\n" + "=" * 60)
print("✅ Byte Career Roadmap Test Completed Successfully!")
print("=" * 60)