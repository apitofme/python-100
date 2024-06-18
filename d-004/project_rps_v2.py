"""
-=< 100 Days of Python >=-
-=[ Day 004 ]=-

Project: BONUS (a.k.a. v2.0)
- Rock, Paper, Scissors, Lizard, Spock

In a game of Rock-Paper-Scissors-Lizard-Spock:
    - Scissors cut Paper,
    - Paper covers Rock,
    - Rock crushes Lizard,
    - Lizard poisons Spock,
    - Spock smashes Scissors,
    - Scissors decapitates Lizard,
    - Lizard eats Paper,
    - Paper disproves Spock,
    - Spock vaporizes Rock,
    - and (as always) Rock breaks Scissors.

Ref: https://wrpsa.com/the-official-rules-for-playing-rock-paper-scissors-lizard-spock/
"""
# imports up top
import random

# define gestures
rock = r"""
	 _.-.-.-.
	;_|_|_|_|_
	|_|_|\__  \
	|    . '  |
	|   (    /
	 \______/

"""

paper = r"""
	   _.-._
	 _| | | |
	| | | | |
	| | | | |
	| i ' i | ,-,
	|       |/ /
	|     ,-' /
	|    ;    |
	|         /
	 \_______/
"""

scissors = r"""
	    .-.
	    | |    / )
	    | |   / /
	    | |  / /
	 _.-| |_/ /
	; \( \    |
	|\_)\ \   |
	|    ) \  /
	|   (    /
	 \______/
"""

lizard_alt = r"""
                       )/_
             _.--..---"-,--c_
        \L..'           ._O__)_
,-.     _.+  _  \..--( /
  `\.-''__.-' \ (     \_
    `'''       `\__   /\
                ')
"""

lizard = r"""
	  _____________
	 /   ________;_;
	/  /______/ )
	|          /
	 \________/
"""

spock = r"""
	  _    .-._
	 ( \   | | |
	( \ \  | | |
	 \ \ \ | | | ,-,
	  \ \ \| | |/ /
	   |     ,-' /
	   |    ;    |
	   |         /
	    \_______/
"""

game = {"Rock": rock, "Paper": paper, "Scissors": scissors,
        "Lizard": lizard, "Spock": spock}

# welcome message
print("Time to unleash your inner Sheldon...")
print("Let's play a game of Rock, Paper, Scissors, Lizard, Spock!")

# input and validation
print("What do you choose?")
choice = input("[R]ock, [P]aper, [S]cissors, [L]izard or Spoc[K]\n").lower()
while choice not in ['r', 'p', 's', 'l', 'k', 'rock', 'paper', 'scissors'
                     'lizard', 'spock']:
    print("Sorry, please type 'R' for Rock, 'P' for Paper, 'S' for Scissors,\
        'L' for Lizard or 'K' for Spock")
    print("What do you choose?")
    choice = input(
        "[R]ock, [P]aper, [S]cissors, [L]izard or Spoc[K]\n").lower()

# player choice
if len(choice) == 1:
    offset = "rpslk".index(choice)
    player_choice = list(game.keys())[offset]
else:
    player_choice = choice.capitalize()

# computer choice
r_num = random.randint(0, 4)
computer_choice = list(game.keys())[r_num]

# print game output
print(f"You chose '{player_choice}':")
print(game[player_choice])

print(f"The computer chose '{computer_choice}':")
print(game[computer_choice])

# win / lose messages
win = "Congratulations, You Win!"
lose = "Sorry, You Lose!"

# determine winner
if player_choice == computer_choice:
    print("It's a draw!")
else:
    if computer_choice == "Rock":

        if player_choice == "Paper":
            print("Paper covers Rock.")
            print(win)
        elif player_choice == "Spock":
            print("Spock vaporises Rock.")
            print(win)
        elif player_choice == "Scissors":
            print("Rock breaks Scissors.")
            print(lose)
        else:
            print("Rock crushes Lizard.")
            print(lose)

    elif computer_choice == "Paper":

        if player_choice == "Scissors":
            print("Scissors cut Paper.")
            print(win)
        elif player_choice == "Lizard":
            print("Lizard eats Paper.")
            print(win)
        elif player_choice == "Rock":
            print("Paper covers Rock.")
            print(lose)
        else:
            print("Paper disproves Spock.")
            print(lose)

    elif computer_choice == "Scissors":

        if player_choice == "Rock":
            print("Rock breaks Scissors.")
            print(win)
        elif player_choice == "Spock":
            print("Spock smashes Scissors.")
            print(win)
        elif player_choice == "Paper":
            print("Scissors cut Paper.")
            print(lose)
        else:
            print("Scissors decapitate Lizard.")
            print(lose)

    elif computer_choice == "Lizard":

        if player_choice == "Rock":
            print("Rock crushes Lizard.")
            print(win)
        elif player_choice == "Scissors":
            print("Scissors decapitate Lizard.")
            print(win)
        elif player_choice == "Paper":
            print("Lizard eats Paper.")
            print(lose)
        else:
            print("Lizard poisons Spock.")
            print(lose)

    elif computer_choice == "Spock":

        if player_choice == "Paper":
            print("Paper disproves Spock.")
            print(win)
        elif player_choice == "Lizard":
            print("Lizard poisons Spock.")
            print(win)
        elif player_choice == "Rock":
            print("Spock vaporises Rock.")
            print(lose)
        else:
            print("Spock smashes Scissors")
            print(lose)
