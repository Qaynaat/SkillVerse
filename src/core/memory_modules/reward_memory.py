class RewardMemory:
    def __init__(self):
        self.unlocked_rewards = []

    def unlock_reward(self, reward_id):
        if reward_id not in self.unlocked_rewards:
            self.unlocked_rewards.append(reward_id)

    def has_unlocked_reward(self, reward_id):
        return reward_id in self.unlocked_rewards

    def get_unlocked_rewards(self):
        return self.unlocked_rewards.copy()