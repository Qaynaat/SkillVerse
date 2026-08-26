from src.core.learning_outcome_interpreter import LearningOutcomeInterpreter
from src.core.memory import Memory


print("=" * 60)
print("MISSION 077 - LEARNING OUTCOME INTERPRETER TEST")
print("=" * 60)

memory = Memory()
interpreter = LearningOutcomeInterpreter()

report = interpreter.analyze(
    memory,
    outcome="Difficult"
)

print("\n🧠 Learning Outcome Interpretation\n")

print(f"📊 Outcome: {report['outcome']}")
print(f"📈 Impact: {report['impact']}")

print("\n🔎 Meaning:")
print(report["meaning"])

print("\n➡️ Recommendation:")
print(report["recommendation"])

assert report["outcome"] == "Difficult"
assert report["impact"] == "Learning Difficulty"
assert "difficult concept" in report["recommendation"]

print("\n" + "=" * 60)
print("✅ Learning Outcome Interpreter Test Completed Successfully!")
print("=" * 60)