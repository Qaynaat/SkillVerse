class FutureSkillsRecommendationEngine:
    """
    Mission 083
    Recommends future-oriented skills for a selected career.

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
    # FUTURE SKILL KNOWLEDGE
    # ==========================================================

    FUTURE_SKILLS = {
        "Software Engineering": [
            "AI-assisted development",
            "Cloud Computing",
            "Cybersecurity",
            "System Design",
            "DevOps",
            "Testing and Automation",
            "Version Control"
        ],

        "Cybersecurity": [
            "AI Security",
            "Cloud Security",
            "Threat Intelligence",
            "Digital Forensics",
            "Security Automation",
            "Zero Trust Security",
            "Incident Response"
        ],

        "AI Engineering": [
            "Machine Learning",
            "Deep Learning",
            "Generative AI",
            "LLM Engineering",
            "MLOps",
            "Data Engineering",
            "AI Safety"
        ],

        "Data Science": [
            "Machine Learning",
            "Generative AI",
            "Data Engineering",
            "Data Visualization",
            "Statistical Modeling",
            "MLOps",
            "Big Data"
        ],

        "Cloud Engineering": [
            "Cloud Security",
            "DevOps",
            "Infrastructure as Code",
            "Containerization",
            "Kubernetes",
            "Cloud Automation",
            "Distributed Systems"
        ],

        "Game Development": [
            "Game AI",
            "Real-Time Rendering",
            "3D Development",
            "Game Optimization",
            "Multiplayer Systems",
            "Procedural Generation",
            "Game Physics"
        ],

        "Mobile Development": [
            "Cross-Platform Development",
            "Mobile Security",
            "Cloud Integration",
            "Mobile AI",
            "Performance Optimization",
            "App Architecture",
            "Testing Automation"
        ],

        "Web Development": [
            "AI Integration",
            "Web Security",
            "Cloud Development",
            "Progressive Web Apps",
            "Performance Optimization",
            "Backend Architecture",
            "Web Accessibility"
        ],

        "UI/UX Design": [
            "AI-assisted Design",
            "Design Systems",
            "Accessibility",
            "UX Research",
            "Product Design",
            "Interaction Design",
            "Design Prototyping"
        ],

        "DevOps Engineering": [
            "Cloud Engineering",
            "Kubernetes",
            "Infrastructure as Code",
            "DevSecOps",
            "Observability",
            "CI/CD Automation",
            "Platform Engineering"
        ]
    }

    # ==========================================================
    # ANALYSIS
    # ==========================================================

    def analyze(self, career_name, current_skills=None):

        career = self._get_career(career_name)

        current_skills = self._normalize_list(
            current_skills
        )

        career_skills = self._normalize_list(
            self._get_value(
                career,
                "skills",
                "required_skills",
                "core_skills",
                default=[]
            )
        )

        future_skills = self.FUTURE_SKILLS.get(
            career_name,
            [
                "Artificial Intelligence",
                "Cloud Computing",
                "Cybersecurity",
                "Automation",
                "Problem Solving"
            ]
        )

        normalized_current = {
            str(skill).strip().lower()
            for skill in current_skills
        }

        normalized_career = {
            str(skill).strip().lower()
            for skill in career_skills
        }

        # Skills the learner already has
        existing = []

        for skill in future_skills:

            if skill.lower() in normalized_current:
                existing.append(skill)

        # Future skills that should be developed
        recommended = [
            skill
            for skill in future_skills
            if skill.lower() not in normalized_current
        ]

        # If no current skills were supplied, recommend all.
        if not current_skills:
            recommended = list(future_skills)

        # ------------------------------------------------------
        # Priority
        # ------------------------------------------------------

        if len(recommended) >= 5:
            priority = "High"

        elif len(recommended) >= 3:
            priority = "Medium"

        else:
            priority = "Low"

        return {
            "career": career_name,
            "current_skills": current_skills,
            "career_skills": career_skills,
            "future_skills": future_skills,
            "existing_future_skills": existing,
            "recommended_future_skills": recommended,
            "priority": priority,
            "recommendation": self._build_recommendation(
                career_name,
                recommended
            )
        }

    # ==========================================================
    # RECOMMENDATION
    # ==========================================================

    @staticmethod
    def _build_recommendation(
        career_name,
        recommended_skills
    ):

        if not recommended_skills:
            return (
                f"Your current skills already cover the "
                f"identified future skills for {career_name}. "
                "Continue strengthening practical experience."
            )

        top_skills = recommended_skills[:3]

        skills_text = ", ".join(top_skills)

        return (
            f"Focus next on {skills_text}. "
            "These skills can strengthen your future readiness "
            "for the selected career."
        )

    # ==========================================================
    # BYTE REPORT
    # ==========================================================

    def format_report(self, report):

        lines = [
            "",
            "🔮 Future Skills Recommendation",
            "",
            f"💻 Career: {report['career']}",
            "",
            "📚 Current Skills:"
        ]

        if report["current_skills"]:

            for skill in report["current_skills"]:
                lines.append(f"• {skill}")

        else:
            lines.append("• No current skills provided.")

        lines.extend([
            "",
            "🚀 Future Skills:",
        ])

        for skill in report["future_skills"]:
            lines.append(f"• {skill}")

        lines.extend([
            "",
            "🎯 Recommended Skills To Develop:"
        ])

        if report["recommended_future_skills"]:

            for skill in report["recommended_future_skills"]:
                lines.append(f"• {skill}")

        else:
            lines.append(
                "• No additional future skills identified."
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
