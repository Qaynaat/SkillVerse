from src.core.user_profile import UserProfile
from src.core.student_profile import StudentProfile
from src.core.config.settings import (
    DEFAULT_XP,
    DEFAULT_MISSIONS,
    DEFAULT_STEP,
)

class Memory:

    def __init__(self):
        # -----------------------------
        # Current Learning State
        # -----------------------------
        self.current_career = None
        self.current_step = DEFAULT_STEP

        # -----------------------------
        # XP System
        # -----------------------------
        self.total_xp = DEFAULT_XP
        self.daily_goal = 200

        # -----------------------------
        # Conversation
        # -----------------------------
        self.conversation_history = []

        # -----------------------------
        # Achievement Progress
        # -----------------------------
        self.completed_missions = DEFAULT_MISSIONS
        self.completed_careers = 0
        self.modules_read = 0
        self.learning_streak = 0
        self.completed_daily_goals = 0
        self.retries_completed = 0
        self.categories_explored = 0
        self.bug_reports = 0

        # -----------------------------
        # Achievement Collection
        # -----------------------------
        self.unlocked_achievements = []


        # -----------------------------
        # User Profile
        # -----------------------------
        self.user_profile = UserProfile()

        # -----------------------------
        # Student Profile
        # -----------------------------


        self.student_profile = StudentProfile()

        # -----------------------------
        # Reward Collection
        # -----------------------------
        self.unlocked_rewards = []

        # -----------------------------
        # Learning Journey
        # -----------------------------
        self.completed_lessons = []
        self.visited_careers = []
        self.favorite_careers = []
        self.career_history = []
        self.last_message = ""
        self.last_login = ""
        self.daily_streak_history = []

    # -----------------------------
    # Career
    # -----------------------------

    def remember_career(self, career_name: str):
        if self.current_career != career_name:
            self.current_career = career_name
            self.visit_career(career_name)
            self.add_career_history(career_name)
            self.reset_progress()

    def get_current_career(self):
        return self.current_career

    # -----------------------------
    # Conversation History
    # -----------------------------

    def add_message(self, speaker: str, message: str):
        self.conversation_history.append((speaker, message))

    def get_history(self):
        return self.conversation_history

    # -----------------------------
    # Learning Progress
    # -----------------------------

    def get_current_step(self):
        return self.current_step

    def advance_step(self):
        self.current_step += 1

    def reset_progress(self):
        self.current_step = DEFAULT_STEP

    # -----------------------------
    # XP
    # -----------------------------

    def add_xp(self, amount):
        self.total_xp += amount

    def get_total_xp(self):
        return self.total_xp
    
    def reset_xp(self):
        self.total_xp = DEFAULT_XP

    def get_daily_goal(self):
        return self.daily_goal

    def get_progress(self):
        return {
            "current": self.total_xp,
            "goal": self.daily_goal
        }

    def has_completed_daily_goal(self):
        return self.total_xp >= self.daily_goal

    # -----------------------------
    # Achievement Progress Counters
    # -----------------------------

    def increment_completed_missions(self):
        self.completed_missions += 1

    def get_completed_missions(self):
        return self.completed_missions

    def increment_completed_careers(self):
        self.completed_careers += 1

    def get_completed_careers(self):
        return self.completed_careers

    def increment_modules_read(self):
        self.modules_read += 1

    def get_modules_read(self):
        return self.modules_read

    def increment_learning_streak(self):
        self.learning_streak += 1

    def get_learning_streak(self):
        return self.learning_streak

    def increment_completed_daily_goals(self):
        self.completed_daily_goals += 1

    def get_completed_daily_goals(self):
        return self.completed_daily_goals

    def increment_retries_completed(self):
        self.retries_completed += 1

    def get_retries_completed(self):
        return self.retries_completed

    def increment_categories_explored(self):
        self.categories_explored += 1

    def get_categories_explored(self):
        return self.categories_explored

    def increment_bug_reports(self):
        self.bug_reports += 1

    def get_bug_reports(self):
        return self.bug_reports

    # -----------------------------
    # Achievements
    # -----------------------------

    def unlock_achievement(self, achievement_id):
        if achievement_id not in self.unlocked_achievements:
            self.unlocked_achievements.append(achievement_id)

    def has_unlocked_achievement(self, achievement_id):
        return achievement_id in self.unlocked_achievements

    def get_unlocked_achievements(self):
        return self.unlocked_achievements
    
    # -----------------------------
    # Reward
    # -----------------------------

    def unlock_reward(self, reward_id):
        if reward_id not in self.unlocked_rewards:
            self.unlocked_rewards.append(reward_id)

    def has_unlocked_reward(self, reward_id):
        return reward_id in self.unlocked_rewards

    def get_unlocked_rewards(self):
        return self.unlocked_rewards


    # -----------------------------
    # User Profile
    # -----------------------------

    def set_user_name(self, name):
        self.user_profile.set_name(name)

    def get_user_name(self):
        return self.user_profile.get_name()

    def set_dream_career(self, career):
        self.student_profile.set_dream_career(career)

    def get_dream_career(self):
        return self.student_profile.get_dream_career()

    # -----------------------------
    # Completed Lessons
    # -----------------------------
    def complete_lesson(self, lesson):
        if lesson not in self.completed_lessons:
            self.completed_lessons.append(lesson)

    def get_completed_lessons(self):
        return self.completed_lessons.copy()

    # -----------------------------
    # Visited Careers
    # -----------------------------    

    def visit_career(self, career):
        if career not in self.visited_careers:
            self.visited_careers.append(career)

    def get_visited_careers(self):
        return self.visited_careers.copy()

    # -----------------------------
    # Favorite Careers
    # -----------------------------   
    
    def add_favorite_career(self, career):
        if career not in self.favorite_careers:
            self.favorite_careers.append(career)

    def get_favorite_careers(self):
        return self.favorite_careers.copy()

    # -----------------------------
    # Career History
    # -----------------------------  

    def add_career_history(self, career):
        self.career_history.append(career)

    def get_career_history(self):
        return self.career_history.copy()
    
    # -----------------------------
    # Last Message
    # ----------------------------- 

    def set_last_message(self, message):
        self.last_message = message

    def get_last_message(self):
        return self.last_message

    # -----------------------------
    # Last Login
    # ----------------------------- 

    def set_last_login(self, date):
        self.last_login = date

    def get_last_login(self):
        return self.last_login

    # -----------------------------
    # Daily Streak History
    # ----------------------------- 

    def add_streak_day(self, day):
        self.daily_streak_history.append(day)

    def get_daily_streak_history(self):
        return self.daily_streak_history.copy()