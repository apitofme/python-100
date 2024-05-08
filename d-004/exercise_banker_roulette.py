"""
-=< 100 Days of Python >=-
-=[ Day 004 ]=-

Coding Exercise: Banker Roulette (L.45)
"""
"""
Slide 1: Task
- Write a program that will select a random name from a list of names.

Imagine you're out for a meal with a group of friends and you want to play
a kind of 'roulette' to see who pays the bill. This program will be able
to take the list of names of the people dining and select one person at
random, the person selected will have to pay the bill!

IMPORTANT: You are not allowed to use the 'choice()' function!

Hints:

    1. You might need the help of the len() function:
    - https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

    2. Remember that Lists start at index 0!

Example Output:

    "Michael is going to buy the meal today!"

"""
# NOTE: I've added the 'behind the scenes' functionality here that is
#       hidden away on the Auditorium exercise
import random
names_string = "Angela, Ben, Jenny, Michael, Chloe"

# This will split the String of names in to a List of individual names
names = names_string.split(", ")

"""
Slide 2: Solution
"""
# print(len(names))
random_offset = random.randint(0, len(names)-1)
# print(random_offset)
name = names[random_offset]
print(f"{name} is going to buy the meal today!")

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/d45f0fbf-1651-4287-9c65-9aec95c8fed4?sl=b4a214ee-8100-49e0-a19d-5e8e38d47265&st=ktNFoqphHSFeMdHP02f3YFAldyJQI1D1
"""
