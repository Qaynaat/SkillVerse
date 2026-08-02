from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte

print("=" * 60)
print("        BYTE REFLECTION TEST")
print("=" * 60)

# ----------------------------------------------------
# Create Memory
# ----------------------------------------------------

memory = Memory()

brain = create_test_byte(memory)

# ----------------------------------------------------
# Test Reflection
# ----------------------------------------------------

print()
print(brain.get_learning_reflection())

print()
print("=" * 60)
print("✅ Byte Reflection Test Completed Successfully!")