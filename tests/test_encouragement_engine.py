from src.core.engine.encouragement_engine import EncouragementEngine
from src.core.memory import Memory

print("=" * 60)
print("      ENCOURAGEMENT ENGINE TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(300)

for _ in range(8):
    memory.increment_completed_missions()

engine = EncouragementEngine()

report = engine.generate_encouragement(memory)

print()
print("🌟 Encouragement")
print()

print(f"⭐ XP: {report['xp']}")
print(f"✅ Missions: {report['missions']}")
print()
print(report["message"])

print()
print("=" * 60)
print("✅ Encouragement Engine Test Completed Successfully!")