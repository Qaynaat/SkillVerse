from src.core.engine.career_comparison_engine import (
    CareerComparisonEngine
)

from src.data.careers.cybersecurity import cybersecurity
from src.data.careers.software_engineering import (
    software_engineering
)


engine = CareerComparisonEngine()

comparison = engine.compare([
    cybersecurity,
    software_engineering
])


print("=" * 60)
print("MISSION 102 - CAREER COMPARISON ENGINE")
print("=" * 60)

print()

for career_name, data in comparison.items():

    print(f"Career: {career_name}")
    print("-" * 40)

    print("Skills:", data["skills"])
    print("Languages:", data["programming_languages"])
    print("Salary:", data["salary"])
    print("Remote Work:", data["remote_work"])
    print("Future Demand:", data["future_demand"])
    print("Difficulty:", data["difficulty"])
    print("Creativity:", data["creativity"])
    print("Mathematics:", data["mathematics"])

    print()


assert "Cybersecurity" in comparison
assert "Software Engineering" in comparison

assert (
    comparison["Cybersecurity"]["skills"]
    == cybersecurity.skills
)

assert (
    comparison["Software Engineering"]["skills"]
    == software_engineering.skills
)

print("All Mission 102 Career Comparison tests passed.")

print("=" * 60)