from src.data.personality_questions import PERSONALITY_QUESTIONS

print("=" * 60)
print("MISSION 020 - PERSONALITY QUESTIONS TEST")
print("=" * 60)

print()
print(f"Total Questions: {len(PERSONALITY_QUESTIONS)}")

print()
print("First Question")
print("-" * 40)
print(PERSONALITY_QUESTIONS[0]["question"])

print()
print("Last Question")
print("-" * 40)
print(PERSONALITY_QUESTIONS[-1]["question"])

print()
print("Categories")
print("-" * 40)

categories = sorted({
    question["category"]
    for question in PERSONALITY_QUESTIONS
})

for category in categories:
    print(category)

print()
print("=" * 60)
print("TEST FINISHED")
print("=" * 60)