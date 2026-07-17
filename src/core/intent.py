from enum import Enum


class Intent(Enum):

    INTRODUCE_CAREER = "introduce_career"

    ASK_DESCRIPTION = "ask_description"

    ASK_PROGRAMMING_LANGUAGES = "ask_programming_languages"

    ASK_SKILLS = "ask_skills"

    ASK_TOOLS = "ask_tools"

    ASK_CAREER_PATHS = "ask_career_paths"

    ASK_FUTURE_DEMAND = "ask_future_demand"

    UNKNOWN = "unknown"