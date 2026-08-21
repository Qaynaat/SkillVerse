class MissionRecommendation:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()
        completed_daily_goals = memory.get_completed_daily_goals()

        # ==================================================
        # Determine Mission Recommendation
        # ==================================================

        if retries >= 5:

            recommendation = "Review a previously difficult concept."

            priority = "High"

            reason = (
                "You have experienced repeated difficulty, so reviewing "
                "a challenging concept should come before taking on new work."
            )

        elif completed_daily_goals == 0 and completed_missions == 0:

            recommendation = "Complete your first learning mission."

            priority = "High"

            reason = (
                "You have not completed a learning mission or daily goal yet. "
                "Starting with one small mission can build momentum."
            )

        elif completed_lessons == 0:

            recommendation = "Complete one learning lesson."

            priority = "High"

            reason = (
                "You have started learning activities but have not completed "
                "a lesson yet. Completing one lesson will strengthen your progress."
            )

        elif completed_missions > completed_lessons:

            recommendation = "Complete a learning lesson."

            priority = "Medium"

            reason = (
                "You are completing missions faster than lessons. "
                "Adding a lesson will balance your learning activity."
            )

        elif modules_read == 0:

            recommendation = "Read one learning module."

            priority = "Medium"

            reason = (
                "You have limited module activity. Reading one module "
                "can strengthen your understanding before further practice."
            )

        elif learning_streak >= 3:

            recommendation = "Continue with another learning mission."

            priority = "Medium"

            reason = (
                "Your learning streak shows consistent activity. "
                "Continuing with another mission can maintain your momentum."
            )

        else:

            recommendation = "Complete a learning mission."

            priority = "Medium"

            reason = (
                "A learning mission is a good next step for building "
                "consistent progress."
            )

        return {
            "recommendation": recommendation,
            "priority": priority,
            "reason": reason,
            "learning_streak": learning_streak,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "completed_daily_goals": completed_daily_goals,
        }