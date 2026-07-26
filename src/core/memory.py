from src.core.user_profile import UserProfile
from src.core.student_profile import StudentProfile

class Memory:

    def __init__(self):
        # -----------------------------
        # Current Learning State
        # -----------------------------
        self.current_career = None
        self.current_step = 0

        # -----------------------------
        # XP System
        # -----------------------------
        self.total_xp = 0
        self.daily_goal = 200

        # -----------------------------
        # Conversation
        # -----------------------------
        self.conversation_history = []

        # -----------------------------
        # Achievement Progress
        # -----------------------------
        self.completed_missions = 0
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

    # ==================================================
    # Career
    # ==================================================

    def remember_career(self, career_name: str):

        if self.current_career != career_name:
            self.current_career = career_name
            self.reset_progress()

    def get_current_career(self):
        return self.current_career

    # ==================================================
    # Conversation History
    # ==================================================

    def add_message(self, speaker: str, message: str):
        self.conversation_history.append((speaker, message))

    def get_history(self):
        return self.conversation_history

    # ==================================================
    # Learning Progress
    # ==================================================

    def get_current_step(self):
        return self.current_step

    def advance_step(self):
        self.current_step += 1

    def reset_progress(self):
        self.current_step = 0

    # ==================================================
    # XP
    # ==================================================

    def add_xp(self, amount):
        self.total_xp += amount

    def get_total_xp(self):
        return self.total_xp

    def reset_xp(self):
        self.total_xp = 0

    def get_daily_goal(self):
        return self.daily_goal

    def get_progress(self):
        return {
            "current": self.total_xp,
            "goal": self.daily_goal
        }

    def has_completed_daily_goal(self):
        return self.total_xp >= self.daily_goal

    # ==================================================
    # Achievement Progress Counters
    # ==================================================

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

    # ==================================================
    # Achievements
    # ==================================================

    def unlock_achievement(self, achievement_id):

        if achievement_id not in self.unlocked_achievements:
            self.unlocked_achievements.append(achievement_id)

    def has_unlocked_achievement(self, achievement_id):
        return achievement_id in self.unlocked_achievements

    def get_unlocked_achievements(self):
        return self.unlocked_achievements

    # ==================================================
    # Reward
    # ==================================================

    def unlock_reward(self, reward_id):

        if reward_id not in self.unlocked_rewards:
            self.unlocked_rewards.append(reward_id)


    def has_unlocked_reward(self, reward_id):
        return reward_id in self.unlocked_rewards


    def get_unlocked_rewards(self):
        return self.unlocked_rewards


    # ==================================================
    # User Profile
    # ==================================================

    def set_user_name(self, name):
        self.user_profile.set_name(name)

    def get_user_name(self):
        return self.user_profile.get_name()

    def set_dream_career(self, career):
        self.student_profile.set_dream_career(career)

    def get_dream_career(self):
        return self.student_profile.get_dream_career()