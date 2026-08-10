class WeaknessDetector:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries_completed = memory.get_retries_completed()

        weaknesses = []

        # ---------------------------------
        # Consistency Weakness
        # ---------------------------------

        if learning_streak < 3:
            weaknesses.append("Consistency")

        # ---------------------------------
        # Goal Completion Weakness
        # ---------------------------------

        if completed_daily_goals < 2:
            weaknesses.append("Goal Completion")

        # ---------------------------------
        # Learning Activity Weakness
        # ---------------------------------

        if modules_read < 2 and completed_lessons < 2:
            weaknesses.append("Learning Activity")

        # ---------------------------------
        # Repeated Difficulty
        # ---------------------------------

        if retries_completed >= 3:
            weaknesses.append("Repeated Difficulty")

        # ---------------------------------
        # Mission Progress
        # ---------------------------------

        if completed_missions == 0:
            weaknesses.append("Mission Progress")

        # ---------------------------------
        # Overall Status
        # ---------------------------------

        if len(weaknesses) >= 3:
            weakness_status = "Needs Attention"

        elif len(weaknesses) >= 1:
            weakness_status = "Developing"

        else:
            weakness_status = "Strong"

        # ---------------------------------
        # Advice
        # ---------------------------------

        if weakness_status == "Needs Attention":
            advice = (
                "Focus on building a regular learning routine "
                "and completing small goals consistently."
            )

        elif weakness_status == "Developing":
            advice = (
                "You have a few areas that need attention. "
                "Work on them gradually and stay consistent."
            )

        else:
            advice = (
                "No major learning weaknesses detected. "
                "Keep maintaining your current routine."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries_completed": retries_completed,
            "weaknesses": weaknesses,
            "weakness_status": weakness_status,
            "advice": advice,
        }