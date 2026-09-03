from src.core.engine.career_matching_engine import CareerMatchingEngine
from src.core.career_database import CareerDatabase


class CareerRecommendationEngine:
    """Generates ranked career recommendations for a student."""

    def __init__(self):

        self.database = CareerDatabase()
        self.matching_engine = CareerMatchingEngine()

    def recommend(self, student_profile, careers=None, top_k=5):

        if careers is None:
            careers = list(self.database.careers.values())

        recommendations = []

        for career in careers:

            score = self.matching_engine.calculate_match(
                student_profile,
                career
            )

            recommendations.append({
                "career": career,
                "score": score
            })

        recommendations.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return recommendations[:top_k]