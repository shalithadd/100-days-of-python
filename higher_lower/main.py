import random
from art import logo, vs
from game_data import data
import os


def clear():
    os.system("cls")


def set_compare():
    random_item = random.choice(data)
    bio = []
    for key, value in random_item.items():
        if key != "follower_count":
            bio.append(value)
    bio = ", ".join(bio)
    return bio, random_item["follower_count"]


def compare_followers(follower_count_a, follower_cont_b, answer, score):
    if follower_count_a > follower_cont_b:
        winner = "a"
    else:
        winner = "b"

    if winner == answer:
        message = f"You are right! Current score: {score + 1}."
        return score + 1, winner, message
    else:
        message = f"Sorry that's wrong. Final score: {score}."
        return score, winner, message


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
        score, winner, message = compare_followers(
            follower_count_a, follower_count_b, answer, score
        )
        if winner == answer:
            clear()
            print(logo)
            print(message)
            bio_a = bio_b
            follower_count_a = follower_count_b
        else:
            correct_answer = False
            clear()
            print(logo)
            print(message)


game()
