from src.core.memory import Memory


class DailyGoalEngine:

    def __init__(self):
        pass

    def generate_goals(self, memory: Memory):

        xp = memory.get_progress()["current"]

        if xp < 100:

            goals = [
                "📖 Finish your current lesson",
                "⭐ Earn 20 XP",
                "💻 Complete one coding exercise",
            ]

        elif xp < 300:

            goals = [
                "✅ Complete one mission",
                "⭐ Earn 50 XP",
                "📚 Review one previous topic",
            ]

        else:

            goals = [
                "🚀 Complete one advanced mission",
                "⭐ Earn 100 XP",
                "🛠 Build or improve a project",
            ]

        return {
            "xp": xp,
            "goals": goals,
        }