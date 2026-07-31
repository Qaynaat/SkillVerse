from src.core.memory import Memory


class ProgressDashboard:

    def __init__(self):
        pass

    def generate(self, memory: Memory):

        xp = memory.get_progress()["current"]
        missions = memory.get_completed_missions()
        current_step = memory.get_current_step()

        achievements = len(
            memory.get_unlocked_achievements()
        )

        rewards = len(
            memory.get_unlocked_rewards()
        )

        if xp < 100:
            level = "Beginner"
        elif xp < 300:
            level = "Intermediate"
        else:
            level = "Advanced"

        return {
            "xp": xp,
            "missions": missions,
            "current_step": current_step,
            "achievements": achievements,
            "rewards": rewards,
            "level": level,
        }