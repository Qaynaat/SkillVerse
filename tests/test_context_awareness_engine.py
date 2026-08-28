from src.core.context_awareness_engine import (
    ContextAwarenessEngine
)


print("=" * 60)
print("MISSION 088 - CONTEXT AWARENESS ENGINE TEST")
print("=" * 60)


history = [
    {
        "user": "Tell me about Software Engineering",
        "byte": (
            "Software Engineering is a technology career."
        ),
        "intent": "INTRODUCE_CAREER",
        "career": "Software Engineering",
    },
    {
        "user": "What skills do I need?",
        "byte": (
            "Programming and problem solving are important."
        ),
        "intent": "ASK_SKILLS",
        "career": "Software Engineering",
    },
]


engine = ContextAwarenessEngine()

report = engine.analyze(
    "What should I learn next?",
    history
)

print(engine.format_report(report))


assert report["previous_career"] == (
    "Software Engineering"
)

assert report["previous_intent"] == (
    "ASK_SKILLS"
)

assert report["context_available"] is True


print("=" * 60)
print(
    "✅ Context Awareness Engine Test "
    "Completed Successfully!"
)
print("=" * 60)