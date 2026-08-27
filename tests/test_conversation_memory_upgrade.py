from src.core.conversation_memory_upgrade import (
    ConversationMemoryUpgrade
)


print("=" * 60)
print("MISSION 087 - CONVERSATION MEMORY UPGRADE TEST")
print("=" * 60)


memory = ConversationMemoryUpgrade(
    max_history=3
)


# ==========================================================
# Record conversation
# ==========================================================

memory.record_turn(
    user_message="Tell me about Software Engineering",
    byte_response="Software Engineering involves building software.",
    intent="INTRODUCE_CAREER",
    career="Software Engineering"
)

memory.record_turn(
    user_message="What skills do I need?",
    byte_response="You need programming, problem solving, and debugging.",
    intent="ASK_SKILLS",
    career="Software Engineering"
)

memory.record_turn(
    user_message="What career paths are available?",
    byte_response="You can explore backend, frontend, and full-stack development.",
    intent="ASK_CAREER_PATHS",
    career="Software Engineering"
)


# ==========================================================
# Assertions
# ==========================================================

history = memory.get_history()

assert len(history) == 3

assert (
    memory.get_current_career()
    == "Software Engineering"
)

assert (
    memory.get_last_intent()
    == "ASK_CAREER_PATHS"
)

assert (
    memory.get_last_user_message()
    == "What career paths are available?"
)

assert (
    memory.contains_message("skills")
)

context = memory.get_recent_context()

assert len(context) == 3

assert context[-1]["intent"] == "ASK_CAREER_PATHS"


# ==========================================================
# History limit
# ==========================================================

memory.record_turn(
    user_message="What about cybersecurity?",
    byte_response="Cybersecurity focuses on protecting systems and networks.",
    intent="INTRODUCE_CAREER",
    career="Cybersecurity"
)

assert len(memory.get_history()) == 3

assert (
    memory.get_current_career()
    == "Cybersecurity"
)


# ==========================================================
# Status
# ==========================================================

status = memory.get_status()

assert status["history_size"] == 3
assert status["max_history"] == 3
assert status["has_conversation"] is True


# ==========================================================
# Clear
# ==========================================================

memory.clear()

assert memory.get_history() == []
assert memory.get_current_career() is None
assert memory.get_last_intent() is None
assert memory.get_last_user_message() is None
assert memory.get_last_byte_response() is None


print()
print("✅ Conversation memory recording works.")
print("✅ History limit works.")
print("✅ Career state works.")
print("✅ Intent state works.")
print("✅ Recent context works.")
print("✅ Conversation search works.")
print("✅ Clear operation works.")
print()
print("=" * 60)
print("✅ Conversation Memory Upgrade Test Completed Successfully!")
print("=" * 60)