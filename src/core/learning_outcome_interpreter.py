class LearningOutcomeInterpreter:
    """
    Mission 077
    Interprets the outcome of a learner's recent action.
    """

    def analyze(self, memory, outcome=None):
        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # --------------------------------------------------
        # If no outcome has been supplied, infer from memory
        # --------------------------------------------------

        if outcome is None:
            if (
                learning_streak == 0
                and completed_daily_goals == 0
                and completed_missions == 0
                and completed_lessons == 0
                and modules_read == 0
                and retries == 0
            ):
                outcome = "No Recent Outcome"
            elif retries >= 3:
                outcome = "Difficult"
            elif (
                completed_daily_goals > 0
                or completed_missions > 0
                or completed_lessons > 0
                or modules_read > 0
            ):
                outcome = "Positive"
            else:
                outcome = "Limited"

        # --------------------------------------------------
        # Interpret outcome
        # --------------------------------------------------

        interpretations = {
            "Positive": {
                "meaning": "The learning action appears to be helping the learner make progress.",
                "impact": "Positive Progress",
                "recommendation": (
                    "Continue the current learning approach before increasing workload."
                ),
            },
            "Difficult": {
                "meaning": (
                    "The learner is experiencing difficulty and repeated attempts "
                    "may indicate that the concept needs more support."
                ),
                "impact": "Learning Difficulty",
                "recommendation": (
                    "Review the difficult concept and strengthen understanding "
                    "before increasing workload."
                ),
            },
            "Limited": {
                "meaning": (
                    "The learner has made limited progress and may need a simpler "
                    "or more focused learning action."
                ),
                "impact": "Limited Progress",
                "recommendation": (
                    "Use a smaller learning task and monitor the next outcome."
                ),
            },
            "No Recent Outcome": {
                "meaning": (
                    "There is not enough recent learning activity to determine "
                    "whether the current approach is effective."
                ),
                "impact": "Insufficient Data",
                "recommendation": (
                    "Complete the recommended learning action before evaluating progress."
                ),
            },
        }

        interpretation = interpretations.get(
            outcome,
            interpretations["Limited"]
        )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "outcome": outcome,
            "meaning": interpretation["meaning"],
            "impact": interpretation["impact"],
            "recommendation": interpretation["recommendation"],
        }

    def format_report(self, report):
        return (
            "🧠 Learning Outcome Interpretation\n\n"
            f"📊 Outcome: {report['outcome']}\n"
            f"📈 Impact: {report['impact']}\n\n"
            f"🔎 Meaning:\n"
            f"{report['meaning']}\n\n"
            f"➡️ Recommendation:\n"
            f"{report['recommendation']}\n"
        )