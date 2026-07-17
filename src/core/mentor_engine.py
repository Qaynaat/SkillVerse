from src.data.career_profile import CareerProfile


class MentorEngine:

    def get_learning_roadmap(
        self,
        career: CareerProfile
    ):
        return career.roadmap

    def get_first_step(
        self,
        career: CareerProfile
    ):
        return self.get_step(career, 0)

    def get_step(
        self,
        career: CareerProfile,
        step_index: int
    ):
        if step_index >= len(career.roadmap):
            return None

        return career.roadmap[step_index]