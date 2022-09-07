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
    for alternative in sorted(alternatives):
        print(f"   - {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")