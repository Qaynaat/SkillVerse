from src.core.engine.quiz_scoring_engine import QuizScoringEngine
from src.core.engine.quiz_profile_builder import QuizProfileBuilder
from src.core.services.career_discovery_service import CareerDiscoveryService
from src.core.engine.career_discovery_result_engine import (
    CareerDiscoveryResultEngine
)
from src.core.student_profile import StudentProfile


class CareerDiscoveryOrchestrator:

    def __init__(self):

        self.quiz_scoring_engine = QuizScoringEngine()
        self.quiz_profile_builder = QuizProfileBuilder()
        self.career_discovery_service = CareerDiscoveryService()
        self.result_engine = CareerDiscoveryResultEngine()

    def run_discovery(
        self,
        questions,
        answers,
        careers,
        explanations=None,
        guidance=None
    ):

        # Step 1: Calculate trait scores
        trait_scores = (
            self.quiz_scoring_engine.calculate_trait_scores(
                questions,
                answers
            )
        )

        # Step 2: Create and build student profile
        student_profile = StudentProfile()

        student_profile = self.quiz_profile_builder.build_profile(
            student_profile,
            questions,
            answers
        )

        # Step 3: Discover careers
        discovery = self.career_discovery_service.discover(
            student_profile,
            questions,
            answers,
            careers
        )

        recommendations = discovery["recommendations"]

        # Step 4: Build final result
        result = self.result_engine.build_result(
            student_profile,
            recommendations,
            explanations or [],
            guidance or {}
        )

        return result