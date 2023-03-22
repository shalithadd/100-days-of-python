from art import logo


def caesar(start_text, shift_amount, cipher_direction):
    end_text = []
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in range(len(start_text)):
        new_idx = alphabet.index(start_text[char]) + shift_amount
        if new_idx < len(alphabet):
            end_text.append(alphabet[new_idx])
        else:
            new_idx = new_idx % len(alphabet)
            end_text.append(alphabet[new_idx])
    print("".join(end_text))


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
    shift = int(input("Type the shift_amount number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    choice = input("type 'y' to use again or type 'n' to quit.\n").lower()
    if choice == "y":
        should_continue = True
    else:
        should_continue = False
