from src.core.achievement_engine import AchievementEngine
from src.core.career_database import CareerDatabase
from src.core.career_response_generator import CareerResponseGenerator
from src.core.conversation_engine import ConversationEngine
from src.core.intent import Intent
from src.core.memory import Memory
from src.core.mentor_engine import MentorEngine
from src.core.reward_engine import RewardEngine
from src.core.save_system import SaveSystem
from src.core.learning_analyzer import LearningAnalyzer
from src.core.adaptive_mentor import AdaptiveMentor
from src.core.reflection_engine import ReflectionEngine

class ByteBrain:

    def __init__(
        self,
        career_database: CareerDatabase,
        career_response_generator: CareerResponseGenerator,
        conversation_engine: ConversationEngine,
        achievement_engine: AchievementEngine,
        reward_engine: RewardEngine,
        mentor_engine: MentorEngine,
        reflection_engine: ReflectionEngine,
        memory: Memory,
        save_system: SaveSystem,
        learning_analyzer: LearningAnalyzer,
        adaptive_mentor: AdaptiveMentor,
        
    ):
        self.career_database = career_database
        self.career_responses = career_response_generator
        self.conversation_engine = conversation_engine
        self.achievement_engine = achievement_engine
        self.reward_engine = reward_engine
        self.mentor_engine = mentor_engine
        self.reflection_engine = reflection_engine
        self.memory = memory
        self.save_system = save_system
        self.learning_analyzer = learning_analyzer
        self.adaptive_mentor = adaptive_mentor
        

        # Dispatch table for career information requests
        self.career_handlers = {
            Intent.INTRODUCE_CAREER: self.career_responses.generate_complete_career,
            Intent.ASK_DESCRIPTION: self.career_responses.generate_description,
            Intent.ASK_SKILLS: self.career_responses.generate_skills,
            Intent.ASK_CAREER_PATHS: self.career_responses.generate_career_paths,
            Intent.ASK_PROGRAMMING_LANGUAGES: self.career_responses.generate_programming_languages,
            Intent.ASK_TOOLS: self.career_responses.generate_tools,
            Intent.ASK_UNIVERSITY_SUBJECTS: self.career_responses.generate_university_subjects,
            Intent.ASK_BEGINNER_PROJECTS: self.career_responses.generate_beginner_projects,
            Intent.ASK_LEARNING_RESOURCES: self.career_responses.generate_learning_resources,
            Intent.ASK_RELATED_CAREERS: self.career_responses.generate_related_careers,
            Intent.ASK_SALARY: self.career_responses.generate_salary,
            Intent.ASK_PROS: self.career_responses.generate_pros,
            Intent.ASK_CHALLENGES: self.career_responses.generate_challenges,
            Intent.ASK_REMOTE_WORK: self.career_responses.generate_remote_work,
            Intent.ASK_FUTURE_DEMAND: self.career_responses.generate_future_demand,
        }

        # Load existing save state into memory
        self.save_system.load(self.memory)

    def _get_career(self, career_name: str):
        return self.career_database.get_career(career_name)

    def _reply(self, response: str) -> str:
        """Store Byte's response in memory before returning it."""
        self.memory.add_message("Byte", response)
        return response

    def introduce_career(self, career_name: str) -> str:
        career = self._get_career(career_name)
        self.memory.remember_career(career_name)
        self.save_system.save(self.memory)

        return self._reply(self.career_responses.generate_complete_career(career))

    def set_user_name(self, name: str) -> str:
        self.memory.set_user_name(name)
        self.save_system.save(self.memory)
        return self._reply(f"😊 Nice to meet you, {name}!")

    def set_dream_career(self, career: str) -> str:
        self.memory.set_dream_career(career)
        self.save_system.save(self.memory)
        return self._reply(
            f"🎯 Awesome! I'll remember that your dream career is {career}."
        )

    def get_first_learning_step(self, career_name: str) -> str:
        career = self._get_career(career_name)
        step = self.mentor_engine.get_first_step(career)

        return self._reply(self.career_responses.generate_learning_mission(step))

    def get_current_learning_step(self, career_name: str) -> str:
        career = self._get_career(career_name)
        step = self.mentor_engine.get_step(
            career, self.memory.get_current_step()
        )

        if step is None:
            return self._reply(
                "🎉 Congratulations! You've completed this roadmap!"
            )

        return self._reply(self.career_responses.generate_learning_mission(step))

    def complete_current_step(self) -> str:
        career_name = self.memory.get_current_career()

        if career_name is None:
            return self._reply("🥳 Progress saved!")

        career = self._get_career(career_name)

        step = self.mentor_engine.get_step(
            career, self.memory.get_current_step()
        )

        reward = step["reward_xp"]

        self.memory.add_xp(reward)
        self.memory.increment_completed_missions()
        self.memory.advance_step()

        new_achievements = self.achievement_engine.check_unlocks(self.memory)
        new_rewards = self.reward_engine.check_unlocks(self.memory)

        self.save_system.save(self.memory)

        progress = self.memory.get_progress()

        response = self.career_responses.generate_mission_complete(
            reward, progress
        )

        for achievement in new_achievements:
            response += "\n\n"
            response += self.career_responses.generate_achievement_unlock(
                achievement
            )

        for reward in new_rewards:
            response += "\n\n"
            response += self.career_responses.generate_reward_unlock(reward)

        if self.memory.has_completed_daily_goal():
            response += "\n\n"
            response += self.career_responses.generate_daily_goal_complete()

        next_step = self.mentor_engine.get_step(
            career, self.memory.get_current_step()
        )

        if next_step is None:
            next_mission = "🎉 Congratulations! You've completed this roadmap!"
        else:
            next_mission = self.career_responses.generate_learning_mission(
                next_step
            )

        return self._reply(response + "\n\n" + next_mission)

    def respond(self, message: str, career_name: str = None) -> str:
        # Save user's message
        self.memory.add_message("User", message)

        # Detect intent
        intent = self.conversation_engine.detect_intent(message)

        # Remember current career
        if career_name:
            self.memory.remember_career(career_name)
            self.save_system.save(self.memory)
        else:
            career_name = self.memory.get_current_career()

        # No career selected
        if career_name is None:
            return self._reply(
                "🤔 I don't know which career you're asking about yet.\n"
                "Please tell me a career first."
            )

        career = self._get_career(career_name)
        handler = self.career_handlers.get(intent)

        if handler is not None:
            return self._reply(handler(career))

        return self._reply(
            "🤔 I'm not sure what you mean yet.\n"
            "Could you rephrase your question?"
        )


    def generate_learning_summary(self) -> str:

        report = self.learning_analyzer.analyze(
            self.memory
        )

        summary = self.learning_analyzer.generate_summary(
            report
        )

        return self._reply(summary)


    def get_personalized_recommendation(self, profile) -> str:

        report = self.learning_analyzer.analyze(
            self.memory
        )

        recommendation = self.adaptive_mentor.recommend(
            profile,
            report
        )

        return self._reply(recommendation)

    def get_learning_reflection(self) -> str:
        reflection = self.reflection_engine.generate_summary(
            self.memory
        )

        return self._reply(reflection)