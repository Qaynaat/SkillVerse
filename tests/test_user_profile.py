from src.core.memory import Memory
from src.core.save_system import SaveSystem

print("=" * 60)
print("MISSION 015 - USER PROFILE TEST")
print("=" * 60)

memory = Memory()
save_system = SaveSystem()

memory.set_user_name("Kainat")
memory.set_dream_career("Cybersecurity")

save_system.save(memory)

print("✅ Profile Saved")

new_memory = Memory()

save_system.load(new_memory)

print("\nLoaded Profile")
print("-" * 40)

print("Name:", new_memory.get_user_name())
print("Dream Career:", new_memory.get_dream_career())

print("\n" + "=" * 60)
print("TEST FINISHED")
print("=" * 60)