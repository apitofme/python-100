"""
-=< 100 Days of Python >=-
-=[ Day 014 ]=-

Project: The Higher Lower Game
Ref: https://www.higherlowergame.com

For today's project we're going to be re-creating a curiously simple, yet
addictive game, taking inspiration from the website referenced above.

In this game the player is shown information about two 'famous' entities, in
the context of the Second being compared against the First. The goal is to
accurately guess which one has the largest social-media following by stating
if they think the Second's following is "Higher" or "Lower" than the First's.

If the player guesses correctly then the information is updated to show a new
entity, comparing it against the previous answer, with the player choosing
"Higher" or "Lower" each time until they get one wrong, then it's Game Over!

A sample set of game data is provided in the additional file included inside
this folder. Other than that this project challenge is unsupported, with no
helpful tips or code-along tutorials, you must attempt this solo.
Do your best and see how it goes -- Good Luck!
"""
from os import system
from random import randint
from highlow_game_data import game_data

# CONSTANTS:
LOGO = r"""
  /\  /(_) __ _| |__   ___ _ __  \ \ \ 
 / /_/ / |/ _` | '_ \ / _ \ '__|  \ \ \
/ __  /| | (_| | | | |  __/ |     / / /
\/ /_/ |_|\__, |_| |_|\___|_|    /_/_/ 
          |___/                        
  ____    __                           
 / / /   / /  _____      _____ _ __    
/ / /   / /  / _ \ \ /\ / / _ \ '__|   
\ \ \  / /__| (_) \ V  V /  __/ |      
 \_\_\ \____/\___/ \_/\_/ \___|_|      
"""
VERSUS = r"""
| | / / ___/
| |/ (__  ) 
|___/____/  
"""
GAME_DATA_LENGTH = len(game_data)
MAX_LENGTH_OF_RECENT = 5


def clear_terminal():
    """cross-platform way to clear the terminal screen"""
    system("cls||clear")


def refresh_display():
    """clear the terminal screen and (re)print the logo"""
    clear_terminal()
    print(LOGO)


def easy_debug(obj, msg=""):
    """Easy print objects for debugging"""
    print("\nDebug:")
    print(f" - {msg} {obj}\n")


def update_recent_entities(latest, max_length=MAX_LENGTH_OF_RECENT):
    """Updates the GLOBAL list of the most recently used entities!
    When more than MAX_LENGTH items: Removes the oldest item first, then...
    Appends the index for the latest item onto the list.
    """
    easy_debug(recent_entity_ids, "(fnc:update_recent) Entry List:")
    current_length = len(recent_entity_ids)
    if current_length == max_length:
        recent = [recent_entity_ids[i] for i in range(1, max_length)]
    else:
        recent = recent_entity_ids
    recent.append(latest)
    easy_debug(recent, "(fnc:update_recent) Exit List:")
    return recent


def get_random_id():
    """Returns a random index number for the `game_data` List"""
    return randint(0, GAME_DATA_LENGTH - 1)


def get_random_entity_id():
    """Returns a randomly selected EntityID,
    that is NOT in the given list of recently used IDs"""
    recent = True
    while recent:
        entity_id = get_random_id()
        if entity_id not in recent_entity_ids:
            recent = False
    easy_debug(entity_id, "(fnc:get_random_entity_id) EntityID:")
    return entity_id


def get_entity_data(index):
    """Returns the Dictionary at the given index from the `game_data` List"""
    return game_data[index]


def display_entity_info(entity):
    """Prints out the entity information to be displayed.
    Expects a Dictionary comprising the following Keys:
    - 'name', 'description', 'country', 'follower_count'
    """
    print(f"Name: {entity['name']}")
    print(f"Description: {entity['description']}")
    print(f"Country: {entity['country']}")


def display_game_round(one, two):
    """Prints the display output for the current game round"""
    refresh_display()
    display_entity_info(one)
    print(VERSUS)
    display_entity_info(two)


def get_player_choice():
    """Prompts the player to select their choice for this round,
    Takes their input and validates it,
    Returns their choice as an EntityID [Integer]"""
    valid = False
    while not valid:
        print("\nWho has more followers?")
        choice = input("- Enter 1 or 2: ")
        if choice in ['1', '2']:
            valid = True
        else:
            print("Please enter only 1 or 2!")
    return int(choice)


def get_comparison_option():
    """Returns a Tuple containing a single Entity as (ID, Data)"""
    entity_id = get_random_entity_id()
    entity_data = get_entity_data(entity_id)
    # pylint: disable-next=global-statement
    global recent_entity_ids
    recent_entity_ids = update_recent_entities(entity_id)
    return (entity_id, entity_data)


# Initialise:
recent_entity_ids = []
refresh_display()

# Start game:
compare_this = get_comparison_option()
against_this = get_comparison_option()

easy_debug(compare_this, "Compare Entity 1:")

display_game_round(compare_this[1], against_this[1])
player_choice = get_player_choice()

if player_choice == 1:
    if compare_this[1]['follower_count'] > against_this[1]['follower_count']:
        print("Correct!")
    else:
        print("Sorry, you loose!")
else:
    if against_this[1]['follower_count'] > compare_this[1]['follower_count']:
        print("Correct!")
    else:
        print("Sorry, you loose!")
