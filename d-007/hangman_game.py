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

# import local game modules
from hangman_art import logo, stages
from hangman_words import word_list

# welcome
print("Welcome to")
print(logo)

# set up the player's lives
# lives = 6
# actually, I prefer this idea from another student...
lives = len(stages) - 1
# ...it is more flexible if we want to modify the game
# e.g. to increase the number of Lives
# i.e. by 'building' the Gallows BEFORE drawing the Man
# print(lives)

# chose a word for the player to guess
chosen_word = random.choice(word_list)
print("I have chosen a random word for you to guess!\n")

# set up the masked word to display
word_mask = "_" * len(chosen_word)
print(word_mask + "\n")

# we want to track the players guesses too
guesses = ""


def get_player_guess():
    """get and validate user input as the player's guess"""
    while True:
        player_guess = input("What letter do you guess? ").lower()

        # guesses should only be letters (not numbers or other characters)
        if not player_guess.isalpha():
            print("Please only choose letters!")
            print("- There are no non-alphabetical characters in any of the words.\n")
            continue

        # players should only guess one letter at a time
        if len(player_guess) > 1:
            print("Please only guess one letter at a time!")
            print("- Taking the first letter as your guess this time.\n")
            return player_guess[0]

        # otherwise the guess is fine
        return player_guess


def update_word_mask(guessed_letters):
    """update the word mask with ALL letters guessed so far"""
    mask = ""
    # for each letter in the chosen word...
    for letter in chosen_word:
        # if the letter is in the player's guesses
        if letter in guessed_letters:
            # update the word mask with that letter
            mask += letter
        else:
            # otherwise continue to mask it
            mask += "_"

    return mask


# (optionally) print starting 'stage' from ASCii art
print(stages[-1])

# loop game until player has won or lost
game_over = False
while not game_over:
    # ask player for a letter guess
    guess = get_player_guess()

    # check if the player already guessed that letter
    if guess in guesses:
        print(f"Sorry, you have already tried '{guess}'.")
        # restart the while loop immediately, ignore any remaining code
        continue

    # track the player's guesses
    guesses += guess

    # check for player's guess in chosen word
    if guess in chosen_word:
        print("You guessed correct!\n")
        # update the word mask (function requires ALL guesses!)
        word_mask = update_word_mask(guesses)
    else:
        print(f"Sorry there is no '{guess}' in the word.\n")
        lives -= 1

    # show the current word mask
    print(" ".join(word_mask) + "\n")

    # show all letters the player has guessed so far
    if guesses != "":
        print("Guessed Letters: " + " ".join(guesses))

    # show the game stage for current lives
    print(stages[lives])

    # check if the player has guessed all of the letters in 'chosen_word'
    # - Game Over: WIN
    if "_" not in word_mask:
        print("You escaped the Hangman - You win!\n")
        game_over = True

    # check if the player has run out of lives
    # - Game Over: LOSE
    if lives == 0:
        print("You've been hung - You lose!\n")
        print(f"The word was: {chosen_word}")
        game_over = True
