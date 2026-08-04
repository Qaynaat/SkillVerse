from src.core.memory_modules.learning_memory import LearningMemory
from src.core.memory_modules.progress_memory import ProgressMemory
from src.core.memory_modules.profile_memory import ProfileMemory
from src.core.memory_modules.conversation_memory import ConversationMemory
from src.core.memory_modules.achievement_memory import AchievementMemory
from src.core.memory_modules.reward_memory import RewardMemory


class Memory(
    LearningMemory,
    ProgressMemory,
    ProfileMemory,
    ConversationMemory,
    AchievementMemory,
    RewardMemory,
):
    def __init__(self):
        LearningMemory.__init__(self)
        ProgressMemory.__init__(self)
        ProfileMemory.__init__(self)
        ConversationMemory.__init__(self)
        AchievementMemory.__init__(self)
        RewardMemory.__init__(self)