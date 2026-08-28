from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 089 - BYTE EMPATHETIC RESPONSE TEST")
print("=" * 60)

services = BrainServices.default()

byte = ByteBrain(
    services=services,
    memory=None,
    save_system=None
)

response = byte.analyze_empathetic_response(
    "struggling"
)

print(response)

assert "Empathetic Response" in response
assert "struggling" in response.lower()
assert "Byte Response" in response

print("=" * 60)
print("✅ Byte Empathetic Response Test Completed Successfully!")
print("=" * 60)