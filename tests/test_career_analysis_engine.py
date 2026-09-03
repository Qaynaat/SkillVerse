from src.core.engine.career_analysis_engine import CareerAnalysisEngine
from src.data.careers.cybersecurity import cybersecurity


engine = CareerAnalysisEngine()

analysis = engine.analyze(cybersecurity)


print("=" * 60)
print("MISSION 101 - CAREER ANALYSIS ENGINE")
print("=" * 60)

print()

print("Career:", analysis["name"])
print("Description:", analysis["description"])

print()
print("Skills:", analysis["skills"])
print("Programming Languages:", analysis["programming_languages"])
print("Tools:", analysis["tools"])
print("University Subjects:", analysis["university_subjects"])
print("Career Paths:", analysis["career_paths"])

print()
print("Salary:", analysis["salary"])
print("Remote Work:", analysis["remote_work"])
print("Future Demand:", analysis["future_demand"])
print("Difficulty:", analysis["difficulty"])
print("Creativity:", analysis["creativity"])
print("Mathematics:", analysis["mathematics"])

print()

assert analysis["name"] == cybersecurity.name
assert analysis["skills"] == cybersecurity.skills
assert analysis["programming_languages"] == cybersecurity.programming_languages
assert analysis["career_paths"] == cybersecurity.career_paths

print("All Mission 101 Career Analysis tests passed.")

print("=" * 60)