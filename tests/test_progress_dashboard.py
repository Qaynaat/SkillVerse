from src.core.progress_dashboard import ProgressDashboard
from src.core.memory import Memory

print("=" * 60)
print("      PROGRESS DASHBOARD TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(350)

for _ in range(9):
    memory.increment_completed_missions()

memory.advance_step()

dashboard = ProgressDashboard()

print()
report = dashboard.generate(memory)

print()
print("📊 SkillVerse Progress Dashboard")
print()

print(f"⭐ XP: {report['xp']}")
print(f"🎓 Level: {report['level']}")
print(f"✅ Missions: {report['missions']}")
print(f"📖 Current Step: {report['current_step']}")
print(f"🏆 Achievements: {report['achievements']}")
print(f"🎁 Rewards: {report['rewards']}")

print()
print("=" * 60)
print("✅ Progress Dashboard Test Completed Successfully!")