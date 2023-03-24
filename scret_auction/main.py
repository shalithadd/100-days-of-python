from art import logo
import os


def clear():
    # Clear the terminal
    os.system("cls")


def find_highest_bidder(bid_entry):
    highest_bid = 0
    # loop through each key in bid_entry dict and compare each value with highest_bid
    for bidder in bid_entry:
        if bid_entry[bidder] > highest_bid:
            highest_bid = bid_entry[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")  # pyright:ignore


print(logo)
bidders = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    # add name and bid to bidders dict
    bidders[name] = bid

    # check if need to continue or exit
    if should_continue == "yes":
        bidding_finished = False
        clear()
    else:
        bidding_finished = True
        clear()
        find_highest_bidder(bidders)
