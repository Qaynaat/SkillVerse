from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte

print("=" * 60)
print("      BYTE ENCOURAGEMENT TEST")
print("=" * 60)

memory = Memory()

brain = create_test_byte(memory)

print()
print(brain.get_encouragement())

print()
print("=" * 60)
print("✅ Byte Encouragement Test Completed Successfully!")