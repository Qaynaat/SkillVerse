from src.core.byte_brain import ByteBrain
from src.core.career_database import CareerDatabase
from src.core.engine.personality_engine import PersonalityEngine
from src.core.personality_profile import PersonalityProfile
from src.core.career_response_generator import CareerResponseGenerator
from src.core.engine.conversation_engine import ConversationEngine
from src.core.memory import Memory
from src.core.engine.mentor_engine import MentorEngine

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
    CareerResponseGenerator(PersonalityEngine(profile)),
    ConversationEngine(),
    MentorEngine(),
    Memory()
)

print("=" * 60)
print("UNIVERSITY SUBJECTS TEST")
print("=" * 60)

print(
    brain.respond(
        "Which university subjects should I study?",
        "Software Engineering"
    )
)