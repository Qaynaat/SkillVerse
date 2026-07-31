from src.core.learning_insights import LearningInsights
from src.core.memory import Memory

print("=" * 60)
print("      LEARNING INSIGHTS TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(180)

for _ in range(6):
    memory.increment_completed_missions()

memory.advance_step()

engine = LearningInsights()

print()
report = engine.generate(memory)

print()
print("📊 Learning Insights")
print()

for key, value in report.items():
    print(f"{key}: {value}")

print()
print("=" * 60)
print("✅ Learning Insights Test Completed Successfully!")