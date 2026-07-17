from src.core.career_database import CareerDatabase

database = CareerDatabase()

print("=" * 60)
print("      SKILLVERSE CAREER KNOWLEDGE BASE")
print("=" * 60)

for career in database.get_all_careers():

    print(f"\n🚀 {career.name}")
    print("-" * 40)

    print(career.description)

    print("\nSkills:")
    print(", ".join(career.skills))

    print("\nCareer Paths:")
    print(", ".join(career.career_paths))

    print("\nFuture Demand:", career.future_demand)

print("\n🎉 All careers loaded successfully!")