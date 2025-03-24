from replit import clear
from art import logo, vs
from game_data import data
import random

print(logo)
score = 0

def higher_lower():
    """Plays the Higher Lower Game.

    The game compares two randomly selected items from a dataset (`data`) and asks the user to guess 
    which item has more followers. The user inputs their choice ('A' or 'B'), and the game checks 
    if the guess is correct. The score is incremented for correct guesses, and the game continues 
    until the user makes an incorrect guess. The final score is displayed when the game ends.

    Global Variables:
    - score (int): Tracks the user's current score.

    External Dependencies:
    - `data` (list of dict): A dataset containing items with attributes such as "name", 
      "description", "country", and "follower_count".
    - `vs` (str): A string or graphic used to visually separate the two items being compared.
    - `logo` (str): A string or graphic representing the game's logo.
    - `clear` (function): A function to clear the console output.

    Input:
    - User types 'A' or 'B' to indicate their guess.

    Output:
    - Prints the comparison details, feedback on the user's guess, and the current or final score.
    Higher Lower Game
    """
    global score
    play_game = True
    while play_game:
        A = random.choice(data)
        B = random.choice(data)
        if A == B:
            B = random.choice(data)
        print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}")
        print(vs)
        print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        greater_followers = A if A["follower_count"] > B["follower_count"] else B
        if choice == "a" and A == greater_followers:
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
        elif choice == "b" and B == greater_followers:
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            play_game = False
    
    
higher_lower()
play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
while play_again == "yes":
    score = 0
    clear()
    print(logo)
    higher_lower()
    play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()