from src.core.engine.smart_reminder_engine import (
    SmartReminderEngine
)


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


def test_smart_reminder_engine():

    engine = SmartReminderEngine()

    new_student = FakeMemory(0, 0)

    result = engine.generate_reminder(new_student)

    assert result["xp"] == 0
    assert result["priority"] == "high"
    assert "first mission" in result["reminder"].lower()

    growing_student = FakeMemory(150, 5)

    result = engine.generate_reminder(growing_student)

    assert result["priority"] == "medium"
    assert "great progress" in result["reminder"].lower()

    advanced_student = FakeMemory(700, 30)

    result = engine.generate_reminder(advanced_student)

    assert result["priority"] == "low"
    assert "advanced mission" in result["reminder"].lower()

    context_result = engine.generate_context_reminder(
        growing_student,
        "Become a Cybersecurity Engineer"
    )

    assert "Cybersecurity Engineer" in (
        context_result["reminder"]
    )

    assert engine.should_send_reminder(
        growing_student
    ) is True

    print("=" * 60)
    print("MISSION 117 - SMART REMINDER ENGINE UPDATE")
    print("=" * 60)

    print()
    print("XP:")
    print(context_result["xp"])

    print()
    print("Priority:")
    print(context_result["priority"])

    print()
    print("Reminder:")
    print(context_result["reminder"])

    print()
    print("All Mission 117 Smart Reminder tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    test_smart_reminder_engine()