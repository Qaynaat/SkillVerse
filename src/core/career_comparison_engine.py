class CareerComparisonEngine:
    """
    Mission 080
    Compares two careers using the existing SkillVerse career database.

    The engine does NOT own the career database.
    It receives the database/service and asks it for career information.
    """

    def __init__(self, career_database):
        self.career_database = career_database

    # ==========================================================
    # CAREER LOOKUP
    # ==========================================================

    def _get_career(self, career_name):
        """
        Retrieve a career from the existing CareerDatabase.

        This adapter supports several common lookup method names
        so the engine can work with the existing SkillVerse database.
        """

        database = self.career_database

        # Most likely existing API
        if hasattr(database, "get_career"):
            return database.get_career(career_name)

        if hasattr(database, "find_career"):
            return database.find_career(career_name)

        if hasattr(database, "get"):
            return database.get(career_name)

        # Dictionary-style database
        if isinstance(database, dict):
            return database.get(career_name)

        raise AttributeError(
            "CareerDatabase does not provide a supported career lookup method."
        )

    # ==========================================================
    # NORMALIZATION
    # ==========================================================

    @staticmethod
    def _get_value(career, *keys, default=None):
        """
        Safely retrieve a field from either a dictionary or object.
        """

        if career is None:
            return default

        for key in keys:

            if isinstance(career, dict):
                if key in career:
                    return career[key]

            if hasattr(career, key):
                return getattr(career, key)

        return default

    @staticmethod
    def _normalize_list(value):
        """
        Convert supported values into a clean list.
        """

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
    # COMPARISON
    # ==========================================================

    def analyze(self, career_one_name, career_two_name):

        career_one = self._get_career(career_one_name)
        career_two = self._get_career(career_two_name)

        if career_one is None:
            raise ValueError(
                f"Career not found: {career_one_name}"
            )

        if career_two is None:
            raise ValueError(
                f"Career not found: {career_two_name}"
            )

        name_one = self._get_value(
            career_one,
            "name",
            "career_name",
            default=career_one_name
        )

        name_two = self._get_value(
            career_two,
            "name",
            "career_name",
            default=career_two_name
        )

        description_one = self._get_value(
            career_one,
            "description",
            "career_description",
            default=""
        )

        description_two = self._get_value(
            career_two,
            "description",
            "career_description",
            default=""
        )

        skills_one = self._normalize_list(
            self._get_value(
                career_one,
                "skills",
                "required_skills",
                "core_skills",
                default=[]
            )
        )

        skills_two = self._normalize_list(
            self._get_value(
                career_two,
                "skills",
                "required_skills",
                "core_skills",
                default=[]
            )
        )

        paths_one = self._normalize_list(
            self._get_value(
                career_one,
                "career_paths",
                "paths",
                default=[]
            )
        )

        paths_two = self._normalize_list(
            self._get_value(
                career_two,
                "career_paths",
                "paths",
                default=[]
            )
        )

        # ------------------------------------------------------
        # Skill comparison
        # ------------------------------------------------------

        normalized_one = {
            str(skill).strip().lower()
            for skill in skills_one
        }

        normalized_two = {
            str(skill).strip().lower()
            for skill in skills_two
        }

        shared_skills = sorted(
            normalized_one.intersection(normalized_two)
        )

        unique_one = sorted(
            normalized_one.difference(normalized_two)
        )

        unique_two = sorted(
            normalized_two.difference(normalized_one)
        )

        # ------------------------------------------------------
        # Build comparison
        # ------------------------------------------------------

        return {
            "career_one": {
                "name": name_one,
                "description": description_one,
                "skills": skills_one,
                "career_paths": paths_one,
            },

            "career_two": {
                "name": name_two,
                "description": description_two,
                "skills": skills_two,
                "career_paths": paths_two,
            },

            "shared_skills": shared_skills,

            "career_one_unique_skills": unique_one,

            "career_two_unique_skills": unique_two,

            "comparison_summary": self._build_summary(
                name_one,
                name_two,
                shared_skills,
                unique_one,
                unique_two
            )
        }

    # ==========================================================
    # SUMMARY
    # ==========================================================

    @staticmethod
    def _build_summary(
        career_one,
        career_two,
        shared_skills,
        unique_one,
        unique_two
    ):

        if shared_skills:
            shared_text = (
                f"{career_one} and {career_two} share "
                f"{len(shared_skills)} skill"
                f"{'s' if len(shared_skills) != 1 else ''}."
            )
        else:
            shared_text = (
                f"{career_one} and {career_two} have no "
                "directly matching skills in the current database."
            )

        if unique_one and unique_two:
            difference_text = (
                f"{career_one} has {len(unique_one)} "
                "skills not listed for the second career, while "
                f"{career_two} has {len(unique_two)} "
                "skills not listed for the first career."
            )

        else:
            difference_text = (
                "The current database does not show major "
                "skill differences between the two careers."
            )

        return f"{shared_text} {difference_text}"

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, report):

        career_one = report["career_one"]
        career_two = report["career_two"]

        lines = [
            "",
            "⚖️ Career Comparison",
            "",
            f"💻 Career 1: {career_one['name']}",
            f"🛡️ Career 2: {career_two['name']}",
            "",
            "📚 Shared Skills:"
        ]

        if report["shared_skills"]:
            for skill in report["shared_skills"]:
                lines.append(f"• {skill}")
        else:
            lines.append("• No shared skills found.")

        lines.extend([
            "",
            f"🎯 {career_one['name']} Skills:"
        ])

        if career_one["skills"]:
            for skill in career_one["skills"]:
                lines.append(f"• {skill}")
        else:
            lines.append("• No skills recorded.")

        lines.extend([
            "",
            f"🎯 {career_two['name']} Skills:"
        ])

        if career_two["skills"]:
            for skill in career_two["skills"]:
                lines.append(f"• {skill}")
        else:
            lines.append("• No skills recorded.")

        lines.extend([
            "",
            "💡 Comparison:",
            report["comparison_summary"],
            ""
        ])

        return "\n".join(lines)