from src.core.student_analyzer import StudentAnalyzer

print("=" * 60)
print("MISSION 019 - STUDENT ANALYZER TEST")
print("=" * 60)

answers = {
    "logical_thinking": 5,
    "creative_thinking": 3,
    "communication": 4
}

analyzer = StudentAnalyzer()

profile = analyzer.analyze(answers)

print()
print("Trait Scores")
print("-" * 40)

for trait, score in profile["scores"].items():
    print(f"{trait}: {score}")

print(profile["strongest_trait"]["name"])

print()
print("Why It Matters")
print("-" * 40)
print(profile["strongest_trait"]["why_it_matters"])

print()
print("Related Careers")
print("-" * 40)
print(", ".join(profile["strongest_trait"]["careers"]))

print()
print("Weakest Trait")
print("-" * 40)
print(profile["weakest_trait"]["name"])

print()
print("=" * 60)
print("TEST FINISHED")
print("=" * 60)