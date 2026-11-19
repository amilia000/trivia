Trivia: Quizzes from Oz
Project Overview

This project is a command-line multiple-choice trivia game. Players answer questions one at a time, get instant feedback on each answer, and see their final score at the end. The application stores quiz questions and high scores in lists of dictionaries, uses loops to move through the questions and menu, and saves high scores to a JSON file so they are still there the next time the game is played.

Key Features & Usage Example

After running the application, the user is presented with a menu of options. They can:

Start a quiz
View the high scores
Exit the application

When a quiz starts, each question is shown with four numbered choices. After every answer, the player is told whether they were correct
or incorrect and sees their running score. When the quiz is over, the player sees their final score and percentage. If the score makes the top 5, the player is asked for their name and the score is added to the leaderboard with the date.

Question 1: In the movie Titanic how did Jack die?
1) flu
2) froze
3) drowned
4) shot

Enter your answer (1-4): 2
Correct! Well done!
Current Score: 1/1 (100%)

Invalid input (letters, an empty answer, or a number outside 1-4) shows a helpful message and asks again instead of crashing.


Setup

Follow these steps to get started:


git clone <your-repository-url>
cd <your-repository-folder>

# Create a virtual environment in a folder named .venv, then turn it on
python3 -m venv .venv
source .venv/bin/activate

# install pytest into the virtual environment
pip install pytest

# Run the application
python3 src/main.py

# If you need to end the program abruptly, use Control+C

On Windows, turn the virtual environment on with .venv\Scripts\activate and use python instead of python3 if python3 is not found.

A virtual environment is a folder that holds its own copy of Python and the project's own installed packages, so the packages you install for this project do not affect any other project on your computer. 
The source .venv/bin/activate command turns the virtual environment on for the current terminal window only. When the virtual environment is on, your terminal prompt begins with (.venv).

Each time you open a new terminal window to work on this project, run source .venv/bin/activate again from the project folder. To turn the virtual environment off, run deactivate.

The application itself needs no third-party packages, because it only uses Python's built-in input() and print() functions and the standard library. The only package you install is pytest, which runs the tests.



Project Structure
src/
  main.py        # entry point: welcome and goodbye messages
  menu.py        # the menu loop and the quiz flow
  quiz_data.py   # the questions, the high scores, and saving/loading scores

tests/
  test_quiz_data.py   # tests for the data layer
high_scores.json     # created automatically after the first saved score
Running Tests

With the virtual environment turned on, run this command from the project folder:

pytest

The pytest command finds the test files in the tests folder and runs every function whose name begins with test_. These tests check that the functions in src/quiz_data.py behave as desired.

Add -v to the command (pytest -v) to see the name of each test and whether it passed.

Key Technologies & Packages

Python 3
input() and print() from the built-in functions
The datetime module from the standard library (for the date on each high score)
The json module from the standard library (for saving and loading high scores)
pytest