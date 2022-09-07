QUESTIONS = {
    "What was Meta Platforms Inc formerly known as" : [
        "Facebook", "Google", "Apple", "Dell"
    ],
    "Which English city is known as the Steel City" : [
        "Sheffield", "London", "Manchester", "Liverpool"
    ],
    "Which former British colony was given back to China in 1997": [
        "Hong Kong", "Shanghai", "Beijing", "Wuhan"
    ]
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"  {label} - {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")