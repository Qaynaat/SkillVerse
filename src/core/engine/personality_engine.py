from src.core.personality_profile import PersonalityProfile



class PersonalityEngine:

    def __init__(self, profile: PersonalityProfile):
        self.profile = profile

    def get_greeting_style(self):
        return self.profile.greeting_style

    def get_closing_style(self):
        return self.profile.closing_style

    def get_support_style(self):
        return self.profile.support_style

    def get_celebration_style(self):
        return self.profile.celebration_style

    def get_playfulness(self):
        return self.profile.playfulness

    def get_primary_tone(self):
        return self.profile.primary_tone

    def get_core_values(self):
        return self.profile.core_values

    # NEW METHOD
    def get_profile(self):
        return self.profile