class AdaptiveDifficulty:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        retries = memory.get_retries_completed()
        completed_daily_goals = memory.get_completed_daily_goals()

        # ==================================================
        # Difficulty Signals
        # ==================================================

        positive_signals = (
            learning_streak
            + completed_missions
            + completed_lessons
            + completed_daily_goals
        )

        difficulty_signals = retries

        # ==================================================
        # Determine Difficulty
        # ==================================================

        if difficulty_signals >= 5 and positive_signals <= 3:

            difficulty = "Easier"

            reason = (
                "You are experiencing repeated difficulty with "
                "your current learning workload. Reducing difficulty "
                "can help rebuild confidence and consistency."
            )

        elif positive_signals >= 8 and difficulty_signals <= 3:

            difficulty = "Harder"

            reason = (
                "You are consistently completing learning activities "
                "with relatively few retries. You appear ready for "
                "a greater challenge."
            )

        else:

            difficulty = "Maintain"

            reason = (
                "Your current learning performance is balanced. "
                "Continue at the current difficulty while building "
                "steady progress."
            )

        # ==================================================
        # Return Report
        # ==================================================

        return {
            "difficulty": difficulty,
            "reason": reason,
            "learning_streak": learning_streak,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "retries": retries,
            "completed_daily_goals": completed_daily_goals,
            "positive_signals": positive_signals,
            "difficulty_signals": difficulty_signals,
        }