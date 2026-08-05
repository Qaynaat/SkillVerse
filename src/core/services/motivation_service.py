class MotivationService:

    def __init__(self, services):
        self.smart_reminder_engine = services.smart_reminder_engine
        self.motivation_engine = services.motivation_engine
        self.encouragement_engine = services.encouragement_engine
        self.celebration_engine = services.celebration_engine
        self.quote_engine = services.quote_engine
        self.learning_tip_engine = services.learning_tip_engine
        self.success_prediction_engine = services.success_prediction_engine

    def reminder(self, memory):
        return self.smart_reminder_engine.generate_reminder(memory)

    def motivation(self, memory):
        return self.motivation_engine.generate_message(memory)

    def encouragement(self, memory):
        return self.encouragement_engine.generate_encouragement(memory)

    def celebration(self, memory):
        return self.celebration_engine.celebrate(memory)

    def quote(self, memory):
        return self.quote_engine.get_quote(memory)

    def learning_tip(self, memory):
        return self.learning_tip_engine.get_tip(memory)

    def success_prediction(self, memory):
        return self.success_prediction_engine.predict(memory)