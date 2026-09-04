from src.core.engine.adaptive_guidance_result_engine import (
    AdaptiveGuidanceResultEngine
)
from src.core.student_profile import StudentProfile


def test_adaptive_guidance_result():

    student = StudentProfile()

    student.set_scores({
        "logical_thinking": 5,
        "curiosity": 4,
        "communication": 2
    })

    student.set_strongest_trait("logical_thinking")
    student.set_weakest_trait("communication")

    guidance = {
        "career": "Cybersecurity",
        "alignment": 88.33,
        "strengths": [
            "logical_thinking",
            "curiosity"
        ],
        "growth_areas": [
            "communication"
        ],
        "next_steps": [
            "Improve communication skills",
            "Practice cybersecurity projects"
        ]
    }

    engine = AdaptiveGuidanceResultEngine()

    result = engine.build_result(
        student,
        guidance
    )

    assert result["career"] == "Cybersecurity"
    assert result["alignment"] == 88.33
    assert result["strongest_trait"] == "logical_thinking"
    assert result["weakest_trait"] == "communication"

    assert "logical_thinking" in result["strengths"]
    assert "communication" in result["growth_areas"]

    assert len(result["next_steps"]) == 2
    assert "Cybersecurity" in result["summary"]

    print("=" * 60)
    print("MISSION 113 - ADAPTIVE GUIDANCE RESULT ENGINE")
    print("=" * 60)

    print()
    print("Career:")
    print(result["career"])

    print()
    print("Alignment:")
    print(f'{result["alignment"]}%')

    print()
    print("Summary:")
    print(result["summary"])

    print()
    print("All Mission 113 Adaptive Guidance Result tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    test_adaptive_guidance_result()