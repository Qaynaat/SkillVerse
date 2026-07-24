from src.core.memory import Memory
from src.core.achievement_database import AchievementDatabase
from src.core.achievement_engine import AchievementEngine


memory = Memory()

database = AchievementDatabase()

engine = AchievementEngine(database)


print("=" * 60)
print("MISSION 011 - ACHIEVEMENT SYSTEM TEST")
print("=" * 60)


print("\nUnlocked Achievements:")
print(memory.get_unlocked_achievements())


print("\nCompleting first mission...")

memory.increment_completed_missions()

new_achievements = engine.check_unlocks(memory)


print("\nNew Achievements:")

for achievement in new_achievements:
    print(f"{achievement['icon']} {achievement['title']}")


print("\nUnlocked Achievements:")
print(memory.get_unlocked_achievements())


print("\nTotal XP:")
print(memory.get_total_xp())


print("\nCompleting four more missions...")

for _ in range(4):
    memory.increment_completed_missions()

new_achievements = engine.check_unlocks(memory)


print("\nNew Achievements:")

for achievement in new_achievements:
    print(f"{achievement['icon']} {achievement['title']}")


print("\nUnlocked Achievements:")
print(memory.get_unlocked_achievements())

print("\nTotal XP:")
print(memory.get_total_xp())


print("\n" + "=" * 60)
print("TEST FINISHED")
print("=" * 60)