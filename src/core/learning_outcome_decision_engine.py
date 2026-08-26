class LearningOutcomeDecisionEngine:

    def analyze(self, outcome_report, interpretation_report):
        outcome = outcome_report.get("outcome", "No Recent Outcome")
        impact = interpretation_report.get(
            "impact",
            "No Learning Impact"
        )

        if outcome == "Successful":
            return {
                "outcome": outcome,
                "impact": impact,
                "decision": "Increase Difficulty",
                "priority": "Normal",
                "reason": (
                    "The learner completed the learning action successfully."
                ),
                "action": (
                    "Increase difficulty slightly and introduce a "
                    "small new challenge."
                ),
                "next_step": (
                    "Complete a slightly more challenging learning task."
                ),
            }

        if outcome == "Difficult":
            return {
                "outcome": outcome,
                "impact": impact,
                "decision": "Targeted Revision",
                "priority": "Critical",
                "reason": (
                    "The learner is experiencing difficulty with the "
                    "learning concept."
                ),
                "action": (
                    "Review the difficult concept before increasing workload."
                ),
                "next_step": (
                    "Choose the difficult concept and complete "
                    "a focused revision task."
                ),
            }

        if outcome == "Partial":
            return {
                "outcome": outcome,
                "impact": impact,
                "decision": "Supported Retry",
                "priority": "High",
                "reason": (
                    "The learner made partial progress but has not "
                    "fully completed the learning objective."
                ),
                "action": (
                    "Retry the same concept with a smaller and "
                    "more supported task."
                ),
                "next_step": (
                    "Retry one small part of the incomplete learning task."
                ),
            }

        if outcome == "Skipped":
            return {
                "outcome": outcome,
                "impact": impact,
                "decision": "Consistency Reset",
                "priority": "High",
                "reason": (
                    "The learning action was skipped, so workload "
                    "should not be increased yet."
                ),
                "action": (
                    "Reduce the task size and rebuild the learning routine."
                ),
                "next_step": (
                    "Complete one small achievable learning action."
                ),
            }

        return {
            "outcome": outcome,
            "impact": impact,
            "decision": "Complete Recommended Action",
            "priority": "Normal",
            "reason": (
                "There is not enough recent learning outcome data "
                "to make an adaptive decision."
            ),
            "action": (
                "Complete the recommended learning action first."
            ),
            "next_step": (
                "Start the recommended learning action."
            ),
        }

    def format_report(self, report):
        return (
            "\n"
            "🧭 Learning Outcome Decision\n\n"
            f"📊 Outcome: {report['outcome']}\n"
            f"📈 Impact: {report['impact']}\n\n"
            f"🎯 Decision: {report['decision']}\n"
            f"📌 Priority: {report['priority']}\n\n"
            f"🔎 Reason:\n"
            f"{report['reason']}\n\n"
            f"🛠 Action:\n"
            f"{report['action']}\n\n"
            f"➡️ Next Step:\n"
            f"{report['next_step']}\n"
        )