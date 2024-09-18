"""
-=< 100 Days of Python >=-
-=[ Day 012 ]=-

Project: Number Guessing Game

The goal of today's project is to create a simple number guessing game.

Have the computer pick a random number between 1 and 100, the player will
then try to guess the number. Each incorrect guess should tell the player
if they were higher or lower than the target number.

Before the game starts the player should have the option to choose 'easy'
or 'hard', which will determine the number of guesses the player gets to
find the target number (10 and 5 respectively).

This project will be your first "flying solo" effort, with no supporting
"repl.it" repository, code-along guide, or hints! -- Good luck!!
"""
from os import system
from random import randint


def clear_terminal():
    """cross-platform way to clear the terminal screen"""
    system("cls||clear")


def refresh_display():
    """clear the terminal screen and (re)print the logo"""
    clear_terminal()
    print(logo)


logo = r"""
 __    _  __   __  __   __  _______  _______  ______      _______  __   __  _______  _______  _______ 
|  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |    |       ||  | |  ||       ||       ||       |
|   |_| ||  | |  ||       || |_|   ||    ___||   | ||    |    ___||  | |  ||    ___||  _____||  _____|
|       ||  |_|  ||       ||       ||   |___ |   |_||_   |   | __ |  |_|  ||   |___ | |_____ | |_____ 
|  _    ||       ||       ||  _   | |    ___||    __  |  |   ||  ||       ||    ___||_____  ||_____  |
| | |   ||       || ||_|| || |_|   ||   |___ |   |  | |  |   |_| ||       ||   |___  _____| | _____| |
|_|  |__||_______||_|   |_||_______||_______||___|  |_|  |_______||_______||_______||_______||_______|
"""


def get_difficulty():
    """Ask player for input to select difficulty level.
    Validate the input.
    Returns an integer"""
    difficulty = False
    while not difficulty:
        difficulty = input("Choose a difficulty - Type 'easy' or 'hard': ")
        if difficulty not in ['easy', 'hard']:
            print("Sorry, please type 'easy' or 'hard'!")
            difficulty = False

    if difficulty == 'easy':
        print("Playing in 'easy' mode,"
              " you will have 10 attempts to guess the number."
              )
        return 10

    print("Playing in 'hard' mode,"
          " you will only have 5 attempts to guess the number!"
          )
    return 5


def get_random_number(lo=1, hi=100):
    """Returns a random integer between the parameter constraint values"""
    return randint(lo, hi)


def get_player_guess():
    """Ask player to input their guess.
    Validate the input.
    Returns an integer"""
    number = False
    while not number:
        number = input("What is your guess? ")
        if not number.isnumeric():
            print("Sorry, please enter a number!")
            number = False
    return int(number)


def guessing_game():
    """Main game loop"""
    refresh_display()
    print("Welcome to the number guessing game!")
    attempts_left = get_difficulty()
    target = get_random_number()
    print("I'm thinking of a number between 1 and 100...")
    print(f"Try to guess it in less than {attempts_left} attempts! ;)")
    win = False
    while not win and attempts_left > 0:
        guess = get_player_guess()
        # update the attempt counter now so that the output below is correct
        attempts_left -= 1

        if guess == target:
            win = True
        elif guess > target:
            print("Too high.")
        elif guess < target:
            print("Too low.")
        print(f"- You have {attempts_left} more attempts")

    if win:
        print("Congratulations, you correctly guessed the number!")
        print(f"- You had {attempts_left} attempts left")
    else:
        print("Sorry, you failed to guess the number.")
        print(f"- It was {target}!")


def play_again():
    """Ask player if they would like to play again.
    Validate the input.
    Returns a Boolean"""
    response = False
    while not response:
        response = input("Would you like to play again? "
                         "(Type 'y' to play again, type 'n' to quit): "
                         ).lower()
        if response not in ['y', 'n']:
            print("Sorry, please type 'y' or 'n'!")
            response = False

    if response == 'y':
        return True

    return False


# Repeatable Game Loop ('main')
play = True
while play:
    guessing_game()
    if not play_again():
        play = False

print("Thank you for playing!")
