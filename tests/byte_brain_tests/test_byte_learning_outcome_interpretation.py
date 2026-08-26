from src.core.byte_brain import ByteBrain
from src.core.memory import Memory
from src.core.save_system import SaveSystem
from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 077 - BYTE LEARNING OUTCOME INTERPRETATION TEST")
print("=" * 60)

memory = Memory()
save_system = SaveSystem("data/test_byte_learning_outcome.json")
services = BrainServices.default()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system
)

response = byte.analyze_learning_outcome("Difficult")

print("\n🧠 Your Learning Outcome Interpretation\n")
print(response)

assert "Difficult" in response
assert "Learning Difficulty" in response
assert "difficult concept" in response

print("=" * 60)
print("✅ Byte Learning Outcome Interpretation Test Completed Successfully!")
print("=" * 60)