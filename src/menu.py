from quiz_data import start_quiz, questions, high_scores, load_high_scores, view_scores


def show_menu():
    load_high_scores()
    while True:
        print("\nMenu:\n")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Exit")

        option = input("\nChoose an option (Enter 1-3): ").strip()
        if option == "1":
            start_quiz()
        elif option == "2":
            print("\nHighscores:")
            view_scores()
        elif option == "3":
            break
        else:
            print("Invalid choice. Please try again")


# print("You chose: " + option)
# print("High scores coming soon!")
