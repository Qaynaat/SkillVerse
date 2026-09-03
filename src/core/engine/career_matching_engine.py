class CareerMatchingEngine:

    def __init__(self):
        pass

    def calculate_match(self, student_profile, career_profile):

        total_score = 0
        maximum_score = 0

        student_profile_data = student_profile.get_profile()

        for category, career_traits in career_profile.ideal_profile.items():

            student_traits = student_profile_data.get(category, {})

            for trait, importance in career_traits.items():

                student_score = student_traits.get(trait, 0)

                weighted_score = student_score * importance

                maximum_trait_score = 5 * importance

                total_score += weighted_score
                maximum_score += maximum_trait_score

        if maximum_score == 0:
            return 0

        percentage = (total_score / maximum_score) * 100

        return round(percentage, 2)