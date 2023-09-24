
# Python Multiple Choice Quiz
print("""Objective: The objective of the game is to answer a series of multiple-choice questions correctly and accumulate points.

Questions: The game consists of a predefined set of 10 multiple-choice questions.



Scoring:

Each correct answer earns the player one point.
Incorrect answers do not result in point deductions.
Feedback: After each question, the game provides feedback on whether the answer was correct or incorrect.

End of Game: The game ends after all 10 questions have been answered.

Final Score: The game displays the player's final score out of 10 at the end.


Restart: Players can choose to restart the game if they wish to play again.

Have Fun: The primary goal of the game is to have fun and test your knowledge of Python and general trivia.

""")

# Initialize the score
score = 0

# Define the questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Madrid", "Paris"],
        "answer": "Paris"
    },
    {
        "question": "Which of the following is not a programming language?",
        "options": ["Python", "Java", "HTML", "Bicycle"],
        "answer": "Bicycle"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What does 'HTML' stand for?",
        "options": ["Hyper Text Markup Language", "Highly Technical Markup Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which of the following is a Python framework for web development?",
        "options": ["Django", "Node.js", "Ruby on Rails", "Angular"],
        "answer": "Django"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Which programming language is known for its use in data analysis and statistics?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": "Python"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Au", "Ag", "Fe"],
        "answer": "Au"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Mars", "Venus", "Jupiter", "Mercury"],
        "answer": "Mars"
    }
]

# Function to display a question and get the user's answer
def ask_question(question_obj):
    print(question_obj["question"])
    for i, option in enumerate(question_obj["options"], start=1):
        print(f"{i}. {option}")
    user_answer = input("Enter the number corresponding to your answer: ")
    return question_obj["options"][int(user_answer) - 1]

# Iterate through the questions
for question in questions:
    user_choice = ask_question(question)
    if user_choice == question["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['answer']}\n")

# Display the final score
print(f"Your score is: {score}/{len(questions)}")
play_again = input("Do you want to play again? (yes/no): ").strip().lower()
if play_again != "yes":


    # Reset the score for a new game
    score = 0

print("Thank you for playing!")