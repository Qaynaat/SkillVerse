from src.core.engine.career_guidance_engine import (
    CareerGuidanceEngine
)


print("=" * 60)
print("MISSION 108 - CAREER GUIDANCE ENGINE")
print("=" * 60)


engine = CareerGuidanceEngine()


# ==================================================
# HIGH ALIGNMENT
# ==================================================

high_alignment = {
    "career": "Cybersecurity",
    "alignment": 88.33,
    "strong_traits": [
        "logical_thinking",
        "curiosity"
    ],
    "growth_areas": [
        "communication"
    ]
}

result = engine.generate_guidance(high_alignment)

print()
print("High Alignment")
print("-" * 40)

print(result["guidance"])

assert result["career"] == "Cybersecurity"
assert result["alignment"] == 88.33
assert "Cybersecurity" in result["guidance"]
assert "logical_thinking" in result["strengths"]
assert "curiosity" in result["strengths"]
assert "communication" in result["growth_areas"]

assert len(result["next_steps"]) > 0
assert result["next_steps"][0] == (
    "Practice explaining technical ideas clearly "
    "and confidently."
)

# ==================================================
# MEDIUM ALIGNMENT
# ==================================================

medium_alignment = {
    "career": "Software Engineering",
    "alignment": 70,
    "strong_traits": [
        "logical_thinking"
    ],
    "growth_areas": [
        "communication"
    ]
}

result = engine.generate_guidance(medium_alignment)

print()
print("Medium Alignment")
print("-" * 40)

print(result["guidance"])

assert result["career"] == "Software Engineering"
assert result["alignment"] == 70
assert "Software Engineering" in result["guidance"]


# ==================================================
# LOW ALIGNMENT
# ==================================================

low_alignment = {
    "career": "AI Engineering",
    "alignment": 45,
    "strong_traits": [],
    "growth_areas": [
        "mathematical_thinking"
    ]
}

result = engine.generate_guidance(low_alignment)

print()
print("Low Alignment")
print("-" * 40)

print(result["guidance"])

assert result["career"] == "AI Engineering"
assert result["alignment"] == 45

# Byte should guide the student,
# not tell them they cannot pursue the career.
assert "you can't pursue" not in result["guidance"].lower()

# ==================================================
# EMPTY GROWTH AREAS
# ==================================================

perfect_alignment = {
    "career": "Web Development",
    "alignment": 100,
    "strong_traits": [
        "creative_thinking",
        "building"
    ],
    "growth_areas": []
}

result = engine.generate_guidance(perfect_alignment)

assert result["career"] == "Web Development"
assert result["alignment"] == 100
assert len(result["next_steps"]) > 0


print()
print("All Mission 108 Career Guidance tests passed.")
print("=" * 60)