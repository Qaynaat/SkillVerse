from src.core.engine.quiz_profile_builder import QuizProfileBuilder
from src.core.engine.career_recommendation_engine import (
    CareerRecommendationEngine
)
from src.core.engine.recommendation_explanation_engine import (
    RecommendationExplanationEngine
)


class CareerDiscoveryService:
    """Coordinates the complete SkillVerse career discovery flow."""

    def __init__(self):

        self.profile_builder = QuizProfileBuilder()

        self.recommendation_engine = (
            CareerRecommendationEngine()
        )

        self.explanation_engine = (
            RecommendationExplanationEngine()
        )

    def discover(
        self,
        student_profile,
        quiz_questions,
        answers,
        careers,
        top_n=5
    ):

        # Step 1: Build the student's personality profile
        student_profile = self.profile_builder.build_profile(
            student_profile,
            quiz_questions,
            answers
        )

        # Step 2: Find the best career matches
        recommendations = (
            self.recommendation_engine.recommend(
                student_profile=student_profile,
                careers=careers,
                top_k=top_n
            )
        )

        # Step 3: Explain every recommendation
        results = []

        for recommendation in recommendations:

            career = recommendation["career"]
            score = recommendation["score"]

            explanation = (
                self.explanation_engine.explain(
                    student_profile,
                    career,
                    score
                )
            )

            results.append({
                "career": career,
                "score": score,
                "explanation": explanation
            })

        return {
            "student_profile": student_profile,
            "recommendations": results
        }