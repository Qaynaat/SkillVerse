class SmartReminderEngine:

    def generate_reminder(self, memory):

        progress = memory.get_progress()

        xp = progress.get("current", 0)

        missions = memory.get_completed_missions()

        if missions == 0:

            reminder = (
                "🌱 Start your SkillVerse journey today. "
                "Complete your first mission and begin building momentum."
            )

            priority = "high"

        elif xp < 100:

            reminder = (
                "📚 Time to continue your learning journey! "
                "Complete one mission today to build momentum."
            )

            priority = "high"

        elif xp < 300:

            reminder = (
                "🚀 You're making great progress! "
                "Finish one mission today and maintain your consistency."
            )

            priority = "medium"

        elif xp < 600:

            reminder = (
                "🔥 You're building strong momentum! "
                "Continue your current learning path and challenge yourself."
            )

            priority = "medium"

        else:

            reminder = (
                "🏆 You're doing amazing! "
                "Challenge yourself with an advanced mission today."
            )

            priority = "low"

        return {
            "xp": xp,
            "missions_completed": missions,
            "priority": priority,
            "reminder": reminder
        }

    def should_send_reminder(self, memory):

        result = self.generate_reminder(memory)

        return result["missions_completed"] >= 0

    def generate_context_reminder(
        self,
        memory,
        current_goal=None
    ):

        result = self.generate_reminder(memory)

        reminder = result["reminder"]

        if current_goal:

            reminder += (
                f"\n\n🎯 Current Goal: {current_goal}"
            )

        result["reminder"] = reminder

        return result