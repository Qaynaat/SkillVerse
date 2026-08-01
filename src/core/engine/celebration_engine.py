from src.core.memory import Memory


class CelebrationEngine:

    def __init__(self):
        pass

    def celebrate(self, memory: Memory):

        xp = memory.get_progress()["current"]
        missions = memory.get_completed_missions()

        if missions == 0:

            message = (
                "🌱 Every beginning deserves celebration.\n\n"
                "Welcome to your learning journey!"
            )

        elif missions < 5:

            message = (
                "🎉 Awesome!\n\n"
                "You've completed several missions. Keep going!"
            )

        elif missions < 15:

            message = (
                "🏆 Fantastic work!\n\n"
                "Your consistency is paying off."
            )

        else:

            message = (
                "🚀 Incredible achievement!\n\n"
                "You're becoming an exceptional learner."
            )

        return {
            "xp": xp,
            "missions": missions,
            "message": message,
        }