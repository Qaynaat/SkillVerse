class UserProfile:

    def __init__(self):
        self.name = ""
        self.dream_career = ""
        
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_dream_career(self, career):
        self.dream_career = career

    def get_dream_career(self):
        return self.dream_career