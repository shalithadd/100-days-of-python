import random
import hangman_art
import hangman_words

words = hangman_words.word_list
random_word = random.choice(words)
guessed_letters = []
word_length = len(random_word)
lives = 6
stages = hangman_art.stages

# Using "_" in the for loop as value of variable is not needed
for _ in range(word_length):
    guessed_letters.append("_")

end_of_game = False
is_guess_correct = False

print(hangman_art.logo)
while not end_of_game:
    print(stages[lives])
    print(" ".join(guessed_letters))
    user_guess = input("Guess a letter: ").lower()

    if user_guess in random_word:
        is_guess_correct = True
    else:
        is_guess_correct = False

    if is_guess_correct:
        for position in range(word_length):
            letter = random_word[position]
            if letter == user_guess:
                guessed_letters[position] = letter
        if "_" in guessed_letters:
            print(f"You guessed right, you have {lives} guesses left.\n")
        else:
            print("You win.")
            end_of_game = True
    else:
        lives -= 1
        if lives > 0:
            print(f"\nYou are wrong, you have {lives} guesses left.")
        elif lives == 0:
            print(f"You lose. The random word is {random_word}.")
            end_of_game = True
