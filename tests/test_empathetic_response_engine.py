from src.core.empathetic_response_engine import (
    EmpatheticResponseEngine
)


print("=" * 60)
print("MISSION 089 - EMPATHETIC RESPONSE ENGINE TEST")
print("=" * 60)

engine = EmpatheticResponseEngine()

states = [
    "struggling",
    "frustrated",
    "discouraged",
    "confused",
    "success",
]

for state in states:

    report = engine.analyze(state)

    print(engine.format_report(report))

    assert report["state"] == state
    assert report["tone"]
    assert report["response"]


print("=" * 60)
print("✅ Empathetic Response Engine Test Completed Successfully!")
print("=" * 60)