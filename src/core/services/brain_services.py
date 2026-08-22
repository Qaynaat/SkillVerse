from dataclasses import dataclass
from src.core.career_database import CareerDatabase
from src.core.career_response_generator import CareerResponseGenerator
from src.core.engine.conversation_engine import ConversationEngine
from src.core.engine.personality_engine import PersonalityEngine
from src.core.engine.achievement_engine import AchievementEngine
from src.core.achievement_database import AchievementDatabase
from src.core.engine.reward_engine import RewardEngine
from src.core.engine.mentor_engine import MentorEngine
from src.core.engine.reflection_engine import ReflectionEngine
from src.core.learning_analyzer import LearningAnalyzer
from src.core.adaptive_mentor import AdaptiveMentor
from src.core.learning_insights import LearningInsights
from src.core.progress_dashboard import ProgressDashboard
from src.core.study_planner import StudyPlanner
from src.core.engine.daily_goal_engine import DailyGoalEngine
from src.core.engine.smart_reminder_engine import SmartReminderEngine
from src.core.engine.motivation_engine import MotivationEngine
from src.core.engine.encouragement_engine import EncouragementEngine
from src.core.engine.celebration_engine import CelebrationEngine
from src.core.engine.quote_engine import QuoteEngine
from src.core.engine.learning_tip_engine import LearningTipEngine
from src.core.engine.success_prediction_engine import SuccessPredictionEngine
from src.data.byte_personality import BYTE_PERSONALITY
from src.core.habit_analyzer import HabitAnalyzer
from src.core.consistency_analyzer import ConsistencyAnalyzer
from src.core.weakness_detector import WeaknessDetector
from src.core.strength_detector import StrengthDetector
from src.core.learning_style_detector import LearningStyleDetector
from src.core.burnout_detector import BurnoutDetector
from src.core.confidence_estimator import ConfidenceEstimator
from src.core.productivity_analyzer import ProductivityAnalyzer
from src.core.smart_goal_generator import SmartGoalGenerator
from src.core.personalized_roadmap_engine import PersonalizedRoadmapEngine
from src.core.adaptive_difficulty import AdaptiveDifficulty
from src.core.mission_recommendation import MissionRecommendation
from src.core.smart_revision_planner import SmartRevisionPlanner
from src.core.next_best_action_engine import NextBestActionEngine
from src.core.learning_velocity_tracker import LearningVelocityTracker

@dataclass
class BrainServices:

    career_database: CareerDatabase
    career_response_generator: CareerResponseGenerator
    conversation_engine: ConversationEngine
    achievement_engine: AchievementEngine
    reward_engine: RewardEngine
    mentor_engine: MentorEngine
    reflection_engine: ReflectionEngine
    learning_analyzer: LearningAnalyzer
    adaptive_mentor: AdaptiveMentor
    learning_insights: LearningInsights
    progress_dashboard: ProgressDashboard
    study_planner: StudyPlanner
    daily_goal_engine: DailyGoalEngine
    smart_reminder_engine: SmartReminderEngine
    motivation_engine: MotivationEngine
    encouragement_engine: EncouragementEngine
    celebration_engine: CelebrationEngine
    quote_engine: QuoteEngine
    learning_tip_engine: LearningTipEngine
    success_prediction_engine: SuccessPredictionEngine
    habit_analyzer: HabitAnalyzer
    consistency_analyzer: ConsistencyAnalyzer
    weakness_detector: WeaknessDetector
    strength_detector: StrengthDetector
    learning_style_detector: LearningStyleDetector
    burnout_detector: BurnoutDetector
    confidence_estimator: ConfidenceEstimator
    productivity_analyzer: ProductivityAnalyzer
    smart_goal_generator: SmartGoalGenerator
    personalized_roadmap_engine: PersonalizedRoadmapEngine
    adaptive_difficulty: AdaptiveDifficulty
    mission_recommendation: MissionRecommendation
    smart_revision_planner: SmartRevisionPlanner
    next_best_action_engine: NextBestActionEngine
    learning_velocity_tracker: LearningVelocityTracker

    @classmethod
    def default(cls):
        personality = PersonalityEngine(BYTE_PERSONALITY)

        return cls(
            career_database=CareerDatabase(),
            career_response_generator=CareerResponseGenerator(personality),
            conversation_engine=ConversationEngine(),
            achievement_engine=AchievementEngine(AchievementDatabase()),
            reward_engine=RewardEngine(),
            mentor_engine=MentorEngine(),
            reflection_engine=ReflectionEngine(),
            learning_analyzer=LearningAnalyzer(),
            adaptive_mentor=AdaptiveMentor(),
            learning_insights=LearningInsights(),
            progress_dashboard=ProgressDashboard(),
            study_planner=StudyPlanner(),
            daily_goal_engine=DailyGoalEngine(),
            smart_reminder_engine=SmartReminderEngine(),
            motivation_engine=MotivationEngine(),
            encouragement_engine=EncouragementEngine(),
            celebration_engine=CelebrationEngine(),
            quote_engine=QuoteEngine(),
            learning_tip_engine=LearningTipEngine(),
            success_prediction_engine=SuccessPredictionEngine(),
            habit_analyzer=HabitAnalyzer(),
            consistency_analyzer=ConsistencyAnalyzer(),
            weakness_detector=WeaknessDetector(),
            strength_detector=StrengthDetector(),
            learning_style_detector=LearningStyleDetector(),
            burnout_detector=BurnoutDetector(),
            confidence_estimator=ConfidenceEstimator(),
            productivity_analyzer=ProductivityAnalyzer(),
            smart_goal_generator=SmartGoalGenerator(),
            personalized_roadmap_engine=PersonalizedRoadmapEngine(),
            adaptive_difficulty=AdaptiveDifficulty(),
            mission_recommendation=MissionRecommendation(),
            smart_revision_planner=SmartRevisionPlanner(),
            next_best_action_engine=NextBestActionEngine(),
            learning_velocity_tracker=LearningVelocityTracker(),
)       