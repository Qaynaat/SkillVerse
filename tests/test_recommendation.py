import sys
import os

sys.path.append(os.path.abspath("src"))

from core.career_recommendation_engine import CareerRecommendationEngine

student_profile = {
    "personality": {
        "curious": 5,
        "detail_oriented": 5,
        "patient": 4,
        "resilient": 4
    },
    "thinking_style": {
        "logical": 4,
        "analytical": 5,
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