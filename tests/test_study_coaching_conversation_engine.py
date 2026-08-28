from src.core.study_coaching_conversation_engine import (
    StudyCoachingConversationEngine
)


print("=" * 60)
print("MISSION 092 - STUDY COACHING CONVERSATION ENGINE TEST")
print("=" * 60)

engine = StudyCoachingConversationEngine()

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

    result = engine.respond(
        message,
        learning_context=context
    )

    print(
        engine.format_report(result)
    )


print("=" * 60)
print("✅ Study Coaching Conversation Engine Test Completed Successfully!")
print("=" * 60)