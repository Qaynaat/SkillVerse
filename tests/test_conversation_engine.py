from src.core.conversation_engine import ConversationEngine
from src.core.intent import Intent

engine = ConversationEngine()

messages = [

    "Tell me about Software Engineering",

    "Explain Cybersecurity",

    "Describe AI Engineering",

    "What skills should I learn?",

    "Which abilities are required?",

    "What jobs can I get?",

    "Which roles are available?",

    "How is the future demand?",

    "What is the salary?",

    "Explain the skills required for Cybersecurity",

    "Tell me about the future demand of AI Engineering",

    "Hello Byte!",

    "Good morning!",

    "Thank you!"
]

for message in messages:
    print(f"{message}")
    print(engine.detect_intent(message))
    print("-" * 50)