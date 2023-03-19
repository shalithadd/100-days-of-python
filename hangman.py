import random


words = ["aardvark", "baboon", "camel"]
random_word = random.choice(words)
guessed_letters = []

for char in range(len(random_word)):
    guessed_letters.append("_")

print(" ".join(guessed_letters))
lives = 6
while lives > 0:
    user_guess = input("Guess a letter: ").lower()
    for idx, letter in enumerate(random_word):
        if letter == user_guess:
            guessed_letters[idx] = user_guess

    print(" ".join(guessed_letters))
