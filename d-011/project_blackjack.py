"""
-=< 100 Days of Python >=-
-=[ Day 010 ]=-

Project: Blackjack

Today will be our 'Capstone' project for this section, and will require us
to combine all the skills we've learned so far in to one fun, little
interactive game -- Blackjack (a.k.a. "21")


Blackjack: also known as "twenty-one" or "Pontoon" in Europe (or "Ochko" in
Russia), is a comparing card game where players compete against the dealer,
rather than each other. It is the most widely played casino banking game in
the world, typically using between one and eight 'standard' 52-card decks of
playing cards shuffled together.

The object of the game is to reach 21 points without going over. Cards are
counted at their numeric value, while 'Face Cards' are all worth 10 and Aces
can count as 1 _OR_ 11.

At the start of a game cards are dealt singularly to each player in turn
then to the dealer for two rounds, such that all receive a total of 2 cards.
Typically the player's cards are dealt face-up, whilst the dealer receives
their second card face-down.

On their turn Players can choose to "hit" and receive another card, they can
do this as many times as they like whilst remaining under a total of 21,
and/or finally "stand" receiving no more cards and ending their turn, with
play passing to the next player. If the player's total goes over 21 they are
"bust" and immediately loose their bet on that hand.

Once all players have finished their turns play passes to the Dealer, who
reveals their second card and plays their hand out by drawing cards until
the hand achieves a total of 17 or higher. If the dealer has a total of 17
including an ace valued as 11 (a "soft 17"), some games require the dealer
to stand while other games require another draw. If the dealer busts, all
remaining player hands win. If the dealer does NOT bust, each remaining bet
wins if its hand is higher than the dealer's and loses if it is lower.

Ref: https://en.wikipedia.org/wiki/Blackjack#Rules_of_play_at_casinos


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""
from os import system
import random


def clear_terminal():
    """cross-platform way to clear the terminal screen"""
    system("cls||clear")


def refresh_display():
    """clear the terminal screen and (re)print the logo"""
    clear_terminal()
    print(logo)


# GAME FUNCTIONS >>
def deal_card():
    """returns a random card from the deck"""
    # simplified form, but even odds
    # return random.randint(2, 11)
    # corrected odds for blackjack
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)


def deal_cards(count=2):
    """deals the given number of cards and returns them as a List"""
    cards = []
    for _ in range(1, count+1):
        cards.append(deal_card())
    return cards


def create_player():
    """returns a new player (with cards) as a Dictionary!"""
    return {'cards': deal_cards(), 'bust': False}


def new_game():  # Multi-Player -- arg:num_of_players=1 ?
    """set up for a new game of Blackjack"""
    new_player = create_player()
    new_player['total'] = sum(new_player['cards'])
    new_dealer = create_player()
    new_dealer['total'] = sum(new_dealer['cards'])
    return (new_player, new_dealer)


def hit_me(is_dealer=False):
    """return a new card, or False otherwise"""
    # dealer just gets a new card
    if is_dealer:
        card = deal_card()
        return card

    # player is asked to 'hit' or 'stand'
    hit = False
    while str(hit) not in "yn":
        hit = input(
            "Do you want to HIT or STAND? "
            "(Type 'y' to get another card, type 'n' to pass): "
        ).lower()

    if hit == 'y':
        card = deal_card()
        return card

    return False


def show_hand(current_player, is_dealer=False):
    """output the current player's hand and status"""
    pd = "Dealer's" if is_dealer else "Your"
    print(f"{pd} cards are: {current_player['cards']}")
    print(f"{pd} score is: {current_player['total']}\n")


