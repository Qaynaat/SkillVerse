from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.byte_brain import ByteBrain


print("=" * 60)
print("MISSION 082 - BYTE CAREER READINESS SCORE TEST")
print("=" * 60)

services = BrainServices.default()
memory = Memory()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=None
)

# If your ByteBrain currently requires a real SaveSystem,
# use the same SaveSystem setup used by your other Byte tests.

response = byte.get_career_readiness_score(
    "Software Engineering",
    [
        "Problem Solving",
        "Programming",
        "Communication"
    ]
)

print(response)

assert "Career Readiness Score" in response
assert "Software Engineering" in response
assert "43%" in response
assert "Developing" in response
assert "Teamwork" in response
assert "Debugging" in response

print("=" * 60)
print("✅ Byte Career Readiness Score Test Completed Successfully!")
print("=" * 60)