from src.data.career_profile import CareerProfile

data_science = CareerProfile(

    name="Data Science",

    description="Data Science transforms raw data into meaningful insights to support business and technical decisions.",

    recommendation_reason="You enjoy analyzing information, finding patterns, and solving problems using data.",

    ideal_for=[
        "Analytical Thinkers",
        "Problem Solvers",
        "People Who Enjoy Statistics"
    ],
    ideal_profile={
        "personality": {
            "curiosity": 5,
            "patience": 4,
            "detail_oriented": 4
        },
        "thinking_style": {
            "logical_thinking": 4,
            "analytical_thinking": 5,
            "critical_thinking": 5,
            "research": 5,
            "mathematical_thinking": 5
        },
        "work_style": {
            "communication": 5,
            "planning": 4,
            "teamwork": 4
        },
        "interests": {
            "data": 5,
            "business": 5
        }
    },

    required_traits={
        "logical_thinking": 5,
        "analytical_thinking": 5,
        "curiosity": 5,
        "patience": 5,
        "creativity":3
    },

    daily_tasks=[
        "Analyze datasets",
        "Create visualizations",
        "Build predictive models",
        "Communicate insights"
    ],

    skills=[
        "Python",
        "SQL",
        "Statistics",
        "Data Visualization",
        "Machine Learning"
    ],

    programming_languages=[
        "Python",
        "SQL",
        "R"
    ],

    tools=[
        "Pandas",
        "NumPy",
        "Power BI",
        "Tableau",
        "Jupyter Notebook"
    ],

    university_subjects=[
        "Statistics",
        "Database Systems",
        "Machine Learning",
        "Data Mining"
    ],

    career_paths=[
        "Data Scientist",
        "Data Analyst",
        "Business Intelligence Analyst",
        "ML Engineer"
    ],

    roadmap=[
        "Learn Python",
        "Master SQL",
        "Study Statistics",
        "Learn Data Analysis",
        "Build Portfolio Projects"
    ],

    beginner_projects=[
        "Sales Dashboard",
        "Netflix Data Analysis",
        "Student Performance Analysis",
        "COVID Data Dashboard"
    ],

    pros=[
        "High demand",
        "Excellent salary",
        "Work across many industries"
    ],

    challenges=[
        "Requires statistics",
        "Large amounts of data",
        "Continuous learning"
    ],

    remote_work=True,

    future_demand="Very High",

    salary="High",

    related_careers=[
        "AI Engineering",
        "Software Engineering"
    ],

    learning_resources=[
        "Kaggle",
        "DataCamp",
        "freeCodeCamp",
        "Google Colab"
    ],
)