from typing import Dict, Any
from src.core.personality_engine import PersonalityEngine
from src.data.career_profile import CareerProfile


class ResponseGenerator:

    def __init__(self, personality_engine: PersonalityEngine):
        self.personality_engine = personality_engine

    # --------------------------------------------------
    # Complete Career Introduction
    # --------------------------------------------------

    def generate(self, career: CareerProfile) :
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
    # Career Details Public Methods
    # --------------------------------------------------

    def generate_description(self, career: CareerProfile) -> str:
        return self._generate_career_description(career)

    def generate_skills(self, career: CareerProfile) -> str:
        return self._generate_skills(career)

    def generate_career_paths(self, career: CareerProfile) -> str:
        return self._generate_career_paths(career)

    def generate_future_demand(self, career: CareerProfile) -> str:
        return self._generate_future_demand(career)

    def generate_programming_languages(self, career: CareerProfile) -> str:
        languages = "\n• ".join(career.programming_languages)
        return (
            "💻 Programming Languages\n\n"
            f"• {languages}\n\n"
            "🚀 Start with one language, master it, "
            "then gradually learn the others."
        )

    def generate_tools(self, career: CareerProfile) -> str:
        tools = "\n• ".join(career.tools)
        return (
            "🛠️ Tools You'll Use\n\n"
            f"• {tools}\n\n"
            "💡 Master these tools gradually. "
            "They'll make you a more productive developer."
        )

    def generate_university_subjects(self, career: CareerProfile) -> str:
        subjects = "\n".join(
            f"• {subject}"
            for subject in career.university_subjects
        )
        return (
            "📚 University Subjects\n\n"
            f"{subjects}\n\n"
            "🎓 These subjects build the foundation you'll need to become a successful professional."
        )

    def generate_beginner_projects(self, career: CareerProfile) -> str:
        projects = "\n".join(
            f"• {project}"
            for project in career.beginner_projects
        )
        return (
            "🛠 Beginner Projects\n\n"
            f"{projects}\n\n"
            "🚀 Build projects one by one. Every project strengthens your skills and portfolio."
        )

    def generate_learning_resources(self, career: CareerProfile) -> str:
        resources = "\n".join(
            f"• {resource}"
            for resource in career.learning_resources
        )
        return (
            "📚 Learning Resources\n\n"
            f"{resources}\n\n"
            "💡 Great developers never stop learning. Pick one resource and stay consistent."
        )

    def generate_related_careers(self, career: CareerProfile) -> str:
        careers = "\n".join(
            f"• {item}"
            for item in career.related_careers
        )
        return (
            "🔀 Related Careers\n\n"
            f"{careers}\n\n"
            "💡 These careers share similar skills and interests. Feel free to explore them too!"
        )

    def generate_salary(self, career: CareerProfile) -> str:
        return (
            "💰 Salary\n\n"
            f"{career.salary}\n\n"
            "💡 Salary depends on your skills, experience, country, and the company you work for."
        )

    def generate_pros(self, career: CareerProfile) -> str:
        pros = "\n".join(
            f"• {pro}"
            for pro in career.pros
        )
        return (
            "✅ Advantages\n\n"
            f"{pros}\n\n"
            "💜 Every career has strengths. Choose one that matches your goals and interests."
        )

    def generate_challenges(self, career: CareerProfile) -> str:
        challenges = "\n".join(
            f"• {challenge}"
            for challenge in career.challenges
        )
        return (
            "⚠️ Challenges\n\n"
            f"{challenges}\n\n"
            "💪 Every career has challenges. The key is deciding which ones you're willing to overcome."
        )

    def generate_remote_work(self, career: CareerProfile) -> str:
        if career.remote_work:
            status = "✅ Yes! This career offers excellent remote work opportunities."
        else:
            status = "❌ Remote work opportunities are limited in this career."

        return (
            "🏠 Remote Work\n\n"
            f"{status}\n\n"
            "🌍 The availability of remote work also depends on the company, your experience, and the type of role."
        )

    # --------------------------------------------------
    # Learning Missions & Gamification Methods
    # --------------------------------------------------

    def generate_first_learning_step(self, first_step: str) -> str:
        return (
            "🚀 Today's Mission\n\n"
            f"Start with **{first_step}**.\n\n"
            "Master this topic first before moving to the next step "
            "in your learning journey. 💜"
        )

    def generate_learning_mission(self, step: Dict[str, Any]) -> str:
        return (
            "🚀 Today's Mission\n\n"
            f"📘 Learn:\n{step['title']}\n\n"
            f"⏱ Estimated Time:\n{step['estimated_time']} minutes\n\n"
            f"📈 Difficulty:\n{step['difficulty']}\n\n"
            f"⭐ Reward:\n{step['reward_xp']} XP\n\n"
            f"💡 Why?\n{step['why']}\n\n"
            f"🎯 Goal:\n{step['goal']}\n\n"
            f"💜 Tip:\n{step['tip']}"
        )

    def generate_mission_complete(self, reward: int, progress: Dict[str, int]) -> str:
        current = progress["current"]
        goal = progress["goal"]
        progress_bar = self._generate_progress_bar(current, goal)

        return (
            "🎉 Mission Complete!\n\n"
            f"⭐ Reward Earned:\n+{reward} XP\n\n"
            f"🏆 Total XP:\n{current} XP\n\n"
            f"📊 Daily Progress:\n{progress_bar}"
        )

    def generate_achievement_unlock(self, achievement: Dict[str, Any]) -> str:
        reward = achievement["reward"]

        return (
            "🎉 Achievement Unlocked!\n\n"
            f"{achievement['icon']} {achievement['title']}\n\n"
            f"{achievement['description']}\n\n"
            "⭐ Reward:\n"
            f"+{reward.get('xp', 0)} XP"
        )

    def generate_reward_unlock(self, reward):

        return (
            "🎁 Reward Unlocked!\n\n"
            f"🏆 {reward['title']}\n\n"
            f"{reward['description']}\n\n"
            "🎉 Keep learning to unlock even more rewards!"
        )

    def generate_daily_goal_complete(self) -> str:
        return (
            "🏆 Daily Goal Completed!\n\n"
            "🎉 Amazing work!\n\n"
            "You reached today's XP goal!\n\n"
            "Keep up the great work! 🚀💜"
        )

    # --------------------------------------------------
    # Private Helpers
    # --------------------------------------------------

    def _generate_greeting(self) -> str:
        profile = self.personality_engine.get_profile()

        if profile.greeting_style == "Personalized & highly welcoming":
            return "👋 Hello! I'm Byte, and I'm excited to explore careers with you today."

        return "👋 Hello!"

    def _generate_intro(self, career: CareerProfile) -> str:
        return f"📚 Let's explore {career.name} together."

    def _generate_career_description(self, career: CareerProfile) -> str:
        return career.description

    def _generate_skills(self, career: CareerProfile) -> str:
        skill_list = ", ".join(career.skills)
        return (
            f"Key skills you'll develop include: "
            f"{skill_list}."
        )

    def _generate_career_paths(self, career: CareerProfile) -> str:
        paths = ", ".join(career.career_paths)
        return (
            f"Possible career paths include: "
            f"{paths}."
        )

    def _generate_future_demand(self, career: CareerProfile) -> str:
        return f"📈 Future Demand: {career.future_demand}"

    def _generate_progress_bar(self, current: int, goal: int) -> str:
        filled = min(int((current / goal) * 10), 10)
        empty = 10 - filled
        bar = "█" * filled + "□" * empty

        return (
            f"{bar}\n"
            f"{current}/{goal} XP"
        )

    def _generate_encouragement(self) -> str:
        profile = self.personality_engine.get_profile()
        return (
            f"💜 {profile.support_style}\n"
            "Remember, every expert was once a beginner."
        )

    def _generate_closing(self) -> str:
        profile = self.personality_engine.get_profile()
        return f"🚀 {profile.closing_style}"