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
from src.core.performance_trend_analyzer import PerformanceTrendAnalyzer
from src.core.learning_risk_predictor import LearningRiskPredictor
from src.core.learning_recovery_strategist import LearningRecoveryStrategist
from src.core.learning_intervention_engine import LearningInterventionEngine
from src.core.intervention_prioritizer import InterventionPrioritizer
from src.core.learning_decision_engine import LearningDecisionEngine
from src.core.learning_state_engine import LearningStateEngine
from src.core.learner_profile_snapshot import LearnerProfileSnapshot
from src.core.learning_profile_interpreter import LearningProfileInterpreter
from src.core.learning_profile_advisor import LearningProfileAdvisor
from src.core.learning_profile_action_planner import LearningProfileActionPlanner
from src.core.learning_action_execution_engine import LearningActionExecutionEngine
from src.core.learning_action_followup_engine import LearningActionFollowUpEngine
from src.core.learning_action_outcome_tracker import LearningActionOutcomeTracker
from src.core.learning_outcome_interpreter import LearningOutcomeInterpreter
from src.core.learning_outcome_decision_engine import LearningOutcomeDecisionEngine
from src.core.learning_outcome_action_planner import LearningOutcomeActionPlanner
from src.core.career_comparison_engine import CareerComparisonEngine
from src.core.career_roadmap_engine import CareerRoadmapEngine
from src.core.career_readiness_score_engine import CareerReadinessScoreEngine
from src.core.future_skills_recommendation_engine import FutureSkillsRecommendationEngine
from src.core.internship_recommendation_engine import InternshipRecommendationEngine
from src.core.certification_recommendation_engine import CertificationRecommendationEngine




