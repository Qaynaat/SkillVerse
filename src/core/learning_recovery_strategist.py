class LearningRecoveryStrategist:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # Determine Recovery Signals
        # ==================================================

        recovery_signals = []

        if retries >= 5:
            recovery_signals.append("Repeated Difficulty")

        if retries >= 3:
            recovery_signals.append("Repeated Attempts")

        if completed_daily_goals <= 1:
            recovery_signals.append("Weak Daily Goal Completion")

        if learning_streak < 3:
            recovery_signals.append("Weak Learning Consistency")

        if completed_missions < 3:
            recovery_signals.append("Low Mission Completion")

        # ==================================================
        # Determine Recovery Level
        # ==================================================

        recovery_score = len(recovery_signals)

        if recovery_score >= 4:
            recovery_level = "Intensive Recovery"

        elif recovery_score >= 2:
            recovery_level = "Focused Recovery"

        elif recovery_score == 1:
            recovery_level = "Light Recovery"

        else:
            recovery_level = "No Recovery Needed"

        # ==================================================
        # Recovery Plan
        # ==================================================

        recovery_plan = []

        if retries >= 5:
            recovery_plan.append(
                "Review concepts that required repeated attempts."
            )

        if retries >= 3:
            recovery_plan.append(
                "Practice difficult concepts before starting new work."
            )

        if completed_daily_goals <= 1:
            recovery_plan.append(
                "Set a smaller and achievable daily learning goal."
            )

        if learning_streak < 3:
            recovery_plan.append(
                "Rebuild consistency with short daily learning sessions."
            )

        if completed_missions < 3:
            recovery_plan.append(
                "Complete a manageable learning mission to rebuild momentum."
            )

        if not recovery_plan:
            recovery_plan.append(
                "Continue your current learning routine."
            )

        # ==================================================
        # Primary Strategy
        # ==================================================

        if recovery_level == "Intensive Recovery":
            primary_strategy = (
                "Reduce workload, review difficult concepts, "
                "and rebuild consistency before increasing difficulty."
            )

        elif recovery_level == "Focused Recovery":
            primary_strategy = (
                "Focus on difficult concepts and use smaller "
                "learning goals to rebuild momentum."
            )

        elif recovery_level == "Light Recovery":
            primary_strategy = (
                "Make a small adjustment to your learning routine "
                "and continue progressing."
            )

        else:
            primary_strategy = (
                "Maintain your current learning routine and continue progressing."
            )

        # ==================================================
        # Observation
        # ==================================================

        if recovery_level == "Intensive Recovery":
            observation = (
                "🛑 Your learning pattern suggests that recovery should "
                "take priority over increasing workload."
            )

        elif recovery_level == "Focused Recovery":
            observation = (
                "🟡 Some recovery is needed. Strengthening difficult areas "
                "before taking on more work should help restore momentum."
            )

        elif recovery_level == "Light Recovery":
            observation = (
                "🟢 Only a small adjustment appears necessary. "
                "Keep moving forward while addressing the identified issue."
            )

        else:
            observation = (
                "🚀 Your current learning pattern does not require "
                "a recovery intervention."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "recovery_signals": recovery_signals,
            "recovery_score": recovery_score,
            "recovery_level": recovery_level,
            "recovery_plan": recovery_plan,
            "primary_strategy": primary_strategy,
            "observation": observation,
        }