from src.core.byte_brain import ByteBrain
from src.core.memory import Memory
from src.core.daily_goal_engine import DailyGoalEngine
from src.core.study_planner import StudyPlanner
from src.core.progress_dashboard import ProgressDashboard
from src.core.learning_insights import LearningInsights
from src.core.learning_analyzer import LearningAnalyzer
from src.core.adaptive_mentor import AdaptiveMentor
from src.core.reflection_engine import ReflectionEngine
from src.core.achievement_engine import AchievementEngine
from src.core.achievement_database import AchievementDatabase
from src.core.reward_engine import RewardEngine
from src.core.mentor_engine import MentorEngine
from src.core.career_database import CareerDatabase
from src.core.career_response_generator import CareerResponseGenerator
from src.core.conversation_engine import ConversationEngine
from src.core.save_system import SaveSystem
from src.core.personality_engine import PersonalityEngine
from src.data.byte_personality import BYTE_PERSONALITY

print("=" * 60)
print("      BYTE DAILY GOAL TEST")
print("=" * 60)

memory = Memory()

memory.add_xp(180)

personality = PersonalityEngine(BYTE_PERSONALITY)

brain = ByteBrain(
    career_database=CareerDatabase(),
    career_response_generator=CareerResponseGenerator(personality),
    conversation_engine=ConversationEngine(),
    achievement_engine=AchievementEngine(AchievementDatabase()),
    reward_engine=RewardEngine(),
    mentor_engine=MentorEngine(),
    reflection_engine=ReflectionEngine(),
    memory=memory,
    save_system=SaveSystem(),
    learning_analyzer=LearningAnalyzer(),
    adaptive_mentor=AdaptiveMentor(),
    learning_insights=LearningInsights(),
    progress_dashboard=ProgressDashboard(),
    study_planner=StudyPlanner(),
    daily_goal_engine=DailyGoalEngine(),
)

print()
print(brain.get_daily_goals())

print()
print("=" * 60)
print("✅ Byte Daily Goal Test Completed Successfully!")