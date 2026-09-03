class CareerDiscoveryResultEngine:

    def build_result(
        self,
        student_profile,
        recommendations,
        explanations,
        guidance
    ):

        if not recommendations:
            raise ValueError(
                "Career discovery requires recommendations."
            )

        top_recommendation = recommendations[0]

        result = {
            "strongest_trait":
                student_profile.get_strongest_trait(),

            "weakest_trait":
                student_profile.get_weakest_trait(),

            "trait_scores":
                student_profile.get_scores(),

            "top_career":
                top_recommendation["career"],

            "top_match":
                top_recommendation["score"],

            "recommendations":
                recommendations,

            "explanations":
                explanations,

            "guidance":
                guidance
        }

        return result