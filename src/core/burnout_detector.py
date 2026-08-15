class BurnoutDetector:

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        retries = memory.get_retries_completed()
        modules_read = memory.get_modules_read()

        # ==============================================
        # Burnout Signals
        # ==============================================

        burnout_signals = []

        # Repeated difficulty
        if retries >= 3:
            burnout_signals.append("Repeated Difficulty")

        # Heavy learning workload
        if completed_missions >= 5:
            burnout_signals.append("High Mission Load")

        if modules_read >= 5:
            burnout_signals.append("High Study Load")

        # Learning pressure / imbalance
        if completed_daily_goals == 0 and learning_streak >= 3:
            burnout_signals.append("Goal Imbalance")

        # ==============================================
        # Burnout Status
        # ==============================================

        signal_count = len(burnout_signals)

        if signal_count >= 3:
            burnout_status = "High Risk"

        elif signal_count == 2:
            burnout_status = "Moderate Risk"

        elif signal_count == 1:
            burnout_status = "Mild Risk"

        else:
            burnout_status = "Healthy"

        # ==============================================
        # Observation
        # ==============================================

        if burnout_status == "High Risk":
            observation = (
                "⚠️ Your learning activity shows several signs "
                "of possible burnout. Consider reducing your workload "
                "and taking time to recover."
            )

        elif burnout_status == "Moderate Risk":
            observation = (
                "💡 You may be experiencing some learning pressure. "
                "Consider balancing difficult tasks with breaks."
            )

        elif burnout_status == "Mild Risk":
            observation = (
                "🌱 There are a few signs of learning pressure. "
                "Keep an eye on your workload and recovery."
            )

        else:
            observation = (
                "🌟 Your current learning pattern does not show "
                "strong signs of burnout. Keep maintaining a balanced routine."
            )

        return {
            "learning_streak": learning_streak,
            "completed_daily_goals": completed_daily_goals,
            "completed_missions": completed_missions,
            "retries": retries,
            "modules_read": modules_read,
            "burnout_signals": burnout_signals,
            "burnout_status": burnout_status,
            "observation": observation,
        }