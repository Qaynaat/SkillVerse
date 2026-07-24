"""
achievements.py
---------------
Master catalog of all SkillVerse achievements.

This file contains every achievement available in the platform.
Each achievement defines:

- Unlock condition
- Reward
- Category
- Visibility
"""

ACHIEVEMENTS = [

    # ==========================================================
    # MISSION ACHIEVEMENTS
    # ==========================================================

    {
        "id": "first_mission",
        "title": "First Mission",
        "description": "Complete your first learning mission.",
        "icon": "🏅",
        "category": "Mission",

        "requirement_type": "missions",
        "required_count": 1,

        "reward": {
            "xp": 100
        },

        "hidden": False,
    },

    {
        "id": "mission_rookie",
        "title": "Mission Rookie",
        "description": "Successfully complete 5 learning missions.",
        "icon": "🚀",
        "category": "Mission",

        "requirement_type": "missions",
        "required_count": 5,

        "reward": {
            "xp": 200
        },

        "hidden": False,
    },

    {
        "id": "mission_master",
        "title": "Mission Master",
        "description": "Complete 25 learning missions.",
        "icon": "💪",
        "category": "Mission",

        "requirement_type": "missions",
        "required_count": 25,

        "reward": {
            "xp": 500
        },

        "hidden": False,
    },

    # ==========================================================
    # XP MILESTONES
    # ==========================================================

    {
        "id": "xp_beginner",
        "title": "XP Beginner",
        "description": "Earn your first 100 XP.",
        "icon": "⭐",
        "category": "XP",

        "requirement_type": "total_xp",
        "required_count": 100,

        "reward": {
            "xp": 50
        },

        "hidden": False,
    },

    {
        "id": "xp_explorer",
        "title": "XP Explorer",
        "description": "Reach a total of 500 XP.",
        "icon": "🌟",
        "category": "XP",

        "requirement_type": "total_xp",
        "required_count": 500,

        "reward": {
            "xp": 200
        },

        "hidden": False,
    },

    {
        "id": "xp_legend",
        "title": "XP Legend",
        "description": "Accumulate 1,000 XP.",
        "icon": "🏆",
        "category": "XP",

        "requirement_type": "total_xp",
        "required_count": 1000,

        "reward": {
            "xp": 500
        },

        "hidden": False,
    },

    # ==========================================================
    # STREAK & CONSISTENCY
    # ==========================================================

    {
        "id": "daily_champion",
        "title": "Daily Champion",
        "description": "Complete all daily tasks for 7 consecutive days.",
        "icon": "🔥",
        "category": "Streak",

        "requirement_type": "daily_goals",
        "required_count": 7,

        "reward": {
            "xp": 300
        },

        "hidden": False,
    },

    {
        "id": "learning_streak",
        "title": "Learning Streak",
        "description": "Maintain a 30-day active learning streak.",
        "icon": "📚",
        "category": "Streak",

        "requirement_type": "streak_days",
        "required_count": 30,

        "reward": {
            "xp": 600
        },

        "hidden": False,
    },

    {
        "id": "never_give_up",
        "title": "Never Give Up",
        "description": "Retry and complete a failed quiz or assignment.",
        "icon": "🎯",
        "category": "Persistence",

        "requirement_type": "retries_completed",
        "required_count": 1,

        "reward": {
            "xp": 100
        },

        "hidden": False,
    },

    # ==========================================================
    # KNOWLEDGE & CAREER
    # ==========================================================

    {
        "id": "knowledge_seeker",
        "title": "Knowledge Seeker",
        "description": "Read through 10 full learning modules or articles.",
        "icon": "🧠",
        "category": "Learning",

        "requirement_type": "modules_read",
        "required_count": 10,

        "reward": {
            "xp": 200
        },

        "hidden": False,
    },

    {
        "id": "career_explorer",
        "title": "Career Explorer",
        "description": "Complete one full career path module.",
        "icon": "🎓",
        "category": "Career",

        "requirement_type": "careers_completed",
        "required_count": 1,

        "reward": {
            "xp": 500
        },

        "hidden": False,
    },

    # ==========================================================
    # DISCOVERY & COMMUNITY
    # ==========================================================

    {
        "id": "curious_mind",
        "title": "Curious Mind",
        "description": "Explore 5 different subject categories.",
        "icon": "👀",
        "category": "Discovery",

        "requirement_type": "categories_explored",
        "required_count": 5,

        "reward": {
            "xp": 250
        },

        "hidden": True,
    },

    {
        "id": "bug_hunter",
        "title": "Bug Hunter",
        "description": "Report a bug or suggestion to help improve SkillVerse.",
        "icon": "🐛",
        "category": "Community",

        "requirement_type": "bug_reports",
        "required_count": 1,

        "reward": {
            "xp": 200
        },

        "hidden": False,
    },

    # ==========================================================
    # FUTURE ACHIEVEMENTS
    # (Reserved for future SkillVerse releases)
    # ==========================================================

    # {
    #     "id": "night_owl",
    #     "title": "Night Owl",
    #     "description": "Complete a lesson between midnight and 4 AM.",
    #     "icon": "🦉",
    #     "category": "Special",
    #     "requirement_type": "night_lessons",
    #     "required_count": 1,
    #     "reward": {
    #         "xp": 150
    #     },
    #     "hidden": True,
    # },

    # {
    #     "id": "speed_demon",
    #     "title": "Speed Demon",
    #     "description": "Complete a quiz with 100% accuracy in under 2 minutes.",
    #     "icon": "⚡",
    #     "category": "Skill",
    #     "requirement_type": "speed_quizzes",
    #     "required_count": 1,
    #     "reward": {
    #         "xp": 300
    #     },
    #     "hidden": False,
    # },
]