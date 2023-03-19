import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_letters = ""
pwd_symbols = ""
pwd_numbers = ""

# Append random letters to "pwd_letters" string from the list "letters"
for i in range(nr_letters):
    rand_letter = random.randint(0, (len(letters) - 1))
    pwd_letters += letters[rand_letter]
# Append random symbols to "pwd_symbols" string from the list "symbols"
for i in range(nr_symbols):
    rand_symbol = random.randint(0, (len(symbols) - 1))
    pwd_symbols += symbols[rand_symbol]
# Append random number to "pwd_numbers" string from the list "numbers"
for i in range(nr_numbers):
    rand_number = random.randint(0, (len(numbers) - 1))
    pwd_numbers += numbers[rand_number]

# Create the password by concatenating the 3 strings pwd_letters, pwd_symbols and pwd_numbers
pwd = list(pwd_letters + pwd_symbols + pwd_numbers)

# Randomizing the password
rand_pwd = []
for i in range(len(pwd)):
    rand_char = random.randint(0, (len(pwd) - 1))
    rand_pwd.append(
        pwd[rand_char]
    )  # Access random index of the list "pwd" and append to the list "rand_pwd"
    pwd.pop(rand_char)  # delete the random index frm the list "pwd"

# Use .join() method to print only the elements of the list "rand_pwd"
rand_pwd = "".join(rand_pwd)
print(f"Your password is {rand_pwd}")
