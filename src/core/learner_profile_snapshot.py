class LearnerProfileSnapshot:

    def __init__(
        self,
        learning_risk_predictor,
        learning_recovery_strategist,
        learning_intervention_engine,
        intervention_prioritizer,
        learning_decision_engine,
        learning_state_engine,
        learning_velocity_tracker,
        performance_trend_analyzer,
        next_best_action_engine,
    ):

        self.learning_risk_predictor = learning_risk_predictor
        self.learning_recovery_strategist = learning_recovery_strategist
        self.learning_intervention_engine = learning_intervention_engine
        self.intervention_prioritizer = intervention_prioritizer
        self.learning_decision_engine = learning_decision_engine
        self.learning_state_engine = learning_state_engine
        self.learning_velocity_tracker = learning_velocity_tracker
        self.performance_trend_analyzer = performance_trend_analyzer
        self.next_best_action_engine = next_best_action_engine

    def analyze(self, memory):

        risk = self.learning_risk_predictor.analyze(memory)
        recovery = self.learning_recovery_strategist.analyze(memory)
        intervention = self.learning_intervention_engine.analyze(memory)
        priority = self.intervention_prioritizer.analyze(memory)
        decision = self.learning_decision_engine.analyze(memory)
        state = self.learning_state_engine.analyze(memory)
        velocity = self.learning_velocity_tracker.analyze(memory)
        performance = self.performance_trend_analyzer.analyze(memory)
        next_action = self.next_best_action_engine.analyze(memory)

        overall_priority = self._determine_priority(
            risk,
            recovery,
            intervention,
            priority,
            decision,
            state,
        )

        return {
            "learning_state": state["state"],
            "state_priority": state["priority"],

            "risk_status": risk["risk_status"],
            "risk_score": risk["risk_score"],

            "recovery_level": recovery["recovery_level"],

            "intervention": intervention["intervention_type"],
            "intervention_priority": priority["primary_intervention"]["priority"],
            "primary_intervention": priority["primary_intervention"]["type"],
            "primary_intervention_priority": priority["primary_intervention"]["priority"],

            "learning_decision": decision["decision"],
            "decision_priority": decision["priority"],

            "velocity_score": velocity["velocity_score"],
            "velocity_status": velocity["velocity_status"],

            "performance_score": performance["performance_score"],
            "trend_status": performance["trend_status"],

            "next_action": next_action["next_action"],
            "next_action_priority": next_action["priority"],

            "overall_priority": overall_priority,
        }

    def _determine_priority(
        self,
        risk,
        recovery,
        intervention,
        priority,
        decision,
        state,
    ):

        priorities = [
            risk.get("risk_status"),
            recovery.get("recovery_level"),
            intervention.get("priority"),
            priority.get("primary_intervention_priority"),
            decision.get("priority"),
            state.get("priority"),
        ]

        if any(
            value in ["Critical", "Intensive Recovery"]
            for value in priorities
        ):
            return "Critical"

        if any(
            value in ["High", "Moderate Risk"]
            for value in priorities
        ):
            return "High"

        return "Normal"