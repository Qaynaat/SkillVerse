from src.core.student_profile import StudentProfile


class AdaptiveMentor:

    def __init__(self):
        pass

    def recommend(self, profile: StudentProfile, learning_report: dict):
        strongest = profile.get_strongest_trait()
        if strongest is None:
            return (
                "Let's begin your learning journey together."
            )
        trait = strongest["name"]
        level = learning_report["learning_level"]
        if trait == "Analytical Thinker":
            if level == "Beginner":
                return (
                    "🧩 Start with Python and problem-solving. "
                    "Build a strong programming foundation."
                )
            elif level == "Intermediate":
                return (
                    "🧩 You're ready for Data Structures, "
                    "Algorithms, and Cybersecurity basics."
                )
            return (
                "🧩 Challenge yourself with AI, "
                "System Design, and Open Source projects."
            )
        elif trait == "Creative Thinker":
            if level == "Beginner":
                return (
                    "🎨 Learn HTML, CSS, and UI Design fundamentals."
                )
            elif level == "Intermediate":
                return (
                    "🎨 Start building beautiful Flutter "
                    "or Web projects."
                )
            return (
                "🎨 Build a complete portfolio and "
                "design real products."
            )
        elif trait == "Practical Builder":
            return (
                "🛠️ Learn by building projects every week."
            )
        elif trait == "Social Collaborator":
            return (
                "🤝 Practice teamwork and communication "
                "while contributing to group projects."
            )
        return (
            "🚀 Keep learning consistently!"
        )