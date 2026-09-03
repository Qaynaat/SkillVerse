class QuizScoringEngine:
    """Convert career discovery quiz answers into trait scores."""

    def calculate_trait_scores(self, quiz_questions, answers):

        trait_scores = {}

        for question in quiz_questions:

            question_id = question["id"]
            trait = question["trait"]

            if question_id not in answers:
                continue

            score = answers[question_id]

            if trait not in trait_scores:
                trait_scores[trait] = []

            trait_scores[trait].append(score)

        final_scores = {}

        for trait, scores in trait_scores.items():

            average_score = sum(scores) / len(scores)

            final_scores[trait] = round(average_score, 2)

        return final_scores