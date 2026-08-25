class LearningActionExecutionEngine:

    def analyze(self, action_plan):

        profile_type = action_plan["profile_type"]
        focus = action_plan["focus"]
        priority = action_plan["priority"]
        plan_type = action_plan["plan_type"]
        duration = action_plan["duration"]
        steps = action_plan["steps"]

        # ==================================================
        # Determine Execution State
        # ==================================================

        if priority == "Critical":
            execution_state = "Start Immediately"
            execution_priority = "Critical"

        elif priority == "High":
            execution_state = "Ready to Start"
            execution_priority = "High"

        else:
            execution_state = "Ready to Start"
            execution_priority = "Normal"

        # ==================================================
        # Select First Action
        # ==================================================

        if steps:
            first_action = steps[0]
        else:
            first_action = "Start the recommended learning activity."

        # ==================================================
        # Execution Guidance
        # ==================================================

        if priority == "Critical":

            guidance = (
                "Start with the first step only. Avoid adding extra "
                "work until the immediate learning need has been addressed."
            )

        elif focus == "Consistency":

            guidance = (
                "Complete the first small task today and avoid "
                "increasing workload until the routine becomes consistent."
            )

        elif focus == "Revision":

            guidance = (
                "Focus on one difficult concept first, then continue "
                "only if the revision task is completed successfully."
            )

        elif focus == "Challenge":

            guidance = (
                "Begin with the planned challenge and increase difficulty "
                "gradually rather than making a large jump."
            )

        else:

            guidance = (
                "Complete the first planned action before moving to "
                "additional learning activities."
            )

        # ==================================================
        # Expected Completion
        # ==================================================

        expected_completion = (
            "Complete the first action before continuing to the next step."
        )

        # ==================================================
        # Return Execution Report
        # ==================================================

        return {
            "profile_type": profile_type,
            "focus": focus,
            "priority": priority,
            "execution_priority": execution_priority,
            "execution_state": execution_state,
            "plan_type": plan_type,
            "duration": duration,
            "steps": steps,
            "first_action": first_action,
            "guidance": guidance,
            "expected_completion": expected_completion,
        }