import random
from art import logo, vs
from game_data import data
import os


def clear():
    """Clear the terminal"""
    os.system("cls")


def format_data(account):
    """Take an account data and returns in printable format."""
    acc_name = account["name"]
    acc_descr = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_descr}, from {acc_country}."


def check_answer(follower_count_a, follower_count_b, answer):
    """Takes the user guess and follower counts and return if the guess is true or false"""
    if follower_count_a > follower_count_b:
        return answer == "a"
    else:
        return answer == "b"


print(logo)
score = 0
should_continue = True
acc_b = random.choice(data)
while should_continue:
    # Get 2 random accounts form game data
    acc_a = acc_b
    acc_b = random.choice(data)
    while acc_a == acc_b:
        acc_b = random.choice(data)

    # Print account data
    print(f"Compare A: {format_data(acc_a)}")
    print(vs)
    print(f"Against B: {format_data(acc_b)}")

    # Ask user to make a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get the follower count for account A and B
    follower_count_a = acc_a["follower_count"]
    follower_count_b = acc_b["follower_count"]
    # Check if the guess is correct
    is_correct = check_answer(follower_count_a, follower_count_b, guess)

    # Clear terminal and print feedback
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        should_continue = False
