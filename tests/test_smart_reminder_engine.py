from src.core.engine.smart_reminder_engine import SmartReminderEngine
from src.core.memory import Memory

print("=" * 60)
print("      SMART REMINDER ENGINE TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(180)

engine = SmartReminderEngine()

report = engine.generate_reminder(memory)

print()
print("⏰ Smart Reminder")
print()

print(f"⭐ XP: {report['xp']}")
print()
print(report["reminder"])

print()
print("=" * 60)
print("✅ Smart Reminder Engine Test Completed Successfully!")