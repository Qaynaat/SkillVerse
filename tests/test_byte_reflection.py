from src.core.achievement_engine import AchievementEngine
from src.core.byte_brain import ByteBrain
from src.core.career_database import CareerDatabase
from src.core.career_response_generator import CareerResponseGenerator
from src.core.conversation_engine import ConversationEngine
from src.core.memory import Memory
from src.core.mentor_engine import MentorEngine
from src.core.personality_engine import PersonalityEngine
from src.core.reflection_engine import ReflectionEngine
from src.core.reward_engine import RewardEngine
from src.core.save_system import SaveSystem
from src.data.byte_personality import BYTE_PERSONALITY
from src.core.learning_analyzer import LearningAnalyzer
from src.core.adaptive_mentor import AdaptiveMentor
from src.core.achievement_database import AchievementDatabase

print("=" * 60)
print("        BYTE REFLECTION TEST")
print("=" * 60)

# ----------------------------------------------------
# Create Memory
# ----------------------------------------------------

memory = Memory()

memory.add_xp(250)

for _ in range(7):
    memory.increment_completed_missions()

# ----------------------------------------------------
# Create Personality System
# ----------------------------------------------------
personality_engine = PersonalityEngine(BYTE_PERSONALITY)

# ----------------------------------------------------
# Create ByteBrain
# ----------------------------------------------------

brain = ByteBrain(
    career_database=CareerDatabase(),
    career_response_generator=CareerResponseGenerator(
        personality_engine
    ),
    conversation_engine=ConversationEngine(),
    achievement_engine=AchievementEngine(
    AchievementDatabase()
),
    reward_engine=RewardEngine(),
    mentor_engine=MentorEngine(),
    reflection_engine=ReflectionEngine(),
    memory=memory,
    save_system=SaveSystem(),
    learning_analyzer=LearningAnalyzer(),
    adaptive_mentor=AdaptiveMentor(),
)

# ----------------------------------------------------
# Test Reflection
# ----------------------------------------------------

print()
print(brain.get_learning_reflection())

print()
print("=" * 60)
print("✅ Byte Reflection Test Completed Successfully!")