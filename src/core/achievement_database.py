from src.data.achievements import ACHIEVEMENTS


class AchievementDatabase:
    """
    Provides access to all achievement definitions.
    """

    def __init__(self):
        self.achievements = ACHIEVEMENTS

    def get_all(self):
        """
        Return every achievement.
        """
        return self.achievements

    def get_by_id(self, achievement_id):
        """
        Return a single achievement by its ID.
        """

        return next(
            (
                achievement
                for achievement in self.achievements
                if achievement["id"] == achievement_id
            ),
            None,
        )

    def get_by_category(self, category):
        """
        Return all achievements in a category.
        """

        return [
            achievement
            for achievement in self.achievements
            if achievement["category"].lower() == category.lower()
        ]

    def get_visible(self):
        """
        Return all visible achievements.
        """

        return [
            achievement
            for achievement in self.achievements
            if not achievement["hidden"]
        ]

    def get_hidden(self):
        """
        Return all hidden achievements.
        """

        return [
            achievement
            for achievement in self.achievements
            if achievement["hidden"]
        ]