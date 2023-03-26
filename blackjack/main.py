import random
from art import logo
import emoji
import os


def clear():
    os.system("cls")


def win_condition(user_hand, computer_hand, deck):
    user_total = sum(user_hand)
    computer_total = sum(computer_hand)

    user_state = f"Your final hand: {user_hand}, final score: {user_total}"
    computer_state = (
        f"Computer's final hand: {computer_hand}, final score: {computer_total}"
    )
    user_win = emoji.emojize("You win :grinning_face_with_big_eyes:")
    user_lose = emoji.emojize("You lose :frowning_face:")
    game_draw = emoji.emojize("It's a draw :face_with_open_mouth:")

    if user_total > 21:
        print(f"\n  {user_state}\n  {computer_state}")
        print(user_lose)
    elif computer_total < 17:
        if computer_total <= 10:
            deck[0] = 10
        else:
            deck[0] = 1
        computer_hand.append(random.choice(deck))
        win_condition(user_hand, computer_hand, deck)
    elif 21 % user_total > 21 % computer_total:
        print(f"\n  {user_state}\n  {computer_state}")
        print(user_lose)
    elif user_total == computer_total:
        print(f"\n  {user_state}\n  {computer_state}")
        print(game_draw)
    elif 21 % user_total < 21 % computer_total:
        print(f"\n  {user_state}\n  {computer_state}")
        print(user_win)


def blackjack():
    should_continue = True
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = random.choices(deck, k=2)
    computer_hand = random.choices(deck, k=2)

    clear()
    print(logo)
    print(f"\nYour cards: {user_hand}")
    print(f"Computer's first card: [{computer_hand[0]}]\n")

    while should_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            if sum(user_hand) <= 10:
                deck[0] = 11
            else:
                deck[0] = 1
            user_hand.append(random.choice(deck))
            if sum(user_hand) > 21:
                win_condition(user_hand, computer_hand, deck)
                should_continue = False
            else:
                print(f"\nYour cards: {user_hand}")

        else:
            win_condition(user_hand, computer_hand, deck)
            should_continue = False

    if input("\n\nType 'y' to play again, type 'n' to exit: ") == "y":
        blackjack()


blackjack()
