class CareerGuidanceEngine:
    """Generates supportive career guidance from goal alignment results."""

    def generate_guidance(self, alignment_result):
        career = alignment_result["career"]
        alignment = alignment_result["alignment"]
        strong_traits = alignment_result.get("strong_traits", [])
        growth_areas = alignment_result.get("growth_areas", [])

        # ------------------------------------------
        # Alignment Message
        # ------------------------------------------

        if alignment >= 80:
            guidance = (
                f"{career} looks like a strong direction for you. "
                "You already have several traits that align well with "
                "this career."
            )

        elif alignment >= 60:
            guidance = (
                f"{career} could be a good direction for you. "
                "You have a solid foundation, and developing a few "
                "areas could make this path even stronger."
            )

        else:
            guidance = (
                f"{career} may require you to develop some additional "
                "strengths, but that does not mean you cannot pursue it. "
                "Let's identify what you can build."
            )

        # ------------------------------------------
        # Strength Guidance
        # ------------------------------------------

        strengths = list(strong_traits)

        # ------------------------------------------
        # Growth Areas
        # ------------------------------------------

        growth = list(growth_areas)

        # ------------------------------------------
        # Next Steps
        # ------------------------------------------

        next_steps = []

        for trait in growth_areas:
            next_steps.append(
                self._create_growth_action(trait)
            )

        if not next_steps:
            next_steps.append(
                f"Continue developing skills related to {career}."
            )

        return {
            "career": career,
            "alignment": alignment,
            "guidance": guidance,
            "strengths": strengths,
            "growth_areas": growth,
            "next_steps": next_steps
        }

    def _create_growth_action(self, trait):
        """Create a simple development action for a growth trait."""

        actions = {
            "communication": (
                "Practice explaining technical ideas clearly "
                "and confidently."
            ),
            "logical_thinking": (
                "Practice breaking complex problems into smaller "
                "logical steps."
            ),
            "analytical_thinking": (
                "Practice analysing information and identifying "
                "patterns before making decisions."
            ),
            "creative_thinking": (
                "Practice generating multiple solutions to the "
                "same problem."
            ),
            "curiosity": (
                "Explore unfamiliar topics and ask questions "
                "about how things work."
            ),
            "patience": (
                "Practice staying focused while solving difficult "
                "or time-consuming problems."
            ),
            "resilience": (
                "Treat mistakes as learning opportunities and "
                "keep working through difficult problems."
            ),
            "teamwork": (
                "Practice collaborating with others and sharing "
                "ideas toward a common goal."
            ),
            "independent_work": (
                "Practice taking ownership of tasks and completing "
                "them with minimal supervision."
            ),
            "building": (
                "Start creating small projects to turn ideas "
                "into working solutions."
            ),
            "protecting": (
                "Explore how systems, networks, and information "
                "can be protected."
            ),
            "designing": (
                "Practice creating simple, useful, and "
                "user-friendly experiences."
            )
        }

        return actions.get(
            trait,
            f"Develop your {trait.replace('_', ' ')} through practice."
        )