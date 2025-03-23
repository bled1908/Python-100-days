from replit import clear
from art import logo, vs
from game_data import data
import random

print(logo)
score = 0

def higher_lower():
    global score
    play_game = True
    while play_game:
        A = random.choice(data)
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