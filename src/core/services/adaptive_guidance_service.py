from src.core.engine.adaptive_guidance_engine import AdaptiveGuidanceEngine


class AdaptiveGuidanceService:
    """
    Service layer for personalized adaptive guidance.

    Connects StudentProfile/progress data with
    AdaptiveGuidanceEngine.
    """

    def __init__(self, guidance_engine=None):
        self.guidance_engine = guidance_engine or AdaptiveGuidanceEngine()

    def generate_guidance(
        self,
        student_profile,
        progress,
        current_goal=None
    ):
        """
        Generate personalized guidance for a student.
        """

        if student_profile is None:
            raise ValueError("Student profile is required.")

        if not isinstance(progress, dict):
            raise ValueError("Progress must be a dictionary.")

        if current_goal is None:
            getter = getattr(student_profile, "get_current_goal", None)

            if callable(getter):
                current_goal = getter()

        guidance = self.guidance_engine.generate_guidance(
            progress,
            current_goal
        )

        guidance["student_profile"] = student_profile

        return guidance

    def get_guidance(
        self,
        student_profile,
        progress,
        current_goal=None
    ):
        """
        Convenience alias for generate_guidance().
        """

        return self.generate_guidance(
            student_profile,
            progress,
            current_goal
        )