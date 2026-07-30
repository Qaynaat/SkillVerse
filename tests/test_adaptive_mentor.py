from src.core.adaptive_mentor import AdaptiveMentor
from src.core.student_profile import StudentProfile


mentor = AdaptiveMentor()

profile = StudentProfile()

profile.set_strongest_trait({
    "name": "Analytical Thinker"
})

learning_report = {
    "learning_level": "Intermediate"
}

print("=" * 60)
print("        ADAPTIVE MENTOR TEST")
print("=" * 60)

print()

print(
    mentor.recommend(
        profile,
        learning_report
    )
)

print()

print("=" * 60)
print("✅ AdaptiveMentor Test Completed Successfully!")