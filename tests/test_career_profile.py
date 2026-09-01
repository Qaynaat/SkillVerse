from src.data.career_profile import CareerProfile


def create_valid_profile(required_traits):
    return CareerProfile(
        name="Test Career",
        description="Test career description",
        recommendation_reason="Test recommendation reason",
        ideal_for=["Test Students"],
        daily_tasks=["Testing"],
        skills=["Problem Solving"],
        programming_languages=["Python"],
        tools=["Git"],
        university_subjects=["Computer Science"],
        career_paths=["Test Role"],
        roadmap=["Learn Testing"],
        beginner_projects=["Test Project"],
        pros=["Useful"],
        challenges=["Learning"],
        remote_work=True,
        future_demand="High",
        salary="High",
        related_careers=[],
        learning_resources=["Documentation"],
        ideal_profile={
            "personality": {},
            "thinking_style": {},
            "work_style": {},
            "interests": {}
        },
        required_traits=required_traits
    )


def test_valid_required_traits():
    profile = create_valid_profile({
        "logical_thinking": 5,
        "curiosity": 4
    })

    assert profile.required_traits == {
        "logical_thinking": 5,
        "curiosity": 4
    }


def test_empty_required_traits_rejected():
    try:
        create_valid_profile({})
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_unknown_trait_rejected():
    try:
        create_valid_profile({
            "unknown_trait": 5
        })
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_invalid_importance_rejected():
    try:
        create_valid_profile({
            "logical_thinking": 6
        })
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_non_numeric_importance_rejected():
    try:
        create_valid_profile({
            "logical_thinking": "high"
        })
        assert False, "Expected ValueError"
    except ValueError:
        pass


print("=" * 60)
print("MISSION 096 - CAREER PROFILE TRAIT VALIDATION")
print("=" * 60)

test_valid_required_traits()
test_empty_required_traits_rejected()
test_unknown_trait_rejected()
test_invalid_importance_rejected()
test_non_numeric_importance_rejected()

print("All Mission 096 CareerProfile tests passed.")
print("=" * 60)