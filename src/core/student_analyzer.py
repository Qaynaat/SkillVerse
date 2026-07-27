from src.data.personality_traits import PERSONALITY_TRAITS
from src.core.student_profile import StudentProfile

class StudentAnalyzer:

    def __init__(self):
        pass


    def get_trait(self, trait_id):

        for trait in PERSONALITY_TRAITS:
            if trait["id"] == trait_id:
                return trait
        return None

    def analyze(self, answers):

        trait_scores = {}

        for trait_id, score in answers.items():
            trait_scores[trait_id] = score

        strongest_trait_id = max(trait_scores, key=trait_scores.get)
        weakest_trait_id = min(trait_scores, key=trait_scores.get)

        strongest_trait = self.get_trait(strongest_trait_id)
        weakest_trait = self.get_trait(weakest_trait_id)

        profile = StudentProfile()

        profile.set_scores(trait_scores)
        profile.set_strongest_trait(strongest_trait)
        profile.set_weakest_trait(weakest_trait)

        return profile