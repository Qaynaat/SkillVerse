class StudentProfile:

    def __init__(self):

        # Career Goal
        self.dream_career = None

        # ==========================================
        # 4D Personality Profile
        # ==========================================

        self.personality = {}
        self.thinking_style = {}
        self.work_style = {}
        self.interests = {}

        # ==========================================
        # Learning Preferences
        # ==========================================

        self.learning_style = {}

        # ==========================================
        # Byte's Analysis
        # ==========================================

        self.strengths = []
        self.weaknesses = []

        # ==========================================
        # Assessment Results
        # ==========================================

        self.scores = {}
        self.strongest_trait = None
        self.weakest_trait = None

        # ==========================================
        # Current Goal
        # ==========================================

        self.current_goal = None

    # ===========================
    # Profile
    # ===========================

    def get_profile(self):

        return {
            "personality": self.personality,
            "thinking_style": self.thinking_style,
            "work_style": self.work_style,
            "interests": self.interests
        }

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

    # ===========================
    # Scores
    # ===========================

    def set_scores(self, scores):
        self.scores = scores

    def get_scores(self):
        return self.scores

    # ===========================
    # Strongest Trait
    # ===========================

    def set_strongest_trait(self, trait):
        self.strongest_trait = trait
        
    def get_strongest_trait(self):
        return self.strongest_trait

    # ===========================
    # Weakest Trait
    # ===========================

    def set_weakest_trait(self, trait):
        self.weakest_trait = trait

    def get_weakest_trait(self):
        return self.weakest_trait