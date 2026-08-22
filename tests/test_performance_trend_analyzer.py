from src.core.memory import Memory
from src.core.performance_trend_analyzer import PerformanceTrendAnalyzer


print("=" * 60)
print("MISSION 063 - PERFORMANCE TREND ANALYZER TEST")
print("=" * 60)


memory = Memory()

# ==================================================
# Simulate learner activity
# ==================================================

for _ in range(3):
    memory.increment_learning_streak()

for _ in range(2):
    memory.increment_completed_daily_goals()

for _ in range(5):
    memory.increment_completed_missions()

memory.complete_lesson("Python Basics")
memory.complete_lesson("Python Functions")

for _ in range(2):
    memory.increment_modules_read()

for _ in range(2):
    memory.increment_retries_completed()


analyzer = PerformanceTrendAnalyzer()

report = analyzer.analyze(memory)


print("\n📊 Performance Trend Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries']}")

print(f"\n📈 Positive Signals: {report['positive_signals']}")
print(f"⚠️ Difficulty Signals: {report['difficulty_signals']}")
print(f"📊 Performance Score: {report['performance_score']}")
print(f"📈 Trend Status: {report['trend_status']}")

print(f"\n💡 {report['observation']}")


# ==================================================
# Assertions
# ==================================================

assert report["learning_streak"] == 3
assert report["completed_daily_goals"] == 2
assert report["completed_missions"] == 5
assert report["completed_lessons"] == 2
assert report["modules_read"] == 2
assert report["retries"] == 2

assert report["positive_signals"] == 14
assert report["difficulty_signals"] == 2
assert report["performance_score"] == 12
assert report["trend_status"] == "Improving"


print("\n" + "=" * 60)
print("✅ Performance Trend Analyzer Test Completed Successfully!")
print("=" * 60)