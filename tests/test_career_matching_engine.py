from src.core.engine.career_matching_engine import CareerMatchingEngine
from src.core.student_profile import StudentProfile
from src.data.careers.cybersecurity import cybersecurity

# 1. Initialize Engine and Profile
engine = CareerMatchingEngine()
student = StudentProfile()

# 2. Populate 4D Student Traits
student.personality = {
    "curiosity": 5,
    "detail_oriented": 4,
    "patience": 3,
    "resilience": 5
}
student.thinking_style = {
    "logical_thinking": 3,
    "analytical_thinking": 3,
    "critical_thinking": 4,
    "research": 2
}
student.work_style = {
    "independent": 4,
    "planning": 3,
    "communication": 3,
    "adaptability": 5
}
student.interests = {
    "protecting": 5,
    "networking": 4
}

# 3. Calculate Match
match_score = engine.calculate_match(student, cybersecurity)

print(f"\n==========================================")
print(f"🎯 Mission 098 Test Results")
print(f"==========================================")
print(f"Career Target : {cybersecurity.name}")
print(f"Match Score   : {match_score}%")
print(f"==========================================\n")