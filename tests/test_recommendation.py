import sys
import os

sys.path.append(os.path.abspath("src"))

from src.core.engine.career_recommendation_engine import CareerRecommendationEngine

student_profile = {
    "personality": {
        "curiosity": 5,
        "detail_oriented": 5,
        "patience": 4,
        "resilience": 4
    },
    "thinking_style": {
        "logical_thinking": 4,
        "analytical_thinking": 5,
        "critical_thinking": 5,
        "research": 4
    },
    "work_style": {
        "independent": 4,
        "planning": 3,
        "adaptability": 5,
        "communication": 3
    },
    "interests": {
        "protecting": 5,
        "networking": 4
    }
}

engine = CareerRecommendationEngine()

recommendations = engine.recommend_careers(student_profile)

print(recommendations)