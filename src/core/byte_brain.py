from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.save_system import SaveSystem
from src.core.intent import Intent

class ByteBrain:

    def __init__(
        self,
        services: BrainServices,
        memory: Memory,
        save_system: SaveSystem,
    ):
        self.career_database = services.career_database
        self.career_responses = services.career_response_generator
        self.conversation_engine = services.conversation_engine
        self.achievement_engine = services.achievement_engine
        self.reward_engine = services.reward_engine
        self.mentor_engine = services.mentor_engine
        self.reflection_engine = services.reflection_engine
        self.learning_analyzer = services.learning_analyzer
        self.adaptive_mentor = services.adaptive_mentor
        self.learning_insights = services.learning_insights
        self.progress_dashboard = services.progress_dashboard
        self.study_planner = services.study_planner
        self.daily_goal_engine = services.daily_goal_engine
        self.smart_reminder_engine = services.smart_reminder_engine
        self.motivation_engine = services.motivation_engine
        self.encouragement_engine = services.encouragement_engine
        self.celebration_engine = services.celebration_engine
        self.quote_engine = services.quote_engine
        self.learning_tip_engine = services.learning_tip_engine
        self.success_prediction_engine = services.success_prediction_engine
        self.memory = memory
        self.save_system = save_system       

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


    def get_learning_insights(self):
        report = self.learning_insights.generate(
            self.memory
        )
        response = (
            "📊 Your Learning Insights\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions: {report['missions']}\n"
            f"📖 Current Step: {report['current_step']}\n"
            f"🎓 Level: {report['level']}\n\n"
            f"{report['advice']}"
        )
        return self._reply(response)

    def get_progress_dashboard(self):
        report = self.progress_dashboard.generate(
            self.memory
        )
        response = (
            "📊 SkillVerse Progress Dashboard\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"🎓 Level: {report['level']}\n"
            f"✅ Missions: {report['missions']}\n"
            f"📖 Current Step: {report['current_step']}\n"
            f"🏆 Achievements: {report['achievements']}\n"
            f"🎁 Rewards: {report['rewards']}"
        )
        return self._reply(response)


    def get_study_plan(self):
        plan = self.study_planner.generate_plan(
            self.memory
        )
        response = (
            "📅 Today's Study Plan\n\n"
            f"⭐ XP: {plan['xp']}\n"
            f"📖 Current Step: {plan['current_step']}\n\n"
            "📋 Tasks:\n"
        )
        for task in plan["tasks"]:
            response += f"• {task}\n"
        return self._reply(response)

    def get_daily_goals(self):
        report = self.daily_goal_engine.generate_goals(
            self.memory
        )
        response = (
            "🎯 Today's Goals\n\n"
            f"⭐ XP: {report['xp']}\n\n"
        )
        for goal in report["goals"]:
            response += f"• {goal}\n"
        return self._reply(response)

    def get_smart_reminder(self):
        report = self.smart_reminder_engine.generate_reminder(
            self.memory
        )
        response = (
            "⏰ Smart Reminder\n\n"
            f"⭐ XP: {report['xp']}\n\n"
            f"{report['reminder']}"
        )
        return self._reply(response)

    def get_motivation(self):
        report = self.motivation_engine.generate_message(
            self.memory
        )
        response = (
            "💜 Motivation\n\n"
            f"⭐ XP: {report['xp']}\n\n"
            f"{report['message']}"
        )
        return self._reply(response)

    def get_encouragement(self):
        report = self.encouragement_engine.generate_encouragement(
            self.memory
        )
        response = (
            "🌟 Encouragement\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions: {report['missions']}\n\n"
            f"{report['message']}"
        )
        return self._reply(response)


    def get_celebration(self):
        report = self.celebration_engine.celebrate(
            self.memory
        )
        response = (
            "🎉 Celebration\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions: {report['missions']}\n\n"
            f"{report['message']}"
        )
        return self._reply(response)

    def get_daily_quote(self):
        report = self.quote_engine.get_quote(
            self.memory
        )
        response = (
            "💬 Today's Quote\n\n"
            f"{report['quote']}"
        )
        return self._reply(response)


    def get_learning_tip(self):
        report = self.learning_tip_engine.get_tip(
            self.memory
        )
        response = (
            "💡 Today's Learning Tip\n\n"
            f"{report['tip']}"
        )
        return self._reply(response)

    def get_success_prediction(self):
        report = self.success_prediction_engine.predict(
            self.memory
        )
        response = (
            "🔮 Success Prediction\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions: {report['missions']}\n"
            f"📈 Prediction: {report['prediction']}"
        )
        return self._reply(response)