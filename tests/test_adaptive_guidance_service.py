from src.core.services.adaptive_guidance_service import (
    AdaptiveGuidanceService
)
from src.core.student_profile import StudentProfile


def test_guidance_service():
    student = StudentProfile()
    student.set_current_goal("Learn Python")

    service = AdaptiveGuidanceService()

    result = service.generate_guidance(
        student,
        {
            "current": 100,
            "goal": 200
        }
    )

    assert isinstance(result, dict)
    assert result["status"] == "steady_progress"
    assert result["current_goal"] == "Learn Python"
    assert result["student_profile"] is student


def test_explicit_goal():
    student = StudentProfile()

    service = AdaptiveGuidanceService()

    result = service.generate_guidance(
        student,
        {
            "current": 180,
            "goal": 200
        },
        "Build portfolio"
    )

    assert result["status"] == "high_progress"
    assert result["current_goal"] == "Build portfolio"


def test_no_progress():
    student = StudentProfile()

    service = AdaptiveGuidanceService()

    result = service.get_guidance(
        student,
        {
            "current": 0,
            "goal": 200
        }
    )

    assert result["status"] == "no_progress"


def test_invalid_student():
    service = AdaptiveGuidanceService()

    try:
        service.generate_guidance(
            None,
            {
                "current": 50,
                "goal": 100
            }
        )
        assert False
    except ValueError:
        pass


def test_invalid_progress():
    student = StudentProfile()

    service = AdaptiveGuidanceService()

    try:
        service.generate_guidance(
            student,
            "invalid"
        )
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    print("=" * 60)
    print("MISSION 112 - ADAPTIVE GUIDANCE SERVICE")
    print("=" * 60)

    test_guidance_service()
    test_explicit_goal()
    test_no_progress()
    test_invalid_student()
    test_invalid_progress()

    print()
    print("All Mission 112 Adaptive Guidance Service tests passed.")
    print("=" * 60)