from src.core.learning_analyzer import LearningAnalyzer


class ReflectionEngine:

    def __init__(self):
        self.learning_analyzer = LearningAnalyzer()

    def reflect(self, memory):

        progress = memory.get_progress()
        xp = progress.get("current", 0)

        missions = memory.get_completed_missions()

        report = self.learning_analyzer.analyze(memory)

        learning_level = report.get(
            "learning_level",
            "Beginner"
        )

        if missions == 0:
            return (
                "🌱 You're just beginning your journey. "
                "Every expert starts with the first step."
            )

        if xp < 100:
            return (
                "🚀 You're gaining momentum. "
                "Keep completing missions and your confidence will grow."
            )

        if xp < 300:
            return (
                "💪 You're making steady progress. "
                "Your dedication is starting to pay off."
            )

        if xp < 600:

            if learning_level == "Advanced":
                return (
                    "🏆 Outstanding! You're becoming an advanced "
                    "learner. Keep mastering difficult concepts."
                )

            return (
                "🔥 Excellent work! You're becoming a confident "
                "learner with consistent effort."
            )

        return (
            "👑 Incredible progress! You've built strong learning "
            "momentum. Keep challenging yourself and continue "
            "growing toward mastery."
        )

    def generate_summary(self, memory):

        report = self.learning_analyzer.analyze(memory)

        reflection = self.reflect(memory)

        return {
            "xp": report.get("xp", 0),
            "missions_completed": report.get(
                "missions_completed",
                0
            ),
            "learning_level": report.get(
                "learning_level",
                "Beginner"
            ),
            "reflection": reflection
        }

    def generate_report(self, memory):

        summary = self.generate_summary(memory)

        return (
            "📊 Reflection Report\n\n"
            f"⭐ XP: {summary['xp']}\n"
            f"✅ Missions: "
            f"{summary['missions_completed']}\n"
            f"🎓 Level: "
            f"{summary['learning_level']}\n\n"
            f"{summary['reflection']}"
        )