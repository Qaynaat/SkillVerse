class ContextAwarenessEngine:
    """
    Mission 088
    Context Awareness Engine

    Determines the current conversational context from
    recent conversation history and the latest user message.
    """

    def __init__(self, conversation_memory=None):
        self.conversation_memory = conversation_memory

    # ==========================================================
    # CONTEXT EXTRACTION
    # ==========================================================

    def analyze(self, user_message, conversation_history=None):
        """
        Analyze the latest user message together with recent
        conversation history.
        """

        history = conversation_history or []

        current_message = (
            user_message.strip()
            if isinstance(user_message, str)
            else ""
        )

        previous_career = self._find_previous_career(history)
        previous_intent = self._find_previous_intent(history)

        context_type = self._detect_context_type(
            current_message,
            previous_career,
            previous_intent
        )

        return {
            "current_message": current_message,
            "previous_career": previous_career,
            "previous_intent": previous_intent,
            "context_type": context_type,
            "context_available": bool(
                previous_career or previous_intent
            ),
        }

    # ==========================================================
    # CAREER CONTEXT
    # ==========================================================

    @staticmethod
    def _find_previous_career(history):

        for item in reversed(history):

            if not isinstance(item, dict):
                continue

            career = item.get("career")

            if career:
                return career

        return None

    # ==========================================================
    # INTENT CONTEXT
    # ==========================================================

    @staticmethod
    def _find_previous_intent(history):

        for item in reversed(history):

            if not isinstance(item, dict):
                continue

            intent = item.get("intent")

            if intent:
                return intent

        return None

    # ==========================================================
    # CONTEXT TYPE
    # ==========================================================

    @staticmethod
    def _detect_context_type(
        message,
        previous_career,
        previous_intent
    ):

        lowered = message.lower().strip()

        # ------------------------------------------------------
        # Explicit new career
        # ------------------------------------------------------

        career_keywords = [
            "software engineering",
            "cybersecurity",
            "ai engineering",
            "data science",
            "cloud engineering",
            "game development",
            "mobile development",
            "web development",
            "ui/ux design",
            "devops engineering",
        ]

        if any(
            career in lowered
            for career in career_keywords
        ):
            return "NEW_TOPIC"

        # ------------------------------------------------------
        # Follow-up question
        # ------------------------------------------------------

        follow_up_phrases = [
            "what skills",
            "what skill",
            "what about",
            "tell me more",
            "and what",
            "how about",
            "which skills",
            "what should i learn",
            "what do i need",
            "what next",
            "next",
        ]

        if (
            previous_career
            and any(
                phrase in lowered
                for phrase in follow_up_phrases
            )
        ):
            return "FOLLOW_UP"

        # ------------------------------------------------------
        # Context continuation
        # ------------------------------------------------------

        if previous_career and previous_intent:
            return "CONTEXT_CONTINUATION"

        if previous_career:
            return "CAREER_CONTEXT"

        if previous_intent:
            return "INTENT_CONTEXT"

        return "NO_CONTEXT"

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, report):

        lines = [
            "",
            "🧠 Context Awareness",
            "",
            f"💬 Message: {report['current_message']}",
            "",
            f"💻 Previous Career: "
            f"{report['previous_career'] or 'None'}",
            "",
            f"🎯 Previous Intent: "
            f"{report['previous_intent'] or 'None'}",
            "",
            f"🔎 Context Type: {report['context_type']}",
            "",
            f"📌 Context Available: "
            f"{'Yes' if report['context_available'] else 'No'}",
            "",
        ]

        return "\n".join(lines)