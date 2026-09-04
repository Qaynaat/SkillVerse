class AdaptiveGuidanceEngine:

    def __init__(self):
        pass

    def generate_guidance(self, progress, current_goal=None):
        """
        Generate guidance based on the student's current progress.
        """

        if not isinstance(progress, dict):
            raise ValueError("Progress must be a dictionary.")

        current = progress.get("current", 0)
        goal = progress.get("goal", 0)

        if not isinstance(current, (int, float)):
            raise ValueError("Progress current value must be numeric.")

        if not isinstance(goal, (int, float)):
            raise ValueError("Progress goal value must be numeric.")

        if goal <= 0:
            return {
                "status": "not_started",
                "message": "Let's set a clear goal before we begin.",
                "next_step": "Define your current goal."
            }

        percentage = (current / goal) * 100

        if percentage >= 80:
            status = "high_progress"
            message = (
                "You're making excellent progress. "
                "You're ready to take on a more challenging next step."
            )
            next_step = (
                "Increase the difficulty or move to the next stage "
                "of your roadmap."
            )

        elif percentage >= 40:
            status = "steady_progress"
            message = (
                "You're making steady progress. "
                "Keep building consistency."
            )
            next_step = (
                "Continue working toward your current goal "
                "and strengthen your weak areas."
            )

        elif percentage > 0:
            status = "low_progress"
            message = (
                "You're making some progress, but a smaller "
                "and more focused step may help."
            )
            next_step = (
                "Break your current goal into smaller achievable tasks."
            )

        else:
            status = "no_progress"
            message = (
                "It looks like progress has paused. "
                "Let's make the next step simpler."
            )
            next_step = (
                "Choose one small task and complete it before "
                "moving forward."
            )

        return {
            "status": status,
            "progress_percentage": round(percentage, 2),
            "current_goal": current_goal,
            "message": message,
            "next_step": next_step
        }