from src.core.memory import Memory
from src.core.learning_analyzer import LearningAnalyzer

class ReflectionEngine:

    def __init__(self):
        self.learning_analyzer = LearningAnalyzer()

    def reflect(self, memory: Memory):

        xp = memory.get_progress()["current"]
        missions = memory.get_completed_missions()

        report = self.learning_analyzer.analyze(memory)
        learning_level = report["learning_level"]

        if missions == 0:
            return (
                "🌱 You're just beginning your journey. "
                "Every expert starts with the first step."
            )

        elif xp < 100:
            return (
                "🚀 You're gaining momentum. "
                "Keep completing missions and your confidence will grow."
            )

        elif xp < 300:
            return (
                "💪 You're making steady progress. "
                "Your dedication is starting to pay off."
            )

        elif xp < 600:

            if learning_level == "Advanced":
                return (
                    "🏆 Outstanding! "
                    "You're becoming an advanced learner. Keep mastering difficult concepts."
                )

            return (
                "🔥 Excellent work! "
                "You're becoming a confident learner with consistent effort."
            )
    def generate_summary(self, memory: Memory):

        report = self.learning_analyzer.analyze(memory)

        reflection = self.reflect(memory)

        summary = (
            "📊 Reflection Report\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions: {report['missions_completed']}\n"
            f"🎓 Level: {report['learning_level']}\n\n"
            f"{reflection}"
        )

        return summary