from src.core.memory import Memory


class SmartReminderEngine:

    def __init__(self):
        pass

    def generate_reminder(self, memory: Memory):

        xp = memory.get_progress()["current"]

        if xp < 100:

            reminder = (
                "📚 Time to continue your learning journey!\n\n"
                "Complete one lesson today to build momentum."
            )

        elif xp < 300:

            reminder = (
                "🚀 You're making great progress!\n\n"
                "Finish one mission today and keep your consistency."
            )

        else:

            reminder = (
                "🔥 You're doing amazing!\n\n"
                "Challenge yourself with an advanced mission today."
            )

        return {
            "xp": xp,
            "reminder": reminder,
        }