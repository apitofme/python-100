"""
-=< 100 Days of Python >=-
-=[ Day 009 ]=-

Project: Secret Auction

Create a program that will take the name and bid amount from a user then
ask if there are other bidders: if "yes" it clears the screen (to hide the
previous bid) and takes new input from another bidder and adds it to the
auction bidder Dictionary; if "no" (once all bidders are entered) then the
program works out who has the highest bid and therefore wins the auction.

Topics covered by this will mostly focus on:
- Dictionaries; Nesting
"""
# we need a way to clear the screen (as we're not doing this on replit)
from os import system


def clear_terminal():
    """cross-platform way to clear the terminal screen"""
    system("cls||clear")


def screen_refresh():
    """clear the terminal screen and (re)print the logo"""
    clear_terminal()
    print(logo)


def ask_yesno(prompt, default=None):
    """Ask a simple Yes/No confirmation from User"""
    accepted = ['y', 'yes', 'n', 'no']

    # indicate accepted default value in the prompt
    if default in accepted:
        if default[0].lower() == 'y':
            prompt += "[Y / n] "
        else:
            prompt += "[y / N] "

    response_valid = False
    while not response_valid:
        response = input(prompt).lower()
        if default is not None and response.strip() == "":
            response = default
        if response not in accepted:
            print("Please enter 'y' or 'yes', 'n' or 'no'!")
        else:
            response_valid = True
    # NOTE we want to return a Boolean value!
    return bool(accepted.index(response) < 2)


def get_bidder_name():
    """Take the Bidder's name (with minimal validation)"""
    name_correct = False
    while not name_correct:
        bidder_name = input("Please enter your name:\n")
        # let's clear the screen and confirm the name
        screen_refresh()
        print(f"Bidder's name is {bidder_name}")
        name_correct = ask_yesno("Is this correct? ", 'y')
    return bidder_name


def get_bid_amount():
    """Take the bid amount (with minimal validation)"""
    # NOTE: When dealing with Currency we should really be using the
    # "Decimal" module. Here however we are simply using a Floating-Point
    # number, but we will NOT be validating input with more than 2 numbers
    # after the decimal point!
    valid_bid = False
    while not valid_bid:
        # NOTE: float() throws an exception if the input cannot be converted,
        # so let's use a Try->Except block to prevent a potential crash
        try:
            bid_amount = float(input("Please enter your bid: £"))
        except ValueError:
            print("Please enter an amount using only digits and optionally"
                  " a decimal point")
            continue
        valid_bid = True
    return bid_amount


# we're NOT going to bother creating an art module to import the logo from
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                        
                       .-------------.
                      /_______________\\
'''

# PROGRAM OUTPUT >>>
# start with a clean slate
clear_terminal()

print("Welcome to the Secret Auction...")
print(logo)

auction_bidders = {}
bidders_left = True
ask = "Are there other users who want to bid? "

# give everyone who wants to a chance to bid
while bidders_left:
    name = get_bidder_name()
    screen_refresh()
    bid = get_bid_amount()
    auction_bidders[name] = bid
    if not ask_yesno(ask):
        bidders_left = False
    screen_refresh()

# no more bidders so lets see who won
top_amount = 0
top_bidder = ""
for bidder, amount in auction_bidders.items():
    if amount > top_amount:
        top_amount = amount
        top_bidder = bidder

print(f"\n{top_bidder} has won the Secret Auction with a bid of £{
      top_amount:.2f}!\n")

# debug only
print(auction_bidders)
