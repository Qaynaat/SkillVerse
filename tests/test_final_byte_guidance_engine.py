"""
MISSION 118 - FINAL BYTE GUIDANCE ENGINE
"""

from src.core.engine.final_byte_guidance_engine import (
    FinalByteGuidanceEngine
)


def test_final_byte_guidance():

    engine = FinalByteGuidanceEngine()

    student_profile = {
        "scores": {
            "logical_thinking": 5,
            "curiosity": 5,
            "communication": 3
        }
    }

    career_recommendation = {
        "career": "Cybersecurity"
    }

    goal_alignment = {
        "alignment": 88.33
    }

    adaptive_guidance = {
        "next_action": "Improve communication skills"
    }

    career_roadmap = {
        "next_step": "Complete networking fundamentals"
    }

    skill_gap = {
        "gaps": [
            "communication",
            "networking"
        ]
    }

    reflection = {
        "progress": "Good progress"
    }

    smart_reminder = {
        "message": "Practice today"
    }

    result = engine.generate_guidance(
        student_profile,
        career_recommendation,
        goal_alignment,
        adaptive_guidance,
        career_roadmap,
        skill_gap,
        reflection,
        smart_reminder,
    )

    assert result["career"] == "Cybersecurity"
    assert result["alignment"] == 88.33

    assert "logical_thinking" in result["strengths"]
    assert "curiosity" in result["strengths"]

    assert "communication" in result["skill_gaps"]

    assert result["next_action"] == "Improve communication skills"

    assert "Cybersecurity" in result["guidance"]
    assert "88.33" in result["guidance"]

    assert result["reflection"] == reflection
    assert result["reminder"] == smart_reminder


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 118 - FINAL BYTE GUIDANCE ENGINE")
    print("=" * 60)

    test_final_byte_guidance()

    print()
    print("Final Byte Guidance:")
    print("-" * 40)
    print("Cybersecurity")
    print("Alignment: 88.33%")
    print("Next Action: Improve communication skills")

    print()
    print("All Mission 118 Final Byte Guidance tests passed.")
    print("=" * 60)