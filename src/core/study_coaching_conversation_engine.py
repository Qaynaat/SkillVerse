class StudyCoachingConversationEngine:
    """
    Mission 092
    Study Coaching Conversations

    Handles study-related conversations using the learner's
    current learning context.
    """

    # ==========================================================
    # INTENT DETECTION
    # ==========================================================

    def detect_intent(self, message):
        message = message.lower().strip()

        if any(
            phrase in message
            for phrase in [
                "what should i study",
                "what should i learn",
                "what do i study",
                "study today",
                "learn today",
                "next lesson",
                "what next",
            ]
        ):
            return "STUDY_NEXT"

        if any(
            phrase in message
            for phrase in [
                "i don't understand",
                "i dont understand",
                "i am confused",
                "i'm confused",
                "confused about",
                "don't get",
                "dont get",
            ]
        ):
            return "STUDY_CONFUSION"

        if any(
            phrase in message
            for phrase in [
                "struggling with",
                "having difficulty",
                "having trouble",
                "difficult topic",
                "hard topic",
                "study is difficult",
                "studying is difficult",
            ]
        ):
            return "STUDY_STRUGGLE"

        if any(
            phrase in message
            for phrase in [
                "finished my lesson",
                "completed my lesson",
                "finished studying",
                "completed studying",
                "i studied",
                "lesson completed",
            ]
        ):
            return "STUDY_COMPLETED"

        if any(
            phrase in message
            for phrase in [
                "help me revise",
                "need revision",
                "need to revise",
                "revision",
                "revise this",
                "help with revision",
            ]
        ):
            return "STUDY_REVISION"

        if any(
            phrase in message
            for phrase in [
                "haven't studied",
                "havent studied",
                "didn't study",
                "didnt study",
                "not studied",
                "i didn't learn",
                "i did not study",
            ]
        ):
            return "STUDY_INACTIVITY"

        return "STUDY_GENERAL"

    # ==========================================================
    # RESPONSE GENERATION
    # ==========================================================

    def respond(self, message, learning_context=None):

        learning_context = learning_context or {}

        intent = self.detect_intent(message)

        current_skill = learning_context.get(
            "current_skill",
            "your current skill"
        )

        current_topic = learning_context.get(
            "current_topic",
            "your current topic"
        )

        return {
            "intent": intent,
            "current_skill": current_skill,
            "current_topic": current_topic,
            "response": self._build_response(
                intent,
                current_skill,
                current_topic
            )
        }

    # ==========================================================
    # RESPONSE LOGIC
    # ==========================================================

    @staticmethod
    def _build_response(
        intent,
        current_skill,
        current_topic
    ):

        if intent == "STUDY_NEXT":
            return (
                f"Let's continue with {current_topic}. "
                f"Focus on {current_skill} first, then complete "
                "a small practice task before moving forward."
            )

        if intent == "STUDY_CONFUSION":
            return (
                f"It's okay to feel confused about {current_topic}. "
                "Let's break it into smaller parts and work through "
                "one idea at a time."
            )

        if intent == "STUDY_STRUGGLE":
            return (
                f"You're having difficulty with {current_topic}, "
                "so let's slow down instead of rushing ahead. "
                "Review the difficult part and try one small practice task."
            )

        if intent == "STUDY_COMPLETED":
            return (
                f"Great work completing your study session. "
                f"You've made progress with {current_skill}. "
                "Before starting something new, take a moment to check "
                "what you understood and what still needs practice."
            )

        if intent == "STUDY_REVISION":
            return (
                f"Let's revise {current_topic}. "
                "Start with the key idea, test yourself with a small "
                "practice task, then review any mistakes."
            )

        if intent == "STUDY_INACTIVITY":
            return (
                "That's okay. Missing a study session does not erase "
                "your progress. Let's restart with one small learning "
                "task instead of trying to catch up all at once."
            )

        return (
            f"I'm here to help with your study progress. "
            f"We can work on {current_topic} step by step."
        )

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, result):

        lines = [
            "",
            "📚 Study Coaching Conversation",
            "",
            f"🎯 Intent: {result['intent']}",
            f"🧠 Current Skill: {result['current_skill']}",
            f"📖 Current Topic: {result['current_topic']}",
            "",
            "💜 Byte:",
            result["response"],
            ""
        ]

        return "\n".join(lines)