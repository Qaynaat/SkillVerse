class CareerReadinessScoreEngine:
    """
    Mission 082
    Calculates how ready a learner is for a selected career.

    The engine uses the existing CareerDatabase.
    It does not create or own career data.
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
    # VALUE EXTRACTION
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

    # ==========================================================
    # NORMALIZATION
    # ==========================================================

    @staticmethod
    def _normalize_skills(skills):

        if skills is None:
            return []

        if isinstance(skills, str):
            skills = [skills]

        return [
            str(skill).strip()
            for skill in skills
            if str(skill).strip()
        ]

    # ==========================================================
    # READINESS LEVEL
    # ==========================================================

    @staticmethod
    def _get_readiness_level(score):

        if score >= 80:
            return "Career Ready"

        if score >= 60:
            return "Strong Progress"

        if score >= 40:
            return "Developing"

        if score >= 20:
            return "Early Stage"

        return "Starting Point"

    # ==========================================================
    # PRIORITY
    # ==========================================================

    @staticmethod
    def _get_priority(score):

        if score < 40:
            return "Critical"

        if score < 60:
            return "High"

        if score < 80:
            return "Medium"

        return "Low"

    # ==========================================================
    # RECOMMENDATION
    # ==========================================================

    @staticmethod
    def _build_recommendation(
        level,
        missing_skills
    ):

        if not missing_skills:

            return (
                "The learner has matched all currently listed "
                "career skills. Focus on practical experience "
                "and career preparation."
            )

        if level == "Starting Point":

            return (
                "Begin with the foundational career skills "
                "before moving toward advanced preparation."
            )

        if level == "Early Stage":

            return (
                "Build the missing foundational skills "
                "before increasing career difficulty."
            )

        if level == "Developing":

            return (
                "Strengthen the missing core skills while "
                "continuing practical learning."
            )

        if level == "Strong Progress":

            return (
                "Continue strengthening remaining skills "
                "and begin building practical experience."
            )

        return (
            "Maintain your current skills and focus on "
            "practical experience and career opportunities."
        )

    # ==========================================================
    # ANALYSIS
    # ==========================================================

    def analyze(
        self,
        career_name,
        learner_skills=None
    ):

        career = self._get_career(career_name)

        required_skills = self._normalize_skills(
            self._get_value(
                career,
                "skills",
                "required_skills",
                "core_skills",
                default=[]
            )
        )

        learner_skills = self._normalize_skills(
            learner_skills
        )

        required_normalized = {
            skill.lower(): skill
            for skill in required_skills
        }

        learner_normalized = {
            skill.lower()
            for skill in learner_skills
        }

        matched_skills = [
            required_normalized[key]
            for key in required_normalized
            if key in learner_normalized
        ]

        missing_skills = [
            required_normalized[key]
            for key in required_normalized
            if key not in learner_normalized
        ]

        total_required = len(required_skills)

        if total_required == 0:
            score = 0
        else:
            score = round(
                (len(matched_skills) / total_required) * 100
            )

        level = self._get_readiness_level(score)
        priority = self._get_priority(score)

        recommendation = self._build_recommendation(
            level,
            missing_skills
        )

        return {
            "career": career_name,
            "required_skills": required_skills,
            "learner_skills": learner_skills,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "readiness_score": score,
            "readiness_level": level,
            "priority": priority,
            "recommendation": recommendation,
        }

    # ==========================================================
    # BYTE REPORT
    # ==========================================================

    def format_report(self, report):

        lines = [
            "",
            "🎯 Career Readiness Score",
            "",
            f"💻 Career: {report['career']}",
            "",
            f"📊 Readiness Score: "
            f"{report['readiness_score']}%",
            f"📈 Level: "
            f"{report['readiness_level']}",
            f"🔥 Priority: "
            f"{report['priority']}",
            "",
            "✅ Skills Matched:"
        ]

        if report["matched_skills"]:

            for skill in report["matched_skills"]:
                lines.append(f"• {skill}")

        else:
            lines.append("• No required skills matched yet.")

        lines.extend([
            "",
            "⚠️ Skills To Develop:"
        ])

        if report["missing_skills"]:

            for skill in report["missing_skills"]:
                lines.append(f"• {skill}")

        else:
            lines.append("• No missing skills listed.")

        lines.extend([
            "",
            "💡 Recommendation:",
            report["recommendation"],
            ""
        ])

        return "\n".join(lines)