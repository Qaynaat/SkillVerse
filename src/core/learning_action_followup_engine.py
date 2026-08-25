class LearningActionFollowUpEngine:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # Determine learner profile
        # ==================================================

        if retries >= 4 and completed_missions <= 2:
            profile = "Recovering Learner"
            focus = "Revision"
            priority = "Critical"

            next_step = (
                "Complete the small revision task."
            )

            follow_up = (
                "Check your mistakes and identify one concept "
                "that still feels unclear."
            )

            completion_rule = (
                "Only continue after reviewing the mistakes."
            )

            observation = (
                "The learner should strengthen difficult concepts "
                "before increasing workload."
            )

        elif (
            completed_daily_goals <= 1
            and learning_streak <= 2
        ):
            profile = "Stable Learner"
            focus = "Consistency"
            priority = "High"

            next_step = (
                "Record today's completed learning activity."
            )

            follow_up = (
                "Return tomorrow and complete another small "
                "learning goal."
            )

            completion_rule = (
                "Maintain the routine before increasing workload."
            )

            observation = (
                "The learner should maintain a small consistent "
                "routine before increasing workload."
            )

        elif completed_missions >= 5 and retries <= 2:
            profile = "Progressing Learner"
            focus = "Skill Building"
            priority = "Normal"

            next_step = (
                "Continue with the next planned learning task."
            )

            follow_up = (
                "Review what you learned and prepare for the "
                "next learning step."
            )

            completion_rule = (
                "Complete the current task before starting another."
            )

            observation = (
                "The learner is progressing steadily and can "
                "continue building skills."
            )

        else:
            profile = "Developing Learner"
            focus = "Balanced Progress"
            priority = "Normal"

            next_step = (
                "Continue with the next small learning task."
            )

            follow_up = (
                "Review the completed activity and identify "
                "one thing to improve."
            )

            completion_rule = (
                "Complete the current task before adding extra work."
            )

            observation = (
                "The learner should continue with manageable "
                "learning activity."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "profile": profile,
            "focus": focus,
            "priority": priority,
            "next_step": next_step,
            "follow_up": follow_up,
            "completion_rule": completion_rule,
            "observation": observation,
        }