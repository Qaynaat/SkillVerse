from collections import Counter


class ConversationAnalyticsEngine:

    def __init__(self):
        pass

    # ==================================================
    # Basic Statistics
    # ==================================================

    def total_conversations(self, conversations):
        return len(conversations)

    # ==================================================
    # Intent Analysis
    # ==================================================

    def most_common_intents(self, conversations, limit=5):

        intents = [
            conversation.get("intent")
            for conversation in conversations
            if conversation.get("intent")
        ]

        return Counter(intents).most_common(limit)

    # ==================================================
    # Career Analysis
    # ==================================================

    def most_discussed_careers(self, conversations, limit=5):

        careers = [
            conversation.get("career")
            for conversation in conversations
            if conversation.get("career")
        ]

        return Counter(careers).most_common(limit)

    # ==================================================
    # Topic Analysis
    # ==================================================

    def most_discussed_topics(self, conversations, limit=5):

        topics = [
            conversation.get("topic")
            for conversation in conversations
            if conversation.get("topic")
        ]

        return Counter(topics).most_common(limit)

    # ==================================================
    # Repeated Questions
    # ==================================================

    def repeated_questions(self, conversations, limit=5):

        questions = [
            conversation.get("user_message")
            for conversation in conversations
            if conversation.get("user_message")
        ]

        counts = Counter(questions)

        return [
            (question, count)
            for question, count in counts.most_common(limit)
            if count > 1
        ]

    # ==================================================
    # Activity
    # ==================================================

    def conversation_activity(self, conversations):

        total = len(conversations)

        if total == 0:
            return "No conversation activity"

        if total < 5:
            return "Low conversation activity"

        if total < 15:
            return "Moderate conversation activity"

        return "High conversation activity"

    # ==================================================
    # Summary
    # ==================================================

    def analyze(self, conversations):

        return {
            "total_conversations": self.total_conversations(
                conversations
            ),
            "most_common_intents": self.most_common_intents(
                conversations
            ),
            "most_discussed_careers": self.most_discussed_careers(
                conversations
            ),
            "most_discussed_topics": self.most_discussed_topics(
                conversations
            ),
            "repeated_questions": self.repeated_questions(
                conversations
            ),
            "conversation_activity": self.conversation_activity(
                conversations
            ),
        }