from src.core.engine.career_roadmap_engine import (
    CareerRoadmapEngine
)


def test_career_roadmap_engine():

    engine = CareerRoadmapEngine()

    result = engine.build_roadmap(
        career_name="Cybersecurity",
        alignment=88.33,
        strengths=[
            "logical_thinking",
            "curiosity"
        ],
        growth_areas=[
            "communication"
        ]
    )

    assert result["career"] == "Cybersecurity"

    assert result["alignment"] == 88.33

    assert len(result["roadmap"]) == 3

    assert result["roadmap"][0]["phase"] == "Foundation"

    assert result["roadmap"][1]["phase"] == "Growth"

    assert result["roadmap"][2]["phase"] == "Career Preparation"

    print("=" * 60)
    print("MISSION 114 - CAREER ROADMAP ENGINE")
    print("=" * 60)

    print()

    for phase in result["roadmap"]:

        print(phase["phase"])
        print("-" * 40)

        print(phase["focus"])

        print()

    print("All Mission 114 Career Roadmap tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    test_career_roadmap_engine()