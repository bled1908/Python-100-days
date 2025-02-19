# # Exercise 1
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# # Exercise 2
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = round(weight / (height ** 2))

# print(f"Your BMI is {bmi}, you ", end = "")
# if bmi <= 18.5:
#     print("are underweight.")
# elif bmi <= 25:
#     print("have a normal weight.")
# elif bmi <= 30:
#     print("are slightly overweight.")
# elif bmi <= 35:
#     print("are obese.")
# else:
#     print("are clinically obese.")

# # Exercise 3
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

    # or

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year.")
# else:
#     print("Not leap year.")

# Exercise 4

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want cheese? Y or N ")

# bill = 0
# if(size == "S"):
#     bill += 15
# elif(size == "M"):
#     bill += 20
# elif(size == "L"):
#     bill += 25

# if(add_pepperoni == "Y") and (size == "M" or size == "L"):
#     bill += 3
# elif(add_pepperoni == "Y"):
#     bill += 2

# if(extra_cheese == "Y"):
#     bill += 1

# print(f"Your final bill is: ${bill}.")

# Exercise 5

print("Welcome to the love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = (name1 + name2).lower()
t_count = name.count("t")
r_count = name.count("r")
u_count = name.count("u")
e_count = name.count("e")
l_count = name.count("l")
o_count = name.count("o")
v_count = name.count("v")
e_count = name.count("e")

# print(f"T occurs {t_count} times")
# print(f"R occurs {r_count} times")
# print(f"U occurs {u_count} times")
# print(f"E occurs {e_count} times")
total_true = t_count + r_count + u_count + e_count
# print(f"Total = {total_true}")

# print(f"L occurs {l_count} times")
# print(f"O occurs {o_count} times")
# print(f"V occurs {v_count} times")
# print(f"E occurs {e_count} times")
total_love = l_count + o_count + v_count + e_count
# print(f"Total = {total_love}")

total = total_true * 10 + total_love
# or 
# total = int(str(total_true) + str(total_love))
print(f"Your Score is {total}.", end = " ")

if(total <= 10 or total >= 90):
    print("you go together like coke and mentos.")
elif(40 <= total <= 50):
    print("you are alright together")