class CareerConversationEngine:
    """
    Mission 091
    Career Conversations

    Keeps career-related conversations connected to
    the existing CareerDatabase and previous career context.
    """

    def __init__(self, career_database):
        self.career_database = career_database

    # ==========================================================
    # CAREER LOOKUP
    # ==========================================================

    def _get_career(self, career_name):

        if not career_name:
            return None

        database = self.career_database

        if hasattr(database, "get_career"):
            return database.get_career(career_name)

        if hasattr(database, "find_career"):
            return database.find_career(career_name)

        if hasattr(database, "get"):
            return database.get(career_name)

        if isinstance(database, dict):
            return database.get(career_name)

        raise AttributeError(
            "CareerDatabase does not provide a supported lookup method."
        )

    # ==========================================================
    # VALUE HELPERS
    # ==========================================================

    @staticmethod
    def _get_value(career, *keys, default=None):

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
    # CAREER NAME RESOLUTION
    # ==========================================================

    def resolve_career(self, career_name=None, previous_career=None):

        """
        Resolve the career from the current message/context.

        If no career is supplied, the previous career is reused.
        """

        if career_name:
            career = self._get_career(career_name)

            if career is not None:
                return career_name

        if previous_career:
            career = self._get_career(previous_career)

            if career is not None:
                return previous_career

        return None

    # ==========================================================
    # INTENT DETECTION
    # ==========================================================

    @staticmethod
    def detect_intent(message):

        if not message:
            return "UNKNOWN"

        text = message.lower().strip()

        # Skills
        if any(
            word in text
            for word in [
                "skills",
                "skill",
                "what should i learn",
                "what do i need to learn",
                "what do i need"
            ]
        ):
            return "CAREER_SKILLS"

        # Career paths
        if any(
            word in text
            for word in [
                "career path",
                "career paths",
                "roles",
                "jobs",
                "job roles",
                "what can i become"
            ]
        ):
            return "CAREER_PATHS"

        # Description
        if any(
            word in text
            for word in [
                "what is",
                "tell me about",
                "about this career",
                "explain this career",
                "describe"
            ]
        ):
            return "CAREER_OVERVIEW"

        # Future
        if any(
            word in text
            for word in [
                "future",
                "demand",
                "in demand",
                "scope",
                "opportunities"
            ]
        ):
            return "CAREER_FUTURE"

        # Readiness
        if any(
            word in text
            for word in [
                "ready",
                "readiness",
                "am i ready",
                "prepared"
            ]
        ):
            return "CAREER_READINESS"

        # Personal direction
        if any(
            word in text
            for word in [
                "good for me",
                "right for me",
                "suitable for me",
                "should i choose",
                "should i pursue",
                "is this for me"
            ]
        ):
            return "CAREER_DIRECTION"

        return "UNKNOWN"

    # ==========================================================
    # CONVERSATION
    # ==========================================================

    def respond(
        self,
        message,
        career_name=None,
        previous_career=None
    ):

        intent = self.detect_intent(message)

        resolved_career = self.resolve_career(
            career_name=career_name,
            previous_career=previous_career
        )

        if resolved_career is None:

            return {
                "intent": intent,
                "career": None,
                "context_used": False,
                "response": (
                    "I'd be happy to talk about careers with you. "
                    "Which career would you like to explore?"
                )
            }

        career = self._get_career(resolved_career)

        name = self._get_value(
            career,
            "name",
            "career_name",
            default=resolved_career
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

        paths = self._normalize_list(
            self._get_value(
                career,
                "career_paths",
                "paths",
                default=[]
            )
        )

        # ------------------------------------------------------
        # Overview
        # ------------------------------------------------------

        if intent == "CAREER_OVERVIEW":

            response = (
                f"{name} is a career where you can build "
                f"practical skills and grow toward different "
                f"professional roles."
            )

            if description:
                response = description

        # ------------------------------------------------------
        # Skills
        # ------------------------------------------------------

        elif intent == "CAREER_SKILLS":

            if skills:

                skill_text = ", ".join(skills[:5])

                response = (
                    f"For {name}, some important skills include "
                    f"{skill_text}."
                )

                if len(skills) > 5:
                    response += (
                        " There are more skills to develop as "
                        "you progress."
                    )

            else:

                response = (
                    f"The current career database does not yet "
                    f"contain a detailed skill list for {name}."
                )

        # ------------------------------------------------------
        # Career paths
        # ------------------------------------------------------

        elif intent == "CAREER_PATHS":

            if paths:

                path_text = ", ".join(paths[:5])

                response = (
                    f"With {name}, you can explore paths such as "
                    f"{path_text}."
                )

                if len(paths) > 5:
                    response += (
                        " There are additional directions you "
                        "can explore later."
                    )

            else:

                response = (
                    f"The current database does not contain "
                    f"detailed career paths for {name} yet."
                )

        # ------------------------------------------------------
        # Future
        # ------------------------------------------------------

        elif intent == "CAREER_FUTURE":

            response = (
                f"{name} can offer several opportunities for "
                f"professional growth. Your future direction "
                f"will depend on the skills, experience, and "
                f"specialization you develop."
            )

        # ------------------------------------------------------
        # Readiness
        # ------------------------------------------------------

        elif intent == "CAREER_READINESS":

            response = (
                f"We can check your readiness for {name} by "
                f"looking at the skills you already have and "
                f"the skills you still need to develop."
            )

        # ------------------------------------------------------
        # Personal direction
        # ------------------------------------------------------

        elif intent == "CAREER_DIRECTION":

            response = (
                f"{name} could be worth exploring further. "
                f"Instead of deciding immediately, let's look "
                f"at your interests, skills, learning progress, "
                f"and the parts of the career you enjoy."
            )

        # ------------------------------------------------------
        # Unknown career conversation
        # ------------------------------------------------------

        else:

            response = (
                f"I'm here to help you explore {name}. "
                f"We can talk about its skills, career paths, "
                f"future opportunities, or your readiness."
            )

        return {
            "intent": intent,
            "career": name,
            "context_used": previous_career is not None
            and career_name is None,
            "response": response
        }

    # ==========================================================
    # BYTE-FRIENDLY FORMAT
    # ==========================================================

    def format_response(self, result):

        career = result.get("career")
        intent = result.get("intent")
        response = result.get("response")

        lines = [
            "",
            "💬 Career Conversation",
            "",
            f"🎯 Career: {career}" if career else "🎯 Career: Not selected",
            f"🧠 Intent: {intent}",
            "",
            f"💜 Byte: {response}",
            ""
        ]

        if result.get("context_used"):
            lines.insert(
                3,
                "🔗 Previous career context used: Yes"
            )

        return "\n".join(lines)