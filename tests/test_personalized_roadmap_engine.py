from src.core.memory import Memory
from src.core.personalized_roadmap_engine import PersonalizedRoadmapEngine


print("=" * 60)
print("MISSION 057 - PERSONALIZED ROADMAP ENGINE TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate a productive learner
# ==================================================

memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

memory.increment_retries_completed()
memory.increment_retries_completed()
memory.increment_retries_completed()


engine = PersonalizedRoadmapEngine()

report = engine.generate(memory)


print("\n🧭 Personalized Roadmap Report\n")

print(f"📍 Current Stage: {report['current_stage']}")

print(f"\n🎯 Main Goal:")
print(report["main_goal"])

print("\n🛣 Roadmap:")

for index, step in enumerate(report["roadmap"], start=1):
    print(f"{index}. {step}")

print(f"\n📈 Priority: {report['priority']}")

print(f"\n💡 {report['reason']}")


assert report["current_stage"] == "Building Momentum"

assert report["priority"] == "High"

assert len(report["roadmap"]) == 4

assert report["learning_streak"] == 3

assert report["completed_daily_goals"] == 2

assert report["completed_missions"] == 3

assert report["completed_lessons"] == 2

assert report["modules_read"] == 2

assert report["retries"] == 3


print("\n" + "=" * 60)
print("✅ Personalized Roadmap Engine Test Completed Successfully!")
print("=" * 60)