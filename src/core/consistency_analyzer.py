class ConsistencyAnalyzer:

    def analyze(self, memory):
        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        streak_days = memory.get_daily_streak_history()

        streak_days_count = len(streak_days)

        if learning_streak >= 7 and completed_daily_goals >= 5:
            consistency_status = "Excellent"

        elif learning_streak >= 3 and completed_daily_goals >= 2:
            consistency_status = "Consistent"

        elif learning_streak >= 1 or completed_daily_goals >= 1:
            consistency_status = "Developing"

        else:
            consistency_status = "Needs Improvement"

        if consistency_status == "Excellent":
            advice = (
                "🔥 Your learning routine is highly consistent. "
                "Keep maintaining this momentum."
            )

        elif consistency_status == "Consistent":
            advice = (
                "🚀 Your consistency is strong. "
                "Keep following your learning routine."
            )

        elif consistency_status == "Developing":
            advice = (
                "💡 Your consistency is developing. "
                "Try to maintain your learning routine every day."
            )

        else:
            advice = (
                "🌱 Start with small daily learning goals "
                "and build your consistency gradually."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "streak_days_recorded": streak_days_count,
            "consistency_status": consistency_status,
            "advice": advice,
        }