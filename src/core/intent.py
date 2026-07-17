from enum import Enum


class Intent(Enum):

    INTRODUCE_CAREER = "introduce_career"

    ASK_DESCRIPTION = "ask_description"

    ASK_PROGRAMMING_LANGUAGES = "ask_programming_languages"

    ASK_SKILLS = "ask_skills"

    ASK_BEGINNER_PROJECTS = "ask_beginner_projects"

    ASK_LEARNING_RESOURCES = "ask_learning_resources"

    ASK_TOOLS = "ask_tools"

    ASK_UNIVERSITY_SUBJECTS = "ask_university_subjects"

    ASK_CAREER_PATHS = "ask_career_paths"

    ASK_FUTURE_DEMAND = "ask_future_demand"

    UNKNOWN = "unknown"