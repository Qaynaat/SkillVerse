from src.data.personality_traits import PERSONALITY_TRAITS

class StudentAnalyzer:

    def __init__(self):
        pass


    def get_trait(self, trait_id):

        for trait in PERSONALITY_TRAITS:
            if trait["id"] == trait_id:
                return trait
        return None

    def analyze(self, answers):

        profile = {}

        for trait_id, score in answers.items():
            profile[trait_id] = score

        strongest_trait_id = max(profile, key=profile.get)
        weakest_trait_id = min(profile, key=profile.get)

        strongest_trait = self.get_trait(strongest_trait_id)
        weakest_trait = self.get_trait(weakest_trait_id)

        return {
            "scores": profile,
            "strongest_trait": strongest_trait,
            "weakest_trait": weakest_trait
        }