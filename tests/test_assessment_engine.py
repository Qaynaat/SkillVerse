from src.core.engine.assessment_engine import AssessmentEngine

print("=" * 60)
print("MISSION 017 - ASSESSMENT ENGINE TEST")
print("=" * 60)

engine = AssessmentEngine()

questions = [
    {
        "id": "logical",
        "question": "Do you enjoy solving problems?"
    },
    {
        "id": "creative",
        "question": "Do you enjoy designing things?"
    }
]

engine.load_questions(questions)

while not engine.is_finished():

    question = engine.get_current_question()

    print()
    print(question["question"])

    engine.submit_answer(question["id"], 5)

    engine.next_question()

print()
print("Answers")
print("-" * 40)
print(engine.get_answers())

print()
print("=" * 60)
print("TEST FINISHED")
print("=" * 60)