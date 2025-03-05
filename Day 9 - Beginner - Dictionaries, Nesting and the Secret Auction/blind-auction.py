# from art import logo
# from replit import clear
# #HINT: You can call clear() to clear the output in the console.

# print(logo)

# decision = "yes"
# bidders = {}
# while decision == "yes":
#     name = input("What is your name? ")
#     bid = int(input("What is your bid? $"))
#     decision = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
#     bidders[name] = bid
#     clear()

# highest_bid = 0
# highest_bidder = ""
# for bidder in bidders:
#     if bidders[bidder] > highest_bid:
#         highest_bid = bidders[bidder]
#         highest_bidder = bidder
        
# print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

import time
from art import logo
from replit import clear
# HINT: You can call clear() to clear the output in the console.

print(logo)

def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            highest_bidder = bidder
    return highest_bidder, highest_bid

decision = "yes"
bidders = {}
while decision == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    decision = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    bidders[name] = bid
    clear()

while True:
    highest_bidder, highest_bid = find_highest_bidder(bidders)
    print(f"The current highest bid is ${highest_bid} by {highest_bidder}.")
    
    for i in range(1, 4):
        print(f"{i}...")
        time.sleep(1)
        decision = input("Does anyone want to bid higher? Type 'yes' or 'no' ").lower()
        if decision == "yes":
            name = input("What is your name? ")
            bid = int(input("What is your bid? $"))
            bidders[name] = bid
            clear()
            break
    else:
        break

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")