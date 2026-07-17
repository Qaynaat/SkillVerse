class RoleDatabase:
    def __init__(self):
        self.roles={
            "cybersecurity":{
                "security_analyst": {
    "title": "Security Analyst",

    "description":
        "Protects computer systems from cyber threats.",

    "best_for":
        "People who enjoy investigation and solving problems.",

    "primary_tasks": [
        "Monitor security alerts",
        "Investigate incidents",
        "Write security reports"
    ],

    "skills": [
        "Networking",
        "Linux",
        "Problem Solving"
    ]
}
            }
        }
    def get_role(self, career_name, role_name):
        return self.roles.get(career_name, {}).get(role_name)