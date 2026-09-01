from src.data.personality_traits import PERSONALITY_TRAITS


class CareerProfile:
    """Blueprint for every career in SkillVerse.

    Every career should follow this structure.
    """

    def __init__(
            self,
            name,
            description,
            recommendation_reason,
            ideal_for,
            daily_tasks,
            skills,
            programming_languages,
            tools,
            university_subjects,
            career_paths,
            roadmap,
            beginner_projects,
            pros,
            challenges,
            remote_work,
            future_demand,
            salary,
            related_careers,
            learning_resources,
            ideal_profile,

            required_traits=None,

            ):

        self.name = name
        self.description = description
        self.recommendation_reason = recommendation_reason
        self.ideal_for = ideal_for
        self.daily_tasks = daily_tasks
        self.skills = skills
        self.programming_languages = programming_languages
        self.required_traits = required_traits or {}
        self.tools = tools
        self.university_subjects = university_subjects
        self.career_paths = career_paths
        self.roadmap = roadmap
        self.beginner_projects = beginner_projects
        self.pros = pros
        self.challenges = challenges
        self.remote_work = remote_work
        self.future_demand = future_demand
        self.salary = salary
        self.related_careers = related_careers
        self.learning_resources = learning_resources
        self.ideal_profile = ideal_profile

        self.validate()

    def validate(self):
        """Validate the structural integrity of the career profile."""

        required_lists = [
            self.skills,
            self.career_paths,
            self.roadmap,
            self.programming_languages
        ]

        for item in required_lists:
            if not item:
                raise ValueError(
                    "Career profile contains empty required fields."
                )

        # --------------------------------------------------
        # Required Traits Validation
        # --------------------------------------------------

        if not isinstance(self.required_traits, dict):
            raise ValueError(
                "Career profile required_traits must be a dictionary."
            )

        if not self.required_traits:
            raise ValueError(
                "Career profile must define required_traits."
            )

        canonical_trait_ids = {
            trait["id"]
            for trait in PERSONALITY_TRAITS
        }

        for trait_id, importance in self.required_traits.items():

            if not isinstance(trait_id, str):
                raise ValueError(
                    "Career trait IDs must be strings."
                )

            if trait_id not in canonical_trait_ids:
                raise ValueError(
                    f"Unknown career trait: '{trait_id}'. "
                    "Trait must exist in PERSONALITY_TRAITS."
                )

            if not isinstance(importance, (int, float)):
                raise ValueError(
                    f"Importance for '{trait_id}' must be numeric."
                )

            if not 1 <= importance <= 5:
                raise ValueError(
                    f"Importance for '{trait_id}' must be between 1 and 5."
                )
        # --------------------------------------------------
        # Ideal Profile Validation
        # --------------------------------------------------

        if not isinstance(self.ideal_profile, dict):
            raise ValueError(
                "Career ideal profile must be a dictionary."
            )

        required_categories = {
            "personality",
            "thinking_style",
            "work_style",
            "interests"
        }

        if set(self.ideal_profile.keys()) != required_categories:
            raise ValueError(
                "Career ideal profile must contain personality, "
                "thinking_style, work_style, and interests."
            )

        canonical_trait_ids = {
            trait["id"]
            for trait in PERSONALITY_TRAITS
        }

        for category, traits in self.ideal_profile.items():

            if not isinstance(traits, dict):
                raise ValueError(
                    f"Ideal profile category '{category}' "
                    "must be a dictionary."
                )

            for trait_id, score in traits.items():

                if trait_id not in canonical_trait_ids:
                    raise ValueError(
                        f"Unknown ideal profile trait: '{trait_id}'."
                    )

                if not isinstance(score, (int, float)):
                    raise ValueError(
                        f"Ideal profile score for '{trait_id}' "
                        "must be numeric."
                    )

                if not 1 <= score <= 5:
                    raise ValueError(
                        f"Ideal profile score for '{trait_id}' "
                        "must be between 1 and 5."
                    )