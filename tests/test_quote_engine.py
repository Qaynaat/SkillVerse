from src.core.engine.quote_engine import QuoteEngine
from src.core.memory import Memory

print("=" * 60)
print("      QUOTE ENGINE TEST")
print("=" * 60)

memory = Memory()

for _ in range(7):
    memory.increment_completed_missions()

engine = QuoteEngine()

report = engine.get_quote(memory)

print()

print("💬 Today's Quote")

print()

print(report["quote"])

print()

print("=" * 60)
print("✅ Quote Engine Test Completed Successfully!")