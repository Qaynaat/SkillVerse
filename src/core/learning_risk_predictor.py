class LearningRiskPredictor:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = len(memory.get_completed_lessons())
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        # ==================================================
        # Risk Signals
        # ==================================================

        risk_signals = []

        # Repeated difficulty
        if retries >= 5:
            risk_signals.append("Repeated Difficulty")

        # High retry load
        if retries >= 5:
            risk_signals.append("High Retry Load")

        # Goal imbalance
        if completed_daily_goals == 0:
            risk_signals.append("Goal Imbalance")

        # Low learning consistency
        if learning_streak == 0:
            risk_signals.append("Low Learning Consistency")

        # Low activity
        if (
            completed_missions == 0
            and completed_lessons == 0
            and modules_read == 0
        ):
            risk_signals.append("Low Learning Activity")

        # ==================================================
        # Positive Signals
        # ==================================================

        positive_signals = 0

        if learning_streak >= 3:
            positive_signals += 1

        if completed_daily_goals >= 2:
            positive_signals += 1

        if completed_missions >= 3:
            positive_signals += 1

        if completed_lessons >= 2:
            positive_signals += 1

        if modules_read >= 2:
            positive_signals += 1

        # ==================================================
        # Risk Score
        # ==================================================

        risk_score = len(risk_signals) - positive_signals

        if risk_score >= 3:
            risk_status = "High Risk"

        elif risk_score >= 1:
            risk_status = "Moderate Risk"

        else:
            risk_status = "Low Risk"

        # ==================================================
        # Observation
        # ==================================================

        if risk_status == "High Risk":
            observation = (
                "⚠️ Your learning activity shows several risk signals. "
                "Consider reducing difficulty, reviewing challenging concepts, "
                "and rebuilding a sustainable learning routine."
            )

        elif risk_status == "Moderate Risk":
            observation = (
                "🟡 Some learning risk signals are present. "
                "Focus on consistency and address difficult concepts "
                "before increasing your workload."
            )

        else:
            observation = (
                "🟢 Your current learning activity shows relatively low risk. "
                "Continue maintaining consistency while monitoring difficult areas."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "completed_lessons": completed_lessons,
            "modules_read": modules_read,
            "retries": retries,
            "risk_signals": risk_signals,
            "positive_signals": positive_signals,
            "risk_score": risk_score,
            "risk_status": risk_status,
            "observation": observation,
        }