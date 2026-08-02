from src.core.memory import Memory


class LearningTipEngine:

    def __init__(self):

        self.tips = [

            "📚 Study a little every day instead of cramming.",

            "💻 Practice coding after learning every concept.",

            "🧠 Teach someone else what you've learned.",

            "📝 Take short notes while studying.",

            "🎯 Focus on consistency instead of speed."

        ]

    def get_tip(self, memory: Memory):

        missions = memory.get_completed_missions()

        index = missions % len(self.tips)

        return {
            "missions": missions,
            "tip": self.tips[index]
        }