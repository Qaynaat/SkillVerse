class CareerSkillGapEngine:

    def analyze_skill_gaps(
        self,
        student_profile,
        career_profile
    ):

        student_scores = student_profile.get_scores()

        strengths = []
        growth_areas = []
        gaps = {}

        for trait, required_score in career_profile.required_traits.items():

            student_score = student_scores.get(trait, 0)

            gap = round(required_score - student_score, 2)

            if gap <= 0:
                strengths.append(trait)

            else:
                growth_areas.append(trait)
                gaps[trait] = gap

        return {
            "career": career_profile.name,
            "strengths": strengths,
            "growth_areas": growth_areas,
            "gaps": gaps
        }

    def get_priority_growth_areas(
        self,
        gap_analysis
    ):

        gaps = gap_analysis.get("gaps", {})

        sorted_gaps = sorted(
            gaps.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [
            trait
            for trait, gap in sorted_gaps
        ]

    def build_summary(
        self,
        gap_analysis
    ):

        career = gap_analysis["career"]

        strengths = gap_analysis["strengths"]

        growth_areas = gap_analysis["growth_areas"]

        if not growth_areas:
            return (
                f"You currently meet or exceed the main trait "
                f"requirements for {career}."
            )

        growth_text = ", ".join(growth_areas)

        if strengths:
            strength_text = ", ".join(strengths)

            return (
                f"For {career}, your strengths include "
                f"{strength_text}. Focus on improving "
                f"{growth_text}."
            )

        return (
            f"For {career}, focus on developing these areas: "
            f"{growth_text}."
        )