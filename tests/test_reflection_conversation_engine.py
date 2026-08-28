from src.core.reflection_conversation_engine import (
    ReflectionConversationEngine
)


print("=" * 60)
print("MISSION 090 - REFLECTION CONVERSATION ENGINE TEST")
print("=" * 60)

engine = ReflectionConversationEngine()

report = engine.analyze(
    "struggling",
    "I found Python functions difficult today."
)

print(engine.format_report(report))

assert report["learner_state"] == "struggling"
assert report["reflection"] == (
    "I found Python functions difficult today."
)
assert report["has_reflection"] is True
assert report["reflection_quality"] == "Recorded"
assert report["next_prompt"]

print("=" * 60)
print("✅ Reflection Conversation Engine Test Completed Successfully!")
print("=" * 60)