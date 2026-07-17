class CareerProfile:
    """Blueprint for every career in SkillVerse. 
     Every career should follow this structure .
     """
    def __init__(
            self,
            name,
            description,
            recommendation_reason,
            ideal_for,
            daily_tasks,
            skills,
            programming_languages,
            tools,
            university_subjects,
            career_paths,
            roadmap,
            beginner_projects,
            pros,
            challenges,
            remote_work,
            future_demand,
            salary,
            related_careers,
            learning_resources
            ):
        self.name = name 
        self.description =description
        self.recommendation_reason = recommendation_reason
        self.ideal_for =ideal_for
        self.daily_tasks = daily_tasks
        self.skills = skills
        self.programming_languages =programming_languages
        self.tools = tools
        self.university_subjects =university_subjects
        self.career_paths = career_paths
        self.roadmap = roadmap 
        self.beginner_projects = beginner_projects
        self.pros = pros
        self.challenges = challenges
        self.remote_work = remote_work 
        self.future_demand = future_demand 
        self.salary = salary
        self.related_careers = related_careers
        self.learning_resources = learning_resources
        self.validate()

    def validate(self):

        required_lists = [
            self.skills,
            self.career_paths,
            self.roadmap,
            self.programming_languages
        ]

        for item in required_lists:
            if not item:
                raise ValueError("Career profile contains empty required fields.")