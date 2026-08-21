class PersonalizedRoadmapEngine:

    def generate(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # Determine Current Stage
        # ==================================================

        if (
            learning_streak >= 3
            and completed_missions >= 3
        ):
            current_stage = "Building Momentum"

        elif (
            learning_streak >= 1
            or completed_missions >= 1
            or completed_lessons >= 1
        ):
            current_stage = "Developing"

        else:
            current_stage = "Getting Started"

        # ==================================================
        # Determine Roadmap
        # ==================================================

        if current_stage == "Building Momentum":

            main_goal = (
                "Strengthen your learning routine "
                "through consistent practice."
            )

            roadmap = [
                "Complete 2 learning missions.",
                "Finish 1 learning lesson.",
                "Review a previously difficult concept.",
                "Maintain your daily learning goal.",
            ]

            priority = "High"

            reason = (
                "You are showing strong learning activity, "
                "so your roadmap focuses on building momentum."
            )

        elif current_stage == "Developing":

            main_goal = (
                "Build a stable learning routine "
                "through small daily progress."
            )

            roadmap = [
                "Complete 1 learning task.",
                "Finish 1 lesson or learning activity.",
                "Practice a difficult concept.",
                "Maintain your learning routine.",
            ]

            priority = "Medium"

            reason = (
                "Your learning activity is developing. "
                "Small consistent steps will strengthen your progress."
            )

        else:

            main_goal = (
                "Start building a consistent learning routine."
            )

            roadmap = [
                "Complete your first learning task.",
                "Finish one beginner lesson.",
                "Practice the concept once.",
                "Set a small daily learning goal.",
            ]

            priority = "Low"

            reason = (
                "You are at the beginning of your learning journey. "
                "Start small and build consistency gradually."
            )

        # ==================================================
        # Persistence Adjustment
        # ==================================================

        if retries >= 3 and completed_missions > 0:
            reason += (
                " Your repeated attempts show persistence, "
                "so continued practice should remain part of your roadmap."
            )

        # ==================================================
        # Return Roadmap Report
        # ==================================================

        return {
            "current_stage": current_stage,
            "main_goal": main_goal,
            "roadmap": roadmap,
            "priority": priority,
            "reason": reason,
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
        }