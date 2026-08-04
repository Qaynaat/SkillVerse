class AchievementMemory:
    def __init__(self):
        self.unlocked_achievements = []

    def unlock_achievement(self, achievement_id):
        if achievement_id not in self.unlocked_achievements:
            self.unlocked_achievements.append(achievement_id)

    def has_unlocked_achievement(self, achievement_id):
        return achievement_id in self.unlocked_achievements

    def get_unlocked_achievements(self):
        return self.unlocked_achievements.copy()