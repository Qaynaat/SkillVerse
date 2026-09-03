from src.core.engine.career_matching_engine import CareerMatchingEngine
from src.core.career_database import CareerDatabase


class CareerRecommendationEngine:
    """Generates ranked career recommendations for a student."""

    def __init__(self):

        self.database = CareerDatabase()
        self.matching_engine = CareerMatchingEngine()

    def recommend(self, student_profile, limit=5):

        recommendations = []

        for career_name, career_profile in self.database.careers.items():

            score = self.matching_engine.calculate_match(
                student_profile,
                career_profile
            )

            recommendations.append({
                "career": career_name,
                "score": score
            })

        recommendations.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return recommendations[:limit]