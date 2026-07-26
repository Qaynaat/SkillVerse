class StudentProfile:

    def __init__(self):

        # Career Goal
        self.dream_career = None

        # Personality Analysis
        self.personality_traits = {}

        # Interests
        self.interests = {}

        # Work Preferences
        self.work_style = {}

        # Learning Preferences
        self.learning_style = {}

        # Byte's Analysis
        self.strengths = []
        self.weaknesses = []

        # Current Goal
        self.current_goal = None

    # ===========================
    # Dream Career
    # ===========================

    def set_dream_career(self, career):
        self.dream_career = career

    def get_dream_career(self):
        return self.dream_career

    # ===========================
    # Current Goal
    # ===========================

    def set_current_goal(self, goal):
        self.current_goal = goal

    def get_current_goal(self):
        return self.current_goal