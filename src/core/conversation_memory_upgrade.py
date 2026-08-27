class ConversationMemoryUpgrade:
    """
    Mission 087
    Short-term conversation memory for Byte.

    Stores a bounded history of recent conversation turns
    and lightweight conversational metadata.

    This engine does not own the learner's permanent memory.
    """

    def __init__(self, max_history=10):
        self.max_history = max_history
        self.history = []

        self.current_career = None
        self.last_intent = None
        self.last_user_message = None
        self.last_byte_response = None

    # ==========================================================
    # RECORD CONVERSATION
    # ==========================================================

    def record_turn(
        self,
        user_message,
        byte_response,
        intent=None,
        career=None
    ):
        """
        Store one conversation turn.
        """

        user_message = str(user_message).strip()
        byte_response = str(byte_response).strip()

        turn = {
            "user_message": user_message,
            "byte_response": byte_response,
            "intent": intent,
            "career": career,
        }

        self.history.append(turn)

        # Keep only the most recent turns.
        if len(self.history) > self.max_history:
            self.history = self.history[
                -self.max_history:
            ]

        self.last_user_message = user_message
        self.last_byte_response = byte_response

        if intent is not None:
            self.last_intent = intent

        if career is not None:
            self.current_career = career

    # ==========================================================
    # HISTORY
    # ==========================================================

    def get_history(self):
        """
        Return a copy so external code cannot accidentally
        modify the internal conversation history.
        """

        return list(self.history)

    def get_recent_history(self, limit=5):

        if limit <= 0:
            return []

        return self.history[-limit:]

    # ==========================================================
    # CONVERSATION STATE
    # ==========================================================

    def get_current_career(self):
        return self.current_career

    def get_last_intent(self):
        return self.last_intent

    def get_last_user_message(self):
        return self.last_user_message

    def get_last_byte_response(self):
        return self.last_byte_response

    # ==========================================================
    # CONTEXT
    # ==========================================================

    def get_recent_context(self, limit=5):
        """
        Return a lightweight representation of recent
        conversation turns.
        """

        recent_turns = self.get_recent_history(limit)

        context = []

        for turn in recent_turns:

            context.append({
                "user_message": turn["user_message"],
                "intent": turn["intent"],
                "career": turn["career"],
            })

        return context

    # ==========================================================
    # SEARCH
    # ==========================================================

    def contains_message(self, text):

        text = str(text).strip().lower()

        if not text:
            return False

        for turn in self.history:

            if text in turn["user_message"].lower():
                return True

        return False

    # ==========================================================
    # CLEAR
    # ==========================================================

    def clear(self):

        self.history.clear()

        self.current_career = None
        self.last_intent = None
        self.last_user_message = None
        self.last_byte_response = None

    # ==========================================================
    # STATUS
    # ==========================================================

    def get_status(self):

        return {
            "history_size": len(self.history),
            "max_history": self.max_history,
            "current_career": self.current_career,
            "last_intent": self.last_intent,
            "has_conversation": bool(self.history),
        }