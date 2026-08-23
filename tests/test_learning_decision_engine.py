from src.core.learning_decision_engine import LearningDecisionEngine
from src.core.memory import Memory


class TestMemory(Memory):

    def __init__(self):
        super().__init__()

        self._learning_streak = 2
        self._completed_daily_goals = 1
        self._completed_missions = 2
        self._completed_lessons = ["Lesson 1"]
        self._modules_read = 1
        self._retries = 5

    def get_learning_streak(self):
        return self._learning_streak

    def get_completed_daily_goals(self):
        return self._completed_daily_goals

    def get_completed_missions(self):
        return self._completed_missions

    def get_completed_lessons(self):
        return self._completed_lessons

    def get_modules_read(self):
        return self._modules_read

    def get_retries_completed(self):
        return self._retries


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 068 - LEARNING DECISION ENGINE TEST")
    print("=" * 60)

    memory = TestMemory()
    engine = LearningDecisionEngine()

    report = engine.analyze(memory)

    print("\n🧠 Learning Decision Report\n")

    print(f"🔥 Learning Streak: {report['learning_streak']}")
    print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
    print(f"✅ Missions: {report['completed_missions']}")
    print(f"📚 Lessons: {report['completed_lessons']}")
    print(f"📖 Modules Read: {report['modules_read']}")
    print(f"🔁 Retries: {report['retries']}")

    print(f"\n🧠 Decision: {report['decision']}")
    print(f"📈 Priority: {report['priority']}")

    print("\n⚠️ Decision Signals:")

    for signal in report["signals"]:
        print(f"• {signal}")

    print(f"\n🔎 Reason:")
    print(report["reason"])

    print(f"\n🎯 Action:")
    print(report["action"])

    print(f"\n💡 {report['observation']}")

    assert report["decision"] == "Recovery Mode"
    assert report["priority"] == "Critical"

    print("\n" + "=" * 60)
    print("✅ Learning Decision Engine Test Completed Successfully!")
    print("=" * 60)