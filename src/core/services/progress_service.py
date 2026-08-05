class ProgressService:
    def __init__(self, memory):
        self.memory = memory

    def increment_completed_missions(self):
        self.memory.increment_completed_missions()

    def get_completed_missions(self):
        return self.memory.get_completed_missions()