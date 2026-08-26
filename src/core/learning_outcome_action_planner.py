class LearningOutcomeActionPlanner:

    def analyze(self, decision_report):
        outcome = decision_report.get(
            "outcome",
            "No Recent Outcome"
        )

        decision = decision_report.get(
            "decision",
            "No Decision"
        )

        priority = decision_report.get(
            "priority",
            "Normal"
        )

        if decision == "Targeted Revision":
            return {
                "outcome": outcome,
                "decision": decision,
                "priority": priority,
                "plan_type": "Focused Revision Plan",
                "duration": "30–45 minutes",
                "steps": [
                    "Choose the difficult concept.",
                    "Review the concept for 20 minutes.",
                    "Complete one small practice task.",
                    "Check mistakes and identify the weak area.",
                    "Retry the practice task once."
                ],
                "completion_rule": (
                    "Complete the focused revision before "
                    "starting new learning work."
                ),
                "next_action": (
                    "Choose one difficult concept "
                    "and begin focused revision."
                )
            }

        if decision == "Consistency Building":
            return {
                "outcome": outcome,
                "decision": decision,
                "priority": priority,
                "plan_type": "Consistency Building Plan",
                "duration": "15–20 minutes",
                "steps": [
                    "Choose the smallest achievable goal.",
                    "Work on it for 15 minutes.",
                    "Complete the goal before adding more work.",
                    "Record the completed activity.",
                    "Repeat the routine tomorrow."
                ],
                "completion_rule": (
                    "Maintain the small routine before "
                    "increasing workload."
                ),
                "next_action": (
                    "Complete today's smallest "
                    "achievable learning goal."
                )
            }

        if decision == "Continue Learning":
            return {
                "outcome": outcome,
                "decision": decision,
                "priority": priority,
                "plan_type": "Continue Learning Plan",
                "duration": "30–45 minutes",
                "steps": [
                    "Choose the next recommended task.",
                    "Complete the task without adding unnecessary work.",
                    "Check the result.",
                    "Record the completed activity."
                ],
                "completion_rule": (
                    "Complete the recommended task "
                    "before moving to another task."
                ),
                "next_action": (
                    "Start the next recommended "
                    "learning task."
                )
            }

        return {
            "outcome": outcome,
            "decision": decision,
            "priority": priority,
            "plan_type": "Focused Learning Plan",
            "duration": "20–30 minutes",
            "steps": [
                "Choose one learning task.",
                "Work on it with full focus.",
                "Check the result.",
                "Record the activity."
            ],
            "completion_rule": (
                "Complete the current task before "
                "adding additional work."
            ),
            "next_action": (
                "Start one focused learning task."
            )
        }

    def format_report(self, report):

        lines = [
            "",
            "🧭 Learning Outcome Action Plan",
            "",
            f"📊 Outcome: {report['outcome']}",
            f"🎯 Decision: {report['decision']}",
            f"📈 Priority: {report['priority']}",
            f"⏱ Duration: {report['duration']}",
            "",
            f"🛠 Plan: {report['plan_type']}",
            "",
            "📝 Action Steps:"
        ]

        for index, step in enumerate(
            report["steps"],
            start=1
        ):
            lines.append(
                f"{index}. {step}"
            )

        lines.extend([
            "",
            "✅ Completion Rule:",
            report["completion_rule"],
            "",
            "➡️ Next Action:",
            report["next_action"],
            ""
        ])

        return "\n".join(lines)