import random
from art import logo, vs
from game_data import data


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
        print(f"You are right! Current score: {score + 1}.")
        return score + 1
    else:
        print(f"Sorry that's wrong. Final score: {score}.")


def game():
    print(logo)
    bio_a, follower_count_a = set_compare()
    bio_b, follower_count_b = set_compare()
    score = 0
    print(f"Compare A: {bio_a}.")
    print(vs)
    print(f"Compare B: {bio_b}.")
    answer = input("Who has more followers 'A' or 'B': ").lower()
    score = compare_followers(follower_count_a, follower_count_b, answer, score)


game()
