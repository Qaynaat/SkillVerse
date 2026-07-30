from src.core.memory import Memory
from src.core.reflection_engine import ReflectionEngine

print("=" * 60)
print("        REFLECTION ENGINE TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(250)
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()

reflection = ReflectionEngine()

print()
print(reflection.generate_summary(memory))

print()
print("=" * 60)
print("✅ ReflectionEngine Test Completed Successfully!")