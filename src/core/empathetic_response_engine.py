class EmpatheticResponseEngine:
    """
    Mission 089
    Empathetic Response Engine

    Converts a learner's emotional/situational state
    into an appropriate supportive response.

    The engine does not own ByteBrain.
    It provides response guidance that ByteBrain can use.
    """

    # ==========================================================
    # RESPONSE DEFINITIONS
    # ==========================================================

    RESPONSES = {
        "struggling": {
            "tone": "supportive",
            "response": (
                "That's okay. Learning something difficult takes time. "
                "Let's slow down and work through it step by step."
            ),
        },

        "frustrated": {
            "tone": "calming",
            "response": (
                "I understand that this can feel frustrating. "
                "Let's break the problem into smaller, manageable steps."
            ),
        },

        "discouraged": {
            "tone": "encouraging",
            "response": (
                "Don't let one difficult attempt define your progress. "
                "You're still learning, and every attempt gives you useful information."
            ),
        },

        "confused": {
            "tone": "clarifying",
            "response": (
                "It's completely fine to be confused here. "
                "Let's simplify the idea and look at it one step at a time."
            ),
        },

        "success": {
            "tone": "celebratory",
            "response": (
                "That's a great step forward! "
                "You handled it well. Keep building on this progress."
            ),
        },

        "neutral": {
            "tone": "friendly",
            "response": (
                "I'm here with you. Let's figure out the next step together."
            ),
        },
    }

    # ==========================================================
    # NORMALIZATION
    # ==========================================================

    @staticmethod
    def _normalize_state(state):
        """
        Normalize learner state for reliable lookup.
        """

        if state is None:
            return "neutral"

        return str(state).strip().lower()

    # ==========================================================
    # ANALYSIS
    # ==========================================================

    def analyze(self, state):
        """
        Analyze a learner's state and return an
        empathetic response report.
        """

        normalized_state = self._normalize_state(state)

        response_data = self.RESPONSES.get(
            normalized_state,
            self.RESPONSES["neutral"]
        )

        return {
            "state": normalized_state,
            "tone": response_data["tone"],
            "response": response_data["response"],
        }

    # ==========================================================
    # FORMAT REPORT
    # ==========================================================

    def format_report(self, report):

        return (
            "\n"
            "💬 Empathetic Response\n"
            "\n"
            f"🧠 Learner State: {report['state'].title()}\n"
            f"🎭 Response Tone: {report['tone'].title()}\n"
            "\n"
            "💜 Byte Response:\n"
            f"{report['response']}\n"
        )