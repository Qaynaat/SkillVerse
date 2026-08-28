from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.byte_brain import ByteBrain

print("=" * 60)
print("MISSION 088 - BYTE CONTEXT AWARENESS TEST")
print("=" * 60)


services = BrainServices.default()
memory = Memory()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=None
)


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


report = byte.context_awareness_engine.analyze(
    "What should I learn next?",
    history
)

print(
    byte.context_awareness_engine.format_report(
        report
    )
)


assert report["previous_career"] == (
    "Software Engineering"
)

assert report["previous_intent"] == (
    "ASK_SKILLS"
)

assert report["context_available"] is True


print("=" * 60)
print(
    "✅ Byte Context Awareness Test "
    "Completed Successfully!"
)
print("=" * 60)