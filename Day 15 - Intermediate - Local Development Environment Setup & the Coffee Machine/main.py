from art import coffee_logo
from replit import clear

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

# Constants for coin values
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

def print_report() -> None:
    """Prints the current resources and money in the machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def ask_again():
    """Asks the user if they would like to order another drink."""
    choice = input("Would you like to order another drink? Yes/No: ").lower()
    if choice == "yes":
        clear()
    else:
        print("Thank you for using the Coffee Machine. Have a great day!")
        clear()

def check_resource(prompt: str) -> bool:
    """Checks if there are sufficient resources to make the selected drink."""
    for item in MENU[prompt]["ingredients"]:
        if MENU[prompt]["ingredients"][item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins() -> float:
    """Prompts the user to insert coins and calculates the total monetary value."""
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return 0.0
    return quarters * QUARTER + dimes * DIME + nickels * NICKEL + pennies * PENNY

def transaction(total: float, prompt: str) -> bool:
    """Handles the monetary transaction for the selected drink."""
    cost = MENU[prompt]["cost"]
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    global money
    money += cost
    change = total - cost
    if change > 0:
        print(f"Here is ${round(change, 2)} in change.")
    return True

def deduct_resources(prompt: str) -> None:
    """Deducts the required resources for the selected drink."""
    for item in MENU[prompt]["ingredients"]:
        resources[item] -= MENU[prompt]["ingredients"][item]

def CoffeeMachine() -> None:
    """The main function that runs the coffee machine."""
    machine_runs = True

    while machine_runs:
        print(coffee_logo)
        print("Welcome to the Coffee Machine!")
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if prompt == "report":
            print_report()
            ask_again()
        elif prompt == "off":
            machine_runs = False
        elif prompt in MENU:
            if check_resource(prompt):
                total = process_coins()
                if transaction(total, prompt):
                    deduct_resources(prompt)
                    print(f"Here is your {prompt} ☕. Enjoy!")
                    ask_again()
                else:
                    ask_again()
                    
        else:
            print("Invalid selection. Please choose a valid option.")
            ask_again()

CoffeeMachine()