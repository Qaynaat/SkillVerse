from src.core.memory import Memory


class EncouragementEngine:

    def __init__(self):
        pass

    def generate_encouragement(self, memory: Memory):

        xp = memory.get_progress()["current"]
        missions = memory.get_completed_missions()

        if missions == 0:

            message = (
                "🌱 Every journey begins with a single step.\n\n"
                "Today is the perfect day to start."
            )

        elif missions < 5:

            message = (
                "🚀 You've already completed several missions.\n\n"
                "Keep building your momentum!"
            )

        elif missions < 15:

            message = (
                "💪 You're becoming a consistent learner.\n\n"
                "Trust your progress and keep moving forward."
            )

        else:

            message = (
                "🏆 Your dedication is inspiring.\n\n"
                "You're proving that consistency creates success."
            )

        return {
            "xp": xp,
            "missions": missions,
            "message": message,
        }