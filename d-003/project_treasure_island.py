"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-

Project: Treasure Island

The goal of this project is to learn about program 'control-flow' using
conditional statements.

By prompting the User with a series of simple, multiple-choice questions,
and taking their input to choose what action/direction they wish to take,
we will output different outcomes based on those choices in order to
present a simple "Choose Your Own Adventure" style game.

Learning outcomes today include:
- Conditional Statements (If / Elif / Else); Logical Operators;
  Code Blocks; Scope; Global and Local Namespacing and more...

NOTE: I've implemented input validation using WHILE loops (which have not
      yet been covered on the course) -- Please see external file
      "project_treasure_island_official.py" for the 'Official Solution'!
"""
import sys
# import required for proper "exit()" functionality [according to PyLint!]

# ascii-art logo
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Cross-roads:
print("You're at a cross-road. Where do you want to go?")
choice = input('Type "left" or "right":\n').lower()
# validate input
while choice not in ['left', 'right']:
    print("Sorry, I didn't understand that.")
    choice = input('Please type "left" or "right":\n').lower()
# process input
if choice == 'right':
    print("You fell in to a hole. Game Over.")
    sys.exit()

# Lake crossing:
print("You've come to a lake. There is an island in the middle of the lake.")
choice = input(
    'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
# validate input
while choice not in ['wait', 'swim']:
    print("Sorry, I didn't understand that.")
    choice = input(
        'Please type "wait" to wait for a boat, or "swim" to swim across.\n').lower()
# process input
if choice == 'swim':
    print("You get attacked by an angry trout. Game Over")
    sys.exit()

# Coloured doors:
print("You arrive at the island unharmed. There is a house with 3 doors.")
choice = input(
    'One red, one yellow and one blue. Which colour do you choose?\n').lower()
while choice not in ['red', 'yellow', 'blue']:
    print("Sorry, I didn't understand that.")
    choice = input(
        'Which colour do you choose? [Please type "red", "yellow" or "blue"]\n').lower()
# process input
if choice == 'red':
    print("It's a room full or fire. Game Over")
    sys.exit()
if choice == 'blue':
    print("You enter a room of beasts. Game Over")
    sys.exit()

# WINNER!
print("You found the treasure! You Win!")
sys.exit()
