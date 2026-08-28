from src.core.daily_check_in_engine import DailyCheckInEngine


print("=" * 60)
print("MISSION 093 - DAILY CHECK-IN ENGINE TEST")
print("=" * 60)

engine = DailyCheckInEngine()

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

    result = engine.check_in(
        message,
        learning_context=context
    )

    print(
        engine.format_report(result)
    )


print("=" * 60)
print("✅ Daily Check-in Engine Test Completed Successfully!")
print("=" * 60)