from src.core.learning_state_engine import LearningStateEngine


class TestMemory:

    def get_learning_streak(self):
        return 2

    def get_completed_daily_goals(self):
        return 1

    def get_completed_missions(self):
        return 2

    def get_completed_lessons(self):
        return ["Lesson 1"]

    def get_modules_read(self):
        return 1

    def get_retries_completed(self):
        return 5


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 069 - LEARNING STATE ENGINE TEST")
    print("=" * 60)

    memory = TestMemory()
    engine = LearningStateEngine()

    report = engine.analyze(memory)

    print("\n🧠 Learning State Report\n")

    print(f"🔥 Learning Streak: {report['learning_streak']}")
    print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
    print(f"✅ Missions: {report['completed_missions']}")
    print(f"📚 Lessons: {report['completed_lessons']}")
    print(f"📖 Modules Read: {report['modules_read']}")
    print(f"🔁 Retries: {report['retries']}")

    print(f"\n🧠 Current State: {report['state']}")
    print(f"📈 Priority: {report['priority']}")

    print("\n📊 State Signals:")

    for signal in report["signals"]:
        print(f"• {signal}")

    print(f"\n💡 {report['description']}")

    assert report["state"] == "Recovering"
    assert report["priority"] == "Critical"

    print("\n" + "=" * 60)
    print("✅ Learning State Engine Test Completed Successfully!")
    print("=" * 60)