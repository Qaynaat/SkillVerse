from src.core.memory import Memory


class MotivationEngine:

    def __init__(self):
        pass

    def generate_message(self, memory: Memory):

        xp = memory.get_progress()["current"]

        if xp < 100:

            message = (
                "🌱 Every expert was once a beginner.\n\n"
                "Keep learning—you are building your future."
            )

        elif xp < 300:

            message = (
                "🚀 You're making steady progress.\n\n"
                "Stay consistent and success will follow."
            )

        else:

            message = (
                "🔥 Amazing work!\n\n"
                "Your dedication today is creating opportunities for tomorrow."
            )

        return {
            "xp": xp,
            "message": message,
        }