class NextBestActionEngine:

    def analyze(self, memory):

        completed_missions = memory.get_completed_missions()
        completed_lessons = memory.get_completed_lessons()
        retries = memory.get_retries_completed()
        completed_daily_goals = memory.get_completed_daily_goals()
        modules_read = memory.get_modules_read()

        # ==================================================
        # Determine Next Best Action
        # ==================================================

        if retries >= 5:
            action = "Review a difficult concept before starting new work."
            priority = "High"
            reason = (
                "Repeated attempts suggest that strengthening difficult "
                "concepts should come before taking on more work."
            )

        elif completed_daily_goals == 0 and completed_missions > 0:
            action = "Complete your daily learning goal."
            priority = "High"
            reason = (
                "You have learning activity but have not completed "
                "your daily goal yet."
            )

        elif completed_missions == 0:
            action = "Complete your first learning mission."
            priority = "High"
            reason = (
                "Starting with a learning mission will establish "
                "your current learning momentum."
            )

        elif completed_lessons == 0:
            action = "Complete a learning lesson."
            priority = "Medium"
            reason = (
                "A completed lesson will give you a stronger "
                "learning foundation."
            )

        elif modules_read == 0:
            action = "Read a learning module."
            priority = "Medium"
            reason = (
                "Reading a learning module will expand your "
                "current learning activity."
            )

        else:
            action = "Complete another learning mission."
            priority = "Medium"
            reason = (
                "Your current activity suggests that continuing "
                "with another mission is the best next step."
            )

        # ==================================================
        # Return Report
        # ==================================================

        return {
            "next_action": action,
            "priority": priority,
            "reason": reason,
            "completed_missions": completed_missions,
            "completed_lessons": len(completed_lessons),
            "retries": retries,
            "completed_daily_goals": completed_daily_goals,
            "modules_read": modules_read,
        }