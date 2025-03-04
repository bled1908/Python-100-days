# Exercise 1
# Instructions
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 * 4) / 5
#                = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input
# 3
# 9
# Example Output
# You'll need 6 cans of paint.

# Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  result = math.ceil((height * width) / cover)
  print(f"You'll need {result} cans of paint.")



# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercise 2
# Prime numbers
# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.

# Write your code below this line 👇
def prime_checker(number):
  if number < 2:
    print("It's not a prime number.")
    return
    
  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      print("It's not a prime number.")
      return

  print("It's a prime number.")
  return


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

# or

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(number=n)