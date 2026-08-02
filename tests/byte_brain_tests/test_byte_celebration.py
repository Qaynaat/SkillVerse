from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte


print("=" * 60)
print("      BYTE CELEBRATION TEST")
print("=" * 60)

memory = Memory()

brain = create_test_byte(memory)

print()
print(brain.get_celebration())

print()
print("=" * 60)
print("✅ Byte Celebration Test Completed Successfully!")