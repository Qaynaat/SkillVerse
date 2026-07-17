from dataclasses import dataclass, field
from typing import List


@dataclass
class PersonalityProfile:

    # Identity
    name: str
    avatar_key: str

    # Personality
    primary_tone: str
    secondary_traits: List[str]

    communication_style: str
    formality: str

    # Conversation
    greeting_style: str
    closing_style: str
    celebration_style: str

    # Mentoring
    support_style: str
    struggle_reaction: str
    humility_style: str
    analogy_theme: List[str]

    # Style
    emoji_style: str
    playfulness: str
    response_length: str

    # Values
    core_values: List[str] = field(default_factory=list)