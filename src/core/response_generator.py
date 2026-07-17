from src.core.personality_engine import PersonalityEngine
from src.data.career_profile import CareerProfile


class ResponseGenerator:

    def __init__(self, personality_engine: PersonalityEngine):
        self.personality_engine = personality_engine

    # --------------------------------------------------
    # Complete Career Introduction
    # --------------------------------------------------

    def generate(self, career: CareerProfile):

        sections = [

            self._generate_greeting(),

            self._generate_intro(career),

            self._generate_career_description(career),

            self._generate_skills(career),

            self._generate_career_paths(career),

            self._generate_future_demand(career),

            self._generate_encouragement(),

            self._generate_closing()

        ]

        return "\n\n".join(sections)

    # --------------------------------------------------
    # Public Response Methods
    # --------------------------------------------------

    def generate_description(self, career: CareerProfile):
        return self._generate_career_description(career)

    def generate_skills(self, career: CareerProfile):
        return self._generate_skills(career)

    def generate_career_paths(self, career: CareerProfile):
        return self._generate_career_paths(career)

    def generate_future_demand(self, career: CareerProfile):
        return self._generate_future_demand(career)

    # --------------------------------------------------
    # Private Helpers
    # --------------------------------------------------

    def _generate_greeting(self):

        profile = self.personality_engine.get_profile()

        if profile.greeting_style == "Personalized & highly welcoming":
            return "👋 Hello! I'm Byte, and I'm excited to explore careers with you today."

        return "👋 Hello!"

    def _generate_intro(self, career):

        return (
            f"📚 Let's explore {career.name} together."
        )

    def _generate_career_description(self, career: CareerProfile):
        return career.description

    def _generate_skills(self, career: CareerProfile):

        skill_list = ", ".join(career.skills)

        return (
            f"Key skills you'll develop include: "
            f"{skill_list}."
        )

    def _generate_career_paths(self, career: CareerProfile):

        paths = ", ".join(career.career_paths)

        return (
            f"Possible career paths include: "
            f"{paths}."
        )

    def _generate_future_demand(self, career: CareerProfile):

        return (
            f"📈 Future Demand: {career.future_demand}"
        )

    def _generate_encouragement(self):

        profile = self.personality_engine.get_profile()

        return (
            f"💜 {profile.support_style}\n"
            "Remember, every expert was once a beginner."
        )

    def _generate_closing(self):

        profile = self.personality_engine.get_profile()

        return (
            f"🚀 {profile.closing_style}"
        )
    
    def generate_first_learning_step(self, first_step: str):

        return (
            "🚀 Today's Mission\n\n"
            f"Start with **{first_step}**.\n\n"
            "Master this topic first before moving to the next step "
            "in your learning journey. 💜"
        )
    def generate_learning_mission(self, step):

        return (
            "🚀 Today's Mission\n\n"
            f"📘 Learn: {step['title']}\n\n"
            f"💡 Why?\n{step['why']}\n\n"
            f"🎯 Goal:\n{step['goal']}\n\n"
            "One small step today is better than waiting for the perfect time. 💜"
        )
    def generate_programming_languages(self, career):

        languages = "\n• ".join(career.programming_languages)

        return (
            "💻 Programming Languages\n\n"
            f"• {languages}\n\n"
            "🚀 Start with one language, master it, "
            "then gradually learn the others."
        )
    def generate_tools(self, career):

        tools = "\n• ".join(career.tools)

        return (
            "🛠️ Tools You'll Use\n\n"
            f"• {tools}\n\n"
            "💡 Master these tools gradually. "
            "They'll make you a more productive developer."
        )
    def generate_university_subjects(self, career):

        subjects = "\n".join(
            f"• {subject}"
            for subject in career.university_subjects
        )

        return (
            "📚 University Subjects\n\n"
            f"{subjects}\n\n"
            "🎓 These subjects build the foundation you'll need to become a successful professional."
        )