from src.core.memory import Memory
from src.core.engine.reward_engine import RewardEngine

print("=" * 60)
print("MISSION 014 - REWARD SYSTEM TEST")
print("=" * 60)

memory = Memory()
reward_engine = RewardEngine()

print("\nUnlocked Rewards:")
print(memory.get_unlocked_rewards())

print("\nCompleting first mission...")

memory.increment_completed_missions()

new_rewards = reward_engine.check_unlocks(memory)

print("\nNew Rewards:")

for reward in new_rewards:
    print("🎁", reward["title"])

print("\nUnlocked Rewards:")
print(memory.get_unlocked_rewards())

print("\nAdding XP...")

memory.add_xp(1000)

new_rewards = reward_engine.check_unlocks(memory)

print("\nNew Rewards:")

for reward in new_rewards:
    print("🎁", reward["title"])

print("\nUnlocked Rewards:")
print(memory.get_unlocked_rewards())

print("\n" + "=" * 60)
print("TEST FINISHED")
print("=" * 60)
