from src.core.engine.quiz_profile_builder import QuizProfileBuilder
from src.core.student_profile import StudentProfile


def run_tests():

    print("=" * 60)
    print("MISSION 105 - QUIZ PROFILE BUILDER")
    print("=" * 60)

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
        },

        {
            "id": "q4",
            "trait": "communication"
        }

    ]

    answers = {

        "q1": 5,
        "q2": 4,
        "q3": 5,
        "q4": 2

    }

    student = StudentProfile()

    builder = QuizProfileBuilder()

    profile = builder.build_profile(
        student,
        quiz_questions,
        answers
    )

    scores = profile.get_scores()

    assert scores["logical_thinking"] == 4.5
    assert scores["curiosity"] == 5.0
    assert scores["communication"] == 2.0

    assert profile.get_strongest_trait() == "curiosity"
    assert profile.get_weakest_trait() == "communication"

    print()
    print("Trait Scores:")

    for trait, score in scores.items():
        print(f"{trait}: {score}")

    print()
    print(f"Strongest Trait: {profile.get_strongest_trait()}")
    print(f"Weakest Trait: {profile.get_weakest_trait()}")

    print()
    print("All Mission 105 Quiz Profile Builder tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()