from src.core.study_planner import StudyPlanner
from src.core.memory import Memory

print("=" * 60)
print("        STUDY PLANNER TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(220)
memory.advance_step()

planner = StudyPlanner()

plan = planner.generate_plan(memory)

print()
print("📅 Today's Study Plan")
print()

print(f"⭐ XP: {plan['xp']}")
print(f"📖 Current Step: {plan['current_step']}")
print("📋 Tasks:")

for task in plan["tasks"]:
    print(f"• {task}")

print()
print("=" * 60)
print("✅ Study Planner Test Completed Successfully!")