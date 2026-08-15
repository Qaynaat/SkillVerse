class ConfidenceEstimator:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()
        categories_explored = memory.get_categories_explored()

        # ==============================================
        # Confidence Signals
        # ==============================================

        confidence_score = 0

        # Consistent learning
        if learning_streak >= 3:
            confidence_score += 2

        elif learning_streak >= 1:
            confidence_score += 1

        # Goal achievement
        if completed_daily_goals >= 2:
            confidence_score += 2

        elif completed_daily_goals >= 1:
            confidence_score += 1

        # Mission completion
        if completed_missions >= 5:
            confidence_score += 2

        elif completed_missions >= 2:
            confidence_score += 1

        # Lessons
        if completed_lessons >= 2:
            confidence_score += 1

        # Modules
        if modules_read >= 2:
            confidence_score += 1

        # Exploration
        if categories_explored >= 2:
            confidence_score += 1

        # Persistence through retries
        if retries >= 3:
            confidence_score += 1

        # ==============================================
        # Confidence Level
        # ==============================================

        if confidence_score >= 8:
            confidence_level = "High"

        elif confidence_score >= 4:
            confidence_level = "Moderate"

        elif confidence_score >= 1:
            confidence_level = "Developing"

        else:
            confidence_level = "Low"

        # ==============================================
        # Observation
        # ==============================================

        if confidence_level == "High":
            observation = (
                "🌟 Your learning activity shows strong evidence "
                "of confidence, consistency, and persistence."
            )

        elif confidence_level == "Moderate":
            observation = (
                "💪 You are developing solid confidence in your "
                "learning abilities. Keep building consistency."
            )

        elif confidence_level == "Developing":
            observation = (
                "🌱 Your confidence is beginning to develop. "
                "Small successful learning experiences can strengthen it."
            )

        else:
            observation = (
                "💡 Your learning history shows limited evidence "
                "of confidence so far. Start with small achievable goals."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "categories_explored": categories_explored,
            "confidence_score": confidence_score,
            "confidence_level": confidence_level,
            "observation": observation,
        }