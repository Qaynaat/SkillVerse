class LearningActionOutcomeTracker:

    def analyze(self, memory):
        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        signals = []
        outcome = "No Recent Outcome"
        status = "Waiting"
        recommendation = "Complete the recommended learning action first."

        # ---------------------------------------------
        # Strong positive outcome
        # ---------------------------------------------

        if (
            learning_streak >= 3
            and completed_daily_goals >= 2
            and completed_missions >= 3
            and retries <= 2
        ):
            signals.append("Improved Consistency")
            signals.append("Strong Learning Completion")
            signals.append("Reduced Retry Load")

            outcome = "Positive Progress"
            status = "Improving"
            recommendation = (
                "The learner can gradually increase workload."
            )

        # ---------------------------------------------
        # Recovery outcome
        # ---------------------------------------------

        elif (
            retries >= 4
            and completed_missions <= 2
        ):
            signals.append("Difficulty Persists")
            signals.append("High Retry Load")
            signals.append("Low Mission Completion")

            outcome = "Recovery Still Needed"
            status = "Needs Support"
            recommendation = (
                "Continue targeted revision before increasing workload."
            )

        # ---------------------------------------------
        # Consistency outcome
        # ---------------------------------------------

        elif (
            learning_streak >= 2
            and completed_daily_goals >= 1
        ):
            signals.append("Consistency Improving")
            signals.append("Daily Goal Activity")

            outcome = "Consistency Improving"
            status = "Building"
            recommendation = (
                "Maintain the current routine before increasing workload."
            )

        # ---------------------------------------------
        # Basic activity
        # ---------------------------------------------

        elif (
            completed_missions > 0
            or completed_lessons > 0
            or modules_read > 0
        ):
            signals.append("Learning Activity Detected")

            outcome = "Partial Progress"
            status = "Developing"
            recommendation = (
                "Continue the current learning routine."
            )

        # ---------------------------------------------
        # No activity
        # ---------------------------------------------

        else:
            signals.append("No Recent Learning Activity")

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "signals": signals,
            "outcome": outcome,
            "status": status,
            "recommendation": recommendation,
        }