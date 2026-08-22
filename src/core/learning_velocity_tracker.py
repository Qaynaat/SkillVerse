class LearningVelocityTracker:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # Learning Velocity Score
        # ==================================================

        velocity_score = (
            learning_streak
            + (completed_daily_goals * 2)
            + (completed_missions * 2)
            + completed_lessons
            + modules_read
            + retries
        )

        # ==================================================
        # Determine Velocity Status
        # ==================================================

        if velocity_score >= 15:
            velocity_status = "High Velocity"

        elif velocity_score >= 8:
            velocity_status = "Steady Velocity"

        elif velocity_score >= 3:
            velocity_status = "Slow Velocity"

        else:
            velocity_status = "Developing"

        # ==================================================
        # Observation
        # ==================================================

        if velocity_status == "High Velocity":
            observation = (
                "🚀 You are progressing at a strong pace with "
                "consistent learning activity."
            )

        elif velocity_status == "Steady Velocity":
            observation = (
                "📈 Your learning progress is steady. "
                "Maintaining consistency can increase your momentum."
            )

        elif velocity_status == "Slow Velocity":
            observation = (
                "🐢 Your learning progress is developing slowly. "
                "Small consistent actions can help increase your pace."
            )

        else:
            observation = (
                "🌱 Your learning activity is still developing. "
                "Start with small consistent learning actions."
            )

        # ==================================================
        # Return Report
        # ==================================================

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "velocity_score": velocity_score,
            "velocity_status": velocity_status,
            "observation": observation,
        }