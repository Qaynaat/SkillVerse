from src.core.engine.career_discovery_result_engine import (
    CareerDiscoveryResultEngine
)

from src.core.student_profile import StudentProfile


def test_discovery_result():

    student = StudentProfile()

    student.set_scores({
        "logical_thinking": 5,
        "curiosity": 4,
        "communication": 2
    })

    student.set_strongest_trait(
        "logical_thinking"
    )

    student.set_weakest_trait(
        "communication"
    )

    recommendations = [
        {
            "career": "Cybersecurity",
            "score": 88.5
        },
        {
            "career": "Software Engineering",
            "score": 80.0
        }
    ]

    explanations = [
        "Cybersecurity matches your logical thinking."
    ]

    guidance = {
        "message":
            "Cybersecurity looks like a strong direction."
    }

    engine = CareerDiscoveryResultEngine()

    result = engine.build_result(
        student,
        recommendations,
        explanations,
        guidance
    )

    assert result["strongest_trait"] == "logical_thinking"

    assert result["weakest_trait"] == "communication"

    assert result["top_career"] == "Cybersecurity"

    assert result["top_match"] == 88.5

    assert len(result["recommendations"]) == 2


if __name__ == "__main__":

    print("=" * 60)

    print(
        "MISSION 109 - CAREER DISCOVERY RESULT ENGINE"
    )

    print("=" * 60)

    test_discovery_result()

    print()

    print(
        "All Mission 109 Career Discovery Result tests passed."
    )

    print("=" * 60)