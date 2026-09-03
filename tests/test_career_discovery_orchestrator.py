from src.core.services.career_discovery_orchestrator import (
    CareerDiscoveryOrchestrator
)
from src.data.career_discovery_quiz import CAREER_DISCOVERY_QUESTIONS

from src.data.careers import (
    cybersecurity,
    software_engineering,
    ai_engineering
)


def test_career_discovery_orchestrator():

    answers = [
        {
            "trait": "logical_thinking",
            "score": 5
        },
        {
            "trait": "logical_thinking",
            "score": 4
        },
        {
            "trait": "curiosity",
            "score": 5
        },
        {
            "trait": "communication",
            "score": 3
        }
    ]

    careers = [
        cybersecurity,
        software_engineering,
        ai_engineering
    ]

    orchestrator = CareerDiscoveryOrchestrator()

    result = orchestrator.run_discovery(
        CAREER_DISCOVERY_QUESTIONS,
        answers,
        careers
    )

    assert "strongest_trait" in result
    assert "weakest_trait" in result

    assert "recommendations" in result

    assert "top_career" in result
    assert "top_match" in result

    assert len(result["recommendations"]) > 0


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 110 - CAREER DISCOVERY ORCHESTRATOR")
    print("=" * 60)

    test_career_discovery_orchestrator()

    print()
    print(
        "All Mission 110 Career Discovery Orchestrator "
        "tests passed."
    )
    print("=" * 60)