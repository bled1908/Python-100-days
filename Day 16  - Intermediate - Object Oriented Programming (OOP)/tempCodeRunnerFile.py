from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

choice = input(f"What would you like? ({menu.get_items()}): ")
if choice == "off":
    exit()
elif choice == "report":
    coffee_maker.report()
    money_machine.report()
else:
    drink = menu.find_drink(choice)
    if is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)