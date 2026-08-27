from src.core.learning_health_score import LearningHealthScore


class MockMemory:

    def get_learning_streak(self):
        return 7

    def get_completed_daily_goals(self):
        return 5

    def get_completed_missions(self):
        return 10

    def get_completed_lessons(self):
        return ["lesson1", "lesson2", "lesson3"]

    def get_modules_read(self):
        return 5

    def get_retries_completed(self):
        return 3


print("=" * 60)
print("MISSION 086 - LEARNING HEALTH SCORE TEST")
print("=" * 60)

memory = MockMemory()

engine = LearningHealthScore()

report = engine.analyze(memory)

print(
    engine.format_report(report)
)

assert "health_score" in report
assert "health_level" in report
assert "priority" in report
assert "factors" in report
assert "areas_to_improve" in report
assert "recommendation" in report

assert 0 <= report["health_score"] <= 100

print("=" * 60)
print("✅ Learning Health Score Test Completed Successfully!")
print("=" * 60)