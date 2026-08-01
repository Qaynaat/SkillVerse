from src.core.career_database import CareerDatabase
class CareerRecommendationEngine:
    def __init__(self):
        self.database = CareerDatabase()
    def calculate_match(self, student_profile, career_profile):
        total_score=0
        total_traits=0
        for category in career_profile:
            if category not in student_profile:
                continue

            for trait in career_profile[category]:
                student_score =student_profile[category].get(trait,0)
                career_data =career_profile[category].get(trait,0)
                if career_data == 0:
                    continue
                match_percentage = ( min(student_score, career_data) / career_data) * 100
                total_score += match_percentage
                total_traits += 1
        if total_traits == 0:
            return 0
        
        return round(total_score / total_traits, 2)

    def recommend_careers(self, student_profile):
        recommendations = []

        all_careers = self.database.get_all_careers()

        for career_name, career_data in all_careers:

            percentage = self.calculate_match(
                student_profile,
                career_data["profile"]
            )

            recommendations.append((career_name, percentage))

        recommendations.sort(key=lambda item: item[1], reverse=True)

        return recommendations[:3]

