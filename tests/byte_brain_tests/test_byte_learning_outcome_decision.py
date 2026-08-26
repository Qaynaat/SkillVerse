from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.save_system import SaveSystem


print("=" * 60)
print("MISSION 078 - BYTE LEARNING OUTCOME DECISION TEST")
print("=" * 60)

services = BrainServices.default()
memory = Memory()
save_system = SaveSystem("data/test_byte_learning_outcome_decision.json")

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system
)

outcome_report = {
    "outcome": "Difficult"
}

response = byte.analyze_learning_outcome_decision(
    outcome_report
)

print(response)

assert "Targeted Revision" in response
assert "Critical" in response
assert "Review" in response
assert "Next Step" in response

print("\n" + "=" * 60)
print("✅ Byte Learning Outcome Decision Test Completed Successfully!")
print("=" * 60)