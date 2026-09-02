from src.data.career_profile import CareerProfile

software_engineering = CareerProfile(

    name="Software Engineering",

    description="Software Engineering is the process of designing, developing, testing, and maintaining software applications that solve real-world problems.",

    recommendation_reason="You enjoy logical thinking, problem solving, building things, and continuously learning new technologies.",

    ideal_for=[
        "Problem Solvers",
        "Creative Thinkers",
        "Logical Minds",
        "People who enjoy technology",
        "Continuous Learners"
    ],
    ideal_profile={
        "personality": {
            "curiosity": 4,
            "creativity": 4,
            "detail_oriented": 5,
            "resilience": 4
        },
        "thinking_style": {
            "logical_thinking": 5,
            "analytical_thinking": 4,
            "critical_thinking": 4
        },
        "work_style": {
            "independent": 4,
            "teamwork": 3,
            "communication": 3,
            "planning": 3,
            "adaptability": 4
        },
        "interests": {
            "building": 5,
            "automation": 5
        }
    },
    required_traits={
        "logical_thinking": 5,
        "analytical_thinking": 5,
        "creativity": 4,
        "curiosity": 5,
        "patience": 4,
        "resilience": 4,
        "building": 5
    },

    daily_tasks=[
        "Write code",
        "Fix bugs",
        "Design software",
        "Work with a team",
        "Review code",
        "Test applications"
    ],

    skills=[
        "Problem Solving",
        "Programming",
        "Communication",
        "Teamwork",
        "Debugging",
        "Critical Thinking",
        "Version Control"
    ],

    programming_languages=[
        "Python",
        "Java",
        "C++",
        "JavaScript",
        "C#"
    ],

    tools=[
        "VS Code",
        "PyCharm",
        "Git",
        "GitHub",
        "Docker",
        "Postman"
    ],

    university_subjects=[
        "Programming Fundamentals",
        "Object-Oriented Programming",
        "Data Structures",
        "Algorithms",
        "Database Systems",
        "Software Engineering",
        "Operating Systems"
    ],

    career_paths=[
        "Backend Developer",
        "Frontend Developer",
        "Full Stack Developer",
        "Mobile Developer",
        "Desktop Application Developer",
        "Software Engineer",
        "QA Engineer",
        "DevOps Engineer"
    ],

    roadmap=[
        {
            "title": "Learn Programming",

            "why": "Programming is the foundation of Software Engineering. Every application starts with code.",

            "goal": "Write your first Python program.",

            "estimated_time": 30,

            "difficulty": "Beginner",

            "reward_xp": 50,

            "tip": "Focus on understanding the logic instead of memorizing syntax."
        },
        {
            "title": "Learn Git & GitHub",

            "why": "Git allows developers to manage code changes and collaborate with teams.",

            "goal": "Upload your first project to GitHub.",

            "estimated_time": 45 ,

            "difficulty": "Beginner",

            "reward_xp": 60,

            "tip": "Commit small changes often with meaningful commit messages."
        }
    ],
    
    beginner_projects=[
        "Calculator",
        "To-Do App",
        "Weather App",
        "Library Management System",
        "Student Management System",
        "Portfolio Website"
    ],

    pros=[
        "High demand",
        "Remote work opportunities",
        "Excellent salary",
        "Many career paths",
        "Continuous learning"
    ],

    challenges=[
        "Technology changes quickly",
        "Requires lifelong learning",
        "Can involve debugging for long hours",
        "Deadlines can be stressful"
    ],

    remote_work=True,

    future_demand="Very High",

    salary="High",

    related_careers=[
        "Cybersecurity",
        "AI Engineering",
        "Cloud Computing",
        "Data Science",
        "Game Development"
    ],

    learning_resources=[
        "freeCodeCamp",
        "CS50",
        "Roadmap.sh",
        "GeeksforGeeks",
        "W3Schools"
    ],
    

)