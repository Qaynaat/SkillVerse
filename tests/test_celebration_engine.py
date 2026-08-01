from src.core.engine.celebration_engine import CelebrationEngine
from src.core.memory import Memory

print("=" * 60)
print("      CELEBRATION ENGINE TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(420)

for _ in range(12):
    memory.increment_completed_missions()

engine = CelebrationEngine()

report = engine.celebrate(memory)

print()

print("🎉 Celebration")

print()

print(f"⭐ XP: {report['xp']}")
print(f"✅ Missions: {report['missions']}")

print()

print(report["message"])

print()

print("=" * 60)
print("✅ Celebration Engine Test Completed Successfully!")