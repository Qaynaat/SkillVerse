from src.core.memory import Memory


class LearningInsights:

    def __init__(self):
        pass

    def generate(self, memory: Memory):

        xp = memory.get_progress()["current"]
        missions = memory.get_completed_missions()
        current_step = memory.get_current_step()

        if xp < 100:
            level = "Beginner"
            advice = (
                "🌱 You're just getting started. "
                "Focus on building strong fundamentals."
            )

        elif xp < 300:
            level = "Intermediate"
            advice = (
                "🚀 You're making excellent progress. "
                "Keep practicing consistently."
            )

        else:
            level = "Advanced"
            advice = (
                "🔥 You're becoming an advanced learner. "
                "Start tackling more challenging projects."
            )

        return {
            "xp": xp,
            "missions": missions,
            "current_step": current_step,
            "level": level,
            "advice": advice,
        }