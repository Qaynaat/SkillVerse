from src.core.services.brain_services import BrainServices


print("=" * 60)
print("MISSION 091 - BYTE CAREER CONVERSATION TEST")
print("=" * 60)


services = BrainServices.default()

engine = services.career_conversation_engine


# First career message
first = engine.respond(
    "Tell me about Software Engineering",
    career_name="Software Engineering"
)

print(engine.format_response(first))

assert first["career"] == "Software Engineering"


# Follow-up message
second = engine.respond(
    "What skills do I need?",
    previous_career=first["career"]
)

print(engine.format_response(second))

assert second["career"] == "Software Engineering"
assert second["context_used"] is True
assert second["intent"] == "CAREER_SKILLS"


# Another follow-up
third = engine.respond(
    "What career paths can I follow?",
    previous_career=second["career"]
)

print(engine.format_response(third))

assert third["career"] == "Software Engineering"
assert third["intent"] == "CAREER_PATHS"


print("=" * 60)
print("✅ Byte Career Conversation Test Completed Successfully!")
print("=" * 60)