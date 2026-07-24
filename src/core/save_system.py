import json
from pathlib import Path


class SaveSystem:
    DEFAULT_SAVE_PATH = "saves/save_data.json"

    def __init__(self, save_path=DEFAULT_SAVE_PATH):
        self.save_path = Path(save_path)

    def _get_default_data(self):

        return {
            "current_career": None,
            "current_step": 0,
            "total_xp": 0,
            "daily_goal": 200,
            "completed_missions": 0,
            "completed_careers": 0,
            "modules_read": 0,
            "learning_streak": 0,
            "completed_daily_goals": 0,
            "retries_completed": 0,
            "categories_explored": 0,
            "bug_reports": 0,
            "unlocked_achievements": [],
            "unlocked_rewards": [],
            "user_name": "",
            "dream_career": "",
        }

    def _save_exists(self):
        return self.save_path.exists()

    def _create_default_save(self):
        self.save_path.parent.mkdir(parents=True, exist_ok=True)
        data = self._get_default_data()
        
        with open(self.save_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def _memory_to_dict(self, memory):

        data = {
            "current_career": memory.get_current_career(),
            "current_step": memory.get_current_step(),
            "total_xp": memory.get_total_xp(),
            "daily_goal": memory.get_daily_goal(),
            "completed_missions": memory.get_completed_missions(),
            "completed_careers": memory.get_completed_careers(),
            "modules_read": memory.get_modules_read(),
            "learning_streak": memory.get_learning_streak(),
            "completed_daily_goals": memory.get_completed_daily_goals(),
            "retries_completed": memory.get_retries_completed(),
            "categories_explored": memory.get_categories_explored(),
            "bug_reports": memory.get_bug_reports(),
            "unlocked_achievements": memory.get_unlocked_achievements(),
            "unlocked_rewards": memory.get_unlocked_rewards(),
            "user_name": memory.get_user_name(),
            "dream_career": memory.get_dream_career(),
        }
        return data

    def save(self, memory):
        # Ensure parent directories exist before creating/writing the file
        self.save_path.parent.mkdir(parents=True, exist_ok=True)
        data = self._memory_to_dict(memory)

        with open(self.save_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        # Default values are used if the save file is missing fields.
    def _dict_to_memory(self, memory, data):
        defaults = self._get_default_data()

        # Safely extract data with default fallbacks to prevent KeyErrors
        memory.current_career = data.get("current_career", defaults["current_career"])
        memory.current_step = data.get("current_step", defaults["current_step"])
        memory.total_xp = data.get("total_xp", defaults["total_xp"])
        memory.daily_goal = data.get("daily_goal", defaults["daily_goal"])
        memory.completed_missions = data.get("completed_missions", defaults["completed_missions"])
        memory.completed_careers = data.get("completed_careers", defaults["completed_careers"])
        memory.modules_read = data.get("modules_read", defaults["modules_read"])
        memory.learning_streak = data.get("learning_streak", defaults["learning_streak"])
        memory.completed_daily_goals = data.get("completed_daily_goals", defaults["completed_daily_goals"])
        memory.retries_completed = data.get("retries_completed", defaults["retries_completed"])
        memory.categories_explored = data.get("categories_explored", defaults["categories_explored"])
        memory.bug_reports = data.get("bug_reports", defaults["bug_reports"])
        memory.unlocked_achievements = data.get("unlocked_achievements", defaults["unlocked_achievements"])
        memory.unlocked_rewards = data.get("unlocked_rewards",defaults["unlocked_rewards"])

        memory.set_user_name (data.get("user_name",defaults["user_name"]))
        memory.set_dream_career (data.get("dream_career",defaults["dream_career"]))

    def load(self, memory):
        if not self._save_exists():
            self._create_default_save()

        with open(self.save_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self._dict_to_memory(memory, data)