from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices


def main():

    print("=" * 60)
    print("MISSION 095 - BYTE CONVERSATION ANALYTICS TEST")
    print("=" * 60)

    services = BrainServices.default()

    byte = ByteBrain(
        services=services,
        memory=services.long_term_memory,
        save_system=None,
    )

    conversations = [

        {
            "user_message": "Tell me about Software Engineering",
            "intent": "INTRODUCE_CAREER",
            "career": "Software Engineering",
            "topic": "Career Overview",
        },

        {
            "user_message": "What skills do I need?",
            "intent": "ASK_SKILLS",
            "career": "Software Engineering",
            "topic": "Skills",
        },

        {
            "user_message": "What skills do I need?",
            "intent": "ASK_SKILLS",
            "career": "Software Engineering",
            "topic": "Skills",
        },

        {
            "user_message": "What should I study?",
            "intent": "STUDY_NEXT",
            "career": "Software Engineering",
            "topic": "Python",
        },

    ]

    analysis = byte.analyze_conversations(
        conversations
    )

    print("\n🧠 Byte Conversation Analytics")

    print(
        f"\n💬 Total Conversations: "
        f"{analysis['total_conversations']}"
    )

    print("\n🎯 Most Discussed Careers:")

    for career, count in analysis["most_discussed_careers"]:
        print(f"• {career}: {count}")

    print("\n🧠 Most Common Intents:")

    for intent, count in analysis["most_common_intents"]:
        print(f"• {intent}: {count}")

    print("\n📚 Most Discussed Topics:")

    for topic, count in analysis["most_discussed_topics"]:
        print(f"• {topic}: {count}")

    print("\n🔁 Repeated Questions:")

    for question, count in analysis["repeated_questions"]:
        print(f"• {question}: {count}")

    print(
        f"\n📈 Activity: "
        f"{analysis['conversation_activity']}"
    )

    print("\n" + "=" * 60)
    print("✅ Byte Conversation Analytics Test Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()