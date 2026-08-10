from src.core.memory import Memory
from src.core.weakness_detector import WeaknessDetector

print("=" * 60)
print("MISSION 050 - WEAKNESS DETECTOR TEST")
print("=" * 60)

memory = Memory()

# Simulate learning weaknesses

memory.increment_retries_completed()
memory.increment_retries_completed()
memory.increment_retries_completed()

analyzer = WeaknessDetector()

report = analyzer.analyze(memory)

print("\n📊 Weakness Report\n")

print(f"🔥 Learning Streak: {report['learning_streak']}")
print(f"🎯 Daily Goals: {report['completed_daily_goals']}")
print(f"✅ Missions: {report['completed_missions']}")
print(f"📚 Lessons: {report['completed_lessons']}")
print(f"📖 Modules Read: {report['modules_read']}")
print(f"🔁 Retries: {report['retries_completed']}")
print(f"⚠️ Weaknesses: {report['weaknesses']}")
print(f"📈 Weakness Status: {report['weakness_status']}")
print(f"\n💡 {report['advice']}")

assert "Consistency" in report["weaknesses"]
assert "Goal Completion" in report["weaknesses"]
assert "Learning Activity" in report["weaknesses"]
assert "Repeated Difficulty" in report["weaknesses"]
assert "Mission Progress" in report["weaknesses"]

assert report["weakness_status"] == "Needs Attention"

print("\n" + "=" * 60)
print("✅ Weakness Detector Test Completed Successfully!")
print("=" * 60)