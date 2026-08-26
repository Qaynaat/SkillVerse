from src.core.byte_brain import ByteBrain
from src.core.memory import Memory
from src.core.save_system import SaveSystem
from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 079 - BYTE LEARNING OUTCOME ACTION PLAN TEST")
print("=" * 60)

memory = Memory()
save_system = SaveSystem("data/test_byte_learning_outcome_action_plan.json")
services = BrainServices.default()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system
)

decision_report = {
    "outcome": "Difficult",
    "decision": "Targeted Revision",
    "priority": "Critical"
}

response = byte.analyze_learning_outcome_action_plan(
    decision_report
)

print(response)

assert "Targeted Revision" in response
assert "Focused Revision Plan" in response
assert "difficult concept" in response.lower()
assert "Completion Rule" in response
assert "Next Action" in response

print("=" * 60)
print("✅ Byte Learning Outcome Action Plan Test Completed Successfully!")
print("=" * 60)