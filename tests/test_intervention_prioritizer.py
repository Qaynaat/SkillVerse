from src.core.memory import Memory
from src.core.intervention_prioritizer import InterventionPrioritizer


print("=" * 60)
print("MISSION 067 - INTERVENTION PRIORITIZER TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate Learner
# ==================================================

for _ in range(2):
    memory.increment_learning_streak()

memory.increment_completed_daily_goals()

for _ in range(2):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")

memory.increment_modules_read()

for _ in range(5):
    memory.increment_retries_completed()


# ==================================================
# Analyze
# ==================================================

engine = InterventionPrioritizer()

report = engine.analyze(memory)


# ==================================================
# Display
# ==================================================

print("\n🎯 Intervention Priority Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print(
    f"\n📊 Total Interventions: "
    f"{report['total_interventions']}"
)

print("\n🛠 Intervention Priority:\n")

for index, intervention in enumerate(
    report["interventions"],
    start=1,
):
    print(
        f"{index}. "
        f"{intervention['type']} "
        f"({intervention['priority']})"
    )

print("\n🚨 Primary Intervention:")

primary = report["primary_intervention"]

print(f"🎯 {primary['type']}")
print(f"📈 Priority: {primary['priority']}")
print(f"💡 Reason: {primary['reason']}")
print(f"➡️ Action: {primary['action']}")


# ==================================================
# Assertions
# ==================================================

assert report["learning_streak"] == 2
assert report["completed_daily_goals"] == 1
assert report["completed_missions"] == 2
assert report["completed_lessons"] == 1
assert report["modules_read"] == 1
assert report["retries"] == 5

assert report["total_interventions"] == 5

assert (
    report["primary_intervention"]["type"]
    == "Targeted Revision"
)

assert (
    report["primary_intervention"]["priority"]
    == "Critical"
)

assert (
    report["interventions"][0]["type"]
    == "Targeted Revision"
)


print("\n" + "=" * 60)
print("✅ Intervention Prioritizer Test Completed Successfully!")
print("=" * 60)