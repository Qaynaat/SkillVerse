from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices
from src.core.memory import Memory


print("=" * 60)
print("MISSION 093 - BYTE DAILY CHECK-IN TEST")
print("=" * 60)


services = BrainServices.default()
memory = Memory()


byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=None
)

context = {
    "learner_name": "Learner",
    "current_skill": "Python",
    "current_topic": "Python Functions",
    "learning_streak": 7,
    "completed_daily_goals": 2,
    "total_daily_goals": 3,
    "completed_missions": 20,
}


messages = [
    "Good morning Byte",
    "How am I doing today?",
    "I completed my goals",
    "I haven't studied today",
    "I'm struggling today",
    "I finished studying",
]


for message in messages:

    print("\n👤 User:")
    print(message)

    print(
        byte.daily_check_in(
            message,
            learning_context=context
        )
    )


print("=" * 60)
print("✅ Byte Daily Check-in Test Completed Successfully!")
print("=" * 60)