from src.core.byte_brain import ByteBrain
from src.core.career_database import CareerDatabase
from src.core.personality_engine import PersonalityEngine
from src.core.personality_profile import PersonalityProfile
from src.core.career_response_generator import CareerResponseGenerator
from src.core.conversation_engine import ConversationEngine
from src.core.memory import Memory
# -----------------------------
# Create Byte Personality
# -----------------------------
byte_profile = PersonalityProfile(
    name="Byte" ,
    avatar_key="byte" ,

    primary_tone="Warm",

    secondary_traits=[
        "Friendly",
        "Encouraging"
    ],

    communication_style="Peer Mentor" ,

    formality="Casual-Professional" ,

    greeting_style="Personalized & highly welcoming" ,

    closing_style="Let's keep learning together!",

    celebration_style="Celebrate every step forward!" ,

    support_style="High encouragement , patient pacing .",

    struggle_reaction="Break problem into smaller steps ." ,

    humility_style="Honest and curious ." ,

    analogy_theme=[
        "Gaming" ,
        "Building" ,
        "Exploration"
    ],

    emoji_style="Sometimes",

    playfulness="Light tech jokes",

    response_length="Medium",

    core_values=[
       "Curiosity" ,
       "Consistency",
       "Growth"
    ]

)
# -----------------------------
# Build Byte
# -----------------------------

personality_engine =PersonalityEngine(byte_profile)
career_database = CareerDatabase()
response_generator = CareerResponseGenerator(personality_engine)
conversation_engine = ConversationEngine()
memory = Memory()

brain = ByteBrain(
    career_database,
    personality_engine,
    response_generator,
    conversation_engine,
    memory
)
conversation = [

    (
        "Tell me about Software Engineering",
        "Software Engineering"
    ),

    (
        "What skills do I need?",
        None
    ),

    (
        "What jobs can I get?",
        None
    ),

    (
        "What is the future demand?",
        None
    ),

    (
        "Tell me about Cybersecurity",
        "Cybersecurity"
    ),

    (
        "What skills do I need?",
        None
    ),

    (
        "What jobs can I get?",
        None
    ),

]
print("=" * 70)
print("BYTE CONVERSATION TEST")
print("=" * 70)

for message, career in conversation:

    print(f"\n👤 USER: {message}\n")

    response = brain.respond(message, career)

    print("🤖 BYTE:")

    print(response)

    print("\n" + "-" * 70)