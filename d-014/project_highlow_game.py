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


def update_recent(latest, recent, max_length=MAX_LENGTH_OF_RECENT):
    """Updates a given list of the most recently used entities.
    When more than MAX_LENGTH items: Removes the oldest item first, then...
    Appends the index for the latest item onto the list
    """
    easy_debug(recent, "(fnc:update_recent) Entry List:")
    current_length = len(recent)
    if current_length == max_length:
        recent = [recent[i] for i in range(1, max_length)]
    recent.append(latest)
    easy_debug(recent, "(fnc:update_recent) Exit List:")
    return recent


def get_next_data(recent):
    """Returns a randomly selected entity from the list of game data"""
    selected = randint(0, len(game_data)-1)
    while selected in recent:
        selected = randint(0, len(game_data)-1)
    recent = update_recent(selected, recent)
    return (recent, [selected, game_data[selected]])


def display_entity_info(entity):
    """Prints out the entity information to be displayed.
    Expects a Dictionary comprising the following fields:
    - 'name', 'description', 'country', 'follower_count'
    """
    print(f"Name: {entity.name}")
    print(f"Description: {entity.description}")
    print(f"Country: {entity.country}")


recent_selections = []
refresh_display()

recent_selections, option_one = get_next_data(recent_selections)
recent_selections, option_two = get_next_data(recent_selections)
