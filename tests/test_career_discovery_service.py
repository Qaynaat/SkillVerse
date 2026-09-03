from src.core.services.career_discovery_service import (
    CareerDiscoveryService
)

from src.core.student_profile import StudentProfile

from src.data.careers import (
    cybersecurity,
    software_engineering,
    ai_engineering
)


def run_tests():

    print("=" * 60)
    print("MISSION 106 - CAREER DISCOVERY SERVICE")
    print("=" * 60)

    quiz_questions = [

        {
            "id": "q1",
            "trait": "logical_thinking"
        },

        {
            "id": "q2",
            "trait": "analytical_thinking"
        },

        {
            "id": "q3",
            "trait": "curiosity"
        },

        {
            "id": "q4",
            "trait": "protecting"
        }

    ]

    answers = {

        "q1": 5,
        "q2": 5,
        "q3": 5,
        "q4": 5

    }

    careers = [
        cybersecurity,
        software_engineering,
        ai_engineering
    ]

    student = StudentProfile()

    service = CareerDiscoveryService()

    result = service.discover(
        student_profile=student,
        quiz_questions=quiz_questions,
        answers=answers,
        careers=careers,
        top_n=3
    )

    profile = result["student_profile"]
    recommendations = result["recommendations"]

    # Profile tests
    assert profile.get_scores()
    assert profile.get_strongest_trait() is not None
    assert profile.get_weakest_trait() is not None

    # Recommendation tests
    assert recommendations
    assert len(recommendations) <= 3

    # Explanation tests
    for recommendation in recommendations:

        assert "career" in recommendation
        assert "score" in recommendation
        assert "explanation" in recommendation

        assert recommendation["explanation"]

    print()

    print("Strongest Trait:")
    print(profile.get_strongest_trait())

    print()

    print("Career Recommendations:")

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        career = recommendation["career"]
        score = recommendation["score"]

        print(
            f"{index}. {career.name} → {score}%"
        )

        print(
            recommendation["explanation"]
        )

        print()

    print("All Mission 106 Career Discovery Service tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()