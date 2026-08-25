class LearningProfileAdvisor:

    def analyze(self, interpretation):

        profile_type = interpretation["profile_type"]
        dominant_pattern = interpretation["dominant_pattern"]
        primary_need = interpretation["primary_need"]
        recommended_direction = interpretation["recommended_direction"]
        overall_priority = interpretation["overall_priority"]

        # ==================================================
        # Determine Advisor Action
        # ==================================================

        if primary_need == "Targeted Revision":

            action = "Review difficult concepts before starting new work."

            focus = "Revision"

            reason = (
                "Your profile shows repeated difficulty, so strengthening "
                "weak concepts should come before increasing workload."
            )

        elif primary_need == "Difficulty Reduction":

            action = (
                "Reduce learning difficulty temporarily and rebuild "
                "understanding through smaller tasks."
            )

            focus = "Difficulty Reduction"

            reason = (
                "Your current profile suggests that the workload may be "
                "too difficult and should be reduced temporarily."
            )

        elif primary_need == "Consistency Building":

            action = (
                "Complete one small learning goal every day to rebuild "
                "consistency."
            )

            focus = "Consistency"

            reason = (
                "Your profile indicates that consistency is currently "
                "more important than increasing workload."
            )

        elif primary_need == "Challenge Increase":

            action = (
                "Increase learning difficulty gradually while maintaining "
                "your current learning consistency."
            )

            focus = "Challenge"

            reason = (
                "Your profile shows strong learning momentum and suggests "
                "that you are ready for greater challenge."
            )

        else:

            action = (
                "Continue building consistent learning habits and "
                "strengthen your existing skills."
            )

            focus = "Skill Building"

            reason = (
                "Your profile appears relatively balanced, so steady "
                "skill development should remain the focus."
            )

        # ==================================================
        # Determine Urgency
        # ==================================================

        if overall_priority == "Critical":
            urgency = "Immediate"

        elif overall_priority == "High":
            urgency = "High"

        else:
            urgency = "Normal"

        # ==================================================
        # Determine Next Step
        # ==================================================

        if primary_need == "Targeted Revision":

            next_step = (
                "Choose one difficult concept and complete a "
                "revision-focused task."
            )

        elif primary_need == "Difficulty Reduction":

            next_step = (
                "Choose one smaller task and complete it without "
                "increasing difficulty."
            )

        elif primary_need == "Consistency Building":

            next_step = (
                "Complete today's smallest achievable learning goal."
            )

        elif primary_need == "Challenge Increase":

            next_step = (
                "Start one slightly more difficult learning mission."
            )

        else:

            next_step = (
                "Continue with your current learning routine."
            )

        # ==================================================
        # Generate Advisor Message
        # ==================================================

        advisor_message = (
            f"Your profile is currently classified as {profile_type}. "
            f"The dominant pattern is {dominant_pattern}. "
            f"Your primary focus should be {focus}. "
            f"{reason}"
        )

        return {
            "profile_type": profile_type,
            "dominant_pattern": dominant_pattern,
            "primary_need": primary_need,
            "recommended_direction": recommended_direction,
            "overall_priority": overall_priority,
            "action": action,
            "focus": focus,
            "reason": reason,
            "urgency": urgency,
            "next_step": next_step,
            "advisor_message": advisor_message,
        }