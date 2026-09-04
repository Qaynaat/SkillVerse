from src.core.engine.adaptive_guidance_engine import AdaptiveGuidanceEngine


engine = AdaptiveGuidanceEngine()


def test_high_progress():
    result = engine.generate_guidance(
        {"current": 180, "goal": 200},
        "Complete Python project"
    )

    assert result["status"] == "high_progress"
    assert result["progress_percentage"] == 90.0
    assert "challenging" in result["message"].lower()


def test_steady_progress():
    result = engine.generate_guidance(
        {"current": 100, "goal": 200},
        "Learn Python"
    )

    assert result["status"] == "steady_progress"


def test_low_progress():
    result = engine.generate_guidance(
        {"current": 20, "goal": 200},
        "Learn networking"
    )

    assert result["status"] == "low_progress"
    assert "smaller" in result["next_step"].lower()


def test_no_progress():
    result = engine.generate_guidance(
        {"current": 0, "goal": 200},
        "Build portfolio"
    )

    assert result["status"] == "no_progress"


def test_invalid_progress():
    try:
        engine.generate_guidance("invalid")
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    print("=" * 60)
    print("MISSION 111 - ADAPTIVE GUIDANCE ENGINE")
    print("=" * 60)

    test_high_progress()
    test_steady_progress()
    test_low_progress()
    test_no_progress()
    test_invalid_progress()

    print()
    print("All Mission 111 Adaptive Guidance tests passed.")
    print("=" * 60)