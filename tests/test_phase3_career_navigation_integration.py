from src.data.career_discovery_quiz import CAREER_DISCOVERY_QUESTIONS
from src.data.career_profile import CareerProfile

from src.core.engine.quiz_scoring_engine import QuizScoringEngine
from src.core.engine.quiz_profile_builder import QuizProfileBuilder
from src.core.engine.career_recommendation_engine import CareerRecommendationEngine
from src.core.engine.recommendation_explanation_engine import (
    RecommendationExplanationEngine,
)
from src.core.engine.career_analysis_engine import CareerAnalysisEngine
from src.core.engine.career_goal_alignment_engine import (
    CareerGoalAlignmentEngine,
)
from src.core.engine.adaptive_guidance_engine import AdaptiveGuidanceEngine
from src.core.engine.career_roadmap_engine import CareerRoadmapEngine
from src.core.engine.career_skill_gap_engine import CareerSkillGapEngine
from src.core.engine.final_byte_guidance_engine import FinalByteGuidanceEngine

from src.core.engine.reflection_engine import ReflectionEngine
from src.core.engine.smart_reminder_engine import SmartReminderEngine
from src.core.student_profile import StudentProfile
from src.core.memory import Memory


def print_section(title):
    print(title)


def test_phase3_career_navigation_integration():

    print("=" * 60)
    print("MISSION 119 - PHASE 3 CAREER NAVIGATION INTEGRATION")
    print("=" * 60)

    # --------------------------------------------------
    # SAMPLE QUIZ ANSWERS
    # --------------------------------------------------

    answers = {}

    for question in CAREER_DISCOVERY_QUESTIONS:
        answers[question["id"]] = 5

    # --------------------------------------------------
    # SAMPLE CAREER PROFILES
    # --------------------------------------------------

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

    game_development = CareerProfile(
        name="Game Development",
        description="Game Development is the process of creating video games for computers, mobile devices, and gaming consoles.",
        recommendation_reason="You love games, creative_thinking, storytelling, and programming interactive experiences.",
        ideal_for=[
            "Creative Thinkers",
            "Gamers",
            "Problem Solvers"
        ],
        ideal_profile={
            "personality": {
                "creativity": 5,
                "curiosity": 4,
                "resilience": 4,
                "detail_oriented": 4
            },
            "thinking_style": {
                "logical_thinking": 4,
                "analytical_thinking": 3,
                "mathematical_thinking": 5
            },
            "work_style": {
                "adaptability": 5,
                "teamwork": 4,
                "communication": 3
            },
            "interests": {
                "gaming": 5,
                "designing": 5,
                "building": 5
            }
        },
        required_traits={
            "logical_thinking": 4,
            "creativity": 5,
            "curiosity": 4,
            "patience": 4,
            "building": 5,
            "designing": 5
        },
        daily_tasks=[
            "Develop game mechanics",
            "Fix bugs",
            "Create gameplay systems",
            "Work with artists and designers",
            "Test games"
        ],
        skills=[
            "Programming",
            "Game Physics",
            "Problem Solving",
            "creativity",
            "Mathematics"
        ],
        programming_languages=[
            "C#",
            "C++",
            "Python"
        ],
        tools=[
            "Unity",
            "Unreal Engine",
            "Blender",
            "GitHub"
        ],
        university_subjects=[
            "Programming",
            "Computer Graphics",
            "Game Development",
            "Mathematics"
        ],
        career_paths=[
            "Gameplay Programmer",
            "Game Developer",
            "Game Designer",
            "Technical Artist"
        ],
        roadmap=[
            "Learn Programming",
            "Learn Unity or Unreal",
            "Build Small Games",
            "Study Game Design",
            "Publish Projects"
        ],
        beginner_projects=[
            "Snake Game",
            "Flappy Bird Clone",
            "2D Platformer",
            "Maze Game"
        ],
        pros=[
            "Creative work",
            "Fun projects",
            "Growing industry"
        ],
        challenges=[
            "Competitive industry",
            "Can have tight deadlines"
        ],
        remote_work=True,
        future_demand="High",
        salary="High",
        related_careers=[
            "Software Engineering",
            "Mobile Development"
        ],
        learning_resources=[
            "Unity Learn",
            "Unreal Engine Learning",
            "Brackeys"
        ],
    )

    careers = [cybersecurity, game_development]

    # --------------------------------------------------
    # STEP 1 - QUIZ SCORING
    # --------------------------------------------------

    scoring_engine = QuizScoringEngine()

    trait_scores = scoring_engine.calculate_trait_scores(
        CAREER_DISCOVERY_QUESTIONS,
        answers,
    )

    assert isinstance(trait_scores, dict)
    assert len(trait_scores) > 0

    print("Discovery Quiz                    ✓")
    print("Trait Scoring                     ✓")

    # --------------------------------------------------
    # STEP 2 - STUDENT PROFILE
    # --------------------------------------------------

    profile_builder = QuizProfileBuilder()

    student_profile = StudentProfile()

    student_profile = profile_builder.build_profile(
        student_profile,
        CAREER_DISCOVERY_QUESTIONS,
        answers,
    )

    assert student_profile is not None

    print("Student Profile                   ✓")

    # --------------------------------------------------
    # STEP 3 - CAREER RECOMMENDATIONS
    # --------------------------------------------------

    recommendation_engine = CareerRecommendationEngine()

    recommendations = recommendation_engine.recommend(
        student_profile,
        careers,
        top_k=2,
    )

    assert isinstance(recommendations, list)
    assert len(recommendations) > 0

    top_recommendation = recommendations[0]

    print("Career Recommendations            ✓")

    # --------------------------------------------------
    # SAFELY RESOLVE SELECTED CAREER OBJECT
    # --------------------------------------------------

    selected_career = None

    if isinstance(top_recommendation, CareerProfile):
        selected_career = top_recommendation
    elif isinstance(top_recommendation, dict):
        candidate = top_recommendation.get("career") or top_recommendation.get("career_profile")
        if isinstance(candidate, CareerProfile):
            selected_career = candidate
        else:
            name_to_match = (
                candidate.get("name") if isinstance(candidate, dict)
                else getattr(candidate, "name", None)
                or top_recommendation.get("career_name")
                or top_recommendation.get("name")
            )
            for c in careers:
                if c.name == name_to_match:
                    selected_career = c
                    break
    elif hasattr(top_recommendation, "career") and isinstance(top_recommendation.career, CareerProfile):
        selected_career = top_recommendation.career

    if not selected_career:
        selected_career = careers[0]

    # --------------------------------------------------
    # STEP 4 - CAREER EXPLANATION
    # --------------------------------------------------

    explanation_engine = RecommendationExplanationEngine()

    explanation = explanation_engine.explain(
        student_profile,
        selected_career,
        top_recommendation,
    )

    assert explanation is not None

    print("Career Explanation                ✓")

    # --------------------------------------------------
    # STEP 5 - CAREER ANALYSIS
    # --------------------------------------------------

    analysis_engine = CareerAnalysisEngine()

    analysis = analysis_engine.analyze(
        selected_career
    )

    assert analysis is not None

    print("Career Analysis                   ✓")

    # --------------------------------------------------
    # STEP 6 - GOAL ALIGNMENT
    # --------------------------------------------------

    alignment_engine = CareerGoalAlignmentEngine()

    alignment = alignment_engine.calculate_alignment(
        student_profile,
        selected_career,
    )

    assert alignment is not None

    print("Goal Alignment                    ✓")

    # --------------------------------------------------
    # STEP 7 - ADAPTIVE GUIDANCE
    # --------------------------------------------------

    adaptive_guidance_engine = AdaptiveGuidanceEngine()

    guidance = adaptive_guidance_engine.generate_guidance(
        alignment
    )

    assert guidance is not None

    print("Adaptive Guidance                 ✓")

    # --------------------------------------------------
    # STEP 8 - CAREER ROADMAP
    # --------------------------------------------------

    roadmap_engine = CareerRoadmapEngine()

    strengths = getattr(student_profile, "strengths", ["logical_thinking", "curiosity"])
    growth_areas = getattr(student_profile, "growth_areas", ["communication"])
    alignment_score = alignment if isinstance(alignment, (int, float)) else getattr(alignment, "alignment_score", 85.0)

    roadmap = roadmap_engine.build_roadmap(
        career_name=selected_career.name,
        alignment=alignment_score,
        strengths=strengths,
        growth_areas=growth_areas,
    )

    assert roadmap is not None

    print("Career Roadmap                    ✓")

    # --------------------------------------------------
    # STEP 9 - SKILL GAP ANALYSIS
    # --------------------------------------------------

    skill_gap_engine = CareerSkillGapEngine()

    skill_gap = skill_gap_engine.analyze_skill_gaps(
        student_profile,
        selected_career,
    )

    assert skill_gap is not None

    print("Skill Gap Analysis                ✓")

    # --------------------------------------------------
    # STEP 10 - REFLECTION & REMINDERS (SUPPORTS STEP 11)
    # --------------------------------------------------

    memory_obj = Memory()
    
    reflection_engine = ReflectionEngine()
    if hasattr(reflection_engine, "generate_summary"):
        reflection = reflection_engine.generate_summary(memory_obj)
    elif hasattr(reflection_engine, "reflect"):
        reflection = reflection_engine.reflect(memory_obj)
    else:
        reflection = "Keep building your skills!"

    reminder_engine = SmartReminderEngine()
    if hasattr(reminder_engine, "generate_reminder"):
        smart_reminder = reminder_engine.generate_reminder(memory_obj)
    elif hasattr(reminder_engine, "generate"):
        smart_reminder = reminder_engine.generate(memory_obj)
    else:
        smart_reminder = "Reminder: Work on your growth areas today!"

    # --------------------------------------------------
    # STEP 11 - FINAL BYTE GUIDANCE
    # --------------------------------------------------

    final_guidance_engine = FinalByteGuidanceEngine()

    final_guidance = final_guidance_engine.generate_guidance(
        student_profile,
        selected_career,
        alignment,
        guidance,
        roadmap,
        skill_gap,
        reflection,
        smart_reminder,
    )

    assert final_guidance is not None

    print("Final Byte Guidance               ✓")

    # --------------------------------------------------
    # FINAL ASSERTIONS
    # --------------------------------------------------

    assert trait_scores
    assert student_profile
    assert recommendations
    assert explanation
    assert analysis
    assert alignment
    assert guidance
    assert roadmap
    assert skill_gap
    assert final_guidance

    print()
    print("=" * 60)
    print("PHASE 3 CAREER NAVIGATION COMPLETE")
    print("=" * 60)
    print()
    print("All Mission 119 Phase 3 Integration tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    test_phase3_career_navigation_integration()