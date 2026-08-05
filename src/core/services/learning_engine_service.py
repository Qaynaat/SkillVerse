class LearningEngineService:

    def __init__(self, services):
        self.mentor_engine = services.mentor_engine
        self.learning_analyzer = services.learning_analyzer
        self.learning_insights = services.learning_insights

    def get_first_step(self, career):
        return self.mentor_engine.get_first_step(career)

    def get_step(self, career, step):
        return self.mentor_engine.get_step(career, step)

    def analyze(self, memory):
        return self.learning_analyzer.analyze(memory)

    def generate_summary(self, report):
        return self.learning_analyzer.generate_summary(report)

    def generate_insights(self, memory):
        return self.learning_insights.generate(memory)