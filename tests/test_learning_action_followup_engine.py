from src.core.learning_action_followup_engine import  LearningActionFollowUpEngine

from src.core.memory import Memory


print("=" * 60)
print("MISSION 075 - LEARNING ACTION FOLLOW-UP ENGINE TEST")
print("=" * 60)

memory = Memory()

# Simulate a recovering learner
memory.increment_completed_missions()
memory.increment_completed_missions()

for _ in range(5):
    memory.increment_retries_completed()

engine = LearningActionFollowUpEngine()

report = engine.analyze(memory)

print()
print("🔄 Learning Action Follow-Up")
print()

print(f"📍 Profile: {report['profile']}")
print(f"🎯 Focus: {report['focus']}")
print(f"📈 Priority: {report['priority']}")
print()

print("➡️ Next Step:")
print(report["next_step"])
print()

print("💡 Follow-Up:")
print(report["follow_up"])
print()

print("✅ Completion Rule:")
print(report["completion_rule"])
print()

print(f"💡 {report['observation']}")
print()

assert report["profile"] == "Recovering Learner"
assert report["focus"] == "Revision"
assert report["priority"] == "Critical"
assert report["next_step"] == (
    "Complete the small revision task."
)

print("=" * 60)
print("✅ Learning Action Follow-Up Engine Test Completed Successfully!")
print("=" * 60)