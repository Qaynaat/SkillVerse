class ReflectionService:

    def __init__(self, services):
        self.reflection_engine = services.reflection_engine
        self.adaptive_mentor = services.adaptive_mentor

    def generate_reflection(self, memory):
        return self.reflection_engine.generate_summary(memory)

    def recommend(self, profile, report):
        return self.adaptive_mentor.recommend(profile, report)