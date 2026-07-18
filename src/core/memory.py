class Memory:

    def __init__(self):
        self.current_career = None
        self.current_step = 0
        self.total_xp = 0
        self.conversation_history = []

    def remember_career(self, career_name: str):

        if self.current_career != career_name:
            self.current_career = career_name
            self.reset_progress()

    def get_current_career(self):
        return self.current_career

    def add_message(self, speaker: str, message: str):
        self.conversation_history.append(
            (speaker, message)
        )

    def get_history(self):
        return self.conversation_history
    
    def get_current_step(self):
        return self.current_step


    def advance_step(self):
        self.current_step += 1


    def reset_progress(self):
        self.current_step = 0

    def add_xp(self , amount):
        self.total_xp += amount

    def get_total_xp(self):
        return self.total_xp
    
    def reset_xp(self):
        self.total_xp = 0
