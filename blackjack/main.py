import random
from art import logo


def win_condition(user_hand, computer_hand, deck):
    user_total = sum(user_hand)
    computer_total = sum(computer_hand)
    user_state = f"Your cards are {user_hand} and total is {user_total}."
    computer_state = (
        f"Computer's cards are {computer_hand} and total is {computer_total}."
    )

    if user_total > 21:
        print(f"\nYou lost. {user_state}")
    elif computer_total < 17:
        computer_hand.append(random.choice(deck))
        win_condition(user_hand, computer_hand, deck)
    elif 21 % user_total > 21 % computer_total:
        print(f"\nYou lost. {user_state}\n{computer_state}")
    elif user_total == computer_total:
        print(f"\nIt's draw! {user_state}\n{computer_state}")
    elif 21 % user_total < 21 % computer_total:
        print(f"\nYou won! {user_state}\n{computer_state}")


def blackjack():
    should_continue = True
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = random.choices(deck, k=2)
    computer_hand = random.choices(deck, k=2)
    print(logo)
    print(f"\nYour cards: {user_hand}")
    print(f"Computer's first card: [{computer_hand[0]}]\n")

    while should_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            user_hand.append(random.choice(deck))
            print(f"\nYour cards: {user_hand}")
            if sum(user_hand) > 21:
                win_condition(user_hand, computer_hand, deck)
                should_continue = False
        else:
            win_condition(user_hand, computer_hand, deck)
            should_continue = False

    if input("\nType 'y' to play again, type 'n' to exit: ") == "y":
        blackjack()


blackjack()
