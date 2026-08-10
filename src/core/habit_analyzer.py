class HabitAnalyzer:

    def analyze(self, memory):
        learning_streak = memory.get_learning_streak()
        completed_missions = memory.get_completed_missions()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_lessons = len(memory.get_completed_lessons())
        daily_streak_history = memory.get_daily_streak_history()

        # ---------------------------------
        # Habit Status
        # ---------------------------------

        if learning_streak >= 7 and completed_daily_goals >= 5:
            habit_status = "Excellent"

        elif learning_streak >= 3 and completed_daily_goals >= 2:
            habit_status = "Consistent"

        elif completed_missions > 0 or completed_lessons > 0:
            habit_status = "Developing"

        else:
            habit_status = "Needs Improvement"

        # ---------------------------------
        # Habit Observation
        # ---------------------------------

        if habit_status == "Excellent":
            observation = (
                "You are maintaining a strong and consistent learning routine."
            )

        elif habit_status == "Consistent":
            observation = (
                "You are building a consistent learning habit. "
                "Keep maintaining your routine."
            )

        elif habit_status == "Developing":
            observation = (
                "You have started building your learning habit. "
                "Consistency will make it stronger."
            )

        else:
            observation = (
                "Your learning routine needs more consistency. "
                "Try completing at least one learning task regularly."
            )

        # ---------------------------------
        # Return Habit Report
        # ---------------------------------

        return {
            "learning_streak": learning_streak,
            "completed_missions": completed_missions,
            "completed_daily_goals": completed_daily_goals,
            "completed_lessons": completed_lessons,
            "streak_days_recorded": len(daily_streak_history),
            "habit_status": habit_status,
            "observation": observation,
        }