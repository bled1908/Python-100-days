# # Coding exercise 1

# import random

# choice = random.randint(0, 1)
# if choice == 0:
#     print("Heads")
# else:
#     print("Tails")

# or

# import random

# random_number = random.randint(0,1)
# print("Heads" if random_number == 1 else "Tails")

# # Coding Exercise 2

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# import random

# print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")
# # we can replace {names[random.randint(0, len(names) - 1)]} with random.choice(names)
# or
# import random
# len_names = len(names)
# print("{} is going to buy the meal today!".format(names[random.randint(0, len_names - 1)]))

# Coding exercise 3 - Treasure Map

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

map[int(position[1]) - 1][int(position[0]) - 1] = "X"
# we can also do
# horizontal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# if
# Example Input 1
# B3
# Example Output 1
# Hiding your treasure! X marks the spot.
# ['⬜️', '️⬜️', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', 'X', '⬜️️']

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input("Where do you want to put the treasure?: ")
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# row = int(position[1])
# column = 0 if position[0] == "A" else 1  if position[0] == "B" else 2
# map[row - 1][column] = "X"
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")