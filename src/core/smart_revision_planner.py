class SmartRevisionPlanner:

    def analyze(self, memory):

        completed_lessons = memory.get_completed_lessons()
        retries = memory.get_retries_completed()
        modules_read = memory.get_modules_read()

        # ==================================================
        # Determine Revision Priority
        # ==================================================

        if retries >= 5:
            priority = "High"
            revision_focus = (
                "Review concepts that required repeated attempts."
            )

        elif retries >= 2:
            priority = "Medium"
            revision_focus = (
                "Review recently practiced concepts."
            )

        elif completed_lessons > 0:
            priority = "Low"
            revision_focus = (
                "Review completed lessons to strengthen retention."
            )

        else:
            priority = "Low"
            revision_focus = (
                "Start learning before scheduling revision."
            )

        # ==================================================
        # Build Revision Plan
        # ==================================================

        revision_plan = []

        if completed_lessons:
            revision_plan.append(
                f"Review {min(2, len(completed_lessons))} completed lessons."
            )

        if retries >= 2:
            revision_plan.append(
                "Revisit concepts that required repeated attempts."
            )

        if modules_read > 0:
            revision_plan.append(
                "Review previously studied modules."
            )

        if not revision_plan:
            revision_plan.append(
                "Complete a learning activity before revision."
            )

        # ==================================================
        # Observation
        # ==================================================

        if retries >= 5:
            observation = (
                "Your repeated attempts suggest that some concepts "
                "would benefit from focused revision before moving forward."
            )

        elif retries >= 2:
            observation = (
                "A short revision session can help strengthen "
                "the concepts you have been practicing."
            )

        elif completed_lessons > 0:
            observation = (
                "Regular revision of completed lessons can help "
                "strengthen long-term retention."
            )

        else:
            observation = (
                "There is not enough learning activity yet to build "
                "a meaningful revision plan."
            )

        return {
            "revision_focus": revision_focus,
            "priority": priority,
            "revision_plan": revision_plan,
            "completed_lessons": len(completed_lessons),
            "modules_read": modules_read,
            "retries": retries,
            "observation": observation,
        }