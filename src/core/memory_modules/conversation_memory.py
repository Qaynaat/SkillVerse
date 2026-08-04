class ConversationMemory:
    def __init__(self):
        self.conversation_history = []
        self.last_message = ""

    # ============================
    # Conversation History
    # ============================

    def add_message(self, speaker, message):
        self.conversation_history.append((speaker, message))
        self.last_message = message

    def get_history(self):
        return self.conversation_history.copy()

    # ============================
    # Last Message
    # ============================

    def set_last_message(self, message):
        self.last_message = message

    def get_last_message(self):
        return self.last_message