from art import logo
import os


def clear():
    os.system("cls")


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


def calculator():
    clear()
    print(logo)

    should_continue = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while should_continue:
        operator = input("Select the operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operator]
        answer = calculation_function(n1=num1, n2=num2)

        print(f"{num1} {operator} {num2} = {answer}")
        user_choice = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation or type 'q' to exit: "
        )

        if user_choice == "y":
            num1 = answer
        elif user_choice == "n":
            calculator()
        else:
            should_continue = False


calculator()
