from src.core.user_profile import UserProfile
from src.core.student_profile import StudentProfile


class ProfileMemory:
    def __init__(self):
        self.user_profile = UserProfile()
        self.student_profile = StudentProfile()

    def set_user_name(self, name):
        self.user_profile.set_name(name)

    def get_user_name(self):
        return self.user_profile.get_name()

    def set_dream_career(self, career):
        self.student_profile.set_dream_career(career)

    def get_dream_career(self):
        return self.student_profile.get_dream_career()