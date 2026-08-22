class PerformanceTrendAnalyzer:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # Positive Performance Signals
        # ==================================================

        positive_signals = (
            learning_streak
            + completed_daily_goals
            + completed_missions
            + completed_lessons
            + modules_read
        )

        # ==================================================
        # Difficulty Signals
        # ==================================================

        difficulty_signals = retries

        # ==================================================
        # Performance Score
        # ==================================================

        performance_score = positive_signals - difficulty_signals

        # ==================================================
        # Determine Performance Trend
        # ==================================================

        if performance_score >= 10:
            trend_status = "Improving"

        elif performance_score >= 5:
            trend_status = "Stable"

        elif performance_score >= 1:
            trend_status = "Declining"

        else:
            trend_status = "Developing"

        # ==================================================
        # Observation
        # ==================================================

        if trend_status == "Improving":
            observation = (
                "📈 Your recent learning activity shows positive "
                "performance growth. Keep building on this momentum."
            )

        elif trend_status == "Stable":
            observation = (
                "➡️ Your learning performance appears stable. "
                "Consistent practice can help you move toward stronger growth."
            )

        elif trend_status == "Declining":
            observation = (
                "📉 Your learning performance may be slowing down. "
                "Review difficult areas and rebuild consistency."
            )

        else:
            observation = (
                "🌱 Your performance pattern is still developing. "
                "Focus on small, consistent learning actions."
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
            "positive_signals": positive_signals,
            "difficulty_signals": difficulty_signals,
            "performance_score": performance_score,
            "trend_status": trend_status,
            "observation": observation,
        }