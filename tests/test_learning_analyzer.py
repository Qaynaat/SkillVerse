from src.core.learning_analyzer import LearningAnalyzer
from src.core.memory import Memory


memory = Memory()

# Simulate student progress
memory.add_xp(250)

for _ in range(12):
    memory.increment_completed_missions()

for _ in range(5):
    memory.advance_step()


analyzer = LearningAnalyzer()

report = analyzer.analyze(memory)

print("=" * 60)
print("        LEARNING ANALYZER TEST")
print("=" * 60)

print("\n📊 Report\n")
print(report)

print("\n" + "=" * 60)

print("\n📝 Summary\n")
print(analyzer.generate_summary(report))

print("\n" + "=" * 60)
print("✅ LearningAnalyzer Test Completed Successfully!")