from src.core.engine.career_skill_gap_engine import (
    CareerSkillGapEngine
)

from src.core.student_profile import StudentProfile


class FakeCareer:

    def __init__(self):

        self.name = "Cybersecurity"

        self.required_traits = {
            "logical_thinking": 5,
            "analytical_thinking": 5,
            "curiosity": 4,
            "communication": 3
        }


def test_career_skill_gap_engine():

    student = StudentProfile()

    student.set_scores({
        "logical_thinking": 5,
        "analytical_thinking": 3,
        "curiosity": 4,
        "communication": 1
    })

    career = FakeCareer()

    engine = CareerSkillGapEngine()

    result = engine.analyze_skill_gaps(
        student,
        career
    )

    assert result["career"] == "Cybersecurity"

    assert "logical_thinking" in result["strengths"]

    assert "curiosity" in result["strengths"]

    assert "analytical_thinking" in result["growth_areas"]

    assert "communication" in result["growth_areas"]

    assert result["gaps"]["analytical_thinking"] == 2

    assert result["gaps"]["communication"] == 2

    priorities = engine.get_priority_growth_areas(
        result
    )

    assert len(priorities) == 2

    summary = engine.build_summary(result)

    assert "Cybersecurity" in summary

    assert "analytical_thinking" in summary

    print("=" * 60)
    print("MISSION 115 - CAREER SKILL GAP ENGINE")
    print("=" * 60)

    print()

    print("Career:")
    print(result["career"])

    print()

    print("Strengths:")
    for trait in result["strengths"]:
        print(trait)

    print()

    print("Growth Areas:")
    for trait in result["growth_areas"]:
        print(
            f"{trait} → Gap: {result['gaps'][trait]}"
        )

    print()

    print("Priority Growth Areas:")
    for trait in priorities:
        print(trait)

    print()

    print("Summary:")
    print(summary)

    print()
    print("All Mission 115 Career Skill Gap tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    test_career_skill_gap_engine()