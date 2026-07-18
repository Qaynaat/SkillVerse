from src.core.career_database import CareerDatabase
from src.core.personality_engine import PersonalityEngine
from src.core.response_generator import ResponseGenerator
from src.core.conversation_engine import ConversationEngine
from src.core.intent import Intent
from src.core.memory import Memory
from src.core.mentor_engine import MentorEngine


class ByteBrain:

    def __init__(
        self,
        career_database: CareerDatabase,
        personality_engine: PersonalityEngine,
        response_generator: ResponseGenerator,
        conversation_engine: ConversationEngine,
        mentor_engine: MentorEngine,
        memory: Memory
    ):
        self.career_database = career_database
        self.personality_engine = personality_engine
        self.response_generator = response_generator
        self.conversation_engine = conversation_engine
        self.mentor_engine = mentor_engine
        self.memory = memory

    def _reply(self, response: str):
        """
        Store Byte's response before returning it.
        """
        self.memory.add_message("Byte", response)
        return response

    def introduce_career(self, career_name: str):

        career = self.career_database.get_career(career_name)

        self.memory.remember_career(career_name)

        return self._reply(
            self.response_generator.generate(career)
        )
    def get_first_learning_step(self, career_name: str):

        career = self.career_database.get_career(career_name)

        step = self.mentor_engine.get_first_step(career)

        return self._reply(
            self.response_generator.generate_learning_mission(step)
        )
    def get_current_learning_step(self, career_name):

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
    def complete_current_step(self):

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

        self.memory.advance_step()

        total_xp = self.memory.get_total_xp()

        message = self.response_generator.generate_mission_complete(
            reward,
            total_xp
        )

        next_mission = self.get_current_learning_step(career_name)

        return self._reply(
            message + "\n\n" + next_mission
        )

    def respond(self, message: str, career_name: str = None):

        # Save user's message
        self.memory.add_message("User", message)

        # Detect intent
        intent = self.conversation_engine.detect_intent(message)

        # Remember the current career if provided
        if career_name:
            self.memory.remember_career(career_name)
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