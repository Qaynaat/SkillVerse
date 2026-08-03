from src.core.achievement_database import AchievementDatabase
from src.core.engine.achievement_engine import AchievementEngine
from src.core.byte_brain import ByteBrain
from src.core.career_database import CareerDatabase
from src.core.career_response_generator import CareerResponseGenerator
from src.core.engine.conversation_engine import ConversationEngine
from src.core.memory import Memory
from src.core.engine.mentor_engine import MentorEngine
from src.core.engine.personality_engine import PersonalityEngine
from src.core.personality_profile import PersonalityProfile
from src.core.engine.reward_engine import RewardEngine
from src.core.save_system import SaveSystem

# --------------------------------------------------
# Create Byte's Personality
# --------------------------------------------------
byte_profile = PersonalityProfile(
    # Identity
    name="Byte",
    avatar_key="byte",
    # Personality
    primary_tone="Warm",
    secondary_traits=["Friendly", "Encouraging", "Patient"],
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
    analogy_theme=["Gaming", "Building", "Exploration"],
    # Style
    emoji_style="Sometimes",
    playfulness="Light tech jokes",
    response_length="Medium",
    # Values
    core_values=["Curiosity", "Consistency", "Growth"],
)


# --------------------------------------------------
# Initialize SkillVerse Components
# --------------------------------------------------
personality_engine = PersonalityEngine(byte_profile)

career_database = CareerDatabase()

# Note: response_generator still receives personality_engine here!
response_generator = CareerResponseGenerator(personality_engine)

conversation_engine = ConversationEngine()

achievement_database = AchievementDatabase()

# Note: achievement_engine still receives achievement_database here!
achievement_engine = AchievementEngine(achievement_database)

reward_engine = RewardEngine()

mentor_engine = MentorEngine()

memory = Memory()

save_system = SaveSystem()

# --------------------------------------------------
# Build Byte's Brain (Exact 8 dependencies matched!)
# --------------------------------------------------
brain = ByteBrain(
    career_database=career_database,
    career_response_generator=response_generator,
    conversation_engine=conversation_engine,
    achievement_engine=achievement_engine,
    reward_engine=reward_engine,
    mentor_engine=mentor_engine,
    memory=memory,
    save_system=save_system,
)


# --------------------------------------------------
# Integration Test
# --------------------------------------------------
if __name__ == "__main__":

    print("=" * 70)
    print("                 BYTE VERSION 1")
    print("=" * 70)

    careers = ["Software Engineering", "Cybersecurity", "AI Engineering"]

    for career_name in careers:

        print(f"\n📚 {career_name}")
        print("-" * 70)

        response = brain.introduce_career(career_name)

        print(response)

        print("\n" + "=" * 70)

    print("\n🎉 Byte Version 1 Integration Test Completed Successfully!")