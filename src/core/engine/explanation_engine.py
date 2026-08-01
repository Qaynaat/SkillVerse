class ExplanationEngine:

    def __init__(self):
        pass

    def explain_career(self, student_profile, career):

        strongest_trait = student_profile.get_strongest_trait()["name"]
        explanation = (
            f"I recommended {career.name} because your strongest trait is "
            f"{strongest_trait.replace('_', ' ').title()}. "
            f"{career.recommendation_reason}"
        )

        return explanation