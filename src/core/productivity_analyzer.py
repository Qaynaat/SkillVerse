class ProductivityAnalyzer:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # Productivity Score
        # ==================================================

        productivity_score = (
            learning_streak
            + completed_daily_goals
            + completed_missions
            + completed_lessons
            + modules_read
            + retries
        )

        # ==================================================
        # Productivity Status
        # ==================================================

        if productivity_score >= 20:
            productivity_status = "Excellent"

        elif productivity_score >= 10:
            productivity_status = "Productive"

        elif productivity_score >= 5:
            productivity_status = "Developing"

        else:
            productivity_status = "Needs Improvement"

        # ==================================================
        # Productivity Observation
        # ==================================================

        if productivity_status == "Excellent":

            observation = (
                "🌟 You are maintaining a highly productive "
                "learning routine across multiple activities."
            )

        elif productivity_status == "Productive":

            observation = (
                "🚀 You are showing strong learning productivity. "
                "Keep maintaining this momentum."
            )

        elif productivity_status == "Developing":

            observation = (
                "💡 Your learning productivity is developing. "
                "Try completing small learning tasks consistently."
            )

        else:

            observation = (
                "🌱 Your productivity needs improvement. "
                "Start with small achievable learning goals."
            )

        # ==================================================
        # Return Productivity Report
        # ==================================================

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "productivity_score": productivity_score,
            "productivity_status": productivity_status,
            "observation": observation,
        }