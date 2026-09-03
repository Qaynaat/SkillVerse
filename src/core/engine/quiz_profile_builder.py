from src.core.engine.quiz_scoring_engine import QuizScoringEngine


class QuizProfileBuilder:
    """Build a StudentProfile from career discovery quiz answers."""

    def __init__(self):
        self.scoring_engine = QuizScoringEngine()

    def build_profile(
        self,
        student_profile,
        quiz_questions,
        answers
    ):

        trait_scores = self.scoring_engine.calculate_trait_scores(
            quiz_questions,
            answers
        )

        student_profile.set_scores(trait_scores)

        if trait_scores:

            strongest_trait = max(
                trait_scores,
                key=trait_scores.get
            )

            weakest_trait = min(
                trait_scores,
                key=trait_scores.get
            )

            student_profile.set_strongest_trait(
                strongest_trait
            )

            student_profile.set_weakest_trait(
                weakest_trait
            )

        return student_profile