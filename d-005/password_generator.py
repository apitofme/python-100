"""
-=< 100 Days of Python >=-
-=[ Day 005 ]=-

Project: Password Generator

The goal of this project is to build an automated password generator that
will take input from the user to determine how many Letters, Numbers and
Symbols should be used to create a completely random and secure password.
"""
# imports up top!
import random

# use list comprehensions to construct lists of lowercase and uppercase
# characters when given a range of unicode values where:
#
#   - ord() returns the integer value of the given character in Unicode.
#           Ref: https://docs.python.org/3.12/library/functions.html#ord
#   - chr() returns the character string of the given integer value in Unicode
#           Ref: https://docs.python.org/3.12/library/functions.html#chr
#
# NOTE: we still need to +1 to the range to include the upper-bound value
lower_case = [chr(value) for value in range(ord("a"), ord("z") + 1)]
upper_case = [chr(value) for value in range(ord("A"), ord("Z") + 1)]
characters = lower_case + upper_case
# create a list of integers from 0 to 9 inclusive
numbers = list(range(0, 10))
# create a list of accepted symbols
symbols = ["!", "£", "$", "€", "%", "^", "&", "*", "(", ")", "-", "_",
           "+", "=", "[", "]", "{", "}", ";", ":", "@", "#", "~", ",",
           ".", "<", ">", "?", "`", "'"]

# greeting
print("Welcome to my automated secure password generator!")
print("The generated password should contain:")
# get user input for password specifications
n_ltrs = int(input("- How many letters?\n"))
n_syms = int(input("- How many symbols?\n"))
n_nums = int(input("- How many numbers?\n"))
# calculate the total password length
pw_length = n_ltrs + n_syms + n_nums

# initialise temporary list variables for password components
pw_chars = []
pw_syms = []
pw_nums = []

# loop to generate the required number of random characters:
for n in range(0, n_ltrs):
    r = random.randint(0, len(characters)-1)
    pw_chars.append(characters[r])
# loop to generate the required number of random symbols:
for n in range(0, n_syms):
    r = random.randint(0, len(symbols)-1)
    pw_syms.append(symbols[r])
# loop to generate the required number of random numbers:
for n in range(0, n_nums):
    r = random.randint(0, len(numbers)-1)
    pw_nums.append(str(numbers[r]))

# combine the components in to a single list
pw_list = pw_chars + pw_syms + pw_nums
# shuffle the list to randomise the distribution
# NOTE: this operation acts in-place on the List, updating it
random.shuffle(pw_list)
# compile the randomised List in to a single String using 'join()'
password = "".join(pw_list)

# finally output the secure random password for the user
print(f"Your secure password is: {password}")

"""
TODO: optional improvements
>   Add input validation to prevent crash on empty string with 'int()'
>   Ask the user for the desired password length (i.e. overall length),
    then ask how many symbols and numbers to include in that.
>   Allow user to input any specific characters, numbers or symbols that
    should be EXCLUDED (e.g. could be a String)
"""
