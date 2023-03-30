

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
    "money": 0,
}


def print_report():
    for key, value in resources.items():
        if key == "money":
            print(f"{key}: ${value}")
        else:
            print(f"{key}: {value}")


def check_resources(order):
    order_ingredients = MENU[order]["ingredients"]
    if order_ingredients["water"] > resources["water"]:
        print("Sorry there's not enough water.")
    elif order_ingredients["coffee"] > resources["coffee"]:
        print("Sorry there's not enough coffee.")
    elif "milk" in order_ingredients.keys() and order_ingredients["milk"] > resources["milk"]:
        print("Sorry there's not enough milk.")
    else:
        return MENU[order]["cost"], order_ingredients


def process_coins():
    coin_types = {
        "quarters": {
            "count": 0,
            "value": .25,
        },
        "dimes": {
            "count": 0,
            "value": .10,
        },
        "nickles": {
            "count": 0,
            "value": .05,
        },
        "pennies": {
            "count": 0,
            "value": .01
        },
    }
    for coin in coin_types:
        coin_types[coin]["count"] = int(input(f"How many {coin}?: "))
    # Calculate coins total
    coins_total = 0
    for coin in coin_types:
        coins_total += coin_types[coin]["count"] * coin_types[coin]["value"]
    return coins_total


def make_coffee(order, order_ingredients):
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
        price, ingredients = check_resources(user_choice)

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




