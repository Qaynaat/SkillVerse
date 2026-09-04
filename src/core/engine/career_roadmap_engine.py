class CareerRoadmapEngine:

    def build_roadmap(
        self,
        career_name,
        alignment,
        strengths,
        growth_areas
    ):

        phases = []

        phases.append({
            "phase": "Foundation",
            "focus": self._build_foundation(
                career_name,
                strengths
            )
        })

        phases.append({
            "phase": "Growth",
            "focus": self._build_growth(
                growth_areas
            )
        })

        phases.append({
            "phase": "Career Preparation",
            "focus": self._build_career_preparation(
                career_name,
                alignment
            )
        })

        return {
            "career": career_name,
            "alignment": alignment,
            "strengths": strengths,
            "growth_areas": growth_areas,
            "roadmap": phases
        }

    def _build_foundation(
        self,
        career_name,
        strengths
    ):

        if strengths:
            strength_text = ", ".join(strengths)

            return (
                f"Build on your existing strengths in "
                f"{strength_text} while learning the "
                f"foundations of {career_name}."
            )

        return (
            f"Start by learning the core foundations "
            f"of {career_name}."
        )

    def _build_growth(
        self,
        growth_areas
    ):

        if growth_areas:
            areas = ", ".join(growth_areas)

            return (
                f"Focus on improving these areas: {areas}."
            )

        return (
            "Continue strengthening your skills through "
            "practice and real projects."
        )

    def _build_career_preparation(
        self,
        career_name,
        alignment
    ):

        if alignment >= 80:
            return (
                f"You have strong alignment with {career_name}. "
                f"Start building projects and preparing for "
                f"real career opportunities."
            )

        if alignment >= 60:
            return (
                f"You have a solid foundation for {career_name}. "
                f"Continue developing your skills and build "
                f"practical projects."
            )

        return (
            f"Explore {career_name} further while developing "
            f"the important skills required for this career."
        )