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

user_prompt = input("What would you like? (espresso/latte/cappuccino): ")

# TODO: 1. Print report - print all the resources in the machine including any money when user prompt "report"
if user_prompt == "report":
    for key, value in resources.items():
        print(f"{key}: {value}")

# TODO: 2. If user prompt is 'off' exit the program


# TODO: 3. Check if resources are sufficient to make the drink


# TODO: 4. Process coins. quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01


# TODO: 5. Check transaction successful, if enough coin make drink and add to profit else refund coins


# TODO: 6. Make coffee, ff transaction successful make coffee and deduct ingredients form resources


