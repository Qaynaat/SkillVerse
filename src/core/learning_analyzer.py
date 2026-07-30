from src.core.memory import Memory

class LearningAnalyzer:

    def __init__(self):
        pass

    def analyze(self, memory: Memory):
        xp = memory.get_progress()["current"]
        completed = memory.get_completed_missions()
        current_step = memory.get_current_step()
        # Learning Level
        if xp >= 500:
            level = "Advanced"
        elif xp >= 200:
            level = "Intermediate"
        else:
            level = "Beginner"
        # Recommended Study Pace
        if completed >= 20:
            pace = "Maintain your current pace."
        elif completed >= 10:
            pace = "You're doing well. Try completing one mission every day."
        else:
            pace = (
                "Try completing at least one mission daily "
                "to build consistency."
            )
        report = {
            "xp": xp,
            "missions_completed": completed,
            "current_step": current_step,
            "learning_level": level,
            "recommended_pace": pace,
        }
        return report

    def generate_feedback(self, report: dict):

        level = report["learning_level"]

        if level == "Beginner":
            return (
                "🌱 You're just getting started. "
                "Stay consistent and focus on learning one step at a time."
            )
        elif level == "Intermediate":
            return (
                "🚀 Great progress! "
                "You're building solid skills. Keep challenging yourself."
            )
        return (
            "🔥 Amazing work! "
            "You're becoming highly skilled. Keep pushing your limits!"
        )

    def generate_summary(self, report: dict):

        feedback = self.generate_feedback(report)

        return (
            "📊 Learning Summary\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions Completed: {report['missions_completed']}\n"
            f"📖 Current Step: {report['current_step']}\n"
            f"🎓 Learning Level: {report['learning_level']}\n\n"
            f"📅 Study Pace:\n{report['recommended_pace']}\n\n"
            f"{feedback}"
        )