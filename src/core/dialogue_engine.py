class DialogueEngine:
    """
    Creates natural conversations between Byte and the student.
    """

    def __init__(self):
        pass

    def greeting(self):
        return (
            "Hi! 👋\n"
            "I'm Byte, your AI career mentor.\n"
            "I'm here to help you discover your strengths and find the career that's right for you."
        )

    def career_recommendation(self, student_profile, career):
        strongest_trait = student_profile.get_strongest_trait()["name"]
        return (
            f"I recommend {career.name} because your strongest trait is "
            f"{strongest_trait}. "
            f"I think this career matches your abilities very well."
        )