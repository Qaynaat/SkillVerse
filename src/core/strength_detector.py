class StrengthDetector:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries_completed = memory.get_retries_completed()

        strengths = []

        # ---------------------------------
        # Consistency Strength
        # ---------------------------------

        if learning_streak >= 3:
            strengths.append("Consistency")

        # ---------------------------------
        # Goal Achievement Strength
        # ---------------------------------

        if completed_daily_goals >= 2:
            strengths.append("Goal Achievement")

        # ---------------------------------
        # Mission Completion Strength
        # ---------------------------------

        if completed_missions >= 2:
            strengths.append("Mission Completion")

        # ---------------------------------
        # Learning Activity Strength
        # ---------------------------------

        if modules_read >= 2 or completed_lessons >= 2:
            strengths.append("Learning Activity")

        # ---------------------------------
        # Persistence Strength
        # ---------------------------------

        if retries_completed >= 3:
            strengths.append("Persistence")

        # ---------------------------------
        # Overall Strength Status
        # ---------------------------------

        if len(strengths) >= 4:
            strength_status = "Excellent"

        elif len(strengths) >= 2:
            strength_status = "Strong"

        elif len(strengths) >= 1:
            strength_status = "Developing"

        else:
            strength_status = "Needs Development"

        # ---------------------------------
        # Advice
        # ---------------------------------

        if strength_status == "Excellent":
            advice = (
                "🌟 You are showing strong learning habits across "
                "multiple areas. Keep using these strengths."
            )

        elif strength_status == "Strong":
            advice = (
                "💪 You have several strong learning habits. "
                "Keep building on them consistently."
            )

        elif strength_status == "Developing":
            advice = (
                "🌱 You are beginning to develop useful learning "
                "strengths. Keep practicing consistently."
            )

        else:
            advice = (
                "💡 Focus on building small daily learning habits "
                "to develop your strengths."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries_completed": retries_completed,
            "strengths": strengths,
            "strength_status": strength_status,
            "advice": advice,
        }