class DailyCheckInEngine:
    """
    Mission 093
    Daily Check-ins

    Helps Byte conduct simple daily learning check-ins
    using the learner's current learning context.
    """

    # ==========================================================
    # INITIALIZATION
    # ==========================================================

    def __init__(self):
        self.check_in_count = 0

    # ==========================================================
    # INTENT DETECTION
    # ==========================================================

    def detect_intent(self, message):

        message = message.lower().strip()

        if any(
            phrase in message
            for phrase in [
                "good morning",
                "morning byte",
                "morning",
                "start my day",
                "starting my day",
            ]
        ):
            return "MORNING_CHECK_IN"

        if any(
            phrase in message
            for phrase in [
                "how am i doing",
                "how am i doing today",
                "how is my progress",
                "check my progress",
                "my progress",
                "how did i do",
            ]
        ):
            return "PROGRESS_CHECK"

        if any(
            phrase in message
            for phrase in [
                "completed my goals",
                "finished my goals",
                "completed today's goals",
                "completed my goals today",
                "i completed my goals",
                "i finished my goals",
            ]
        ):
            return "GOALS_COMPLETED"

        if any(
            phrase in message
            for phrase in [
                "haven't studied",
                "havent studied",
                "didn't study",
                "didnt study",
                "not studied today",
                "i did not study",
                "i haven't learned",
            ]
        ):
            return "STUDY_MISSED"

        if any(
            phrase in message
            for phrase in [
                "i am struggling",
                "i'm struggling",
                "struggling today",
                "today is difficult",
                "having a difficult day",
                "study is difficult today",
            ]
        ):
            return "STRUGGLING"

        if any(
            phrase in message
            for phrase in [
                "i studied today",
                "i studied",
                "finished studying",
                "completed studying",
                "had a good study session",
                "study session completed",
            ]
        ):
            return "STUDY_COMPLETED"

        return "GENERAL_CHECK_IN"

    # ==========================================================
    # CHECK-IN
    # ==========================================================

    def check_in(
        self,
        message,
        learning_context=None
    ):

        self.check_in_count += 1

        learning_context = learning_context or {}

        intent = self.detect_intent(message)

        learner_name = learning_context.get(
            "learner_name",
            "there"
        )

        current_skill = learning_context.get(
            "current_skill",
            "your current skill"
        )

        current_topic = learning_context.get(
            "current_topic",
            "your current topic"
        )

        learning_streak = learning_context.get(
            "learning_streak",
            0
        )

        completed_daily_goals = learning_context.get(
            "completed_daily_goals",
            0
        )

        total_daily_goals = learning_context.get(
            "total_daily_goals",
            0
        )

        completed_missions = learning_context.get(
            "completed_missions",
            0
        )

        return {
            "intent": intent,
            "learner_name": learner_name,
            "current_skill": current_skill,
            "current_topic": current_topic,
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "total_daily_goals": total_daily_goals,
            "completed_missions": completed_missions,
            "response": self._build_response(
                intent=intent,
                learner_name=learner_name,
                current_skill=current_skill,
                current_topic=current_topic,
                learning_streak=learning_streak,
                completed_daily_goals=completed_daily_goals,
                total_daily_goals=total_daily_goals,
                completed_missions=completed_missions
            )
        }

    # ==========================================================
    # RESPONSE GENERATION
    # ==========================================================

    @staticmethod
    def _build_response(
        intent,
        learner_name,
        current_skill,
        current_topic,
        learning_streak,
        completed_daily_goals,
        total_daily_goals,
        completed_missions
    ):

        if intent == "MORNING_CHECK_IN":

            streak_text = ""

            if learning_streak > 0:
                streak_text = (
                    f" You currently have a {learning_streak}-day "
                    "learning streak."
                )

            return (
                f"Good morning, {learner_name}! 💜"
                f"{streak_text} "
                f"Let's make steady progress with "
                f"{current_topic} today. "
                "Start with one focused learning task."
            )

        if intent == "PROGRESS_CHECK":

            if total_daily_goals > 0:

                return (
                    f"You're making progress. "
                    f"You've completed "
                    f"{completed_daily_goals} of "
                    f"{total_daily_goals} daily goals. "
                    f"You've also completed "
                    f"{completed_missions} missions. "
                    f"Your current focus is {current_skill}."
                )

            return (
                f"You're currently working on {current_skill}. "
                f"Keep moving forward with {current_topic} "
                "and focus on one meaningful task at a time."
            )

        if intent == "GOALS_COMPLETED":

            return (
                "That's excellent! 🎉 "
                "You've completed your goals for today. "
                f"You made progress with {current_skill}. "
                "Take a moment to recognize that progress "
                "before deciding what comes next."
            )

        if intent == "STUDY_MISSED":

            return (
                "That's okay. 💜 "
                "One missed study session doesn't erase your progress. "
                f"Let's restart with one small task related to "
                f"{current_topic} instead of trying to catch up all at once."
            )

        if intent == "STRUGGLING":

            return (
                "I hear you. 💜 "
                f"If {current_topic} feels difficult today, "
                "we don't need to rush. "
                "Let's reduce the task to one small step, "
                "work through it carefully, and build from there."
            )

        if intent == "STUDY_COMPLETED":

            return (
                f"Well done! 🎉 "
                f"You completed a study session and worked on "
                f"{current_skill}. "
                "Before moving on, quickly check what you understood "
                "and what still needs practice."
            )

        return (
            f"I'm here with you, {learner_name}. 💜 "
            f"Your current focus is {current_topic}. "
            "Let's check your progress and choose one useful "
            "learning action for today."
        )

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, result):

        lines = [
            "",
            "📅 Daily Check-in",
            "",
            f"👤 Learner: {result['learner_name']}",
            f"🎯 Intent: {result['intent']}",
            f"🧠 Current Skill: {result['current_skill']}",
            f"📖 Current Topic: {result['current_topic']}",
            f"🔥 Learning Streak: {result['learning_streak']}",
            f"✅ Daily Goals: "
            f"{result['completed_daily_goals']}/"
            f"{result['total_daily_goals']}",
            f"🏆 Completed Missions: "
            f"{result['completed_missions']}",
            "",
            "💜 Byte:",
            result["response"],
            ""
        ]

        return "\n".join(lines)