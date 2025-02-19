# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇

# import random

# choice = [rock, paper, scissors]
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if (0 <= user_choice <= 2):
#     print(choice[user_choice])

#     computer_choice = random.randint(0, 2)
#     print("Computer chose:\n", choice[computer_choice])

#     if((user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0)):
#         print("You Lose!")
#     elif((user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1)):
#         print("You Win!")
#     elif(user_choice == computer_choice):
#         print("It's a tie!")
# else:
#     print("Invalid Choice!")
    
# or

# import random

# # ASCII art for choices
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# # List of choices
# choices = [rock, paper, scissors]

# print("Welcome to Rock, Paper, Scissors!")
# print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

# # Get user input
# try:
#     user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
#     if user_choice < 0 or user_choice > 2:
#         print("Invalid choice! Please choose 0, 1, or 2.")
#     else:
#         # Show user choice
#         print("You chose:\n", choices[user_choice])

#         # Computer choice
#         computer_choice = random.randint(0, 2)
#         print("Computer chose:\n", choices[computer_choice])

#         # Determine winner
#         if user_choice == computer_choice:
#             print("It's a tie!")
#         elif (user_choice - computer_choice) % 3 == 1:
#             print("You Win!")
#         else:
#             print("You Lose!")
# except ValueError:
#     print("Invalid input! Please enter a number (0, 1, or 2).")


# Angela Yu Solution

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: ")
    print(game_images[computer_choice])

    
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!") 
