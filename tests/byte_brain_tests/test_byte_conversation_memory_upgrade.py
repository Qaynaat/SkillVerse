from src.core.services.brain_services import BrainServices
from src.core.byte_brain import ByteBrain
from src.core.memory import Memory
from src.core.save_system import SaveSystem

print("=" * 60)
print("MISSION 087 - BYTE CONVERSATION MEMORY UPGRADE TEST")
print("=" * 60)

services = BrainServices.default()
memory = Memory()

byte = ByteBrain(
    services=services,
    memory=memory,
    save_system=None
)

byte.remember_conversation_turn(
    user_message="Tell me about Software Engineering",
    byte_response="Software Engineering is a technology career.",
    intent="INTRODUCE_CAREER",
    career="Software Engineering"
)

byte.remember_conversation_turn(
    user_message="What skills do I need?",
    byte_response="Programming and problem solving are important.",
    intent="ASK_SKILLS",
    career="Software Engineering"
)


history = byte.get_conversation_history()

assert len(history) == 2

assert (
    history[-1]["user_message"]
    == "What skills do I need?"
)

context = byte.get_conversation_context()

assert len(context) == 2

assert (
    context[-1]["intent"]
    == "ASK_SKILLS"
)

status = byte.get_conversation_memory_status()

assert status["history_size"] == 2
assert status["has_conversation"] is True


print()
print("🧠 Byte Conversation Memory")

print()
print("📚 Recent Conversation:")

for turn in history:

    print(
        f"👤 User: {turn['user_message']}"
    )

    print(
        f"🤖 Byte: {turn['byte_response']}"
    )

    print(
        f"🎯 Intent: {turn['intent']}"
    )

    print(
        f"💻 Career: {turn['career']}"
    )

    print()


print("=" * 60)
print("✅ Byte Conversation Memory Upgrade Test Completed Successfully!")
print("=" * 60)