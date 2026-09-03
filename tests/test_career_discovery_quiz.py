from src.data.career_discovery_quiz import (
    CAREER_DISCOVERY_QUESTIONS
)

from src.data.personality_traits import PERSONALITY_TRAITS


print("=" * 60)
print("MISSION 103 - CAREER DISCOVERY QUIZ FOUNDATION")
print("=" * 60)


canonical_traits = {
    trait["id"]
    for trait in PERSONALITY_TRAITS
}


question_ids = set()


for question in CAREER_DISCOVERY_QUESTIONS:

    assert "id" in question
    assert "question" in question
    assert "trait" in question

    assert question["id"] not in question_ids

    question_ids.add(question["id"])

    assert question["trait"] in canonical_traits

    assert isinstance(question["question"], str)

    assert question["question"].strip()


print()
print(
    f"Total Discovery Questions: "
    f"{len(CAREER_DISCOVERY_QUESTIONS)}"
)

print()
print("All Mission 103 Career Discovery Quiz tests passed.")

print("=" * 60)