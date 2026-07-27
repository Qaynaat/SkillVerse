from src.core.byte_recommendation_engine import ByteRecommendationEngine


# Fake Career Class
class FakeCareer:

    def __init__(self, name, traits):

        self.name = name
        self.required_traits = traits


# Sample Careers
careers = [

    FakeCareer(
        "Cybersecurity",
        {
            "logical_thinking": 5,
            "analytical_thinking": 5,
            "communication": 3
        }
    ),

    FakeCareer(
        "Software Engineering",
        {
            "logical_thinking": 5,
            "analytical_thinking": 4,
            "communication": 4
        }
    ),

    FakeCareer(
        "UI/UX Design",
        {
            "creative_thinking": 5,
            "communication": 5
        }
    )

]


student = {

    "scores": {

        "logical_thinking": 5,
        "analytical_thinking": 4,
        "communication": 3,
        "creative_thinking": 2

    }

}

engine = ByteRecommendationEngine()

results = engine.recommend_careers(student, careers)

print("=" * 60)
print("MISSION 023 - BYTE RECOMMENDATION ENGINE TEST")
print("=" * 60)

print()

for result in results:

    print(f"{result['career'].name} : {result['match_score']}%")

print()

print("=" * 60)
print("TEST FINISHED")
print("=" * 60)