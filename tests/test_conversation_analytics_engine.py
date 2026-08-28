from src.core.conversation_analytics_engine import (
    ConversationAnalyticsEngine
)


def main():

    print("=" * 60)
    print("MISSION 095 - CONVERSATION ANALYTICS ENGINE TEST")
    print("=" * 60)

    engine = ConversationAnalyticsEngine()

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

        {
            "user_message": "I need revision",
            "intent": "STUDY_REVISION",
            "career": "Software Engineering",
            "topic": "Python",
        },

    ]

    # ==================================================
    # Total Conversations
    # ==================================================

    total = engine.total_conversations(conversations)

    print(f"\n💬 Total Conversations: {total}")

    assert total == 5

    # ==================================================
    # Intent Analysis
    # ==================================================

    intents = engine.most_common_intents(conversations)

    print("\n🧠 Most Common Intents:")

    for intent, count in intents:
        print(f"• {intent}: {count}")

    # ==================================================
    # Career Analysis
    # ==================================================

    careers = engine.most_discussed_careers(conversations)

    print("\n🎯 Most Discussed Careers:")

    for career, count in careers:
        print(f"• {career}: {count}")

    # ==================================================
    # Topic Analysis
    # ==================================================

    topics = engine.most_discussed_topics(conversations)

    print("\n📚 Most Discussed Topics:")

    for topic, count in topics:
        print(f"• {topic}: {count}")

    # ==================================================
    # Repeated Questions
    # ==================================================

    repeated = engine.repeated_questions(conversations)

    print("\n🔁 Repeated Questions:")

    for question, count in repeated:
        print(f"• {question}: {count}")

    # ==================================================
    # Activity
    # ==================================================

    activity = engine.conversation_activity(conversations)

    print(f"\n📈 Conversation Activity: {activity}")

    # ==================================================
    # Full Analysis
    # ==================================================

    analysis = engine.analyze(conversations)

    assert analysis["total_conversations"] == 5
    assert activity == "Moderate conversation activity"

    print("\n📊 Conversation Analytics Summary:")
    print(analysis)

    print("\n" + "=" * 60)
    print("✅ Conversation Analytics Engine Test Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()