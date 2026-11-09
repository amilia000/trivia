import datetime

questions = [
    {
        "question": "In the movie Titanic how did Jack die?",
        "choices": ["flu", "froze", "drowned", "shot"],
        "answer_index": 1,
    },
    {
        "question": "What is Hulk from Avengers real name? ",
        "choices": ["David Bruce", "Bruce Banner", "David Green", "Tony Stark"],
        "answer_index": 1,
    },
    {
        "question": "In Mean Girls what day does Amanda say everyone should wear pink?",
        "choices": ["Friday", "Monday", "Wednesday", "Tuesday"],
        "answer_index": 2,
    },
    {
        "question": "Who lives on Drury Lane in the movie Shrek?",
        "choices": ["Gingerbread man", "Fiona", "Muffin man", "Shrek"],
        "answer_index": 2,
    },
]
high_scores = []


def start_quiz():
    score = 0
    total = len(questions)

    for q in questions:
        # print each question with a number
        print(q["question"])
        # gives you a number and a text choice together
        for i, choice in enumerate(q["choices"], start=1):
            print(f"{i}) {choice}")

        # loop for getting the answer
        # turns the typed text into a number.
        while True:
            answer = input("Enter your answer (1-4): ")
            try:
                answer = int(answer)
                if 1 <= answer <= 4:
                    if answer - 1 == q["answer_index"]:
                        score = score + 1  # is where score = 0 gets used.
                        print("Correct! Well done!")
                    else:
                        print("Wrong!")

                    break
                else:
                    print("Please enter a number from 1 to 4.")
            except ValueError:
                print("Invalid choice. Please try again")
                # converts the user’s 1-4 into the 0-3 that answer_index uses.

    # game over
    percent = round(score / total * 100)
    print("\nQuiz Complete!")
    print(f"Final Score: {score}/{total} ({percent}%)")
    print("Thanks for playing!")
    # .strftime turns the date or time a str in the format you choose.
    today = datetime.date.today().strftime("%m/%d/%y")
    name = input("Enter your name: ").strip()
    # .append puts a new item at the end of a list.
    high_scores.append({"name": name, "score": percent, "date": today})


def view_scores():
    high_scores.sort(key=get_score, reverse=True)
    for entry in high_scores:
        print(f"{entry['name']} {entry['score']}%, {entry['date']}")


def get_score(entry):
    return entry["score"]
