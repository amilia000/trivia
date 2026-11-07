from menu import show_menu


# This is the main entry point for the application.
def start_app():
    print("Welcome to Trivia!")
    show_menu()
    print("\nThanks for playing, goodbye!")


if __name__ == "__main__":
    start_app()
