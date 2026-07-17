
from core.career_database import CareerDatabase
class CareerIntroduction:
    def __init__(self):
       self.career_database=CareerDatabase()
    def show_career(self,career_name):
        career_data=self.career_database.get_career(career_name)
        if career_data is None:
            print("career not Found")
            return
        print("=" * 50)
        print("🛡 CAREER RECOMMENDATION")
        print("=" * 50)
        print(career_data.get("title"))
        print()
        print("Description:")
        print(career_data.get("description"))
        print()
        print("Best For:")
        print(career_data.get("ideal_for"))
        print()
        print("Roles:")
        for role in career_data.get("roles"):
            print(f"• {role}")
        print()
        print("=" * 50)

