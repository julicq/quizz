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

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label} - {alternative}")

    while(answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")