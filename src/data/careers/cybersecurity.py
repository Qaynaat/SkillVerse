from src.data.career_profile import CareerProfile

cybersecurity = CareerProfile(

    name="Cybersecurity",

    description="Cybersecurity focuses on protecting computer systems, networks, and data from cyber threats and attacks.",

    recommendation_reason="You enjoy solving puzzles, thinking like a detective, and protecting digital systems.",

    ideal_for=[
        "Analytical Thinkers",
        "Problem Solvers",
        "Curious Learners",
        "People Interested in Security"
    ],
    ideal_profile={
        "personality": {
            "curiosity": 5,
            "detail_oriented": 5,
            "patience": 5,
            "resilience": 5
        },
        "thinking_style": {
            "logical_thinking": 3,
            "analytical_thinking": 3,
            "critical_thinking": 5,
            "research": 3
        },
        "work_style": {
            "independent": 3,
            "planning": 3,
            "communication": 3,
            "adaptability": 5
        },
        "interests": {
            "protecting": 5,
            "networking": 5
        }
    },
    required_traits={
        "logical_thinking": 5,
        "analytical_thinking": 5,
        "curiosity": 5,
        "resilience": 4,
        "protecting": 5
    },

    daily_tasks=[
        "Monitor networks",
        "Investigate attacks",
        "Perform security testing",
        "Analyze vulnerabilities",
        "Respond to incidents"
    ],

    skills=[
        "Networking",
        "Linux",
        "Python",
        "Ethical Hacking",
        "Problem Solving",
        "Communication"
    ],

    programming_languages=[
        "Python",
        "Bash",
        "PowerShell",
        "C",
        "JavaScript"
    ],

    tools=[
        "Wireshark",
        "Nmap",
        "Burp Suite",
        "Metasploit",
        "Kali Linux"
    ],

    university_subjects=[
        "Computer Networks",
        "Operating Systems",
        "Cybersecurity",
        "Cryptography"
    ],

    career_paths=[
        "SOC Analyst",
        "Penetration Tester",
        "Security Engineer",
        "Security Analyst",
        "Incident Responder"
    ],

    roadmap=[
        "Learn Networking",
        "Learn Linux",
        "Learn Python",
        "Study Cybersecurity Basics",
        "Practice on Labs",
        "Earn Certifications"
    ],

    beginner_projects=[
        "Port Scanner",
        "Password Generator",
        "Network Scanner",
        "Log Analyzer"
    ],

    pros=[
        "High demand",
        "Excellent salary",
        "Exciting work"
    ],

    challenges=[
        "Continuous learning",
        "High responsibility",
        "Rapidly changing threats"
    ],

    remote_work=True,

    future_demand="Very High",

    salary="High",

    related_careers=[
        "Software Engineering",
        "Cloud Engineering",
        "DevOps"
    ],

    learning_resources=[
        "TryHackMe",
        "Hack The Box",
        "OWASP",
        "Cisco Skills for All"
    ],
)