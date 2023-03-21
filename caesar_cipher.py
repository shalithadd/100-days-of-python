def encrypt(text, shift):
    new_text = []
    for char in range(len(text)):
        new_idx = alphabet.index(text[char]) + shift
        if new_idx < len(alphabet):
            new_text.append(alphabet[new_idx])
        else:
            new_idx = new_idx % len(alphabet)
            new_text.append(alphabet[new_idx])
    print("".join(new_text))


def decrypt(text, shift):
    new_text = []
    for char in range(len(text)):
        new_idx = alphabet.index(text[char]) - shift
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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
