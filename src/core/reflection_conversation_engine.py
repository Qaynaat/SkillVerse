class ReflectionConversationEngine:
    """
    Mission 090
    Handles reflective conversations with the learner.

    The engine helps Byte guide the learner toward:
    - understanding their learning experience
    - identifying difficulties
    - recognizing progress
    - identifying improvements
    - forming a next reflection step
    """

    # ==========================================================
    # REFLECTION STATES
    # ==========================================================

    REFLECTION_PROMPTS = {
        "struggling": [
            "What part felt the hardest?",
            "What do you think caused the difficulty?",
            "What would make this easier to understand?"
        ],

        "frustrated": [
            "What frustrated you the most?",
            "Was there a specific moment that became difficult?",
            "What could we break into smaller steps?"
        ],

        "discouraged": [
            "What made you feel discouraged?",
            "What progress have you made despite the difficulty?",
            "What is one small improvement you could make next?"
        ],

        "confused": [
            "Which part feels unclear?",
            "What idea is causing the most confusion?",
            "Would breaking the concept into smaller parts help?"
        ],

        "success": [
            "What do you think helped you succeed?",
            "What did you learn from this success?",
            "How can you build on this progress?"
        ],

        "neutral": [
            "How did your learning session go?",
            "What did you learn today?",
            "What would you like to improve next?"
        ]
    }

    # ==========================================================
    # STATE NORMALIZATION
    # ==========================================================

    @staticmethod
    def _normalize_state(state):

        if not state:
            return "neutral"

        return str(state).strip().lower()

    # ==========================================================
    # REFLECTION PROMPT
    # ==========================================================

    def get_prompt(self, learner_state="neutral"):

        state = self._normalize_state(learner_state)

        prompts = self.REFLECTION_PROMPTS.get(
            state,
            self.REFLECTION_PROMPTS["neutral"]
        )

        return prompts[0]

    # ==========================================================
    # REFLECTION QUESTIONS
    # ==========================================================

    def get_questions(self, learner_state="neutral"):

        state = self._normalize_state(learner_state)

        return list(
            self.REFLECTION_PROMPTS.get(
                state,
                self.REFLECTION_PROMPTS["neutral"]
            )
        )

    # ==========================================================
    # ANALYZE REFLECTION
    # ==========================================================

    def analyze(self, learner_state, reflection):

        state = self._normalize_state(learner_state)

        reflection_text = (
            str(reflection).strip()
            if reflection is not None
            else ""
        )

        if not reflection_text:

            return {
                "learner_state": state,
                "reflection": "",
                "has_reflection": False,
                "reflection_quality": "Missing",
                "next_prompt": self.get_prompt(state)
            }

        return {
            "learner_state": state,
            "reflection": reflection_text,
            "has_reflection": True,
            "reflection_quality": "Recorded",
            "next_prompt": self.get_prompt(state)
        }

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, report):

        lines = [
            "",
            "🪞 Reflection Conversation",
            "",
            f"🧠 Learner State: "
            f"{report['learner_state'].title()}",
            "",
            f"📝 Reflection: "
            f"{report['reflection'] or 'No reflection provided.'}",
            "",
            f"📊 Reflection Status: "
            f"{report['reflection_quality']}",
            "",
            "💬 Byte's Reflection Question:",
            report["next_prompt"],
            ""
        ]

        return "\n".join(lines)