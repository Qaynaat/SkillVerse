from src.core.memory import Memory
from src.core.next_best_action_engine import NextBestActionEngine


print("=" * 60)
print("MISSION 061 - NEXT BEST ACTION ENGINE TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate learner activity
# ==================================================

memory.increment_completed_missions()
memory.increment_completed_missions()
memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

memory.increment_modules_read()
memory.increment_modules_read()

memory.increment_completed_daily_goals()

for _ in range(5):
    memory.increment_retries_completed()


engine = NextBestActionEngine()

report = engine.analyze(memory)


print("\n🎯 Next Best Action Report\n")

print(f"🎯 Next Action: {report['next_action']}")
print(f"📈 Priority: {report['priority']}")

print(f"\n🔥 Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"🔁 Retries: {report['retries']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"📖 Modules Read: {report['modules_read']}")

print(f"\n💡 {report['reason']}")


assert report["next_action"] == (
    "Review a difficult concept before starting new work."
)

assert report["priority"] == "High"
assert report["completed_missions"] == 3
assert report["completed_lessons"] == 2
assert report["retries"] == 5
assert report["completed_daily_goals"] == 1
assert report["modules_read"] == 2


print("\n" + "=" * 60)
print("✅ Next Best Action Engine Test Completed Successfully!")
print("=" * 60)