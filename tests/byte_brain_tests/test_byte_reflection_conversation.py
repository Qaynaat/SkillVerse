from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 090 - BYTE REFLECTION CONVERSATION TEST")
print("=" * 60)

services = BrainServices.default()

byte = ByteBrain(
    services=services,
    memory=None,
    save_system=None
)

response = byte.reflect_on_learning(
    "struggling",
    "I found Python functions difficult today."
)

print(response)

assert "Reflection Conversation" in response
assert "struggling" in response.lower()
assert "Python functions" in response
assert "Reflection Question" in response

print("=" * 60)
print("✅ Byte Reflection Conversation Test Completed Successfully!")
print("=" * 60)