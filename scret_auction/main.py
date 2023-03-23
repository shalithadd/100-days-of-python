from art import logo
import os


def clear():
    # Clear the terminal
    os.system("cls")


print(logo)
bidders = {}

should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    # add name and bid to bidders dict
    bidders[name] = bid
    # get the highest bid with max()
    highest_bid = max(bidders.values())

    # get the key of the highest bid
    for key, value in bidders.items():
        if value == highest_bid:
            winner = key

    if other_bidders == "yes":
        should_continue = True
        clear()
    else:
        should_continue = False
        clear()
        print(f"The winner is {winner}.")  # pyright: ignore
