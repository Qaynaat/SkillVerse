class LearningStateEngine:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        signals = []

        # ============================================
        # RECOVERING
        # ============================================

        if (
            retries >= 5
            and completed_missions <= 2
            and completed_daily_goals <= 1
        ):
            state = "Recovering"
            priority = "Critical"

            signals.extend([
                "High Retry Load",
                "Low Mission Completion",
                "Weak Daily Goal Completion",
            ])

            description = (
                "Your current learning pattern suggests that "
                "recovery and consistency should take priority."
            )

        # ============================================
        # STRUGGLING
        # ============================================

        elif retries >= 4:
            state = "Struggling"
            priority = "High"

            signals.extend([
                "Repeated Difficulty",
                "High Retry Load",
            ])

            description = (
                "You are experiencing repeated difficulty, "
                "so strengthening difficult concepts should "
                "come before increasing workload."
            )

        # ============================================
        # HIGH MOMENTUM
        # ============================================

        elif (
            learning_streak >= 3
            and completed_daily_goals >= 2
            and completed_missions >= 4
            and retries <= 2
        ):
            state = "High Momentum"
            priority = "Normal"

            signals.extend([
                "Strong Learning Streak",
                "Strong Mission Completion",
                "Low Retry Load",
            ])

            description = (
                "You are demonstrating strong consistency, "
                "high activity, and relatively few difficulties."
            )

        # ============================================
        # IMPROVING
        # ============================================

        elif (
            completed_missions >= 3
            and completed_daily_goals >= 2
            and retries <= 3
        ):
            state = "Improving"
            priority = "Normal"

            signals.extend([
                "Positive Learning Activity",
                "Consistent Goal Completion",
            ])

            description = (
                "Your recent learning activity shows positive "
                "progress and improving consistency."
            )

        # ============================================
        # STABLE
        # ============================================

        else:
            state = "Stable"
            priority = "Normal"

            signals.append("Stable Learning Pattern")

            description = (
                "Your current learning activity appears stable. "
                "Continue building consistent learning habits."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "state": state,
            "priority": priority,
            "signals": signals,
            "description": description,
        }