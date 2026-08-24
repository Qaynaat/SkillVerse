class LearningProfileInterpreter:

    def analyze(self, snapshot):

        learning_state = snapshot["learning_state"]
        risk_status = snapshot["risk_status"]
        recovery_level = snapshot["recovery_level"]
        intervention = snapshot["intervention"]
        intervention_priority = snapshot["intervention_priority"]
        learning_decision = snapshot["learning_decision"]
        velocity_status = snapshot["velocity_status"]
        trend_status = snapshot["trend_status"]
        overall_priority = snapshot["overall_priority"]

        # ==================================================
        # Determine Profile Type
        # ==================================================

        if learning_state == "Recovering":
            profile_type = "Recovering Learner"

        elif learning_state == "At Risk":
            profile_type = "At-Risk Learner"

        elif (
            learning_state == "Building Momentum"
            or velocity_status == "High Velocity"
        ):
            profile_type = "High-Performing Learner"

        elif learning_state == "Developing":
            profile_type = "Developing Learner"

        else:
            profile_type = "Stable Learner"

        # ==================================================
        # Determine Dominant Pattern
        # ==================================================

        if (
            intervention == "Targeted Revision"
            or recovery_level in (
                "Intensive Recovery",
                "Recovery",
            )
        ):
            dominant_pattern = "Difficulty Dominant"

        elif intervention in (
            "Consistency Reset",
            "Goal Reduction",
        ):
            dominant_pattern = "Consistency Dominant"

        elif trend_status == "Improving":
            dominant_pattern = "Performance Dominant"

        elif velocity_status == "High Velocity":
            dominant_pattern = "Momentum Dominant"

        else:
            dominant_pattern = "Balanced Learning"

        # ==================================================
        # Determine Primary Need
        # ==================================================

        if intervention == "Targeted Revision":
            primary_need = "Targeted Revision"

        elif intervention == "Difficulty Reduction":
            primary_need = "Difficulty Reduction"

        elif intervention in (
            "Consistency Reset",
            "Goal Reduction",
        ):
            primary_need = "Consistency Building"

        elif (
            learning_decision == "Increase Difficulty"
            or velocity_status == "High Velocity"
        ):
            primary_need = "Challenge Increase"

        else:
            primary_need = "Confidence Building"

        # ==================================================
        # Determine Recommended Direction
        # ==================================================

        if learning_state == "Recovering":
            recommended_direction = (
                "Recover → Stabilize → Build Momentum"
            )

        elif learning_state == "At Risk":
            recommended_direction = (
                "Stabilize → Recover → Rebuild Consistency"
            )

        elif learning_state == "Developing":
            recommended_direction = (
                "Build Consistency → Improve Performance → Increase Difficulty"
            )

        elif (
            velocity_status == "High Velocity"
            and trend_status == "Improving"
        ):
            recommended_direction = (
                "Maintain Momentum → Increase Difficulty → Expand Challenge"
            )

        else:
            recommended_direction = (
                "Build Consistency → Strengthen Skills → Increase Difficulty"
            )

        # ==================================================
        # Generate Profile Summary
        # ==================================================

        if dominant_pattern == "Difficulty Dominant":
            profile_summary = (
                "Repeated difficulty and retry activity indicate that "
                "strengthening difficult concepts should come before "
                "increasing workload."
            )

        elif dominant_pattern == "Consistency Dominant":
            profile_summary = (
                "Your learning pattern shows that consistency is the "
                "main area that needs strengthening before increasing "
                "your workload."
            )

        elif dominant_pattern == "Performance Dominant":
            profile_summary = (
                "Your recent learning activity shows improving "
                "performance. Continue building on this progress."
            )

        elif dominant_pattern == "Momentum Dominant":
            profile_summary = (
                "You are progressing at a strong pace. You appear ready "
                "for greater challenge while maintaining consistency."
            )

        else:
            profile_summary = (
                "Your learning profile appears balanced. Continue "
                "building consistent learning habits."
            )

        return {
            "profile_type": profile_type,
            "dominant_pattern": dominant_pattern,
            "primary_need": primary_need,
            "recommended_direction": recommended_direction,
            "profile_summary": profile_summary,
            "learning_state": learning_state,
            "risk_status": risk_status,
            "recovery_level": recovery_level,
            "intervention": intervention,
            "intervention_priority": intervention_priority,
            "learning_decision": learning_decision,
            "velocity_status": velocity_status,
            "trend_status": trend_status,
            "overall_priority": overall_priority,
        }