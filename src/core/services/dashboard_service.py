class DashboardService:

    def __init__(self, services):
        self.progress_dashboard = services.progress_dashboard
        self.study_planner = services.study_planner
        self.daily_goal_engine = services.daily_goal_engine

    def generate_dashboard(self, memory):
        return self.progress_dashboard.generate(memory)

    def generate_plan(self, memory):
        return self.study_planner.generate_plan(memory)

    def generate_goals(self, memory):
        return self.daily_goal_engine.generate_goals(memory)