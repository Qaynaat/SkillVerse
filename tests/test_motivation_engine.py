from src.core.engine.motivation_engine import MotivationEngine
from src.core.memory import Memory

print("=" * 60)
print("      MOTIVATION ENGINE TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(250)

engine = MotivationEngine()

report = engine.generate_message(memory)

print()
print("💜 Motivation")
print()

print(f"⭐ XP: {report['xp']}")
print()
print(report["message"])

print()
print("=" * 60)
print("✅ Motivation Engine Test Completed Successfully!")