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
 _   _______
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
    if isinstance(obj, list):
        for o, m in obj:
            print(f" - {m} {o}")
    else:
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


def display_game_round():
    """Prints the display output for the current game round"""
    refresh_display()
    for i, data_id in enumerate(game_round):
        # easy_debug(i, "(fnc:display_game_round) Loop counter:")
        display_entity_info(get_entity_data(data_id))
        if i == 0:
            print(VERSUS)


def get_player_choice():
    """Prompts the player to select their choice for this round,
    Takes their input and validates it,
    Returns an Integer (list index for choice in current `game_round`)"""
    valid = False
    while not valid:
        print("\nWho has more followers?")
        choice = input("- Enter 1 or 2: ")
        if choice in ['1', '2']:
            valid = True
        else:
            print("Please enter only 1 or 2!")
    return int(choice) - 1


def get_comparison_option():
    """Returns a Tuple containing a single Entity as (ID, Data)"""
    entity_id = get_random_entity_id()
    entity_data = get_entity_data(entity_id)
    # pylint: disable-next=global-statement
    global recent_entity_ids
    recent_entity_ids = update_recent_entities(entity_id)
    return (entity_id, entity_data)


def new_round(first=False):
    """Create a new comparison round"""
    if not first:
        first = get_random_entity_id()
    second = get_random_entity_id()
    return [first, second]


def display_win():
    """Displays the current game score if the player won the last round"""
    print(f"Correct! Current score: {current_round}")


def display_lose():
    """Displays the current game score if the player lost"""
    print(f"Sorry, you got it wrong! Final score: {current_round}")


def get_highest():
    """Returns the index ID of the entity with the highest follower count
    for the current round"""
    debug_me = []
    round_data = []
    for data_id in game_round:
        round_data.append([data_id, game_data[data_id]])

    debug_me.append([
        [round_data[0][0], round_data[0][1]['follower_count']],
        "(fnc:get_highest) D1:"
    ])
    debug_me.append([
        [round_data[1][0], round_data[1][1]['follower_count']],
        "(fnc:get_highest) D2:"
    ])

    if round_data[0][1]['follower_count'] > round_data[1][1]['follower_count']:
        highest = round_data[0][0]
    else:
        highest = round_data[1][0]

    debug_me.append([highest, "(fnc:get_highest) Highest ID:"])
    easy_debug(debug_me)

    return highest


def check_answer():
    """Checks if the Player's choice was correct
    - i.e. has the highest number of followers
    Returns a Boolean"""
    if player_choice == get_highest():
        return True
    return False


# Initialise:
recent_entity_ids = []
current_round = 0
refresh_display()

# Start game:
# 1. Get a (first) random ID
# ?? start_id = get_random_entity_id()

# 2. Get a second random ID
# !! game_round = new_round(start_id)
game_round = new_round()
easy_debug(game_data[game_round[0]], "First:")
# 3. Display info: First vs Second
display_game_round()

# 4. Ask player to guess which has the most followers
player_choice = game_round[get_player_choice()]
easy_debug(player_choice, "Player's choice [ID]:")

# 5. Check the player's guess
correct = check_answer()

# 6. If player was right, play on:
#    - i.e. select a new ID to play against their answer
if correct:
    current_round += 1
    refresh_display()
    display_win()
    game_round = new_round(game_round[1])

# 7. If player was wrong, game over:
#    - ask to play again?
else:
    refresh_display()
    display_lose()
    # ask player to play again?

# 8. Keep track of score (i.e. How many rounds guessed right?)
# - This is taken care of with the `current_round` variable!
