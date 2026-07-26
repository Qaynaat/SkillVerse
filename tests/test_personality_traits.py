from src.data.personality_traits import PERSONALITY_TRAITS

print("=" * 60)
print("MISSION 018 - PERSONALITY TRAITS TEST")
print("=" * 60)

print()
print(f"Total Traits: {len(PERSONALITY_TRAITS)}")

print()
print("First Trait")
print("-" * 40)
print(PERSONALITY_TRAITS[0]["name"])

print()
print("Last Trait")
print("-" * 40)
print(PERSONALITY_TRAITS[-1]["name"])

print()
print("=" * 60)
print("TEST FINISHED")
print("=" * 60)