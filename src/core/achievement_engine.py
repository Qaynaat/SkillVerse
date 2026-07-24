from src.core.achievement_database import AchievementDatabase


class AchievementEngine:

    def __init__(self, database: AchievementDatabase):
        self.database = database

    # ==================================================
    # Public Methods
    # ==================================================

    def check_unlocks(self, memory):

        newly_unlocked = []

        achievements = self.database.get_all()

        for achievement in achievements:

            if memory.has_unlocked_achievement(
                achievement["id"]
            ):
                continue

            if self._is_unlocked(achievement, memory):

                self._unlock_achievement(
                    achievement,
                    memory
                )

                newly_unlocked.append(
                    achievement
                )

        return newly_unlocked

    # ==================================================
    # Private Helpers
    # ==================================================

    def _is_unlocked(self, achievement, memory):

        requirement = achievement["requirement_type"]
        required = achievement["required_count"]

        if requirement == "missions":
            return memory.get_completed_missions() >= required

        elif requirement == "total_xp":
            return memory.get_total_xp() >= required

        elif requirement == "daily_goals":
            return memory.get_completed_daily_goals() >= required

        elif requirement == "streak_days":
            return memory.get_learning_streak() >= required

        elif requirement == "retries_completed":
            return memory.get_retries_completed() >= required

        elif requirement == "modules_read":
            return memory.get_modules_read() >= required

        elif requirement == "careers_completed":
            return memory.get_completed_careers() >= required

        elif requirement == "categories_explored":
            return memory.get_categories_explored() >= required

        elif requirement == "bug_reports":
            return memory.get_bug_reports() >= required

        return False

    def _unlock_achievement(self, achievement, memory):

        reward = achievement["reward"]

        memory.unlock_achievement(
            achievement["id"]
        )

        memory.add_xp(
            reward.get("xp", 0)
        )