import random
from art import logo
import os

# pyright: reportUnboundVariable=false


def clear():
    """Clear the terminal"""
    os.system("cls")


def deal_card():
    """Returns a random card from the deck."""
    # Ace is indicated by 11. Jack,king and queen indicated by 10
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score of cards."""
    # If sum of cards equal to 21 return 0 to indicate blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Ace can be 1 or 11 depending on the score
    # If score is less than or equal to 10 ace is 11 otherwise 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(user_score, computer_score):
    """Compare the user's against computer's score and return the winner."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, computer has blackjack 😱"
    elif user_score == 0:
        return "Win with a blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Computer went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    clear()
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []

    # Draw 2 random cards for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # If either user or computer has blackjack or user's score above 21 game over
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # if computer do not have blackjack and the score is less than 17 deal another card
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}. final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

    while input("Do you want to play again? type 'y' or 'n': ").lower() == "y":
        play_game()


play_game()
