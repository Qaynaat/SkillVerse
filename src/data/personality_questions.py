"""
===========================================================
SkillVerse Personality Questions Database

This file contains all assessment questions used by Byte
to understand a student's personality, thinking style,
work style, and interests.

These questions are used for:

• Personality Assessment
• Student Analysis
• Career Matching
• Recommendation Engine

===========================================================
"""


PERSONALITY_QUESTIONS = [

    # ==================================================
    # 🧠 Thinking Style Questions
    # ==================================================

    {
    "id": "Q001",

    "question":
        "I enjoy solving difficult problems.",

    "trait":
        "logical_thinking",

    "category":
        "thinking_style",

    "weight": 1
},

{
    "id": "Q002",

    "question":
        "I enjoy analysing information before making decisions.",

    "trait":
        "analytical_thinking",

    "category":
        "thinking_style",

    "weight": 1
},

{
    "id": "Q003",

    "question":
        "I enjoy finding creative solutions to problems.",

    "trait":
        "creative_thinking",

    "category":
        "thinking_style",

    "weight": 1
},

    # ==================================================
    # 🌱 Personality Questions
    # ==================================================

    {
    "id": "Q004",

    "question":
        "I enjoy learning new things even without being asked.",

    "trait":
        "curiosity",

    "category":
        "personality",

    "weight": 1
},

{
    "id": "Q005",

    "question":
        "I stay calm when solving difficult problems.",

    "trait":
        "patience",

    "category":
        "personality",

    "weight": 1
},

{
    "id": "Q006",

    "question":
        "I keep trying even when something is difficult.",

    "trait":
        "resilience",

    "category":
        "personality",

    "weight": 1
},

    # ==================================================
    # 🤝 Work Style Questions
    # ==================================================


 {
    "id": "Q007",

    "question":
        "I enjoy working with other people.",

    "trait":
        "teamwork",

    "category":
        "work_style",

    "weight": 1
},

{
    "id": "Q008",

    "question":
        "I enjoy working independently on my own tasks.",

    "trait":
        "independent_work",

    "category":
        "work_style",

    "weight": 1
},

{
    "id": "Q009",

    "question":
        "I feel comfortable explaining my ideas to others.",

    "trait":
        "communication",

    "category":
        "work_style",

    "weight": 1
},

    # ==================================================
    # ❤️ Interest Questions
    # ==================================================

{
    "id": "Q010",

    "question":
        "I enjoy building things from scratch.",

    "trait":
        "building",

    "category":
        "interest",

    "weight": 1
},

{
    "id": "Q011",

    "question":
        "I enjoy protecting people, systems, or information.",

    "trait":
        "protecting",

    "category":
        "interest",

    "weight": 1
},

{
    "id": "Q012",

    "question":
        "I enjoy designing attractive and user-friendly experiences.",

    "trait":
        "designing",

    "category":
        "interest",

    "weight": 1
},

]