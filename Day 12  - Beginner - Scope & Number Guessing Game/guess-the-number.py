#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from replit import clear
from art import logo
import random

def game():
    """Number Guessing Game Function 
    This function is the main function that runs the game.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            attempts -= 1
        elif guess < number:
            print("Too low.")
            attempts -= 1
        else:
            print(f"You got it! The answer was {number}.")
            take_decision()
        
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            take_decision()
            
def take_decision():
    """Take Decision Function
    This function asks the user if they want to play again.
    """
    decision = input("Do you want to play a game? Type 'yes' or 'no': ")
    if decision == "yes":
        clear()
        game()
    else:
        print("Goodbye.")

game()