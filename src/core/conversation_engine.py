from src.core.intent import Intent


class ConversationEngine:

    INTENT_KEYWORDS = {

        Intent.ASK_SKILLS: [
            "skill",
            "skills",
            "learn",
            "study",
            "required"
        ],

        Intent.ASK_CAREER_PATHS: [
            "job",
            "jobs",
            "career path",
            "career paths",
            "role",
            "roles"
        ],

        Intent.ASK_FUTURE_DEMAND: [
            "future",
            "demand",
            "scope",
            "salary"
        ],

        Intent.ASK_DESCRIPTION: [
            "describe",
            "description",
            "overview",
            "details",
            "detail",
            "more information",
            "information"
        ],

        Intent.INTRODUCE_CAREER: [
            "tell me about",
            "introduce",
            "what is",
            "explain"
        ],

        Intent.ASK_PROGRAMMING_LANGUAGES: [
            "language",
            "languages",
            "programming language",
            "programming languages",
            "coding language",
            "python",
            "java",
            "c++",
            "javascript"

        ],

        Intent.ASK_TOOLS: [
            "tool",
            "tools",
            "software",
            "software used",
            "applications",
            "application",
            "ide",
            "editor",
            "vs code",
            "pycharm",
            "git"

        ]
    }

    def detect_intent(self, message: str):

        message = message.lower()

        matched_intents = []

        for intent, keywords in self.INTENT_KEYWORDS.items():

            for keyword in keywords:

                if keyword in message:
                    matched_intents.append(intent)

        if not matched_intents:
            return Intent.UNKNOWN

        best_intent = min(
            matched_intents,
            key=lambda intent: INTENT_PRIORITY[intent]
        )

        return best_intent
    
INTENT_PRIORITY = {

    Intent.ASK_SKILLS: 2,

    Intent.ASK_CAREER_PATHS: 2,

    Intent.ASK_PROGRAMMING_LANGUAGES: 2,

    Intent.ASK_TOOLS: 1,


    Intent.ASK_FUTURE_DEMAND: 3,

    Intent.ASK_DESCRIPTION: 4,

    Intent.INTRODUCE_CAREER: 5,

    Intent.UNKNOWN: 999

}