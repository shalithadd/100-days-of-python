from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    coffee_menu = Menu()
    coffee_machine = CoffeeMaker()
    transactions = MoneyMachine()
    user_choice = input(f"What would you like? ({coffee_menu.get_items()}): ")

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_machine.report()
        transactions.report()
    else:
        user_order = coffee_menu.find_drink(user_choice)
        coffee_machine.is_resource_sufficient(user_order)
