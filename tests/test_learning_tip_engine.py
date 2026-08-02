from src.core.engine.learning_tip_engine import LearningTipEngine
from src.core.memory import Memory

print("=" * 60)
print("      LEARNING TIP ENGINE TEST")
print("=" * 60)

memory = Memory()

for _ in range(9):
    memory.increment_completed_missions()

engine = LearningTipEngine()

report = engine.get_tip(memory)

print()

print("💡 Today's Learning Tip")

print()

print(report["tip"])

print()

print("=" * 60)
print("✅ Learning Tip Engine Test Completed Successfully!")