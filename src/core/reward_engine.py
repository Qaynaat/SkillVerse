from src.data.rewards import ALL_REWARDS


class RewardEngine:

    def __init__(self):
        self.rewards = ALL_REWARDS

    def check_unlocks(self, memory):

        new_rewards = []

        for reward in self.rewards:

            if memory.has_unlocked_reward(reward["id"]):
                continue

            if self._is_unlocked(memory, reward):

                memory.unlock_reward(reward["id"])

                new_rewards.append(reward)

        return new_rewards

    def _is_unlocked(self, memory, reward):

        unlock_type = reward["unlock_type"]

        required = reward["required_count"]

        if unlock_type == "missions":
            return (
                memory.get_completed_missions() >= required
            )

        elif unlock_type == "xp":
            return (
                memory.get_total_xp() >= required
            )

        return False