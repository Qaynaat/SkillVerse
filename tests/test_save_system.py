from src.core.memory import Memory
from src.core.save_system import SaveSystem


print("=" * 60)
print("MISSION 012 - SAVE SYSTEM TEST")
print("=" * 60)

memory = Memory()

memory.remember_career("Cybersecurity")
memory.advance_step()
memory.advance_step()

memory.add_xp(250)
memory.increment_completed_missions()

save_system = SaveSystem()

print("\nSaving data...")
save_system.save(memory)

loaded_memory = Memory()

print("Loading data...")
save_system.load(loaded_memory)

print("\nLoaded Data")
print("-" * 40)

print("Career:", loaded_memory.get_current_career())
print("Step:", loaded_memory.get_current_step())
print("XP:", loaded_memory.get_total_xp())
print("Completed Missions:", loaded_memory.get_completed_missions())

print("\n" + "=" * 60)
print("TEST FINISHED")
print("=" * 60)