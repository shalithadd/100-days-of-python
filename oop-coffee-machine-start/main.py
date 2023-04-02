from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_menu = Menu()
coffee_machine = CoffeeMaker()
transactions = MoneyMachine()
while is_on:
    user_choice = input(f"What would you like? ({coffee_menu.get_items()}): ")

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_machine.report()
        transactions.report()
    else:
        user_order = coffee_menu.find_drink(user_choice)
        is_enough_resources = coffee_machine.is_resource_sufficient(user_order)
        if is_enough_resources:
            if transactions.make_payment(user_order.cost):  # pyright:ignore
                coffee_machine.make_coffee(user_order)
