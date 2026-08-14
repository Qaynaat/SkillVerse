class LearningStyleDetector:

    def analyze(self, memory):

        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()
        completed_daily_goals = memory.get_completed_daily_goals()
        categories_explored = memory.get_categories_explored()
        conversation_history = memory.get_history()

        # ==================================================
        # Learning Style Scores
        # ==================================================

        reading_score = (
            modules_read
            + completed_lessons
        )

        practice_score = (
            completed_missions
            + retries
        )

        goal_score = (
            completed_daily_goals
            + completed_missions
        )

        exploration_score = categories_explored

        interactive_score = len(conversation_history)

        # ==================================================
        # Determine Learning Style
        # ==================================================

        scores = {
            "Reading-Oriented": reading_score,
            "Practice-Oriented": practice_score,
            "Goal-Oriented": goal_score,
            "Exploration-Oriented": exploration_score,
            "Interactive": interactive_score,
        }

        strongest_style = max(scores, key=scores.get)
        strongest_score = scores[strongest_style]

        # ==================================================
        # Not Enough Evidence
        # ==================================================

        if strongest_score == 0:
            learning_style = "Developing"
            observation = (
                "There is not enough learning activity yet "
                "to identify a clear learning pattern."
            )

        else:
            learning_style = strongest_style

            if learning_style == "Reading-Oriented":
                observation = (
                    "You show a strong preference for learning "
                    "through lessons and reading-based activities."
                )

            elif learning_style == "Practice-Oriented":
                observation = (
                    "You learn strongly through missions, practice, "
                    "and repeated attempts."
                )

            elif learning_style == "Goal-Oriented":
                observation = (
                    "You respond well to structured goals and "
                    "task-based learning."
                )

            elif learning_style == "Exploration-Oriented":
                observation = (
                    "You enjoy exploring different learning areas "
                    "and expanding your interests."
                )

            else:
                observation = (
                    "You engage actively through conversations "
                    "and interactive learning."
                )

        # ==================================================
        # Return Learning Style Report
        # ==================================================

        return {
            "learning_style": learning_style,
            "reading_score": reading_score,
            "practice_score": practice_score,
            "goal_score": goal_score,
            "exploration_score": exploration_score,
            "interactive_score": interactive_score,
            "observation": observation,
        }