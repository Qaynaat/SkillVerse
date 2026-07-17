from src.core.byte_brain import ByteBrain
from src.core.career_database import CareerDatabase
from src.core.personality_engine import PersonalityEngine
from src.core.personality_profile import PersonalityProfile
from src.core.response_generator import ResponseGenerator
from src.core.conversation_engine import ConversationEngine
from src.core.memory import Memory
from src.core.mentor_engine import MentorEngine

profile = PersonalityProfile(
    name="Byte",
    avatar_key="byte",
    primary_tone="Warm",
    secondary_traits=["Friendly"],
    communication_style="Mentor",
    formality="Casual",
    greeting_style="Personalized & highly welcoming",
    closing_style="Let's keep learning together!",
    celebration_style="Celebrate",
    support_style="High encouragement, patient pacing.",
    struggle_reaction="Break problems down.",
    humility_style="Honest",
    analogy_theme=["Gaming"],
    emoji_style="Sometimes",
    playfulness="Light",
    response_length="Medium",
    core_values=["Growth"]
)

brain = ByteBrain(
    CareerDatabase(),
    PersonalityEngine(profile),
    ResponseGenerator(PersonalityEngine(profile)),
    ConversationEngine(),
    MentorEngine(),
    Memory()
)

print("=" * 60)
print("SALARY TEST")
print("=" * 60)

print(
    brain.respond(
        "Tesll me about salary?",
        "Software Engineering"
    )
)