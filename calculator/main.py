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
num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)

while should_continue:
    operator = input("Select the operation: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operator]
    answer = calculation_function(n1=num1, n2=num2)

    print(f"{num1} {operator} {num2} = {answer}")

    if (
        input(f"Type 'y' to continue calculating with {answer} or type 'q' to exit: ")
        == "y"
    ):
        num1 = answer
    else:
        should_continue = False
