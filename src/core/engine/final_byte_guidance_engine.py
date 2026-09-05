"""
============================================================
SkillVerse - Mission 118
Final Byte Guidance Engine

Combines:
• Student Profile
• Career Recommendation
• Goal Alignment
• Adaptive Guidance
• Career Roadmap
• Skill Gap Analysis
• Reflection
• Smart Reminders

Produces Byte's final actionable guidance.
============================================================
"""


class FinalByteGuidanceEngine:

    def __init__(self):
        pass

    def generate_guidance(
        self,
        student_profile,
        career_recommendation,
        goal_alignment,
        adaptive_guidance,
        career_roadmap,
        skill_gap,
        reflection,
        smart_reminder,
    ):
        career = self._get_career(career_recommendation)
        alignment = self._get_alignment(goal_alignment)
        strengths = self._get_strengths(student_profile)
        gaps = self._get_gaps(skill_gap)
        next_action = self._get_next_action(
            adaptive_guidance,
            career_roadmap,
            smart_reminder,
            gaps,
        )

        summary = self._build_summary(
            career,
            alignment,
            strengths,
            gaps,
        )

        return {
            "career": career,
            "alignment": alignment,
            "strengths": strengths,
            "skill_gaps": gaps,
            "next_action": next_action,
            "summary": summary,
            "reflection": reflection,
            "reminder": smart_reminder,
            "guidance": (
                f"Based on your profile and progress, "
                f"{career} is your current recommended direction. "
                f"Your alignment is {alignment}%. "
                f"Focus next on {next_action}"
            ),
        }

    def _get_career(self, recommendation):
        if isinstance(recommendation, str):
            return recommendation

        if isinstance(recommendation, dict):
            return (
                recommendation.get("career")
                or recommendation.get("name")
                or recommendation.get("title")
                or "your selected career"
            )

        return "your selected career"

    def _get_alignment(self, alignment):
        if isinstance(alignment, (int, float)):
            return round(alignment, 2)

        if isinstance(alignment, dict):
            value = (
                alignment.get("alignment")
                or alignment.get("score")
                or alignment.get("percentage")
                or 0
            )
            return round(float(value), 2)

        return 0

    def _get_strengths(self, student_profile):
        if isinstance(student_profile, dict):
            strengths = student_profile.get("strengths")

            if strengths:
                return list(strengths)

            scores = student_profile.get("scores", {})

        else:
            strengths = getattr(student_profile, "strengths", None)

            if strengths:
                return list(strengths)

            scores = getattr(student_profile, "scores", {})

        if not scores:
            return []

        return [
            trait
            for trait, score in scores.items()
            if isinstance(score, (int, float)) and score >= 4
        ]

    def _get_gaps(self, skill_gap):
        if not skill_gap:
            return []

        if isinstance(skill_gap, list):
            return skill_gap

        if isinstance(skill_gap, dict):
            return (
                skill_gap.get("gaps")
                or skill_gap.get("skill_gaps")
                or skill_gap.get("missing_skills")
                or []
            )

        return []

    def _get_next_action(
        self,
        adaptive_guidance,
        career_roadmap,
        smart_reminder,
        gaps,
    ):
        if isinstance(adaptive_guidance, dict):
            action = (
                adaptive_guidance.get("next_action")
                or adaptive_guidance.get("recommendation")
                or adaptive_guidance.get("action")
            )

            if action:
                return action

        if isinstance(career_roadmap, dict):
            action = (
                career_roadmap.get("next_step")
                or career_roadmap.get("next_action")
            )

            if action:
                return action

        if gaps:
            return f"develop your {gaps[0]} skill"

        if smart_reminder:
            if isinstance(smart_reminder, str):
                return smart_reminder

            if isinstance(smart_reminder, dict):
                return (
                    smart_reminder.get("message")
                    or smart_reminder.get("reminder")
                    or "continue your planned learning activity"
                )

        return "continue your learning roadmap"

    def _build_summary(
        self,
        career,
        alignment,
        strengths,
        gaps,
    ):
        strength_text = (
            ", ".join(strengths)
            if strengths
            else "your existing strengths"
        )

        gap_text = (
            ", ".join(gaps)
            if gaps
            else "your remaining development areas"
        )

        return (
            f"{career} currently shows {alignment}% alignment. "
            f"Your strongest areas include {strength_text}. "
            f"Your main development focus should be {gap_text}."
        )