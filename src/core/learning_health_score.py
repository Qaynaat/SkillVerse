class LearningHealthScore:
    """
    Mission 086
    Calculates an overall learning health score
    from the learner's existing memory data.

    This engine does not own memory.
    It receives memory and analyzes the current
    learning signals.
    """

    # ==========================================================
    # SCORE CALCULATION
    # ==========================================================

    def analyze(self, memory):

        learning_streak = memory.get_learning_streak()
        completed_daily_goals = memory.get_completed_daily_goals()
        completed_missions = memory.get_completed_missions()
        completed_lessons = memory.get_completed_lessons()
        modules_read = memory.get_modules_read()
        retries = memory.get_retries_completed()

        completed_lessons_count = len(completed_lessons)

        # ------------------------------------------------------
        # Individual health scores
        # ------------------------------------------------------

        streak_score = self._streak_score(
            learning_streak
        )

        daily_goal_score = self._daily_goal_score(
            completed_daily_goals
        )

        mission_score = self._activity_score(
            completed_missions
        )

        lesson_score = self._activity_score(
            completed_lessons_count
        )

        module_score = self._activity_score(
            modules_read
        )

        retry_score = self._retry_score(
            retries
        )

        # ------------------------------------------------------
        # Overall score
        # ------------------------------------------------------

        health_score = round(
            (
                streak_score
                + daily_goal_score
                + mission_score
                + lesson_score
                + module_score
                + retry_score
            ) / 6
        )

        health_level = self._get_health_level(
            health_score
        )

        priority = self._get_priority(
            health_score
        )

        areas_to_improve = []

        if streak_score < 60:
            areas_to_improve.append(
                "Consistency"
            )

        if daily_goal_score < 60:
            areas_to_improve.append(
                "Daily goal completion"
            )

        if mission_score < 60:
            areas_to_improve.append(
                "Mission completion"
            )

        if lesson_score < 60:
            areas_to_improve.append(
                "Lesson completion"
            )

        if module_score < 60:
            areas_to_improve.append(
                "Module progress"
            )

        if retry_score < 60:
            areas_to_improve.append(
                "Practice and retries"
            )

        recommendation = self._build_recommendation(
            health_score,
            areas_to_improve
        )

        return {
            "health_score": health_score,
            "health_level": health_level,
            "priority": priority,

            "factors": {
                "learning_streak": streak_score,
                "daily_goals": daily_goal_score,
                "missions": mission_score,
                "lessons": lesson_score,
                "modules": module_score,
                "retries": retry_score,
            },

            "areas_to_improve": areas_to_improve,

            "recommendation": recommendation,
        }

    # ==========================================================
    # INDIVIDUAL SCORES
    # ==========================================================

    @staticmethod
    def _streak_score(streak):

        if streak <= 0:
            return 0

        if streak < 3:
            return 40

        if streak < 7:
            return 70

        if streak < 14:
            return 85

        return 100

    @staticmethod
    def _daily_goal_score(goals):

        if goals <= 0:
            return 0

        if goals == 1:
            return 50

        if goals < 5:
            return 75

        return 100

    @staticmethod
    def _activity_score(value):

        if value <= 0:
            return 0

        if value < 3:
            return 50

        if value < 10:
            return 75

        return 100

    @staticmethod
    def _retry_score(retries):

        if retries <= 0:
            return 40

        if retries < 3:
            return 65

        if retries < 7:
            return 85

        return 100

    # ==========================================================
    # HEALTH LEVEL
    # ==========================================================

    @staticmethod
    def _get_health_level(score):

        if score >= 80:
            return "Excellent"

        if score >= 60:
            return "Healthy"

        if score >= 40:
            return "Developing"

        return "Needs Attention"

    # ==========================================================
    # PRIORITY
    # ==========================================================

    @staticmethod
    def _get_priority(score):

        if score >= 80:
            return "Low"

        if score >= 60:
            return "Medium"

        if score >= 40:
            return "High"

        return "Critical"

    # ==========================================================
    # RECOMMENDATION
    # ==========================================================

    @staticmethod
    def _build_recommendation(
        score,
        areas_to_improve
    ):

        if score >= 80:
            return (
                "Your learning health is strong. "
                "Maintain your current learning routine."
            )

        if score >= 60:

            if areas_to_improve:
                focus = ", ".join(
                    areas_to_improve[:2]
                )

                return (
                    f"Your learning health is stable. "
                    f"Focus next on {focus}."
                )

            return (
                "Maintain your current learning routine "
                "and continue making steady progress."
            )

        if score >= 40:

            if areas_to_improve:
                focus = ", ".join(
                    areas_to_improve[:2]
                )

                return (
                    f"Strengthen {focus} before increasing "
                    "your learning workload."
                )

            return (
                "Rebuild consistency before increasing "
                "your learning workload."
            )

        return (
            "Your learning activity needs attention. "
            "Start with one small learning action and "
            "rebuild consistency gradually."
        )

    # ==========================================================
    # BYTE-FRIENDLY REPORT
    # ==========================================================

    def format_report(self, report):

        lines = [
            "",
            "🧠 Learning Health Score",
            "",
            f"📊 Health Score: "
            f"{report['health_score']}%",
            f"📈 Health Level: "
            f"{report['health_level']}",
            f"🔥 Priority: "
            f"{report['priority']}",
            "",
            "📋 Health Factors:",
            "",
            f"🔥 Learning Streak: "
            f"{self._factor_label(report['factors']['learning_streak'])}",
            f"🎯 Daily Goals: "
            f"{self._factor_label(report['factors']['daily_goals'])}",
            f"✅ Missions: "
            f"{self._factor_label(report['factors']['missions'])}",
            f"📚 Lessons: "
            f"{self._factor_label(report['factors']['lessons'])}",
            f"📖 Modules: "
            f"{self._factor_label(report['factors']['modules'])}",
            f"🔁 Retries: "
            f"{self._factor_label(report['factors']['retries'])}",
            "",
            "⚠️ Areas To Improve:",
        ]

        if report["areas_to_improve"]:

            for area in report["areas_to_improve"]:
                lines.append(
                    f"• {area}"
                )

        else:
            lines.append(
                "• No major areas currently detected."
            )

        lines.extend([
            "",
            "💡 Recommendation:",
            report["recommendation"],
            ""
        ])

        return "\n".join(lines)

    @staticmethod
    def _factor_label(score):

        if score >= 80:
            return "Strong"

        if score >= 60:
            return "Good"

        if score >= 40:
            return "Moderate"

        return "Needs Attention"