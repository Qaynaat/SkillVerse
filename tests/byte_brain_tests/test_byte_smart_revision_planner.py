from src.core.byte_brain import ByteBrain
from src.core.memory import Memory
from src.core.save_system import SaveSystem
from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 061 - BYTE SMART REVISION PLANNER TEST")
print("=" * 60)


memory = Memory()
services = BrainServices.default()
save_system = SaveSystem()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=save_system,
)


# ==================================================
# Simulate learning activity
# ==================================================

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

for _ in range(5):
    memory.increment_retries_completed()


# ==================================================
# Generate Byte's Smart Revision Response
# ==================================================

response = byte.get_smart_revision_plan()


print("\n🧠 Byte's Smart Revision Report\n")
print(response)


# ==================================================
# Assertions
# ==================================================

assert "Smart Revision Plan" in response
assert "High" in response
assert "2" in response
assert "5" in response
assert "repeated attempts" in response


print("\n" + "=" * 60)
print("✅ Byte Smart Revision Planner Test Completed Successfully!")
print("=" * 60)