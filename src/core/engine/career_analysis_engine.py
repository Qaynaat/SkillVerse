class CareerAnalysisEngine:
    """Analyzes a career profile and returns structured career information."""

    def analyze(self, career_profile):
        return {
            "name": getattr(career_profile, "name", ""),
            "description": getattr(career_profile, "description", ""),
            "skills": getattr(career_profile, "skills", []),
            "programming_languages": getattr(career_profile, "programming_languages", []),
            "tools": getattr(career_profile, "tools", []),
            "university_subjects": getattr(career_profile, "university_subjects", []),
            "career_paths": getattr(career_profile, "career_paths", []),
            "salary": getattr(career_profile, "salary", {}),
            "remote_work": getattr(career_profile, "remote_work", False),
            "future_demand": getattr(career_profile, "future_demand", ""),
            "difficulty": getattr(career_profile, "difficulty", "Medium"),
            "creativity": getattr(career_profile, "creativity", "Medium"),
            "mathematics": getattr(career_profile, "mathematics", "Medium"),
            "daily_tasks": getattr(career_profile, "daily_tasks", []),
            "pros": getattr(career_profile, "pros", []),
            "challenges": getattr(career_profile, "challenges", []),
        }