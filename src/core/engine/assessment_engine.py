class AssessmentEngine:

    def __init__(self):

        self.questions = []
        self.current_question = 0
        self.answers = {}
    def load_questions(self, questions):
        self.questions = questions
        self.current_question = 0
        self.answers = {}

    def get_current_question(self):
        if self.current_question >= len(self.questions):
            return None
        return self.questions[self.current_question]

    def submit_answer(self, question_id, answer):
        self.answers[question_id] = answer

    def next_question(self):
        self.current_question += 1

    def is_finished(self):
        return self.current_question >= len(self.questions)

    def get_answers(self):
        return self.answers

    def reset(self):
        self.questions = []
        self.current_question = 0
        self.answers = {}