from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte

print("=" * 60)
print("      BYTE LEARNING INSIGHTS TEST")
print("=" * 60)

memory = Memory()
brain = create_test_byte(memory)

print()
print(brain.get_learning_insights())

print()
print("=" * 60)
print("✅ Byte Learning Insights Test Completed Successfully!")