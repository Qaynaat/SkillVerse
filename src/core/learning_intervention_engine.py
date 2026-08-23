class LearningInterventionEngine:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # Determine Intervention Signals
        # ==================================================

        signals = []

        if retries >= 5:
            signals.append("Repeated Difficulty")

        if retries >= 3:
            signals.append("High Retry Load")

        if completed_daily_goals <= 1:
            signals.append("Low Daily Goal Completion")

        if learning_streak < 3:
            signals.append("Weak Consistency")

        if completed_missions < 3:
            signals.append("Low Mission Completion")

        # ==================================================
        # Determine Intervention
        # ==================================================

        if retries >= 5 and completed_missions < 3:
            intervention_type = "Targeted Revision"
            priority = "Critical"
            reason = (
                "Repeated attempts combined with low mission completion "
                "suggest that difficult concepts should be strengthened "
                "before increasing workload."
            )
            action = (
                "Review difficult concepts and complete a small "
                "revision-focused task."
            )
            expected_outcome = (
                "Improved understanding and reduced retry frequency."
            )

        elif retries >= 5:
            intervention_type = "Difficulty Reduction"
            priority = "High"
            reason = (
                "A high retry load suggests that the current learning "
                "difficulty may be too demanding."
            )
            action = (
                "Reduce task difficulty temporarily and focus on "
                "mastering difficult concepts."
            )
            expected_outcome = (
                "Lower frustration and stronger task completion."
            )

        elif completed_daily_goals <= 1 and learning_streak < 3:
            intervention_type = "Consistency Reset"
            priority = "High"
            reason = (
                "Low goal completion and weak consistency suggest that "
                "the learner needs a simpler routine."
            )
            action = (
                "Set one small daily learning goal and rebuild "
                "the learning streak."
            )
            expected_outcome = (
                "Improved consistency and daily engagement."
            )

        elif completed_daily_goals <= 1:
            intervention_type = "Goal Reduction"
            priority = "Medium"
            reason = (
                "Low daily goal completion suggests that the current "
                "daily workload may be too large."
            )
            action = (
                "Reduce the daily learning target to a smaller "
                "achievable goal."
            )
            expected_outcome = (
                "Higher daily goal completion."
            )

        elif learning_streak < 3:
            intervention_type = "Consistency Reset"
            priority = "Medium"
            reason = (
                "The learner's recent consistency is below the "
                "desired level."
            )
            action = (
                "Use short, manageable learning sessions to "
                "rebuild the learning streak."
            )
            expected_outcome = (
                "Stronger learning consistency."
            )

        elif completed_missions >= 5 and retries <= 2:
            intervention_type = "Challenge Increase"
            priority = "Medium"
            reason = (
                "Strong mission completion with few retries suggests "
                "the learner is ready for greater challenge."
            )
            action = (
                "Increase task difficulty or introduce a more "
                "challenging learning mission."
            )
            expected_outcome = (
                "Continued growth through increased challenge."
            )

        else:
            intervention_type = "Maintain Current Pace"
            priority = "Low"
            reason = (
                "Current learning signals do not indicate a strong "
                "need for intervention."
            )
            action = (
                "Continue the current learning routine."
            )
            expected_outcome = (
                "Stable learning progress."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "signals": signals,
            "intervention_type": intervention_type,
            "priority": priority,
            "reason": reason,
            "action": action,
            "expected_outcome": expected_outcome,
        }