class AdaptiveGuidanceResultEngine:
    """
    Mission 113
    Converts adaptive guidance data into a clean,
    student-friendly result.
    """

    def build_result(self, student_profile, guidance):
        strongest_trait = (
            student_profile.get_strongest_trait()
            or "your strongest traits"
        )

        weakest_trait = (
            student_profile.get_weakest_trait()
            or "an area for growth"
        )

        if guidance is None:
            guidance = {}

        career = guidance.get("career")
        alignment = guidance.get("alignment", 0)
        next_steps = guidance.get("next_steps", [])
        strengths = guidance.get("strengths", [])
        growth_areas = guidance.get("growth_areas", [])

        result = {
            "career": career,
            "alignment": alignment,
            "strongest_trait": strongest_trait,
            "weakest_trait": weakest_trait,
            "strengths": strengths,
            "growth_areas": growth_areas,
            "next_steps": next_steps,
        }

        result["summary"] = self._build_summary(
            career,
            alignment,
            strongest_trait,
            weakest_trait,
        )

        return result

    def _build_summary(
        self,
        career,
        alignment,
        strongest_trait,
        weakest_trait,
    ):
        career_name = career or "This career"

        if alignment >= 80:
            return (
                f"{career_name} is a strong direction for you with "
                f"{alignment}% alignment. Your {strongest_trait} is a "
                f"valuable strength, while {weakest_trait} is an area "
                f"you can continue developing."
            )

        if alignment >= 60:
            return (
                f"{career_name} could be a good direction for you with "
                f"{alignment}% alignment. Your {strongest_trait} gives "
                f"you a useful foundation, while {weakest_trait} can "
                f"be developed further."
            )

        return (
            f"{career_name} may require some additional development, "
            f"with {alignment}% alignment. Your {strongest_trait} is "
            f"a strength to build on, while {weakest_trait} is an "
            f"important growth area."
        )