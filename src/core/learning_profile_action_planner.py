class LearningProfileActionPlanner:

    def analyze(self, advice):

        profile_type = advice["profile_type"]
        focus = advice["focus"]
        urgency = advice["urgency"]
        action = advice["action"]
        next_step = advice["next_step"]
        primary_need = advice["primary_need"]

        # ==================================================
        # Build Action Plan
        # ==================================================

        if primary_need == "Targeted Revision":

            steps = [
                "Choose one difficult concept.",
                "Review the concept for 20 minutes.",
                "Complete one small practice task.",
                "Check mistakes and retry once.",
                "Stop after the focused revision session.",
            ]

            duration = "30–45 minutes"
            plan_type = "Focused Recovery Plan"

        elif primary_need == "Difficulty Reduction":

            steps = [
                "Choose one smaller learning task.",
                "Work on it for 15–20 minutes.",
                "Avoid increasing difficulty.",
                "Complete the task before starting another one.",
                "Record what still feels difficult.",
            ]

            duration = "20–30 minutes"
            plan_type = "Difficulty Reduction Plan"

        elif primary_need == "Consistency Building":

            steps = [
                "Choose today's smallest learning goal.",
                "Work on it for 15 minutes.",
                "Complete the goal before adding more work.",
                "Record the completed activity.",
                "Repeat the routine tomorrow.",
            ]

            duration = "15–20 minutes"
            plan_type = "Consistency Building Plan"

        elif primary_need == "Challenge Increase":

            steps = [
                "Choose one slightly harder learning task.",
                "Work on it for 25 minutes.",
                "Attempt the task independently.",
                "Review mistakes after completion.",
                "Increase difficulty gradually.",
            ]

            duration = "30–40 minutes"
            plan_type = "Controlled Challenge Plan"

        else:

            steps = [
                "Choose one current learning task.",
                "Work on it with full focus.",
                "Complete the task before switching activities.",
                "Review what you learned.",
                "Continue the same routine tomorrow.",
            ]

            duration = "20–30 minutes"
            plan_type = "Steady Progress Plan"

        # ==================================================
        # Determine Priority
        # ==================================================

        if urgency == "Immediate":
            priority = "Critical"

        elif urgency == "High":
            priority = "High"

        else:
            priority = "Normal"

        # ==================================================
        # Build Plan Summary
        # ==================================================

        summary = (
            f"{plan_type} recommended for a {profile_type}. "
            f"The primary focus is {focus}. "
            f"The learner should follow a small, focused action plan "
            f"before increasing workload."
        )

        return {
            "profile_type": profile_type,
            "focus": focus,
            "urgency": urgency,
            "priority": priority,
            "primary_need": primary_need,
            "action": action,
            "next_step": next_step,
            "plan_type": plan_type,
            "duration": duration,
            "steps": steps,
            "summary": summary,
        }