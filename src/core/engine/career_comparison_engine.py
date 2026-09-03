from src.core.engine.career_analysis_engine import CareerAnalysisEngine


class CareerComparisonEngine:
    """Compares multiple careers using structured career data."""

    def __init__(self):

        self.analysis_engine = CareerAnalysisEngine()

    def compare(self, careers):

        comparison = {}

        for career in careers:

            analysis = self.analysis_engine.analyze(career)

            comparison[career.name] = {
                "skills": analysis["skills"],
                "programming_languages":
                    analysis["programming_languages"],
                "university_subjects":
                    analysis["university_subjects"],
                "tools": analysis["tools"],
                "salary": analysis["salary"],
                "remote_work": analysis["remote_work"],
                "future_demand": analysis["future_demand"],
                "difficulty": analysis["difficulty"],
                "creativity": analysis["creativity"],
                "mathematics": analysis["mathematics"]
            }

        return comparison