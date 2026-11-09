import datetime
from quiz_data import questions, high_scores


def show_menu():
    while True:
        print("Menu:")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Exit")

        option = input("Choose an option (Enter 1-3): ").strip()
        if option == "1":
            score = 0
            total = len(questions)

            for q in questions:
                # print each question with a number
                print(q["question"])
                # gives you a number and a text choice together
                for i, choice in enumerate(q["choices"], start=1):
                    print(f"{i}) {choice}")
                # turns the typed text into a number.
                answer = int(input("Enter your answer (1-4): "))
                # converts the user’s 1-4 into the 0-3 that answer_index uses.
                if answer - 1 == q["answer_index"]:
                    score = score + 1  # is where score = 0 gets used.
                    print("Correct! Well done!")
                else:
                    print("Wrong!")
            percent = round(score / total * 100)
            print("\nQuiz Complete!")
            print(f"Final Score: {score}/{total} ({percent}%)")
            print("Thanks for playing!")
            # .strftime turns the date or time a str in the format you choose.
            today = datetime.date.today().strftime("%m/%d/%y")
            name = input("Enter your name: ").strip()
            # .append puts a new item at the end of a list.
            high_scores.append({"name": name, "score": percent, "date": today})
        elif option == "2":
            print("\nHighscores:")
            for entry in high_scores:
                print(entry["name"], entry["score"], entry["date"])
        elif option == "3":
            break
        else:
            print("Invalid choice. Please try again")


# print("You chose: " + option)
# print("High scores coming soon!")
