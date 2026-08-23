class InterventionPrioritizer:

    PRIORITY_ORDER = {
        "Critical": 4,
        "High": 3,
        "Medium": 2,
        "Low": 1,
    }

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        interventions = []

        # ==================================================
        # Repeated Difficulty
        # ==================================================

        if retries >= 5:
            interventions.append({
                "type": "Targeted Revision",
                "priority": "Critical",
                "reason": "Repeated attempts indicate difficult concepts.",
                "action": "Review difficult concepts before starting new work.",
            })

        # ==================================================
        # High Retry Load
        # ==================================================

        if retries >= 3:
            interventions.append({
                "type": "Difficulty Reduction",
                "priority": "High",
                "reason": "A high retry load suggests excessive difficulty.",
                "action": "Temporarily reduce task difficulty.",
            })

        # ==================================================
        # Weak Daily Goals
        # ==================================================

        if completed_daily_goals <= 1:
            interventions.append({
                "type": "Goal Reduction",
                "priority": "High",
                "reason": "Daily goal completion is low.",
                "action": "Set a smaller achievable daily goal.",
            })

        # ==================================================
        # Weak Consistency
        # ==================================================

        if learning_streak < 3:
            interventions.append({
                "type": "Consistency Reset",
                "priority": "High",
                "reason": "Learning consistency is currently weak.",
                "action": "Use short daily learning sessions.",
            })

        # ==================================================
        # Low Mission Completion
        # ==================================================

        if completed_missions < 3:
            interventions.append({
                "type": "Mission Simplification",
                "priority": "High",
                "reason": "Mission completion is currently low.",
                "action": "Complete one smaller manageable mission.",
            })

        # ==================================================
        # Strong Performance
        # ==================================================

        if completed_missions >= 5 and retries <= 2:
            interventions.append({
                "type": "Challenge Increase",
                "priority": "Medium",
                "reason": "Strong completion with few retries suggests readiness.",
                "action": "Increase learning challenge gradually.",
            })

        # ==================================================
        # Default
        # ==================================================

        if not interventions:
            interventions.append({
                "type": "Maintain Current Pace",
                "priority": "Low",
                "reason": "No major intervention signal detected.",
                "action": "Continue the current learning routine.",
            })

        # ==================================================
        # Sort by Priority
        # ==================================================

        interventions.sort(
            key=lambda item: self.PRIORITY_ORDER[item["priority"]],
            reverse=True,
        )

        primary = interventions[0]

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "interventions": interventions,
            "primary_intervention": primary,
            "total_interventions": len(interventions),
        }