from art import logo


def caesar(text, shift, direction):
    new_text = []
    if direction == "decode":
        shift *= -1
    for char in range(len(text)):
        new_idx = alphabet.index(text[char]) + shift
        if new_idx < len(alphabet):
            new_text.append(alphabet[new_idx])
        else:
            new_idx = new_idx % len(alphabet)
            new_text.append(alphabet[new_idx])
    print("".join(new_text))


alphabet = [
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
]

print(logo)
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    choice = input("type 'y' to use again or type 'n' to quit.\n").lower()
    if choice == "y":
        should_continue = True
    else:
        should_continue = False
