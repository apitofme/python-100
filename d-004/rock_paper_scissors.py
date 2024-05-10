"""
-=< 100 Days of Python >=-
-=[ Day 004 ]=-

Project: Rock, Paper, Scissors
"""
# imports up top
import random

# define gestures
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = {"Rock": rock, "Paper": paper, "Scissors": scissors}

# welcome message
print("Let's play a game of Rock, Paper, Scissors!")

# input and validation
choice = input("What do you choose? [R]ock, [P]aper or [S]cissors\n").lower()
while choice not in ['r', 'p', 's', 'rock', 'paper', 'scissors']:
    print("Sorry, please type 'R' for Rock, 'P' for Paper or 'S' for Scissors")
    choice = input(
        "What do you choose? [R]ock, [P]aper or [S]cissors\n").lower()

# player choice
if len(choice) == 1:
    if choice == 'r':
        player_choice = "Rock"
    elif choice == 'p':
        player_choice = "Paper"
    elif choice == 's':
        player_choice = "Scissors"
    else:
        # this should NEVER happen, but just in case...
        raise ValueError(f"Invalid option: '{choice}'")
else:
    player_choice = choice.capitalize()

# computer choice
r_num = random.randint(0, 2)
computer_choice = list(game.keys())[r_num]

# print game output
print(f"You chose '{player_choice}':")
print(game[player_choice])

print(f"The computer chose '{computer_choice}':")
print(game[computer_choice])

# win / lose messages
win = "Congratulations, You Win!"
lose = "Sorry, You Lost!"

# determine winner
if player_choice == computer_choice:
    print("It's a draw!")
else:
    if computer_choice == "Rock":
        if player_choice == "Paper":
            print(win)
        else:
            print(lose)
    elif computer_choice == "Paper":
        if player_choice == "Scissors":
            print(win)
        else:
            print(lose)
    else:  # i.e. computer_choice == "Scissors"
        if player_choice == "Rock":
            print(win)
        else:
            print(lose)
