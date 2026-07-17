from .role_database import RoleDatabase


class RoleIntroduction:
    def __init__(self):
        self.role_database = RoleDatabase()

    def show_role(self, career_name, role_name):
        role_data = self.role_database.get_role(career_name, role_name)

        if role_data is None:
            print("Role not found.")
            return

        print("=" * 50)
        print("🎯 ROLE INTRODUCTION")
        print("=" * 50)

        print(f"Role: {role_data.get('title')}")
        print()

        print("Description:")
        print(role_data.get("description"))
        print()

        print("Best For:")
        print(role_data.get("best_for"))
        print()

        print("Primary Tasks:")
        for task in role_data.get("primary_tasks"):
            print(f"• {task}")
        print()

        print("Skills Required:")
        for skill in role_data.get("skills"):
            print(f"• {skill}")

        print("=" * 50)