from src.core.career_database import CareerDatabase
from src.core.career_conversation_engine import (
    CareerConversationEngine
)


print("=" * 60)
print("MISSION 091 - CAREER CONVERSATION ENGINE TEST")
print("=" * 60)

db = CareerDatabase()

engine = CareerConversationEngine(db)


# ==========================================================
# Conversation 1
# ==========================================================

result = engine.respond(
    "Tell me about Software Engineering",
    career_name="Software Engineering"
)

print(engine.format_response(result))

assert result["career"] == "Software Engineering"
assert result["intent"] == "CAREER_OVERVIEW"


# ==========================================================
# Conversation 2
# ==========================================================

result = engine.respond(
    "What skills do I need?",
    previous_career="Software Engineering"
)

print(engine.format_response(result))

assert result["career"] == "Software Engineering"
assert result["intent"] == "CAREER_SKILLS"
assert result["context_used"] is True


# ==========================================================
# Conversation 3
# ==========================================================

result = engine.respond(
    "What career paths can I follow?",
    previous_career="Software Engineering"
)

print(engine.format_response(result))

assert result["career"] == "Software Engineering"
assert result["intent"] == "CAREER_PATHS"


# ==========================================================
# Conversation 4
# ==========================================================

result = engine.respond(
    "Is this career right for me?",
    previous_career="Software Engineering"
)

print(engine.format_response(result))

assert result["career"] == "Software Engineering"
assert result["intent"] == "CAREER_DIRECTION"


print("=" * 60)
print("✅ Career Conversation Engine Test Completed Successfully!")
print("=" * 60)