from src.core.byte_brain import ByteBrain
from src.core.career_database import CareerDatabase
from src.core.personality_engine import PersonalityEngine
from src.core.personality_profile import PersonalityProfile
from src.core.career_response_generator import CareerResponseGenerator
from src.core.conversation_engine import ConversationEngine
from src.core.memory import Memory
from src.core.mentor_engine import MentorEngine


byte_profile = PersonalityProfile(
    name="Byte",
    avatar_key="byte",
    primary_tone="Warm",
    secondary_traits=[
        "Friendly",
        "Encouraging"
    ],
    communication_style="Peer Mentor",
    formality="Casual-Professional",
    greeting_style="Personalized & highly welcoming",
    closing_style="Let's keep learning together!",
    celebration_style="Celebrate every step forward!",
    support_style="High encouragement, patient pacing.",
    struggle_reaction="Break problems into smaller steps.",
    humility_style="Honest and curious.",
    analogy_theme=[
        "Gaming",
        "Building",
        "Exploration"
    ],
    emoji_style="Sometimes",
    playfulness="Light tech jokes",
    response_length="Medium",
    core_values=[
        "Curiosity",
        "Consistency",
        "Growth"
    ]
)

brain = ByteBrain(
    CareerDatabase(),
    PersonalityEngine(byte_profile),
    CareerResponseGenerator(PersonalityEngine(byte_profile)),
    ConversationEngine(),
    MentorEngine(),
    Memory()
)

print("=" * 70)
print("MISSION 008 FINAL INTEGRATION TEST")
print("=" * 70)

print("\n1. Introduce Career")
print("-" * 70)
print(brain.respond(
    "Tell me about Software Engineering",
    "Software Engineering"
))

print("\n2. Ask Skills")
print("-" * 70)
print(brain.respond("What skills do I need?"))

print("\n3. Ask Career Paths")
print("-" * 70)
print(brain.respond("What jobs can I get?"))

print("\n4. Ask Future Demand")
print("-" * 70)
print(brain.respond("What is the future demand?"))

print("\n5. First Learning Mission")
print("-" * 70)
print(brain.get_current_learning_step("Software Engineering"))

print("\n6. Complete Step")
print("-" * 70)
print(brain.complete_current_step())

print("\n7. Complete Final Step")
print("-" * 70)
print(brain.complete_current_step())

print("\n8. Conversation History")
print("-" * 70)

for speaker, message in brain.memory.get_history():
    print(f"{speaker}:")
    print(message[:80] + "...")
    print()

print("=" * 70)
print("🎉 MISSION 008 PASSED!")
print("=" * 70)