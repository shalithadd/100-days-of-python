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
num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operator = input("Select the operation: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operator]
sum = calculation_function(n1=num1, n2=num2)
print(f"{num1} {operator} {num2} = {sum}")
