# Exercise 1: Odd or Even
# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.

number = int(input()) # Which number do you want to check?

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


# Exercise 2: Leap Year
# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.

# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# Exercise 3: FizzBuzz
# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# The code needs to print the solution to the FizzBuzz game.

# Your program should print each number from 1 to x where x is the input number.

# However when the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)