from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)
should_continue = True
new_calculation = True
while should_continue:
    if new_calculation:
        num1 = int(input("What's the first number?: "))

        for symbol in operations:
            print(symbol)

        operator = input("Select the operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operator]
        sum = calculation_function(n1=num1, n2=num2)
        print(f"{num1} {operator} {num2} = {sum}")

    else:
        operator = input("Select the operation: ")
        num3 = int(input("What's the next number?: "))
        calculation_function = operations[operator]
        sum2 = calculation_function(n1=sum, n2=num3)
        print(f"{sum} {operator} {num3} = {sum2}")
        sum = sum2
    user_choice = input(
        f"Type 'y' to continue calculating with {sum} or type 'n' to start new calculation or type 'q' to exit: "
    ).lower()
    if user_choice == "y":
        new_calculation = False
    elif user_choice == "n":
        new_calculation = True
    else:
        should_continue = False
