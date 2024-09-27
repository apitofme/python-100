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
OR = r"""
  ____  _____
 / __ \/ ___/
/ /_/ / /    
\____/_/     
"""
GAME_DATA_LENGTH = len(game_data)
MAX_LENGTH_OF_RECENT = 8


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
        print(f" - {msg} {obj}")
    print("\n")


def update_recent_entities(latest, max_length=MAX_LENGTH_OF_RECENT):
    """Updates the GLOBAL list of the most recently used entities.
    When more than MAX_LENGTH items: Removes the oldest item first, then...
    Appends the index for the latest item onto the list.
    """
    ezdbg.append([latest, "(fnc:update_recent) Latest ID:"])

    current_length = len(recent_entity_ids)
    if current_length == max_length:
        recent = [recent_entity_ids[i] for i in range(1, max_length)]
    else:
        recent = recent_entity_ids
    recent.append(latest)
    # NOTE: Have to use an F-String to debug so it passes the current value,
    # rather than a reference to the variable, which is updated again before
    # it get's printed out ... meaning BOTH values are shown both times!
    ezdbg.append([f"{recent}", "(fnc:update_recent) Updated List:"])
    return recent


def get_random_entity_id():
    """Returns a randomly selected index ID from `game_data`,
    ensuring that is NOT in the list of recently used IDs"""
    recent = True
    while recent:
        entity_id = randint(0, GAME_DATA_LENGTH - 1)
        if entity_id not in recent_entity_ids:
            recent = False
    # easy_debug(entity_id, "(fnc:get_random_entity_id) EntityID:")
    return entity_id


def get_entity_info(entity_id):
    """Returns the dictionary from `game_data` at the given index"""
    return game_data[entity_id]


def format_entity_info(entity):
    """Returns a formatted String of the information for the given entity,
    a Dictionary object, which must contain the following Keys:
    -- 'name', 'description', 'country', 'follower_count'
    """
    output = f"{entity['name']}: "
    output += f"a {entity['description']}, "
    output += f"from {entity['country']}"
    return output


def display_game_round():
    """Prints the display output for the current game round"""
    for i, data_id in enumerate(game_round, 1):
        print(f"{i}. " + format_entity_info(game_data[data_id]))
        if i == 1:
            print(OR)


def get_player_choice():
    """Prompts the player to select their choice for this round,
    Returns an Integer (the `game_data` index for the chosen entity)"""
    valid = False
    while not valid:
        print("\nWho has more followers?")
        choice = input("- Enter 1 or 2: ")
        if choice in ['1', '2']:
            valid = True
        else:
            print("Please enter only 1 or 2!")
    return game_round[int(choice) - 1]


def display_win():
    """Displays the 'won' message and current game score"""
    print(f"Correct! Current score: {score}")


def display_lose():
    """Displays the 'game over' message and final game score"""
    print(f"Sorry, you got it wrong! Final score: {score}\n")


def get_correct_answer():
    """Checks which option has the highest number of followers.
    Returns an Integer [index ID]"""
    if (
        game_data[game_round[0]]['follower_count']
        > game_data[game_round[1]]['follower_count']
    ):
        highest = game_round[0]
    else:
        highest = game_round[1]

    # ezdbg.append([game_data[game_round[0]], "(fnc:get_correct_answer) 1:\n"])
    # ezdbg.append([game_data[game_round[1]], "(fnc:get_correct_answer) 2:\n"])
    ezdbg.append([
        f"{game_data[highest]['name']}; FC={
            game_data[highest]['follower_count']}",
        f"(fnc:get_correct_answer) Highest: ID={highest};"
    ])

    return highest


def play_again():
    """Asks the player if they would like to play again.
    Returns a Boolean"""
    response = False
    while not response:
        response = input("Would you like to play again? "
                         "(Type 'y' to play again, type 'n' to quit): "
                         ).lower()
        if response not in ['y', 'n']:
            print("Sorry, please type 'y' or 'n'!")
            response = False

    if response == 'y':
        return True

    return False


##
# Start game:
##
# Initialise Global Variables:
ezdbg = []
recent_entity_ids = []
current_round = 0
score = 0
# correct_answer = None
# 1. Get initial random entity for comparison:
random_entity = get_random_entity_id()
# NOTE:
# Each round compares a new entity with the 'second' from the previous round.
# We will save this value later, then generate a new one for the next round.
# -- We can also go ahead and update the 'recent' list now too:
recent_entity_ids = update_recent_entities(random_entity)
# -- We also need to initialise the List for the round (because I used a List!)
game_round = [None, random_entity]

# Repeatable Game Loop ('main')
play = True
while play:
    # 1. Set the first entity for this round, updated from the previous round:
    # first_entity = second_entity
    # 2. Get a NEW random second entity for comparison:
    # second_entity = get_random_entity_id()
    # -- Update the game for a new round of comparisons:
    game_round = [game_round[1], get_random_entity_id()]
    # -- AND update the list of recently used entities:
    recent_entity_ids = update_recent_entities(game_round[1])
    ezdbg.append([game_round, "Current IDs:"])

    # -- We can also work out, ahead of time, which answer will win this round!
    correct_answer = get_correct_answer()

    # NOW we can start to handle the game's display output...
    # -- Clear the screen and display the game's logo
    refresh_display()

    # -- Print out any debug messages we accumulated, and reset the list
    if ezdbg:
        easy_debug(ezdbg)
        ezdbg = []

    # -- Determine if the the player won or lost the last round, and show the
    #    relevant message(s):
    # Check >> if the round counter is -1 (means the player LOST)
    if current_round < 0:
        display_lose()

        # Ask player if they want to play again...
        if not play_again():
            # If NOT we can go ahead and exit the game-loop!
            break

        # ...but to play again we must reset the game variables:
        recent_entity_ids = []
        current_round = 0
        score = 0
        # NOTE: Rest game_round, or generate new random seed ID?!!
        # - and loop back to the start
        continue

    # Check >> if this isn't the first round (means the player WON)
    if current_round > 0:
        # 8. Keep track of the player's score:
        score = current_round
        display_win()

    # -- Update the round counter and display the current round:
    current_round += 1
    print(
        f">> Round {current_round}... "
        "Who has the most followers on Social Media?\n"
    )

    # 3. Display the output for this round: First vs Second
    display_game_round()

    # 4. Ask player to guess which entity has the most followers:
    player_choice = get_player_choice()
    ezdbg.append([player_choice, "Player chose [ID]:"])
    # NOTE: The debug message won't be shown until the next round!

    # 5. Check the player's guess:
    # 6. If player was wrong: game over...
    if player_choice != correct_answer:
        # set the round counter to -1 to signify the player lost
        current_round = -1

    # 7. If player was right: play on...
    # -- i.e. let the game-loop continue (no need to do anything here!)

    # Update the debug output for 'recent IDs'
    # -- F-String ensures the value at THIS moment is used!
    ezdbg.append([f"{recent_entity_ids}", "Recent IDs:"])

print("Thank you for playing!")
