from src.core.memory import Memory


class StudyPlanner:

    def __init__(self):
        pass

    def generate_plan(self, memory: Memory):

        xp = memory.get_progress()["current"]
        current_step = memory.get_current_step()

        if xp < 100:

            tasks = [
                "📖 Study your current lesson",
                "💻 Complete one coding exercise",
                "⭐ Earn 20 XP today",
            ]

        elif xp < 300:

            tasks = [
                "✅ Finish one mission",
                "📚 Review previous concepts",
                "💻 Solve one practice problem",
                "⭐ Earn 50 XP today",
            ]

        else:

            tasks = [
                "🚀 Complete one advanced mission",
                "🛠 Build a mini project",
                "📖 Revise difficult concepts",
                "⭐ Earn 100 XP today",
            ]

        return {
            "xp": xp,
            "current_step": current_step,
            "tasks": tasks,
        }