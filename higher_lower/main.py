import random
from art import logo, vs
from game_data import data
import os


def clear():
    """Clear the terminal"""
    os.system("cls")


def set_compare():
    """Return a random bio and the follower count from data list."""
    random_item = random.choice(data)
    bio = []
    for key, value in random_item.items():
        if key != "follower_count":
            bio.append(value)
    bio = ", ".join(bio)
    return bio, random_item["follower_count"]


def compare_followers(follower_count_a, follower_cont_b):
    """Compare the follower count of A vs B and return the winner."""
    if follower_count_a > follower_cont_b:
        winner = "a"
    else:
        winner = "b"
    return winner


def print_score(winner, answer, score):
    """Print score and return the score."""
    clear()
    print(logo)
    if winner == answer:
        print(f"You are right! Current score: {score + 1}.")
        return score + 1
    else:
        print(f"Sorry that's wrong. Final score: {score}.")
        return score


def game():
    clear()
    print(logo)
    correct_answer = True
    score = 0
    bio_a, follower_count_a = set_compare()

    while correct_answer:
        bio_b, follower_count_b = set_compare()
        print(f"Compare A: {bio_a}.")
        print(vs)
        print(f"Compare B: {bio_b}.")
        answer = input("Who has more followers 'A' or 'B': ").lower()
        winner = compare_followers(follower_count_a, follower_count_b)
        # If answer is correct  A becomes B
        if winner == answer:
            score = print_score(winner, answer, score)
            bio_a = bio_b
            follower_count_a = follower_count_b
        else:
            correct_answer = False
            score = print_score(winner, answer, score)


game()
