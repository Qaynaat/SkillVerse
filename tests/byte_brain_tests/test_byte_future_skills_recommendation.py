from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.byte_brain import ByteBrain
from src.core.save_system import SaveSystem


print("=" * 60)
print("MISSION 083 - BYTE FUTURE SKILLS RECOMMENDATION TEST")
print("=" * 60)

services = BrainServices.default()
memory = Memory()

save_system = SaveSystem(
    "data/test_byte_future_skills_recommendation.json"
)

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system
)

response = byte.recommend_future_skills(
    "Software Engineering",
    [
        "Problem Solving",
        "Programming",
        "Communication"
    ]
)

print(response)

assert "Future Skills Recommendation" in response
assert "Software Engineering" in response
assert "AI-assisted development" in response

print("=" * 60)
print("✅ Byte Future Skills Recommendation Test Completed Successfully!")
print("=" * 60)
