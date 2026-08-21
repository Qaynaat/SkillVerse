from src.core.memory import Memory
from src.core.smart_revision_planner import SmartRevisionPlanner


print("=" * 60)
print("MISSION 060 - SMART REVISION PLANNER TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate learning activity
# ==================================================

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

for _ in range(5):
    memory.increment_retries_completed()


planner = SmartRevisionPlanner()

report = planner.analyze(memory)


print("\n🧠 Smart Revision Report\n")

print(f"🎯 Revision Focus: {report['revision_focus']}")
print(f"📈 Priority: {report['priority']}")

print(f"\n📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print("\n📝 Revision Plan:")

for index, item in enumerate(report["revision_plan"], start=1):
    print(f"{index}. {item}")

print(f"\n💡 {report['observation']}")


assert report["priority"] == "High"
assert report["completed_lessons"] == 2
assert report["modules_read"] == 2
assert report["retries"] == 5
assert len(report["revision_plan"]) >= 2


print("\n" + "=" * 60)
print("✅ Smart Revision Planner Test Completed Successfully!")
print("=" * 60)