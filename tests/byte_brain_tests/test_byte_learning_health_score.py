from src.core.services.brain_services import BrainServices
from src.core.byte_brain import ByteBrain


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
print("MISSION 086 - BYTE LEARNING HEALTH SCORE TEST")
print("=" * 60)

services = BrainServices.default()

memory = MockMemory()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=None
)

response = byte.get_learning_health_score()

print(response)

assert "Learning Health Score" in response
assert "Health Score" in response
assert "Health Level" in response
assert "Recommendation" in response

print("=" * 60)
print("✅ Byte Learning Health Score Test Completed Successfully!")
print("=" * 60)