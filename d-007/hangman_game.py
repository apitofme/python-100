"""
-=< 100 Days of Python >=-
-=[ Day 007 ]=-

Project: Hangman Game

    "Hangman is a guessing game for two or more players. One player thinks
    of a word, phrase, or sentence and the other(s) tries to guess it by
    suggesting letters or numbers within a certain number of guesses..."
    - Ref: https://en.wikipedia.org/wiki/Hangman_(game)

The goal of today's project is to implement a playable digital version
of the classic Pencil & Paper game "Hangman" using Python.
"""
# imports up top
import random
from hangman_art import logo

# welcome
print("Welcome to")
print(logo)

# choose a random word for the player to guess
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("I have chosen a random word for you to guess!\n")


def get_player_guess():
    """get and validate user input as the player's guess"""
    while True:
        # player_guess = input("What letter do you guess?\n").lower()
        # TODO remove the 'hard coded' input below... >>
        player_guess = "a"
        standard_input = "a"
        print(input())
        # << ...it is only needed for the VSCode REPL extension
        # guesses should only be letters (not numbers or other characters)
        if not player_guess.isalpha():
            print("Please only choose letters. There are no \
                non-alphabetical characters in any of the words.")
            continue

        # players should only guess one letter at a time
        if len(player_guess) > 1:
            print("Please only guess one letter at a time!")
            print("Taking the first letter as your guess this time.")
            return player_guess[0]

        # otherwise the guess is fine
        return player_guess


# ask player for a letter guess
guess = get_player_guess()

# check for player's guess in chosen word
if guess in chosen_word:
    print(f"Yes there is an {guess} in the word.\n")
else:
    print(f"Sorry there is no {guess} in the word.")
