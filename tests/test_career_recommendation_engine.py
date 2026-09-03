from src.core.engine.career_recommendation_engine import (
    CareerRecommendationEngine
)
from src.core.student_profile import StudentProfile


student = StudentProfile()

student.personality = {
    "curiosity": 5,
    "patience": 4,
    "resilience": 5
}

student.thinking_style = {
    "logical_thinking": 5,
    "analytical_thinking": 5,
    "critical_thinking": 5,
    "research": 4,
    "mathematical": 3
}

student.work_style = {
    "independent_work": 5,
    "teamwork": 3,
    "communication": 3,
    "planning": 4,
    "adaptability": 4
}

student.interests = {
    "protecting": 5,
    "building": 4,
    "automation": 4,
    "data": 3,
    "networking": 5
}


engine = CareerRecommendationEngine()

recommendations = engine.recommend(student)


print("=" * 60)
print("MISSION 099 - CAREER RECOMMENDATION ENGINE")
print("=" * 60)

print()

for index, recommendation in enumerate(
        recommendations,
        start=1
):
    print(
        f"{index}. "
        f"{recommendation['career']} "
        f"→ {recommendation['score']}%"
    )

print()

assert len(recommendations) <= 5

scores = [
    recommendation["score"]
    for recommendation in recommendations
]

assert scores == sorted(scores, reverse=True)

print("All Mission 099 Career Recommendation tests passed.")

print("=" * 60)