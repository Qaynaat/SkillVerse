from src.core.daily_goal_engine import DailyGoalEngine
from src.core.memory import Memory

print("=" * 60)
print("      DAILY GOAL ENGINE TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(180)

engine = DailyGoalEngine()

report = engine.generate_goals(memory)

print()
print("🎯 Today's Goals")
print()

print(f"⭐ XP: {report['xp']}")
print()

for goal in report["goals"]:
    print(f"• {goal}")

print()
print("=" * 60)
print("✅ Daily Goal Engine Test Completed Successfully!")