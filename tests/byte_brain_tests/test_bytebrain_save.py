from src.core.memory import Memory
from src.core.save_system import SaveSystem

print("=" * 60)
print("MISSION 013 - BYTE SAVE TEST")
print("=" * 60)

# First Session
memory = Memory()
save_system = SaveSystem()

memory.remember_career("Cybersecurity")
memory.advance_step()
memory.add_xp(200)
memory.increment_completed_missions()

save_system.save(memory)

print("✅ Progress Saved")

# Simulate restarting SkillVerse
new_memory = Memory()

save_system.load(new_memory)

print("\nLoaded Data")
print("-" * 40)

print("Career:", new_memory.get_current_career())
print("Step:", new_memory.get_current_step())
print("XP:", new_memory.get_total_xp())
print("Completed Missions:", new_memory.get_completed_missions())

print("\n" + "=" * 60)
print("TEST FINISHED")
print("=" * 60)