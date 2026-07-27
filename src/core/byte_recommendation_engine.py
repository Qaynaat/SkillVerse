from src.core.career_matching_engine import CareerMatchingEngine


class ByteRecommendationEngine:

    def __init__(self):

        self.matcher = CareerMatchingEngine()

    def recommend_careers(self, student_profile, careers):

        recommendations = []

        for career in careers:

            match_score = self.matcher.calculate_match(
                student_profile,
                career
            )

            recommendations.append({
                "career": career,
                "match_score": match_score
            })

        recommendations.sort(
            key=lambda career: career["match_score"],
            reverse=True
        )

        return recommendations[:3]