@dataclass
class BrainServices:

    # ==================================================
    # Core / Career Services
    # ==================================================

    career_database: CareerDatabase
    career_response_generator: CareerResponseGenerator
    conversation_engine: ConversationEngine
    career_comparison_engine: CareerComparisonEngine
    career_roadmap_engine:CareerRoadmapEngine
    career_readiness_score_engine:CareerReadinessScoreEngine
    future_skills_recommendation_engine:FutureSkillsRecommendationEngine
    certification_recommendation_engine:CertificationRecommendationEngine

    # ==================================================
    # Mentor / Achievement Services
    # ==================================================

    achievement_engine: AchievementEngine
    reward_engine: RewardEngine
    mentor_engine: MentorEngine
    reflection_engine: ReflectionEngine

    # ==================================================
    # Learning Services
    # ==================================================

    learning_analyzer: LearningAnalyzer
    adaptive_mentor: AdaptiveMentor
    learning_insights: LearningInsights
    progress_dashboard: ProgressDashboard
    study_planner: StudyPlanner

    # ==================================================
    # Daily Learning Services
    # ==================================================

    daily_goal_engine: DailyGoalEngine
    smart_reminder_engine: SmartReminderEngine
    motivation_engine: MotivationEngine
    encouragement_engine: EncouragementEngine
    celebration_engine: CelebrationEngine
    quote_engine: QuoteEngine
    learning_tip_engine: LearningTipEngine
    success_prediction_engine: SuccessPredictionEngine

    # ==================================================
    # Learning Analysis Services
    # ==================================================

    habit_analyzer: HabitAnalyzer
    consistency_analyzer: ConsistencyAnalyzer
    weakness_detector: WeaknessDetector
    strength_detector: StrengthDetector
    learning_style_detector: LearningStyleDetector
    burnout_detector: BurnoutDetector
    confidence_estimator: ConfidenceEstimator
    productivity_analyzer: ProductivityAnalyzer

    # ==================================================
    # Adaptive Intelligence Layer
    # ==================================================

    smart_goal_generator: SmartGoalGenerator
    personalized_roadmap_engine: PersonalizedRoadmapEngine
    adaptive_difficulty: AdaptiveDifficulty
    mission_recommendation: MissionRecommendation
    smart_revision_planner: SmartRevisionPlanner
    next_best_action_engine: NextBestActionEngine
    learning_velocity_tracker: LearningVelocityTracker
    performance_trend_analyzer: PerformanceTrendAnalyzer
    learning_risk_predictor: LearningRiskPredictor
    learning_recovery_strategist: LearningRecoveryStrategist
    learning_intervention_engine: LearningInterventionEngine
    intervention_prioritizer: InterventionPrioritizer
    learning_decision_engine: LearningDecisionEngine
    learning_state_engine: LearningStateEngine
    internship_recommendation_engine: InternshipRecommendationEngine

    # ==================================================
    # Unified Learner Intelligence
    # ==================================================

    learner_profile_snapshot: LearnerProfileSnapshot
    learning_profile_interpreter: LearningProfileInterpreter
    learning_profile_advisor: LearningProfileAdvisor
    learning_profile_action_planner: LearningProfileActionPlanner
    learning_action_execution_engine: LearningActionExecutionEngine
    learning_action_followup_engine: LearningActionFollowUpEngine
    learning_action_outcome_tracker: LearningActionOutcomeTracker
    learning_outcome_interpreter: LearningOutcomeInterpreter
    learning_outcome_decision_engine: LearningOutcomeDecisionEngine
    learning_outcome_action_planner: LearningOutcomeActionPlanner
    

    # ==================================================
    # Default Service Factory
    # ==================================================

    @classmethod
    def default(cls):

        personality = PersonalityEngine(BYTE_PERSONALITY)
        career_database = CareerDatabase()
        # ==================================================
        # Create Intelligence Engines Once
        # ==================================================

        learning_risk_predictor = LearningRiskPredictor()

        learning_recovery_strategist = (
            LearningRecoveryStrategist()
        )

        learning_intervention_engine = (
            LearningInterventionEngine()
        )

        intervention_prioritizer = (
            InterventionPrioritizer()
        )

        learning_decision_engine = (
            LearningDecisionEngine()
        )

        learning_state_engine = (
            LearningStateEngine()
        )

        learning_velocity_tracker = (
            LearningVelocityTracker()
        )

        performance_trend_analyzer = (
            PerformanceTrendAnalyzer()
        )

        next_best_action_engine = (
            NextBestActionEngine()
        )

        # ==================================================
        # Unified Learner Profile Snapshot
        # ==================================================

        learner_profile_snapshot = LearnerProfileSnapshot(
            learning_risk_predictor=learning_risk_predictor,
            learning_recovery_strategist=learning_recovery_strategist,
            learning_intervention_engine=learning_intervention_engine,
            intervention_prioritizer=intervention_prioritizer,
            learning_decision_engine=learning_decision_engine,
            learning_state_engine=learning_state_engine,
            learning_velocity_tracker=learning_velocity_tracker,
            performance_trend_analyzer=performance_trend_analyzer,
            next_best_action_engine=next_best_action_engine,
        )

        # ==================================================
        # Build Brain Services
        # ==================================================

        return cls(

            # --------------------------------------------------
            # Core / Career
            # --------------------------------------------------

            career_database=career_database,

            career_response_generator=(
                CareerResponseGenerator(personality)
            ),

            conversation_engine=ConversationEngine(),

            career_comparison_engine=CareerComparisonEngine(
                career_database
            ),

            career_roadmap_engine=CareerRoadmapEngine(
                career_database
            ),

            career_readiness_score_engine=CareerReadinessScoreEngine(
                career_database
            ),

            future_skills_recommendation_engine=FutureSkillsRecommendationEngine(
                career_database
            ),
                internship_recommendation_engine=InternshipRecommendationEngine(
            career_database
            ),
            certification_recommendation_engine=CertificationRecommendationEngine(
        career_database
            ),


            # --------------------------------------------------
            # Achievement / Mentor
            # --------------------------------------------------

            achievement_engine=(
                AchievementEngine(AchievementDatabase())
            ),

            reward_engine=RewardEngine(),

            mentor_engine=MentorEngine(),

            reflection_engine=ReflectionEngine(),

            # --------------------------------------------------
            # Learning
            # --------------------------------------------------

            learning_analyzer=LearningAnalyzer(),

            adaptive_mentor=AdaptiveMentor(),

            learning_insights=LearningInsights(),

            progress_dashboard=ProgressDashboard(),

            study_planner=StudyPlanner(),

            # --------------------------------------------------
            # Daily Learning
            # --------------------------------------------------

            daily_goal_engine=DailyGoalEngine(),

            smart_reminder_engine=SmartReminderEngine(),

            motivation_engine=MotivationEngine(),

            encouragement_engine=EncouragementEngine(),

            celebration_engine=CelebrationEngine(),

            quote_engine=QuoteEngine(),

            learning_tip_engine=LearningTipEngine(),

            success_prediction_engine=(
                SuccessPredictionEngine()
            ),

            # --------------------------------------------------
            # Learning Analysis
            # --------------------------------------------------

            habit_analyzer=HabitAnalyzer(),

            consistency_analyzer=ConsistencyAnalyzer(),

            weakness_detector=WeaknessDetector(),

            strength_detector=StrengthDetector(),

            learning_style_detector=LearningStyleDetector(),

            burnout_detector=BurnoutDetector(),

            confidence_estimator=ConfidenceEstimator(),

            productivity_analyzer=ProductivityAnalyzer(),

            # --------------------------------------------------
            # Adaptive Intelligence
            # --------------------------------------------------

            smart_goal_generator=SmartGoalGenerator(),

            personalized_roadmap_engine=(
                PersonalizedRoadmapEngine()
            ),

            adaptive_difficulty=AdaptiveDifficulty(),

            mission_recommendation=MissionRecommendation(),

            smart_revision_planner=SmartRevisionPlanner(),

            next_best_action_engine=next_best_action_engine,

            learning_velocity_tracker=learning_velocity_tracker,

            performance_trend_analyzer=performance_trend_analyzer,

            learning_risk_predictor=learning_risk_predictor,

            learning_recovery_strategist=(
                learning_recovery_strategist
            ),

            learning_intervention_engine=(
                learning_intervention_engine
            ),

            intervention_prioritizer=(
                intervention_prioritizer
            ),

            learning_decision_engine=(
                learning_decision_engine
            ),

            learning_state_engine=(
                learning_state_engine
            ),

            # --------------------------------------------------
            # Unified Learner Intelligence
            # --------------------------------------------------

            learner_profile_snapshot=(
                learner_profile_snapshot
            ),
            learning_profile_interpreter=LearningProfileInterpreter(),
            learning_profile_advisor=LearningProfileAdvisor(),
            learning_profile_action_planner=LearningProfileActionPlanner(),
            learning_action_execution_engine=LearningActionExecutionEngine(),
            learning_action_followup_engine=LearningActionFollowUpEngine(),
            learning_action_outcome_tracker=LearningActionOutcomeTracker(),
            learning_outcome_interpreter=LearningOutcomeInterpreter(),
            learning_outcome_decision_engine=LearningOutcomeDecisionEngine(),
            learning_outcome_action_planner=LearningOutcomeActionPlanner(),
        )