class LearningService:
    def __init__(self, memory):
        self.memory = memory

    def remember_career(self, career):
        self.memory.remember_career(career)

    def get_current_career(self):
        return self.memory.get_current_career()

    def add_xp(self, amount):
        self.memory.add_xp(amount)

    def get_total_xp(self):
        return self.memory.get_total_xp()