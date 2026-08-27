class CertificationRecommendationEngine:
    """
    Mission 085

    Recommends certification directions based on
    the selected career from the existing SkillVerse
    CareerDatabase.

    The engine does not own certification data.
    """

    def __init__(self, career_database):
        self.career_database = career_database

    # ==========================================================
    # CAREER LOOKUP
    # ==========================================================

    def _get_career(self, career_name):

        career = self.career_database.get_career(
            career_name
        )

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
    # CERTIFICATION DIRECTION
    # ==========================================================

    @staticmethod
    def _build_certification_directions(
        career_name,
        skills,
        career_paths
    ):

        directions = []

        # Career-path-based recommendations
        for path in career_paths[:3]:

            directions.append(
                f"{path} certification"
            )

        # Skill-based recommendations
        skill_map = {
            "Programming":
                "Programming certification",

            "Python":
                "Python certification",

            "Linux":
                "Linux certification",

            "Networking":
                "Networking certification",

            "Cloud Computing":
                "Cloud certification",

            "Version Control":
                "Version Control certification",

            "Cybersecurity":
                "Cybersecurity certification",

            "Ethical Hacking":
                "Ethical Hacking certification",

            "Data Analysis":
                "Data Analytics certification",

            "Machine Learning":
                "Machine Learning certification",

            "DevOps":
                "DevOps certification",
        }

        for skill in skills:

            recommendation = skill_map.get(skill)

            if recommendation:
                directions.append(
                    recommendation
                )

        # Remove duplicates while preserving order
        unique_directions = []

        for direction in directions:

            if direction not in unique_directions:
                unique_directions.append(direction)

        # Fallback
        if not unique_directions:

            unique_directions.append(
                f"{career_name} professional certification"
            )

        return unique_directions

    # ==========================================================
    # ANALYSIS
    # ==========================================================

    def analyze(self, career_name):

        career = self._get_career(
            career_name
        )

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

        certification_directions = (
            self._build_certification_directions(
                name,
                skills,
                career_paths
            )
        )

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

        recommendation = (
            f"Consider certifications related to "
            f"{', '.join(certification_directions[:3])}. "
            "Choose certifications that strengthen your "
            "career direction and practical skills."
        )

        return {
            "career": name,
            "skills": skills,
            "career_paths": career_paths,
            "recommended_certifications":
                certification_directions,
            "priority": priority,
            "recommendation": recommendation,
        }

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, report):

        lines = [
            "",
            "🎓 Certification Recommendation",
            "",
            f"🎯 Career: {report['career']}",
            "",
            "📜 Recommended Certifications:"
        ]

        if report[
            "recommended_certifications"
        ]:

            for certification in report[
                "recommended_certifications"
            ]:

                lines.append(
                    f"• {certification}"
                )

        else:

            lines.append(
                "• No certification directions available."
            )

        lines.extend([
            "",
            "📚 Relevant Skills:"
        ])

        if report["skills"]:

            for skill in report["skills"]:

                lines.append(
                    f"• {skill}"
                )

        else:

            lines.append(
                "• No skills recorded."
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