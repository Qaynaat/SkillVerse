from src.core.learner_profile_snapshot import LearnerProfileSnapshot
from src.core.learning_risk_predictor import LearningRiskPredictor
from src.core.learning_recovery_strategist import LearningRecoveryStrategist
from src.core.learning_intervention_engine import LearningInterventionEngine
from src.core.intervention_prioritizer import InterventionPrioritizer
from src.core.learning_decision_engine import LearningDecisionEngine
from src.core.learning_state_engine import LearningStateEngine
from src.core.learning_velocity_tracker import LearningVelocityTracker
from src.core.performance_trend_analyzer import PerformanceTrendAnalyzer
from src.core.next_best_action_engine import NextBestActionEngine


class TestMemory:

    def get_learning_streak(self):
        return 2

    def get_completed_daily_goals(self):
        return 1

    def get_completed_missions(self):
        return 2

    def get_completed_lessons(self):
        return ["Lesson 1"]

    def get_modules_read(self):
        return 1

    def get_retries_completed(self):
        return 5


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 070 - LEARNER PROFILE SNAPSHOT TEST")
    print("=" * 60)

    memory = TestMemory()

    # ==================================================
    # Create existing intelligence engines
    # ==================================================

    learning_risk_predictor = LearningRiskPredictor()
    learning_recovery_strategist = LearningRecoveryStrategist()
    learning_intervention_engine = LearningInterventionEngine()
    intervention_prioritizer = InterventionPrioritizer()
    learning_decision_engine = LearningDecisionEngine()
    learning_state_engine = LearningStateEngine()
    learning_velocity_tracker = LearningVelocityTracker()
    performance_trend_analyzer = PerformanceTrendAnalyzer()
    next_best_action_engine = NextBestActionEngine()

    # ==================================================
    # Create Learner Profile Snapshot
    # ==================================================

    snapshot = LearnerProfileSnapshot(
        learning_risk_predictor=learning_risk_predictor,
        learning_recovery_strategist=learning_recovery_strategist,
        learning_intervention_engine=learning_intervention_engine,
        intervention_prioritizer=intervention_prioritizer,
        learning_decision_engine=learning_decision_engine,
        learning_state_engine=learning_state_engine,
        learning_velocity_tracker=learning_velocity_tracker,
        performance_trend_analyzer=performance_trend_analyzer,
        next_best_action_engine=next_best_action_engine,
    )

    # ==================================================
    # Analyze
    # ==================================================

    report = snapshot.analyze(memory)

    print("\n🧠 Learner Profile Snapshot\n")

    print(f"📍 Learning State: {report['learning_state']}")
    print(f"📊 State Priority: {report['state_priority']}")

    print(f"🚨 Risk Status: {report['risk_status']}")
    print(f"📉 Risk Score: {report['risk_score']}")

    print(f"🛟 Recovery Level: {report['recovery_level']}")

    print(f"🛠 Intervention: {report['intervention']}")
    print(f"📈 Intervention Priority: {report['intervention_priority']}")

    print(
        f"🎯 Primary Intervention: "
        f"{report['primary_intervention']}"
    )

    print(
        f"📈 Primary Intervention Priority: "
        f"{report['primary_intervention_priority']}"
    )

    print(
        f"🧭 Learning Decision: "
        f"{report['learning_decision']}"
    )

    print(
        f"📌 Decision Priority: "
        f"{report['decision_priority']}"
    )

    print(f"⚡ Velocity Score: {report['velocity_score']}")
    print(f"📈 Velocity Status: {report['velocity_status']}")

    print(
        f"📊 Performance Score: "
        f"{report['performance_score']}"
    )

    print(
        f"📈 Trend Status: "
        f"{report['trend_status']}"
    )

    print(f"\n➡️ Next Best Action:")
    print(report["next_action"])

    print(
        f"\n📌 Overall Priority: "
        f"{report['overall_priority']}"
    )

    # ==================================================
    # Assertions
    # ==================================================

    assert report["learning_state"] == "Recovering"

    assert report["primary_intervention"] == "Targeted Revision"

    assert report["overall_priority"] == "Critical"

    assert "risk_status" in report
    assert "learning_decision" in report
    assert "velocity_status" in report
    assert "trend_status" in report
    assert "next_action" in report

    print("\n" + "=" * 60)
    print("✅ Learner Profile Snapshot Test Completed Successfully!")
    print("=" * 60)