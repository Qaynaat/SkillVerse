class LearningDecisionEngine:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        signals = []

        # ============================================
        # Critical Recovery
        # ============================================

        if retries >= 5 and completed_missions <= 2:
            decision = "Recovery Mode"
            priority = "Critical"

            reason = (
                "Repeated attempts combined with low mission completion "
                "suggest that recovery should take priority."
            )

            action = (
                "Reduce workload, review difficult concepts, "
                "and rebuild consistency."
            )

            signals.append("Critical Recovery Pattern")

        # ============================================
        # Review First
        # ============================================

        elif retries >= 4:
            decision = "Review First"
            priority = "High"

            reason = (
                "Repeated attempts indicate that some concepts "
                "need reinforcement before new work."
            )

            action = (
                "Review difficult concepts before starting "
                "new learning missions."
            )

            signals.append("Repeated Difficulty")

        # ============================================
        # Reduce Difficulty
        # ============================================

        elif completed_missions <= 2 and completed_daily_goals <= 1:
            decision = "Reduce Difficulty"
            priority = "High"

            reason = (
                "Low mission and goal completion suggests "
                "that the current workload may be too demanding."
            )

            action = (
                "Reduce the workload and complete smaller "
                "learning tasks."
            )

            signals.append("Low Completion")

        # ============================================
        # Continue Learning
        # ============================================

        else:
            decision = "Continue Learning"
            priority = "Normal"

            reason = (
                "Your learning activity appears stable enough "
                "to continue progressing."
            )

            action = (
                "Continue your current learning routine "
                "and complete the next recommended task."
            )

            signals.append("Stable Learning Pattern")

        # ============================================
        # Observation
        # ============================================

        if decision == "Recovery Mode":
            observation = (
                "🛑 Recovery should take priority over increasing "
                "learning workload."
            )

        elif decision == "Review First":
            observation = (
                "🧠 Strengthening difficult concepts should come "
                "before moving forward."
            )

        elif decision == "Reduce Difficulty":
            observation = (
                "⚖️ A smaller workload may help rebuild consistency "
                "and momentum."
            )

        else:
            observation = (
                "🚀 Your current learning pattern supports continued progress."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,

            "decision": decision,
            "priority": priority,
            "signals": signals,
            "reason": reason,
            "action": action,
            "observation": observation,
        }