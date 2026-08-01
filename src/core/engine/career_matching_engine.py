class CareerMatchingEngine:

    def __init__(self):
        pass

    def calculate_match(self, student_profile, career_profile):

        total_score = 0
        maximum_score = 0

        student_scores = student_profile.get_scores()

        for trait, importance in career_profile.required_traits.items():

            student_score = student_scores.get(trait, 0)

            difference = abs(student_score - importance)

            trait_points = max(0, 5 - difference)

            weighted_points = trait_points * importance

            total_score += weighted_points

            maximum_score += 5 * importance

        percentage = round((total_score / maximum_score) * 100)

        return percentage