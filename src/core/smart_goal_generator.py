class SmartGoalGenerator:

    def generate(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # High Activity
        # ==================================================

        if (
            learning_streak >= 3
            and completed_daily_goals >= 2
            and completed_missions >= 3
        ):
            goal = "Complete 2 learning missions today."
            priority = "High"
            reason = (
                "You are showing strong consistency and productivity. "
                "Let's build on your momentum."
            )

        # ==================================================
        # Developing Activity
        # ==================================================

        elif (
            learning_streak >= 1
            or completed_daily_goals >= 1
            or completed_missions >= 1
        ):
            goal = "Complete 1 small learning task today."
            priority = "Medium"
            reason = (
                "Focus on building consistency through "
                "small and achievable daily progress."
            )

        # ==================================================
        # Low Activity
        # ==================================================

        else:
            goal = "Start with 1 small learning task today."
            priority = "Low"
            reason = (
                "Begin with a simple goal and gradually "
                "build your learning routine."
            )

        # ==================================================
        # Persistence Adjustment
        # ==================================================

        if retries >= 3 and completed_missions > 0:
            reason += (
                " Your repeated attempts show persistence, "
                "so keep practicing even when tasks are difficult."
            )

        # ==================================================
        # Return Smart Goal
        # ==================================================

        return {
            "goal": goal,
            "priority": priority,
            "reason": reason,
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
        }