# "import" art module
logo = r"""
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

# start new game
player, dealer = new_game()

# main game loop
game_over = False
while not game_over:

    # PLAYER'S TURN >>
    num_cards = len(player['cards'])
    while not player['bust']:
        refresh_display()

        # player get's to see ONE of the dealer's cards
        print(f"Dealer's first card: {dealer['cards'][0]}\n")

        # handle new card from a 'hit'
        if len(player['cards']) > num_cards:
            num_cards += 1
            print(f"You received: {player['cards'][-1]}")

        # update total
        player['total'] = sum(player['cards'])

        show_hand(player)

        # check if score over 21
        if player['total'] > 21:

            # reduce 'Ace' (11) if present
            if 11 in player['cards']:
                print("Reducing value of 'Ace' to 1...")
                player['cards'][player['cards'].index(11)] = 1
                continue

            # otherwise they 'bust'
            player['bust'] = True
            break

        # hit or stick
        new_card = hit_me()
        if new_card:
            player['cards'].append(new_card)
            continue

        # otherwise player's turn is over
        break

    # PLAYER BUST >> PLAY AGAIN?
    if player['bust']:
        refresh_display()
        show_hand(player)

        print("Sorry you BUST. You LOSE!\n")

        again = False
        while str(again) not in "yn":
            again = input(
                "Would you like to play again? "
                "(Type 'y' to play again, type 'n' to quit): "
            ).lower()

        # NOT playing again >>
        if again == 'n':
            print("Thanks for playing!")
            # END GAME!!
            break  # game_over = True

        # NEW GAME >>
        player, dealer = new_game()
        # loop back and start again
        continue

    # DEALER'S TURN >>
    num_cards = len(dealer['cards'])
    while not dealer['bust']:
        refresh_display()

        # handle new card from a 'hit'
        if len(dealer['cards']) > num_cards:
            num_cards += 1
            # print(f"\nDEBUG: LEN={len(dealer['cards'][2:])} | "
            #      f"TYPE={type(dealer['cards'][2:])}\n")
            for hit_card in dealer['cards'][2:]:
                # print("Dealer cannot stand under 17!")
                print("Dealer hits...")
                print(f"Dealer received: {hit_card}\n")
                # print("Dealer's current score is: "
                #      f"{sum(dealer['cards'][:2]) + hit_card}\n"
                #      )

        # update total
        dealer['total'] = sum(dealer['cards'])

        show_hand(dealer, is_dealer=True)

        # dealer cannot 'stand' below 17
        if dealer['total'] < 17:
            new_card = hit_me(is_dealer=True)
            dealer['cards'].append(new_card)
            continue

        # check if score is over 21
        if dealer['total'] > 21:

            # reduce 'Ace' (11) if present
            if 11 in dealer['cards']:
                dealer['cards'][dealer['cards'].index(11)] = 1
                continue

            # otherwise they 'bust'
            dealer['bust'] = True

        break

    # DEALER BUST >> PLAY AGAIN?
    if dealer['bust']:
        print("The dealer BUST. You WIN!\n")

        again = False
        while str(again) not in "yn":
            again = input(
                "Would you like to play again? "
                "(Type 'y' to play again, type 'n' to quit): "
            ).lower()

        # NOT playing again >>
        if again == 'n':
            print("Thanks for playing!")
            # END GAME!!
            break  # game_over = True

        # NEW GAME >>
        player, dealer = new_game()
        # loop back and start again
        continue

    # NO-ONE BUST >> DETERMINE WINNER:
    # refresh_display()

    player['total'] = sum(player['cards'])
    show_hand(player)

    # dealer['total'] = sum(dealer['cards'])
    # show_hand(dealer, is_dealer=True)

    if player['total'] > dealer['total']:
        print("Congratulations, you WIN!\n")
    else:
        print("Sorry, you LOSE!\n")

    # FINALLY >> PLAY AGAIN?
    again = False
    while str(again) not in "yn":
        again = input(
            "Would you like to play again? "
            "(Type 'y' to play again, type 'n' to quit): "
        ).lower()

    # NOT playing again >>
    if again == 'n':
        print("Thanks for playing!")
        # END GAME!!
        break  # game_over = True

    # NEW GAME >>
    player, dealer = new_game()
    # loop back and start again
    continue
