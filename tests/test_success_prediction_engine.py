from src.core.engine.success_prediction_engine import SuccessPredictionEngine
from src.core.memory import Memory

print("=" * 60)
print("      SUCCESS PREDICTION ENGINE TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(350)

for _ in range(8):
    memory.increment_completed_missions()

engine = SuccessPredictionEngine()

report = engine.predict(memory)

print()

print("🔮 Success Prediction")

print()

print(f"⭐ XP: {report['xp']}")
print(f"✅ Missions: {report['missions']}")
print(f"📈 Prediction: {report['prediction']}")

print()

print("=" * 60)
print("✅ Success Prediction Test Completed Successfully!")