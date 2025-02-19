# # Coding Exercise 1

# # 🚨 Don't change the code below 👇
# from numpy import average


# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# # we can't use len() or sum() functions

# total_height = 0
# num_height = 0
# for height in student_heights:
#   total_height += height
#   num_height += 1
# average_height = round(total_height / num_height)
# print(average_height)

# # Coding Exercise 2

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# # We can use the max() function here, same s the purpose of min() function but in reverse need to find the lowest score

# max_score = 0

# for score in student_scores:
#   if score > max_score:
#     max_score = score

# print(f"The highest score in the class is: {max_score}")

# # Coding exercise 3

# sum = 0
# for num in range(1, 101):
#   if num % 2 == 0:
#     sum += num

# print(f"The sum of all even numbers from 1 to 100 is: {sum}")

# or

# sum = 0
# for num in range(2, 101, 2):
#   sum += num

# print(f"The sum of all even numbers from 1 to 100 is: {sum}") 

# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

# Example Input 1
# 10
# Example Output 1
# 30

# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇
# even_sum = 0
# for n in range(2, target + 1, 2):
#   even_sum += n

# print(even_sum)

# Coding Exercise 4

for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)