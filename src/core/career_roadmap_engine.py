class CareerRoadmapEngine:
    """
    Mission 081
    Generates a structured career roadmap using the existing
    SkillVerse CareerDatabase.

    The engine does NOT own career data.
    It receives the existing CareerDatabase and retrieves
    career information from it.
    """

    def __init__(self, career_database):
        self.career_database = career_database

    # ==========================================================
    # CAREER LOOKUP
    # ==========================================================

    def _get_career(self, career_name):
        """
        Retrieve career information from the existing
        CareerDatabase.
        """

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
        """
        Safely retrieve a value from either a dictionary
        or an object.
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
    # ROADMAP STAGES
    # ==========================================================

    @staticmethod
    def _build_stages(skills, career_paths):
        """
        Convert existing career information into a simple
        learner-friendly progression.

        This is a roadmap, NOT a course system.
        """

        skills = list(skills)
        career_paths = list(career_paths)

        # Keep the roadmap manageable.
        foundation_skills = skills[:3]
        core_skills = skills[3:6]
        advanced_skills = skills[6:]

        stages = []

        if foundation_skills:
            stages.append({
                "stage": 1,
                "title": "Foundations",
                "focus": foundation_skills
            })

        if core_skills:
            stages.append({
                "stage": 2,
                "title": "Core Skills",
                "focus": core_skills
            })

        if advanced_skills:
            stages.append({
                "stage": 3,
                "title": "Practical Development",
                "focus": advanced_skills
            })

        if career_paths:
            stages.append({
                "stage": len(stages) + 1,
                "title": "Career Direction",
                "focus": career_paths
            })

        # Always provide a final career-preparation stage.
        stages.append({
            "stage": len(stages) + 1,
            "title": "Career Preparation",
            "focus": [
                "Build practical experience",
                "Create a portfolio",
                "Prepare for opportunities"
            ]
        })

        return stages

    # ==========================================================
    # ANALYSIS
    # ==========================================================

    def analyze(self, career_name):

        career = self._get_career(career_name)

        name = self._get_value(
            career,
            "name",
            "career_name",
            default=career_name
        )

        description = self._get_value(
            career,
            "description",
            "career_description",
            default=""
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

        stages = self._build_stages(
            skills,
            career_paths
        )

        return {
            "career": name,
            "description": description,
            "skills": skills,
            "career_paths": career_paths,
            "stages": stages,
            "total_stages": len(stages),
            "total_skills": len(skills),
            "roadmap_summary": (
                f"The {name} roadmap begins with foundational "
                f"skills, progresses through core development, "
                f"and leads toward practical experience and "
                f"career preparation."
            )
        }

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, report):

        lines = [
            "",
            "🗺️ Career Roadmap",
            "",
            f"🎯 Career: {report['career']}",
            ""
        ]

        if report["description"]:
            lines.extend([
                "📖 Career Overview:",
                report["description"],
                ""
            ])

        for stage in report["stages"]:

            lines.extend([
                f"🟢 Stage {stage['stage']} — "
                f"{stage['title']}"
            ])

            for focus in stage["focus"]:
                lines.append(f"• {focus}")

            lines.append("")

        lines.extend([
            "📊 Roadmap Summary:",
            report["roadmap_summary"],
            "",
            f"📌 Total Stages: {report['total_stages']}",
            f"📚 Skills Covered: {report['total_skills']}",
            ""
        ])

        return "\n".join(lines)