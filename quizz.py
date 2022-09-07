import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "What was Meta Platforms Inc formerly known as": [
        "Facebook", "Google", "Apple", "Dell"
    ],
    "Which English city is known as the Steel City": [
        "Sheffield", "London", "Manchester", "Liverpool"
    ],
    "Which former British colony was given back to China in 1997": [
        "Hong Kong", "Shanghai", "Beijing", "Wuhan"
    ],
    "The logo for luxury car maker Porsche features which animal": [
        "Horse", "Goat", "Eagle", "Snake"
    ],
    "Which element is said to keep bones strong": [
        "Calcium", "Chromium", "Titanium", "Helium"
    ]
}


def run_quizz():
    # Preprocess
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    # Process (main loop)
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    # Postprocess
    print(f"\nYou got {num_correct} correct out of {num} questions")


def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("* Correct! *")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0



def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"   {label})  {alternative}")

    while (answer_label := input("\nChoice?")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


if __name__ == "__main__":
    run_quizz()