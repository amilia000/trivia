def show_menu():
    while True:
        print("Menu:")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Exit")

        option = input("Choose an option (Enter 1-3)").strip()
        if option == "1":
            print("Quiz coming soon!")
        elif option == "2":
            print("High scores coming soon!")
        elif option == "3":
            break
        else:
            print("Invalid choice. Please try again")


# print("You chose: " + option)
