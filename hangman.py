import random


words = ["aardvark", "baboon", "camel", "apple", "pizza"]
random_word = random.choice(words)
guessed_letters = []
word_length = len(random_word)

# Using "_" in the for loop as value of variable is not needed
for _ in range(word_length):
    guessed_letters.append("_")

print(" ".join(guessed_letters))
lives = 6
while lives > 0:
    user_guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = random_word[position]
        if letter == user_guess:
            guessed_letters[position] = letter

    print(" ".join(guessed_letters))
