class InternshipRecommendationEngine:
    """
    Mission 084
    Recommends internship directions based on the selected career.

    The engine uses the existing CareerDatabase.
    It does not own career data.
    """

    def __init__(self, career_database):
        self.career_database = career_database

    # ==========================================================
    # CAREER LOOKUP
    # ==========================================================

    def _get_career(self, career_name):
        career = self.career_database.get_career(career_name)

        if career is None:
            raise ValueError(
                f"Career not found: {career_name}"
            )

        return career

    # ==========================================================
    # VALUE HELPERS
    # ==========================================================

    @staticmethod
    def _get_value(career, *keys, default=None):

        for key in keys:

            if isinstance(career, dict):
                if key in career:
                    return career[key]

            if hasattr(career, key):
                return getattr(career, key)

        return default

    @staticmethod
    def _normalize_list(value):

        if value is None:
            return []

        if isinstance(value, list):
            return value

        if isinstance(value, tuple):
            return list(value)

        if isinstance(value, set):
            return list(value)

        if isinstance(value, str):
            return [value]

        return [str(value)]

    # ==========================================================
    # INTERNSHIP RECOMMENDATION
    # ==========================================================

    def analyze(self, career_name):

        career = self._get_career(career_name)

        name = self._get_value(
            career,
            "name",
            "career_name",
            default=career_name
        )

        skills = self._normalize_list(
            self._get_value(
                career,
                "skills",
                "required_skills",
                "core_skills",
                default=[]
            )
        )

        career_paths = self._normalize_list(
            self._get_value(
                career,
                "career_paths",
                "paths",
                default=[]
            )
        )

        # ------------------------------------------------------
        # Internship directions
        # ------------------------------------------------------

        internship_roles = []

        for path in career_paths[:5]:
            internship_roles.append(
                f"{path} Intern"
            )

        if not internship_roles:
            internship_roles = [
                f"{name} Intern"
            ]

        # ------------------------------------------------------
        # Skills to strengthen before applying
        # ------------------------------------------------------

        preparation_skills = skills[:5]

        # ------------------------------------------------------
        # Priority
        # ------------------------------------------------------

        if len(skills) >= 5:
            priority = "High"
        elif len(skills) >= 3:
            priority = "Medium"
        else:
            priority = "Foundational"

        # ------------------------------------------------------
        # Recommendation
        # ------------------------------------------------------

        if internship_roles:
            recommendation = (
                f"Start with internships related to "
                f"{', '.join(internship_roles[:3])}. "
                "Strengthen the recommended skills while "
                "building practical experience."
            )
        else:
            recommendation = (
                "Build practical experience and strengthen "
                "career skills before applying."
            )

        return {
            "career": name,
            "skills": skills,
            "recommended_internships": internship_roles,
            "preparation_skills": preparation_skills,
            "priority": priority,
            "recommendation": recommendation,
        }

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, report):

        lines = [
            "",
            "💼 Internship Recommendation",
            "",
            f"🎯 Career: {report['career']}",
            "",
            "🚀 Recommended Internships:"
        ]

        if report["recommended_internships"]:

            for internship in report[
                "recommended_internships"
            ]:
                lines.append(
                    f"• {internship}"
                )

        else:
            lines.append(
                "• No internship directions available."
            )

        lines.extend([
            "",
            "📚 Preparation Skills:"
        ])

        if report["preparation_skills"]:

            for skill in report[
                "preparation_skills"
            ]:
                lines.append(
                    f"• {skill}"
                )

        else:
            lines.append(
                "• No preparation skills recorded."
            )

        lines.extend([
            "",
            f"📈 Priority: {report['priority']}",
            "",
            "💡 Recommendation:",
            report["recommendation"],
            ""
        ])

        return "\n".join(lines)