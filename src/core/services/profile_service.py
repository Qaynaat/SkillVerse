class ProfileService:
    def __init__(self, memory):
        self.memory = memory

    def set_user_name(self, name):
        self.memory.set_user_name(name)

    def get_user_name(self):
        return self.memory.get_user_name()

    def set_dream_career(self, career):
        self.memory.set_dream_career(career)

    def get_dream_career(self):
        return self.memory.get_dream_career()