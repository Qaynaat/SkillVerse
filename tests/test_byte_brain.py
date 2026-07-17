from src.core.byte_brain import ByteBrain
from src.core.career_database import CareerDatabase
from src.core.personality_engine import PersonalityEngine
from src.core.personality_profile import PersonalityProfile
from src.core.response_generator import ResponseGenerator


# --------------------------------------------------
# Create Byte's Personality
# --------------------------------------------------
byte_profile = PersonalityProfile(
    # Identity
    name="Byte",
    avatar_key="byte",

    # Personality
    primary_tone="Warm",
    secondary_traits=[
        "Friendly",
        "Encouraging",
        "Patient"
    ],

    # Communication
    communication_style="Peer Mentor",
    formality="Casual-Professional",

    # Conversation
    greeting_style="Personalized & highly welcoming",
    closing_style="Let's keep learning together!",
    celebration_style="Celebrate every step forward!",

    # Mentoring
    support_style="High encouragement, patient pacing.",
    struggle_reaction="Break problems into smaller steps.",
    humility_style="Honest and curious.",
    analogy_theme=[
        "Gaming",
        "Building",
        "Exploration"
    ],

    # Style
    emoji_style="Sometimes",
    playfulness="Light tech jokes",
    response_length="Medium",

    # Values
    core_values=[
        "Curiosity",
        "Consistency",
        "Growth"
    ]
)


# --------------------------------------------------
# Initialize SkillVerse Components
# --------------------------------------------------
personality_engine = PersonalityEngine(byte_profile)

career_database = CareerDatabase()

response_generator = ResponseGenerator(personality_engine)


# --------------------------------------------------
# Build Byte's Brain
# --------------------------------------------------
brain = ByteBrain(
    career_database,
    personality_engine,
    response_generator
)


# --------------------------------------------------
# Integration Test
# --------------------------------------------------
if __name__ == "__main__":

    print("=" * 70)
    print("                 BYTE VERSION 1")
    print("=" * 70)

    careers = [
        "Software Engineering",
        "Cybersecurity",
        "AI Engineering"
    ]

    for career_name in careers:

        print(f"\n📚 {career_name}")
        print("-" * 70)

        response = brain.introduce_career(career_name)

        print(response)

        print("\n" + "=" * 70)

    print("\n🎉 Byte Version 1 Integration Test Completed Successfully!")