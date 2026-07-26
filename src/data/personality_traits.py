"""
===========================================================
SkillVerse Personality Traits Database

This file contains every personality trait Byte understands.

These traits are used for:

• Personality Assessment
• Career Matching
• Student Analysis
• Recommendation Engine

===========================================================
"""

PERSONALITY_TRAITS = [

    # ==================================================
    # 🧠 Thinking Style Traits
    # ==================================================
    {
    "id": "logical_thinking",

    "name": "Logical Thinking",

    "category": "thinking_style",

    "description":
        "Enjoys analysing problems and finding logical solutions.",

    "why_it_matters":
        "Logical thinkers solve complex problems step by step.",

    "careers": [
        "Software Engineering",
        "Cybersecurity",
        "Data Science",
        "Artificial Intelligence"
               ]
    },


    {
    "id": "analytical_thinking",

    "name": "Analytical Thinking",

    "category": "thinking_style",

    "description":
        "Enjoys examining information carefully before making decisions.",

    "why_it_matters":
        "Analytical thinkers identify patterns, evaluate evidence, and make informed decisions.",

    "careers": [
        "Cybersecurity",
        "Data Science",
        "Business Intelligence",
        "Software Engineering"
    ]
},

{
    "id": "creative_thinking",

    "name": "Creative Thinking",

    "category": "thinking_style",

    "description":
        "Enjoys generating new ideas and solving problems in innovative ways.",

    "why_it_matters":
        "Creative thinkers design unique solutions and improve existing systems.",

    "careers": [
        "UI/UX Design",
        "Game Development",
        "Software Engineering",
        "Artificial Intelligence"
    ]
    },

    # ==================================================
    # 🌱 Personality Traits
    # ==================================================

{
    "id": "curiosity",

    "name": "Curiosity",

    "category": "personality",

    "description":
        "Loves learning new things and exploring unfamiliar ideas.",

    "why_it_matters":
        "Curious people continue learning throughout their careers.",

    "careers": [
        "Cybersecurity",
        "Artificial Intelligence",
        "Research",
        "Software Engineering"
    ]
},

{
    "id": "patience",

    "name": "Patience",

    "category": "personality",

    "description":
        "Remains calm while solving difficult or time-consuming problems.",

    "why_it_matters":
        "Patience helps professionals solve complex challenges without giving up.",

    "careers": [
        "Cybersecurity",
        "Software Engineering",
        "Data Science",
        "QA Engineering"
    ]
},

{
    "id": "resilience",

    "name": "Resilience",

    "category": "personality",

    "description":
        "Recovers quickly from setbacks and keeps moving forward.",

    "why_it_matters":
        "Technology changes constantly, and resilience helps professionals adapt.",

    "careers": [
        "Cybersecurity",
        "Software Engineering",
        "Cloud Computing",
        "DevOps"
    ]
},

    # ==================================================
    # 🤝 Work Style Traits
    # ==================================================

{
    "id": "teamwork",

    "name": "Teamwork",

    "category": "work_style",

    "description":
        "Enjoys collaborating with others to achieve shared goals.",

    "why_it_matters":
        "Most technology projects are built by teams rather than individuals.",

    "careers": [
        "Software Engineering",
        "UI/UX Design",
        "Cloud Computing",
        "Project Management"
    ]
},

{
    "id": "independent_work",

    "name": "Independent Work",

    "category": "work_style",

    "description":
        "Feels comfortable working alone and taking ownership of tasks.",

    "why_it_matters":
        "Independent workers stay productive with minimal supervision.",

    "careers": [
        "Cybersecurity",
        "Data Science",
        "Game Development",
        "Software Engineering"
    ]
},

{
    "id": "communication",

    "name": "Communication",

    "category": "work_style",

    "description":
        "Explains ideas clearly and works effectively with others.",

    "why_it_matters":
        "Communication is essential for teamwork, leadership, and client interaction.",

    "careers": [
        "Project Management",
        "UI/UX Design",
        "Software Engineering",
        "Business Analysis"
    ]
},

    # ==================================================
    #❤️ Interest Traits
    # ==================================================
{
    "id": "building",

    "name": "Building",

    "category": "interest",

    "description":
        "Enjoys creating software, systems, and digital products.",

    "why_it_matters":
        "Builders enjoy turning ideas into real solutions.",

    "careers": [
        "Software Engineering",
        "Game Development",
        "Artificial Intelligence"
    ]
},

{
    "id": "protecting",

    "name": "Protecting",

    "category": "interest",

    "description":
        "Enjoys keeping people, systems, and information safe.",

    "why_it_matters":
        "Protecting digital assets is at the heart of cybersecurity.",

    "careers": [
        "Cybersecurity",
        "Digital Forensics",
        "SOC Analyst"
    ]
},

{
    "id": "designing",

    "name": "Designing",

    "category": "interest",

    "description":
        "Enjoys creating attractive, useful, and user-friendly experiences.",

    "why_it_matters":
        "Design improves how people interact with technology.",

    "careers": [
        "UI/UX Design",
        "Graphic Design",
        "Game Development"
    ]
}

]