from src.core.config.settings import DEFAULT_MISSIONS


class ProgressMemory:
    def __init__(self):
        self.completed_missions = DEFAULT_MISSIONS
        self.completed_careers = 0
        self.modules_read = 0
        self.learning_streak = 0
        self.completed_daily_goals = 0
        self.retries_completed = 0
        self.categories_explored = 0
        self.bug_reports = 0

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