from src.data.careers import ALL_CAREERS

class CareerDatabase:

    def __init__(self):
        self.careers = {
            career.name: career
            for career in ALL_CAREERS
        }
    def get_career(self, career_name):

        return self.careers.get(career_name)

    def get_all_careers(self):

        return list(self.careers.values())

    def add_career(self, career):

        self.careers[career.name] = career