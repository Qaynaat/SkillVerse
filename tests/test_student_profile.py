from src.core.student_profile import StudentProfile

print("=" * 60)
print("MISSION 016 - STUDENT PROFILE TEST")
print("=" * 60)

profile = StudentProfile()

profile.set_dream_career("Cybersecurity")
profile.set_current_goal("Become a SOC Analyst")

print()
print("Student Profile")
print("-" * 40)
print("Dream Career:", profile.get_dream_career())
print("Current Goal:", profile.get_current_goal())

print()
print("=" * 60)
print("TEST FINISHED")
print("=" * 60)