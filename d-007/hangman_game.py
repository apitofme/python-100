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

# chose a word for the player to guess
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("I have chosen a random word for you to guess!\n")

# set up the masked word to display
word_mask = "_" * len(chosen_word)
print(word_mask + "\n")


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


def update_word_mask(guessed_letter):
    """update the word mask when a correct letter was guessed"""
    mask = ""
    # for each letter in the chosen word...
    for letter in chosen_word:
        # if the letter matches the player's guess
        if letter == guessed_letter:
            # update the word mask with the letter
            mask += guessed_letter
        else:
            mask += "_"
    return mask


# loop the player guesses until 'chosen_word' complete
while "_" in word_mask:
    # ask player for a letter guess
    guess = get_player_guess()

    # check for player's guess in chosen word
    if guess in chosen_word:
        print("You guessed correct!\n")
        word_mask = update_word_mask(guess)
        print(" ".join(word_mask) + "\n")
    else:
        print(f"Sorry there is no '{guess}' in the word.")

    if "_" not in word_mask:
        print("You win!")