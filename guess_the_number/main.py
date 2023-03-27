from art import logo
import random
import os


def clear():
    os.system("cls")


def compare_guess(user_guess, random_number):
    if user_guess == random_number:
        return f"\nYou got it! The answer was {random_number}"
    elif user_guess > random_number:
        return "\nToo low.\nGuess again."
    else:
        return "\nToo high.\nGuess again."


def new_game():

    random_number = random.randint(1, 100)
    should_continue = True

    clear()
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        attempts_remaining = 10
    else:
        attempts_remaining = 5

    while attempts_remaining != 0 and should_continue:
        print(
            f"\nYou have {attempts_remaining} attempts remaining to guess the number."
        )
        user_guess = int(input("Make a guess: "))

        if random_number == user_guess:
            should_continue = False
            print(compare_guess(random_number, user_guess))
        else:
            attempts_remaining -= 1
            print(compare_guess(random_number, user_guess))

    if attempts_remaining == 0:
        print("You've ran out of guesses, you lose.")
        print(f"Correct answer was {random_number}.")


if input("Type 'y' to play again or type 'n' to exit: ").lower() == "y":
    new_game()


new_game()
