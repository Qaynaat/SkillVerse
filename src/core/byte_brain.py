from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.save_system import SaveSystem
from src.core.intent import Intent
from src.core.services.learning_service import LearningService
from src.core.services.progress_service import ProgressService
from src.core.services.profile_service import ProfileService

from src.core.services.learning_engine_service import LearningEngineService
from src.core.services.dashboard_service import DashboardService
from src.core.services.motivation_service import MotivationService
from src.core.services.reflection_service import ReflectionService

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
        self.consistency_analyzer = services.consistency_analyzer
        self.memory = memory
        self.save_system = save_system  
        self.learning_service = LearningService(memory)
        self.progress_service = ProgressService(memory)
        self.profile_service = ProfileService(memory)
        self.habit_analyzer = services.habit_analyzer
        self.weakness_detector = services.weakness_detector
        self.strength_detector = services.strength_detector
        self.learning_style_detector = services.learning_style_detector
        self.burnout_detector = services.burnout_detector
        self.confidence_estimator = services.confidence_estimator
        self.productivity_analyzer = services.productivity_analyzer
        self.smart_goal_generator = services.smart_goal_generator
        self.personalized_roadmap_engine = services.personalized_roadmap_engine
        self.adaptive_difficulty = services.adaptive_difficulty
        self.mission_recommendation = services.mission_recommendation
        self.smart_revision_planner = services.smart_revision_planner
        self.next_best_action_engine = services.next_best_action_engine
        self.learning_velocity_tracker = services.learning_velocity_tracker
        self.performance_trend_analyzer = services.performance_trend_analyzer
        self.learning_risk_predictor = services.learning_risk_predictor
        self.learning_recovery_strategist = services.learning_recovery_strategist
        self.learning_intervention_engine = services.learning_intervention_engine
        self.intervention_prioritizer = services.intervention_prioritizer
        self.learning_decision_engine = services.learning_decision_engine
        self.learning_state_engine = services.learning_state_engine
        self.learner_profile_snapshot = services.learner_profile_snapshot
        self.learning_profile_interpreter = services.learning_profile_interpreter
        self.learning_profile_advisor = services.learning_profile_advisor
        self.learning_profile_action_planner = services.learning_profile_action_planner


        self.learning_engine_service = LearningEngineService(services)
        self.dashboard_service = DashboardService(services)
        self.motivation_service = MotivationService(services)
        self.reflection_service = ReflectionService(services)

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
        self.learning_service.remember_career(career_name)
        self.save_system.save(self.memory)
        return self._reply(self.career_responses.generate_complete_career(career))

    def set_user_name(self, name: str) -> str:
        self.profile_service.set_user_name(name)
        self.save_system.save(self.memory)
        return self._reply(f"😊 Nice to meet you, {name}!")

    def set_dream_career(self, career: str) -> str:
        self.profile_service.set_dream_career(career)
        self.save_system.save(self.memory)
        return self._reply(
            f"🎯 Awesome! I'll remember that your dream career is {career}."
        )

    def get_first_learning_step(self, career_name: str) -> str:
        career = self._get_career(career_name)
        step = self.learning_engine_service.get_first_step(career)
        return self._reply(self.career_responses.generate_learning_mission(step))

    def get_current_learning_step(self, career_name: str) -> str:
        career = self._get_career(career_name)
        step = self.learning_engine_service.get_step(
            career,
            self.memory.get_current_step()
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
        step = self.learning_engine_service.get_step(
            career,
            self.memory.get_current_step()
        )
        reward = step["reward_xp"]

        self.learning_service.add_xp(reward)
        self.progress_service.increment_completed_missions()
        self.learning_service.advance_step()

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

        next_step = self.learning_engine_service.get_step(
            career,
            self.memory.get_current_step()
        )
        if next_step is None:
            next_mission = "🎉 Congratulations! You've completed this roadmap!"
        else:
            next_mission = self.career_responses.generate_learning_mission(
                next_step
            )

        return self._reply(response + "\n\n" + next_mission)

    def get_consistency_analysis(self) -> str:
        report = self.consistency_analyzer.analyze(self.memory)
        response = (
            "📈 Your Learning Consistency Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"📅 Streak Days Recorded: {report['streak_days_recorded']}\n"
            f"📈 Consistency Status: {report['consistency_status']}\n\n"
            f"💡 {report['advice']}"
        )
        return self._reply(response)

    def get_weakness_analysis(self) -> str:
        report = self.weakness_detector.analyze(self.memory)
        weaknesses = report["weaknesses"]

        if weaknesses:
            weakness_text = "\n".join(
                f"• {weakness}" for weakness in weaknesses
            )
        else:
            weakness_text = "• No major weaknesses detected."

        response = (
            "⚠️ Your Learning Weakness Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries_completed']}\n\n"
            f"⚠️ Weaknesses:\n{weakness_text}\n\n"
            f"📈 Weakness Status: {report['weakness_status']}\n\n"
            f"💡 {report['advice']}"
        )
        return self._reply(response)

    def get_strength_analysis(self) -> str:
        report = self.strength_detector.analyze(self.memory)
        response = (
            "💪 Your Learning Strength Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries_completed']}\n\n"
            "💪 Strengths:\n"
        )
        for strength in report["strengths"]:
            response += f"• {strength}\n"
        response += (
            f"\n📈 Strength Status: {report['strength_status']}\n\n"
            f"💡 {report['advice']}"
        )
        return self._reply(response)

    def get_learning_style_analysis(self) -> str:
        report = self.learning_style_detector.analyze(self.memory)
        response = (
            "🧠 Your Learning Style Analysis\n\n"
            f"📚 Learning Style: {report['learning_style']}\n"
            f"📖 Reading Score: {report['reading_score']}\n"
            f"💻 Practice Score: {report['practice_score']}\n"
            f"🎯 Goal Score: {report['goal_score']}\n"
            f"🔎 Exploration Score: {report['exploration_score']}\n"
            f"💬 Interactive Score: {report['interactive_score']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)
    
    def get_burnout_analysis(self) -> str:
        report = self.burnout_detector.analyze(self.memory)
        response = (
            "🔥 Your Learning Burnout Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            "⚠️ Burnout Signals:\n"
            + "\n".join(
                f"• {signal}"
                for signal in report["burnout_signals"]
            )
            + "\n\n"
            f"📈 Burnout Status: {report['burnout_status']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)

    def get_confidence_analysis(self) -> str:
        report = self.confidence_estimator.analyze(self.memory)
        response = (
            "🎯 Your Learning Confidence Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n"
            f"🔎 Categories Explored: {report['categories_explored']}\n\n"
            f"⭐ Confidence Score: {report['confidence_score']}\n"
            f"📈 Confidence Level: {report['confidence_level']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)
    
    def get_productivity_analysis(self) -> str:
        report = self.productivity_analyzer.analyze(self.memory)
        response = (
            "⚡ Your Learning Productivity Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            f"⚡ Productivity Score: {report['productivity_score']}\n"
            f"📈 Productivity Status: {report['productivity_status']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)

    def get_smart_goal(self) -> str:
        report = self.smart_goal_generator.generate(self.memory)
        response = (
            "🎯 Your Smart Learning Goal\n\n"
            f"🎯 Goal: {report['goal']}\n"
            f"📈 Priority: {report['priority']}\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            f"💡 {report['reason']}"
        )
        return self._reply(response)

    def get_personalized_roadmap(self) -> str:
        report = self.personalized_roadmap_engine.generate(self.memory)
        roadmap_steps = "\n".join(
            f"{index}. {step}"
            for index, step in enumerate(report["roadmap"], start=1)
        )
        response = (
            "🧭 Your Personalized Learning Roadmap\n\n"
            f"📍 Current Stage: {report['current_stage']}\n\n"
            f"🎯 Main Goal:\n"
            f"{report['main_goal']}\n\n"
            f"🛣 Roadmap:\n"
            f"{roadmap_steps}\n\n"
            f"📈 Priority: {report['priority']}\n\n"
            f"💡 {report['reason']}"
        )
        return self._reply(response)

    def get_adaptive_difficulty(self) -> str:
        report = self.adaptive_difficulty.analyze(self.memory)
        response = (
            "⚙️ Your Adaptive Difficulty Analysis\n\n"
            f"🎚 Difficulty: {report['difficulty']}\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            f"📊 Positive Signals: {report['positive_signals']}\n"
            f"⚠️ Difficulty Signals: {report['difficulty_signals']}\n\n"
            f"💡 {report['reason']}"
        )
        return self._reply(response)

    def get_mission_recommendation(self) -> str:
        report = self.mission_recommendation.analyze(self.memory)
        response = (
            "🎯 Your Mission Recommendation\n\n"
            f"🎯 Recommendation: {report['recommendation']}\n"
            f"📈 Priority: {report['priority']}\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            f"💡 {report['reason']}"
        )
        return self._reply(response)

    def get_smart_revision_plan(self) -> str:
        report = self.smart_revision_planner.analyze(self.memory)
        revision_plan = "\n".join(
            f"{index}. {plan}"
            for index, plan in enumerate(
                report["revision_plan"],
                start=1
            )
        )
        response = (
            "🧠 Your Smart Revision Plan\n\n"
            f"🎯 Revision Focus: {report['revision_focus']}\n"
            f"📈 Priority: {report['priority']}\n\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            f"📝 Revision Plan:\n"
            f"{revision_plan}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)

    def get_next_best_action_analysis(self) -> str:
        report = self.next_best_action_engine.analyze(self.memory)
        response = (
            "🎯 Your Next Best Learning Action\n\n"
            f"🎯 Next Action: {report['next_action']}\n"
            f"📈 Priority: {report['priority']}\n\n"
            f"🔥 Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"🔁 Retries: {report['retries']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"📖 Modules Read: {report['modules_read']}\n\n"
            f"💡 {report['reason']}"
        )
        return self._reply(response)

    def get_learning_velocity_analysis(self) -> str:
        report = self.learning_velocity_tracker.analyze(self.memory)
        response = (
            "📈 Your Learning Velocity Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            f"📊 Velocity Score: {report['velocity_score']}\n"
            f"📈 Velocity Status: {report['velocity_status']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)

    def get_performance_trend_analysis(self) -> str:
        report = self.performance_trend_analyzer.analyze(self.memory)
        response = (
            "📊 Your Performance Trend Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            f"📈 Positive Signals: {report['positive_signals']}\n"
            f"⚠️ Difficulty Signals: {report['difficulty_signals']}\n"
            f"📊 Performance Score: {report['performance_score']}\n"
            f"📈 Trend Status: {report['trend_status']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)

    def get_learning_risk_analysis(self) -> str:
        report = self.learning_risk_predictor.analyze(self.memory)
        response = (
            "🚨 Your Learning Risk Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            "⚠️ Risk Signals:\n"
            + "\n".join(
                f"• {signal}"
                for signal in report["risk_signals"]
            )
            + "\n\n"
            f"🟢 Positive Signals: {report['positive_signals']}\n"
            f"📊 Risk Score: {report['risk_score']}\n"
            f"📈 Risk Status: {report['risk_status']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)
    
    def get_learning_recovery_analysis(self) -> str:
        report = self.learning_recovery_strategist.analyze(self.memory)
        recovery_plan = "\n".join(
            f"{index}. {step}"
            for index, step in enumerate(
                report["recovery_plan"],
                start=1,
            )
        )
        response = (
            "🛟 Your Learning Recovery Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            "⚠️ Recovery Signals:\n"
            + "\n".join(
                f"• {signal}"
                for signal in report["recovery_signals"]
            )
            + "\n\n"
            f"📊 Recovery Score: {report['recovery_score']}\n"
            f"📈 Recovery Level: {report['recovery_level']}\n\n"
            "🛟 Recovery Plan:\n"
            f"{recovery_plan}\n\n"
            "🎯 Primary Strategy:\n"
            f"{report['primary_strategy']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)

    def get_learning_intervention_analysis(self) -> str:
        report = self.learning_intervention_engine.analyze(
            self.memory
        )
        signals = "\n".join(
            f"• {signal}"
            for signal in report["signals"]
        )
        response = (
            "🎯 Your Learning Intervention Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            "⚠️ Intervention Signals:\n"
            f"{signals}\n\n"
            f"🛠 Intervention: {report['intervention_type']}\n"
            f"📈 Priority: {report['priority']}\n\n"
            "🔎 Reason:\n"
            f"{report['reason']}\n\n"
            "🎯 Action:\n"
            f"{report['action']}\n\n"
            "🌱 Expected Outcome:\n"
            f"{report['expected_outcome']}"
        )
        return self._reply(response)

    def get_intervention_priority_analysis(self) -> str:
        report = self.intervention_prioritizer.analyze(
            self.memory
        )
        priority_lines = "\n".join(
            f"{index}. "
            f"{item['type']} "
            f"({item['priority']})"
            for index, item in enumerate(
                report["interventions"],
                start=1,
            )
        )
        primary = report["primary_intervention"]
        response = (
            "🎯 Your Intervention Priority Analysis\n\n"
            f"🔥 Learning Streak: "
            f"{report['learning_streak']}\n"
            f"🎯 Daily Goals: "
            f"{report['completed_daily_goals']}\n"
            f"✅ Missions: "
            f"{report['completed_missions']}\n"
            f"📚 Lessons: "
            f"{report['completed_lessons']}\n"
            f"📖 Modules Read: "
            f"{report['modules_read']}\n"
            f"🔁 Retries: "
            f"{report['retries']}\n\n"
            f"📊 Total Interventions: "
            f"{report['total_interventions']}\n\n"
            "🛠 Intervention Priority:\n"
            f"{priority_lines}\n\n"
            "🚨 Primary Intervention:\n\n"
            f"🎯 {primary['type']}\n"
            f"📈 Priority: {primary['priority']}\n"
            f"💡 Reason: {primary['reason']}\n"
            f"➡️ Action: {primary['action']}"
        )
        return self._reply(response)

    def get_learning_decision(self) -> str:
        report = self.learning_decision_engine.analyze(self.memory)
        response = (
            "🧠 Your Learning Decision\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"

            f"🧠 Decision: {report['decision']}\n"
            f"📈 Priority: {report['priority']}\n\n"

            "⚠️ Decision Signals:\n"
            + "\n".join(
                f"• {signal}"
                for signal in report["signals"]
            )
            + "\n\n"
            f"🔎 Reason:\n{report['reason']}\n\n"
            f"🎯 Action:\n{report['action']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)

    def get_learning_state(self) -> str:
        report = self.learning_state_engine.analyze(self.memory)
        response = (
            "🧠 Your Learning State\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📖 Modules Read: {report['modules_read']}\n"
            f"🔁 Retries: {report['retries']}\n\n"
            f"🧠 Current State: {report['state']}\n"
            f"📈 Priority: {report['priority']}\n\n"

            "📊 State Signals:\n"
            + "\n".join(
                f"• {signal}"
                for signal in report["signals"]
            )
            + "\n\n"

            f"💡 {report['description']}"
        )
        return self._reply(response)

    def get_learner_profile_snapshot(self) -> str:
        report = self.learner_profile_snapshot.analyze(self.memory)
        response = (
            "🧠 Your Learner Profile Snapshot\n\n"

            f"📍 Learning State: {report['learning_state']}\n"
            f"🚨 Risk Status: {report['risk_status']}\n"
            f"📊 Performance: {report['trend_status']}\n"
            f"📈 Velocity: {report['velocity_status']}\n\n"

            f"🛠 Primary Intervention: "
            f"{report['primary_intervention']}\n"

            f"🎯 Learning Decision: "
            f"{report['learning_decision']}\n\n"

            f"➡️ Next Best Action:\n"
            f"{report['next_action']}\n\n"

            f"📌 Overall Priority: "
            f"{report['overall_priority']}"
        )
        return self._reply(response)

    def get_learning_profile_interpretation(self) -> str:
        snapshot = self.learner_profile_snapshot.analyze(
            self.memory
        )
        report = self.learning_profile_interpreter.analyze(
            snapshot
        )
        response = (
            "🧠 Your Learning Profile\n\n"
            f"📍 Profile Type: {report['profile_type']}\n"
            f"🎯 Dominant Pattern: {report['dominant_pattern']}\n\n"
            f"🛠 Primary Need: {report['primary_need']}\n\n"
            f"🧭 Recommended Direction:\n"
            f"{report['recommended_direction']}\n\n"
            f"💡 {report['profile_summary']}"
        )
        return self._reply(response)

    def get_learning_profile_advice(self) -> str:
        snapshot = self.learner_profile_snapshot.analyze(
            self.memory
        )
        interpretation = self.learning_profile_interpreter.analyze(
            snapshot
        )
        advice = self.learning_profile_advisor.analyze(
            interpretation
        )
        response = (
            "🧭 Your Learning Profile Advice\n\n"
            f"📍 Profile: {advice['profile_type']}\n"
            f"🎯 Focus: {advice['focus']}\n"
            f"📈 Urgency: {advice['urgency']}\n\n"
            f"🛠 What You Should Do:\n"
            f"{advice['action']}\n\n"
            f"➡️ Next Step:\n"
            f"{advice['next_step']}\n\n"
            f"💡 {advice['reason']}"
        )
        return self._reply(response)

    def get_learning_profile_action_plan(self) -> str:
        snapshot = self.learner_profile_snapshot.analyze(
            self.memory
        )
        interpretation = self.learning_profile_interpreter.analyze(
            snapshot
        )
        advice = self.learning_profile_advisor.analyze(
            interpretation
        )
        plan = self.learning_profile_action_planner.analyze(
            advice
        )
        response = (
            "🧭 Your Learning Action Plan\n\n"
            f"📍 Profile: {plan['profile_type']}\n"
            f"🎯 Focus: {plan['focus']}\n"
            f"📈 Priority: {plan['priority']}\n"
            f"⏱ Duration: {plan['duration']}\n\n"
            f"🛠 Plan: {plan['plan_type']}\n\n"
            "📝 Today's Steps:\n"
        )
        for index, step in enumerate(plan["steps"], start=1):
            response += f"{index}. {step}\n"

        response += (
            f"\n💡 {plan['summary']}"
        )
        return self._reply(response)

    def respond(self, message: str, career_name: str = None) -> str:
        # Save user's message
        self.memory.add_message("User", message)
        # Detect intent
        intent = self.conversation_engine.detect_intent(message)
        # Remember current career
        if career_name:
            self.learning_service.remember_career(career_name)
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

    def get_habit_analysis(self) -> str:
        report = self.habit_analyzer.analyze(self.memory)
        response = (
            "📊 Your Learning Habit Analysis\n\n"
            f"🔥 Learning Streak: {report['learning_streak']}\n"
            f"✅ Missions: {report['completed_missions']}\n"
            f"🎯 Daily Goals: {report['completed_daily_goals']}\n"
            f"📚 Lessons: {report['completed_lessons']}\n"
            f"📈 Habit Status: {report['habit_status']}\n\n"
            f"💡 {report['observation']}"
        )
        return self._reply(response)
    
    def generate_learning_summary(self) -> str:
        report = self.learning_engine_service.analyze(self.memory)

        summary = self.learning_engine_service.generate_summary(report)
        return self._reply(summary)


    def get_personalized_recommendation(self, profile) -> str:
        recommendation = self.reflection_service.recommend(
            profile,
            self.memory
        )
        return self._reply(recommendation)

    def get_learning_reflection(self) -> str:
        reflection = self.reflection_service.generate_reflection(
            self.memory
        )
        return self._reply(reflection)


    def get_learning_insights(self) -> str:
        report = self.learning_engine_service.generate_insights(
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

    def get_progress_dashboard(self) -> str:
        report = self.dashboard_service.generate_dashboard(
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


    def get_study_plan(self) -> str:
        plan = self.dashboard_service.generate_plan(
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

    def get_daily_goals(self) -> str:
        report = self.dashboard_service.generate_goals(
            self.memory
        )
        response = (
            "🎯 Today's Goals\n\n"
            f"⭐ XP: {report['xp']}\n\n"
        )
        for goal in report["goals"]:
            response += f"• {goal}\n"
        return self._reply(response)

    def get_smart_reminder(self) -> str:
        report = self.motivation_service.reminder(
            self.memory
        )
        response = (
            "⏰ Smart Reminder\n\n"
            f"⭐ XP: {report['xp']}\n\n"
            f"{report['reminder']}"
        )
        return self._reply(response)

    def get_motivation(self) -> str:
        report = self.motivation_service.motivation(
            self.memory
        )
        response = (
            "💜 Motivation\n\n"
            f"⭐ XP: {report['xp']}\n\n"
            f"{report['message']}"
        )
        return self._reply(response)

    def get_encouragement(self) -> str:
        report = self.motivation_service.encouragement(
            self.memory
        )
        response = (
            "🌟 Encouragement\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions: {report['missions']}\n\n"
            f"{report['message']}"
        )
        return self._reply(response)


    def get_celebration(self) -> str:
        report = self.motivation_service.celebration(
            self.memory
        )
        response = (
            "🎉 Celebration\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions: {report['missions']}\n\n"
            f"{report['message']}"
        )
        return self._reply(response)

    def get_daily_quote(self) -> str:
        report = self.motivation_service.quote(
            self.memory
        )
        response = (
            "💬 Today's Quote\n\n"
            f"{report['quote']}"
        )
        return self._reply(response)


    def get_learning_tip(self) -> str:
        report = self.motivation_service.learning_tip(
            self.memory
        )
        response = (
            "💡 Today's Learning Tip\n\n"
            f"{report['tip']}"
        )
        return self._reply(response)

    def get_success_prediction(self) -> str:
        report = self.motivation_service.success_prediction(
            self.memory
        )
        response = (
            "🔮 Success Prediction\n\n"
            f"⭐ XP: {report['xp']}\n"
            f"✅ Missions: {report['missions']}\n"
            f"📈 Prediction: {report['prediction']}"
        )
        return self._reply(response)