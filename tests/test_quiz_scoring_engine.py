from src.core.engine.quiz_scoring_engine import QuizScoringEngine


def run_tests():

    engine = QuizScoringEngine()

    quiz_questions = [

        {
            "id": "q1",
            "trait": "logical_thinking"
        },

        {
            "id": "q2",
            "trait": "logical_thinking"
        },

        {
            "id": "q3",
            "trait": "curiosity"
        }

    ]

    answers = {

        "q1": 5,
        "q2": 3,
        "q3": 4

    }

    scores = engine.calculate_trait_scores(
        quiz_questions,
        answers
    )

    assert scores["logical_thinking"] == 4
    assert scores["curiosity"] == 4

    print("=" * 60)
    print("MISSION 104 - QUIZ SCORING ENGINE")
    print("=" * 60)

    print()
    print("Calculated Trait Scores:")

    for trait, score in scores.items():
        print(f"{trait}: {score}")

    print()
    print("All Mission 104 Quiz Scoring tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()