from src.core.memory import Memory
from tests.helpers.create_test_byte import create_test_byte

print("=" * 60)
print("      BYTE SUCCESS PREDICTION TEST")
print("=" * 60)

memory = Memory()
brain = create_test_byte(memory)

print()
print(brain.get_success_prediction())

print()
print("=" * 60)
print("✅ Byte Success Prediction Test Completed Successfully!")