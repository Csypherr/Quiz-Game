#====================================================================================
#   Author: Mela Bamiji.
#   Date:   25th December, 2023.
#
#   This is a simple quiz game designed for learning purposes only. The concepts
#   employed in this code is meant to put into practice key functionalities of 
#   Python programming language. 
#====================================================================================

def new_game():
    """Start a new game by displaying the questions and answers.""" 

    guesses = []
    correct_guesses = 0
    question_number = 1

    # display questions 
    for key in questions:
        print("----------------------------------------------------------------------")
        print(key)
        # display possible answers
        for i in options[question_number - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ") 
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1
    
    # display scores
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    """Check that the user entered the correct answer or guess."""

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
def display_score(correct_guesses, guesses):
    """Dynamically display the scores to the user."""

    print("----------------------------------------------------------------------")
    print("RESULTS")
    print("----------------------------------------------------------------------")

    # display the answers
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    # display the guesses
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # display the score 
    score = int((correct_guesses / len(questions) * 100))
    print("Your score is: " + str(score) + "%")

def play_again():
    """Ask player to restart the game."""

    response = input("Do you want to play again? (yes or no):") 
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# collection of questions asked 
questions = {
    "Who created Python Programming Language? ": "A",
    "What year was Python Programming Language created? ": "B",
    "Python Programming Language is attributed to which comedy group? ": "C",
    "Is the Earth round? ": "A"
}

# collection of answers
options = [["A. Guido van Rossum", "B. Jeff Bezos", "C. Bill Gates", "D. Elon Musk"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]] 


# prompt user to begin the game 
new_game()

# ask user to play a new game 
while play_again():
    new_game()

# exit message 
print("Goodbye!")