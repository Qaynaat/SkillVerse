from src.core.config.settings import (
    DEFAULT_STEP,
    DEFAULT_XP,
    DEFAULT_DAILY_GOAL,
)


class LearningMemory:
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
        self.daily_goal = DEFAULT_DAILY_GOAL

        # -----------------------------
        # Learning Journey
        # -----------------------------
        self.completed_lessons = []
        self.visited_careers = []
        self.favorite_careers = []
        self.career_history = []

        # -----------------------------
        # Session Information
        # -----------------------------
        self.last_message = ""
        self.last_login = ""
        self.daily_streak_history = []

    # ==================================================
    # Career
    # ==================================================

    def remember_career(self, career_name):
        if self.current_career != career_name:
            self.current_career = career_name
            self.visit_career(career_name)
            self.add_career_history(career_name)
            self.reset_progress()

    def get_current_career(self):
        return self.current_career

    # ==================================================
    # Learning Progress
    # ==================================================

    def get_current_step(self):
        return self.current_step

    def advance_step(self):
        self.current_step += 1

    def reset_progress(self):
        self.current_step = DEFAULT_STEP

    # ==================================================
    # XP
    # ==================================================

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
            "goal": self.daily_goal,
        }

    def has_completed_daily_goal(self):
        return self.total_xp >= self.daily_goal

    # ==================================================
    # Completed Lessons
    # ==================================================

    def complete_lesson(self, lesson):
        if lesson not in self.completed_lessons:
            self.completed_lessons.append(lesson)

    def get_completed_lessons(self):
        return self.completed_lessons.copy()

    # ==================================================
    # Visited Careers
    # ==================================================

    def visit_career(self, career):
        if career not in self.visited_careers:
            self.visited_careers.append(career)

    def get_visited_careers(self):
        return self.visited_careers.copy()

    # ==================================================
    # Favorite Careers
    # ==================================================

    def add_favorite_career(self, career):
        if career not in self.favorite_careers:
            self.favorite_careers.append(career)

    def get_favorite_careers(self):
        return self.favorite_careers.copy()

    # ==================================================
    # Career History
    # ==================================================

    def add_career_history(self, career):
        self.career_history.append(career)

    def get_career_history(self):
        return self.career_history.copy()

    # ==================================================
    # Last Login
    # ==================================================

    def set_last_login(self, date):
        self.last_login = date

    def get_last_login(self):
        return self.last_login

    # ==================================================
    # Daily Streak History
    # ==================================================

    def add_streak_day(self, day):
        self.daily_streak_history.append(day)

    def get_daily_streak_history(self):
        return self.daily_streak_history.copy()