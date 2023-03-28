from art import logo
import random
import os


EASY_DIFFICULTY_TURNS = 10
HIGH_DIFFICULTY_TURNS = 5


def clear():
    """Clear the terminal."""
    os.system("cls")


def set_difficulty():
    """Return the number of attempts for difficulty level."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_DIFFICULTY_TURNS
    else:
        return HIGH_DIFFICULTY_TURNS


def compare_guess(user_guess, random_number, attempts):
    """Compare the user guess against random number and returns remaining attempts."""
    if user_guess == random_number:
        print(f"\nYou got it! The answer was {random_number} 👍")
    elif user_guess > random_number:
        print("\nToo high.")
        return attempts - 1
    else:
        print("\nToo low.")
        return attempts - 1


def new_game():

    random_number = random.randint(1, 100)

    clear()
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    attempts = set_difficulty()
    user_guess = 0

    while random_number != user_guess:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attempts = compare_guess(user_guess, random_number, attempts)

        if attempts == 0:
            print("You've ran out of guesses, you lose.")
            print(f"Correct answer was {random_number}.")
            break
        elif user_guess != random_number:
            print("Guess again.")

    if input("Type 'y' to play again or type 'n' to exit: ").lower() == "y":
        new_game()


new_game()
