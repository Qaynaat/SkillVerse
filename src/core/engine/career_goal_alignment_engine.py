class CareerGoalAlignmentEngine:
    """Measures how well a student's profile aligns with a chosen career."""

    def calculate_alignment(self, student_profile, career_profile):
        student_scores = student_profile.get_scores()
        required_traits = career_profile.required_traits

        total_score = 0
        maximum_score = 0

        strong_traits = []
        growth_areas = []

        for trait, importance in required_traits.items():

            student_score = student_scores.get(trait, 0)

            difference = abs(student_score - importance)

            trait_score = max(0, 5 - difference)

            weighted_score = trait_score * importance
            maximum_trait_score = 5 * importance

            total_score += weighted_score
            maximum_score += maximum_trait_score

            # ------------------------------------------
            # Strong Trait
            # ------------------------------------------

            if student_score >= importance:
                strong_traits.append(trait)

            # ------------------------------------------
            # Growth Area
            # ------------------------------------------

            elif student_score < importance:
                growth_areas.append(trait)

        if maximum_score == 0:
            alignment = 0
        else:
            alignment = round(
                (total_score / maximum_score) * 100,
                2
            )

        return {
            "career": career_profile.name,
            "alignment": alignment,
            "strong_traits": strong_traits,
            "growth_areas": growth_areas
        }