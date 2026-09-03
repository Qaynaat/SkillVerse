class RecommendationExplanationEngine:
    """Explains why a career matches a student's profile."""

    def explain(self, student_profile, career_profile, match_score):

        student_data = student_profile.get_profile()
        ideal_profile = career_profile.ideal_profile

        strengths = []

        for category, career_traits in ideal_profile.items():

            student_traits = student_data.get(category, {})

            for trait, importance in career_traits.items():

                student_score = student_traits.get(trait, 0)

                if student_score >= 4 and importance >= 4:
                    strengths.append(trait)

        career_name = career_profile.name

        if strengths:

            trait_text = ", ".join(
                trait.replace("_", " ")
                for trait in strengths[:4]
            )

            return (
                f"{career_name} is a {match_score}% match for you. "
                f"Your {trait_text} align strongly with this career."
            )

        return (
            f"{career_name} is a {match_score}% match for you. "
            "Your overall profile shows potential for this career."
        )