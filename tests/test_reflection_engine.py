from src.core.engine.reflection_engine import ReflectionEngine


class FakeMemory:

    def __init__(self, xp, missions):
        self.xp = xp
        self.missions = missions

    def get_progress(self):
        return {
            "current": self.xp
        }

    def get_completed_missions(self):
        return self.missions


class FakeLearningAnalyzer:

    def analyze(self, memory):

        xp = memory.get_progress()["current"]

        if xp >= 500:
            level = "Advanced"
        elif xp >= 100:
            level = "Intermediate"
        else:
            level = "Beginner"

        return {
            "xp": xp,
            "missions_completed":
                memory.get_completed_missions(),
            "learning_level": level
        }


def test_reflection_engine():

    engine = ReflectionEngine()

    engine.learning_analyzer = FakeLearningAnalyzer()

    beginner_memory = FakeMemory(0, 0)

    reflection = engine.reflect(beginner_memory)

    assert "beginning" in reflection.lower()

    growing_memory = FakeMemory(150, 5)

    reflection = engine.reflect(growing_memory)

    assert "steady progress" in reflection.lower()

    advanced_memory = FakeMemory(500, 20)

    reflection = engine.reflect(advanced_memory)

    assert "advanced learner" in reflection.lower()

    summary = engine.generate_summary(advanced_memory)

    assert summary["xp"] == 500
    assert summary["missions_completed"] == 20
    assert summary["learning_level"] == "Advanced"

    report = engine.generate_report(advanced_memory)

    assert "Reflection Report" in report
    assert "XP: 500" in report
    assert "Missions: 20" in report

    print("=" * 60)
    print("MISSION 116 - REFLECTION ENGINE UPDATE")
    print("=" * 60)

    print()
    print(report)

    print()
    print("All Mission 116 Reflection Engine tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    test_reflection_engine()