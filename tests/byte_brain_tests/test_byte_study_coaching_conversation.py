from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 092 - BYTE STUDY COACHING CONVERSATION TEST")
print("=" * 60)

services = BrainServices.default()

byte = ByteBrain(
    services=services,
    memory=None,
    save_system=None
)

context = {
    "current_skill": "Python",
    "current_topic": "Python Functions"
}

messages = [
    "What should I study today?",
    "I don't understand this topic",
    "I'm struggling with Python",
    "I finished my lesson",
    "I need help with revision",
    "I haven't studied today"
]

for message in messages:

    print("\n👤 User:")
    print(message)

    print(
        byte.study_coaching_conversation(
            message,
            learning_context=context
        )
    )

print("=" * 60)
print("✅ Byte Study Coaching Conversation Test Completed Successfully!")
print("=" * 60)