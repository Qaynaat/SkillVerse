from src.core.memory import Memory
from src.core.consistency_analyzer import ConsistencyAnalyzer


print("=" * 60)
print("MISSION 049 - CONSISTENCY ANALYZER TEST")
print("=" * 60)

memory = Memory()

# Simulate consistent learning activity
memory.increment_learning_streak()
memory.increment_learning_streak()
memory.increment_learning_streak()

memory.increment_completed_daily_goals()
memory.increment_completed_daily_goals()

memory.add_streak_day("2026-08-01")
memory.add_streak_day("2026-08-02")
memory.add_streak_day("2026-08-03")

analyzer = ConsistencyAnalyzer()

report = analyzer.analyze(memory)

print("\n📊 Consistency Report\n")
print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"📅 Streak Days Recorded: {report['streak_days_recorded']}")
print(f"📈 Consistency Status: {report['consistency_status']}")
print(f"\n💡 {report['advice']}")

assert report["learning_streak"] == 3
assert report["completed_daily_goals"] == 2
assert report["streak_days_recorded"] == 3
assert report["consistency_status"] == "Consistent"

print("\n" + "=" * 60)
print("✅ Consistency Analyzer Test Completed Successfully!")
print("=" * 60)