from src.core.memory import Memory


class QuoteEngine:

    def __init__(self):

        self.quotes = [

            "💜 Learning never exhausts the mind.",

            "🚀 Small progress every day leads to big success.",

            "🌟 Consistency beats talent when talent stops working.",

            "🔥 Every mission completed makes you stronger.",

            "📚 Knowledge is the best investment you can make."

        ]

    def get_quote(self, memory: Memory):

        missions = memory.get_completed_missions()

        index = missions % len(self.quotes)

        return {
            "missions": missions,
            "quote": self.quotes[index]
        }