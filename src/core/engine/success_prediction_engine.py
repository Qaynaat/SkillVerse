from src.core.memory import Memory


class SuccessPredictionEngine:

    def predict(self, memory: Memory):

        xp = memory.get_total_xp()
        missions = memory.get_completed_missions()

        score = xp + (missions * 20)

        if score >= 700:
            prediction = "🌟 Excellent"

        elif score >= 400:
            prediction = "🚀 Very Good"

        elif score >= 200:
            prediction = "👍 Good"

        else:
            prediction = "🌱 Beginner"

        return {
            "xp": xp,
            "missions": missions,
            "prediction": prediction
        }