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

def check_resource(prompt):
    """
    Checks if there are sufficient resources to make the selected drink.

    Iterates through the ingredients of the selected drink from the MENU and 
    compares the required amount with the available resources. If any resource 
    is insufficient, it prints a message indicating the shortage and returns False. 
    Otherwise, it returns True.
    
    Args:
        prompt (str): The name of the drink selected by the user.
        bool: True if resources are sufficient to make the drink, False otherwise.
    Raises:
        KeyError: If the selected drink is not found in the MENU.

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
    for item in MENU[prompt]["ingredients"]:
        if MENU[prompt]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

money = 0

def process_coins():
    """
    Prompts the user to insert coins and calculates the total monetary value.

    Asks the user for the number of quarters, dimes, nickels, and pennies they are inserting.
    Calculates the total value based on the coin denominations and returns the total.

    Returns:
        float: The total monetary value of the inserted coins.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total

def transaction(total, prompt):
    """
    Handles the monetary transaction for the selected drink.

    Compares the total amount of money inserted by the user with the cost of the selected drink.
    If the inserted money is less than the cost, it prints a message and refunds the money.
    If the inserted money is sufficient, it adds the cost of the drink to the machine's money,
    calculates the change to be returned, and prints the change amount.

    Args:
        total (float): The total monetary value inserted by the user.
        prompt (str): The name of the drink selected by the user.

    Returns:
        bool: True if the transaction is successful, False otherwise.
    """
    if total < MENU[prompt]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total >= MENU[prompt]["cost"]:
        global money
        money += MENU[prompt]["cost"]
        change = total - MENU[prompt]["cost"]
        print(f"Here is ${round(change, 2)} in change.")
        return True

def CoffeeMachine():
    """
    The main function that runs the coffee machine.

    The function prompts the user for the drink they would like to order.
    If the user enters 'report', it prints the current resources of the machine.
    If the user enters 'off', it turns off the machine.
    If the user enters a drink, it checks the resources, processes the coins, and handles the transaction
    for the selected drink.
    """
    machine_runs = True

    while machine_runs:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if prompt == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif prompt == "off":
            machine_runs = False
        else:
            if check_resource(prompt):
                total = process_coins()
                if transaction(total, prompt):
                    for item in MENU[prompt]["ingredients"]:
                        resources[item] -= MENU[prompt]["ingredients"][item]
                    print(f"Here is your {prompt} ☕. Enjoy!")
            
CoffeeMachine()        
