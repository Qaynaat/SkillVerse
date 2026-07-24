from src.core.career_database import CareerDatabase
from src.core.personality_engine import PersonalityEngine
from src.core.response_generator import ResponseGenerator
from src.core.conversation_engine import ConversationEngine
from src.core.intent import Intent
from src.core.memory import Memory
from src.core.mentor_engine import MentorEngine
from src.core.achievement_engine import AchievementEngine
from src.core.save_system import SaveSystem
from src.core.reward_engine import RewardEngine


class ByteBrain:

    def __init__(
        self,
        career_database: CareerDatabase,
        personality_engine: PersonalityEngine,
        response_generator: ResponseGenerator,
        conversation_engine: ConversationEngine,
        achievement_engine: AchievementEngine,
        reward_engine: RewardEngine,
        mentor_engine: MentorEngine,
        memory: Memory,
        save_system: SaveSystem,
        
    ):
        self.career_database = career_database
        self.response_generator = response_generator
        self.personality_engine = personality_engine
        self.conversation_engine = conversation_engine
        self.achievement_engine = achievement_engine
        self.reward_engine = reward_engine
        self.mentor_engine = mentor_engine
        self.memory = memory
        self.save_system = save_system

        self.save_system.load(self.memory)

    def _reply(self, response: str) -> str:
        """
        Store Byte's response before returning it.
        """
        self.memory.add_message("Byte", response)
        return response

    def introduce_career(self, career_name: str) -> str:
        career = self.career_database.get_career(career_name)
        self.memory.remember_career(career_name)

        self.save_system.save(self.memory)

        return self._reply(
            self.response_generator.generate(career)
        )

    def set_user_name(self, name: str):

        self.memory.set_user_name(name)

        self.save_system.save(self.memory)

        return self._reply(
            f"😊 Nice to meet you, {name}!"
        )


    def set_dream_career(self, career: str):

        self.memory.set_dream_career(career)

        self.save_system.save(self.memory)

        return self._reply(
            f"🎯 Awesome! I'll remember that your dream career is {career}."
        )
    

    def get_first_learning_step(self, career_name: str) -> str:
        career = self.career_database.get_career(career_name)
        step = self.mentor_engine.get_first_step(career)

        return self._reply(
            self.response_generator.generate_learning_mission(step)
        )

    def get_current_learning_step(
        self,
        career_name: str
    ) -> str:
        career = self.career_database.get_career(career_name)

        step = self.mentor_engine.get_step(
            career,
            self.memory.get_current_step()
        )

        if step is None:
            return self._reply(
                "🎉 Congratulations! You've completed this roadmap!"
            )

        return self._reply(
            self.response_generator.generate_learning_mission(step)
        )

    def complete_current_step(self) -> str:
        career_name = self.memory.get_current_career()

        if career_name is None:
            return self._reply("🥳 Progress saved!")

        career = self.career_database.get_career(career_name)

        step = self.mentor_engine.get_step(
            career,
            self.memory.get_current_step()
        )

        reward = step["reward_xp"]

        self.memory.add_xp(reward)
        self.memory.increment_completed_missions()
        self.memory.advance_step()


        new_achievements = self.achievement_engine.check_unlocks(
            self.memory
        )
        self.save_system.save(self.memory)


        new_rewards = self.reward_engine.check_unlocks(
            self.memory
        )
        self.save_system.save(self.memory)


        progress = self.memory.get_progress()
        
        message = self.response_generator.generate_mission_complete(
            reward,
            progress
        )

        for achievement in new_achievements:
            message += "\n\n"
            message += (
                self.response_generator.generate_achievement_unlock(
                    achievement
                )
            )

        for reward in new_rewards:

            message += "\n\n"
            message += (
                self.response_generator.generate_reward_unlock(
                    reward
                )
            )

        if self.memory.has_completed_daily_goal():
            message += "\n\n"
            message += self.response_generator.generate_daily_goal_complete()

        next_step = self.mentor_engine.get_step(
            career,
            self.memory.get_current_step()
        )

        if next_step is None:
            next_mission = (
                "🎉 Congratulations! You've completed this roadmap!"
            )
        else:
            next_mission = (
                self.response_generator.generate_learning_mission(
                    next_step
                )
            )

        return self._reply(
            message + "\n\n" + next_mission
        )

    def respond(self, message: str, career_name: str = None) -> str:
        # Save user's message
        self.memory.add_message("User", message)

        # Detect intent
        intent = self.conversation_engine.detect_intent(message)

        # Remember the current career if provided
        if career_name:
            self.memory.remember_career(career_name)

            self.save_system.save(self.memory)
        else:
            career_name = self.memory.get_current_career()

            

        # Byte doesn't know which career yet
        if career_name is None:
            return self._reply(
                "🤔 I don't know which career you're asking about yet.\n"
                "Please tell me a career first."
            )

        career = self.career_database.get_career(career_name)

        # Generate response based on intent
        if intent == Intent.INTRODUCE_CAREER:
            return self._reply(
                self.response_generator.generate(career)
            )

        elif intent == Intent.ASK_DESCRIPTION:
            return self._reply(
                self.response_generator.generate_description(career)
            )

        elif intent == Intent.ASK_PROGRAMMING_LANGUAGES:
            return self._reply(
                self.response_generator.generate_programming_languages(career)
            )

        elif intent == Intent.ASK_TOOLS:
            return self._reply(
                self.response_generator.generate_tools(career)
            )

        elif intent == Intent.ASK_UNIVERSITY_SUBJECTS:
            return self._reply(
                self.response_generator.generate_university_subjects(career)
            )

        elif intent == Intent.ASK_SKILLS:
            return self._reply(
                self.response_generator.generate_skills(career)
            )

        elif intent == Intent.ASK_CAREER_PATHS:
            return self._reply(
                self.response_generator.generate_career_paths(career)
            )

        elif intent == Intent.ASK_BEGINNER_PROJECTS:
            return self._reply(
                self.response_generator.generate_beginner_projects(career)
            )

        elif intent == Intent.ASK_LEARNING_RESOURCES:
            return self._reply(
                self.response_generator.generate_learning_resources(career)
            )

        elif intent == Intent.ASK_RELATED_CAREERS:
            return self._reply(
                self.response_generator.generate_related_careers(career)
            )

        elif intent == Intent.ASK_SALARY:
            return self._reply(
                self.response_generator.generate_salary(career)
            )

        elif intent == Intent.ASK_PROS:
            return self._reply(
                self.response_generator.generate_pros(career)
            )

        elif intent == Intent.ASK_CHALLENGES:
            return self._reply(
                self.response_generator.generate_challenges(career)
            )

        elif intent == Intent.ASK_REMOTE_WORK:
            return self._reply(
                self.response_generator.generate_remote_work(career)
            )

        elif intent == Intent.ASK_FUTURE_DEMAND:
            return self._reply(
                self.response_generator.generate_future_demand(career)
            )

        return self._reply(
            "🤔 I'm not sure what you mean yet.\n"
            "Could you rephrase your question?"
        )