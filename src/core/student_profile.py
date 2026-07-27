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

        # Assessment Results
        self.scores = {}
        self.strongest_trait = None
        self.weakest_trait = None

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

    def set_scores(self, scores):
        self.scores = scores


    def get_scores(self):
        return self.scores


    def set_strongest_trait(self, trait):
        self.strongest_trait = trait


    def get_strongest_trait(self):
        return self.strongest_trait


    def set_weakest_trait(self, trait):
        self.weakest_trait = trait


    def get_weakest_trait(self):
        return self.weakest_trait