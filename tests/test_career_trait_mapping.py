from src.data.personality_traits import PERSONALITY_TRAITS
from src.data.careers import (
    software_engineering,
    cybersecurity,
    ai_engineering,
    cloud_engineering,
    data_science,
    devops,
    game_development,
    mobile_development,
    ui_ux_design,
    web_development
)


EXPECTED_CATEGORIES = {
    "personality",
    "thinking_style",
    "work_style",
    "interests"
}


CAREERS = [
    software_engineering,
    cybersecurity,
    ai_engineering,
    cloud_engineering,
    data_science,
    devops,
    game_development,
    mobile_development,
    ui_ux_design,
    web_development
]


def test_canonical_trait_database():

    assert len(PERSONALITY_TRAITS) == 26

    trait_ids = [
        trait["id"]
        for trait in PERSONALITY_TRAITS
    ]

    assert len(trait_ids) == len(set(trait_ids))

    for trait in PERSONALITY_TRAITS:
        assert trait["id"]
        assert trait["name"]
        assert trait["category"]


def test_career_ideal_profiles():

    canonical_ids = {
        trait["id"]
        for trait in PERSONALITY_TRAITS
    }

    for career in CAREERS:

        profile = career.ideal_profile

        assert set(profile.keys()) == EXPECTED_CATEGORIES

        for category, traits in profile.items():

            assert isinstance(traits, dict)

            for trait_id, score in traits.items():

                assert trait_id in canonical_ids

                assert isinstance(score, (int, float))

                assert 1 <= score <= 5


def test_ideal_profile_categories_match_trait_categories():

    trait_categories = {
        trait["id"]: trait["category"]
        for trait in PERSONALITY_TRAITS
    }

    for career in CAREERS:

        for category, traits in career.ideal_profile.items():

            expected_category = category

            for trait_id in traits:

                actual_category = trait_categories[trait_id]

                if expected_category == "interests":
                    expected_category = "interest"

                assert actual_category == expected_category, (
                    f"{career.name}: trait '{trait_id}' belongs to "
                    f"'{actual_category}', but was placed in "
                    f"'{category}'."
                )


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 097 - CAREER TRAIT MAPPING")
    print("=" * 60)

    test_canonical_trait_database()
    test_career_ideal_profiles()
    test_ideal_profile_categories_match_trait_categories()

    print("All Mission 097 Career Trait Mapping tests passed.")
    print("=" * 60)