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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    """Print all the resources in the machine including money."""
    for key, value in resources.items():
        if key == "money":
            print(f"{key}: ${value}")
        else:
            print(f"{key}: {value}")


def check_resources(order):
    """Takes user's order and check if have enough resources to make the drink.
    Returns order ingredients, order cost and the feedback message if not enough resources."""
    order_ingredients = MENU[order]["ingredients"]
    cost = MENU[order]["cost"]
    message = ""
    if order_ingredients["water"] > resources["water"]:
        message = "Sorry there's not enough water."
    elif order_ingredients["coffee"] > resources["coffee"]:
        message = "Sorry there's not enough coffee."
    elif (
        "milk" in order_ingredients.keys()
        and order_ingredients["milk"] > resources["milk"]
    ):
        message = "Sorry there's not enough milk."

    return cost, order_ingredients, message


def process_coins():
    """Process coins and returns total coins value."""
    coin_types = {
        "quarters": {
            "count": 0,
            "value": 0.25,
        },
        "dimes": {
            "count": 0,
            "value": 0.10,
        },
        "nickles": {
            "count": 0,
            "value": 0.05,
        },
        "pennies": {"count": 0, "value": 0.01},
    }
    print("Please insert coins.")
    for coin in coin_types:
        coin_types[coin]["count"] = int(input(f"How many {coin}?: "))
    # Calculate coins total
    coins_total = 0
    for coin in coin_types:
        coins_total += coin_types[coin]["count"] * coin_types[coin]["value"]
    return coins_total


def make_coffee(order, order_ingredients):
    """Takes user's order and order ingredients, reduces the ingredients from resources,
    prints the feedback message."""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {order} ☕. Enjoy!")


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print_report()
        continue
    elif user_choice == "off":
        is_on = False
        break
    else:
        price, ingredients, message = check_resources(user_choice)
    # If not enough resources to make coffee print message and go to start of the program
    if message:
        print(message)
        continue

    total_coin_value = process_coins()
    if price > total_coin_value:
        print("Sorry that's not enough money. Money refunded")
    elif price == total_coin_value:
        resources["money"] += price
        make_coffee(user_choice, ingredients)
    else:
        resources["money"] += price
        print(f"Here is {total_coin_value % price: .2f} in change.")
        make_coffee(user_choice, ingredients)
