"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-

Project: Treasure Island
"""
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
    exit()

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
    exit()

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
    exit()
if choice == 'blue':
    print("You enter a room of beasts. Game Over")
    exit()

# WINNER!
print("You found the treasure! You Win!")
exit()
