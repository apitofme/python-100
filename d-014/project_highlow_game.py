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


def get_random_id():
    """Returns a random index number for the `game_data` List"""
    return randint(0, GAME_DATA_LENGTH - 1)


def get_random_entity_id():
    """Returns a randomly selected EntityID from `game_data`,
    ensuring that is NOT in the list of recently used IDs"""
    recent = True
    while recent:
        entity_id = get_random_id()
        if entity_id not in recent_entity_ids:
            recent = False
    # easy_debug(entity_id, "(fnc:get_random_entity_id) EntityID:")
    return entity_id


def display_entity_info(entity):
    """Prints out the information from the given `game_data` Item,
    a Dictionary, comprising the following Keys:
    - 'name', 'description', 'country', 'follower_count'
    """
    print(f"Name: {entity['name']}")
    print(f"Description: {entity['description']}")
    print(f"Country: {entity['country']}")


def display_game_round():
    """Generate the display output for the current game round"""
    for i, data_id in enumerate(game_round):
        display_entity_info(game_data[data_id])
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
    return game_round[int(choice) - 1]


def get_new_round(first=False):
    """Creates a new game round with two `game_data` index IDs to compare.
    Returns a List [id_1, id_2]"""
    if not first:
        first = get_random_entity_id()
    second = get_random_entity_id()
    return [first, second]


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
ezdbg = []

# Initialise Global Variables:
# refresh_display()
recent_entity_ids = []
current_round = 0
score = 0
correct_answer = None
# 1. Get a first random ID:
first_id = False
# We only need to initialise this to a FALSE boolean for now because
# later on the 'get_new_round' function will take care of it for us.

# Repeatable Game Loop ('main')
play = True
while play:
    # We can put the game logic at the start of the loop
    # BEFORE we need to worry about any display output...

    # 1. Get a first random ID:
    # 2. Get a second random ID:
    game_round = get_new_round(first_id)
    # We allow ourselves to specify the 'first' ID in the function call because
    # we want to compare against the 'second' ID from each previous round.

    # Update the 'recent' list:
    ezdbg.append([game_round, "Current IDs:"])
    # recent_entity_ids = list(set(recent_entity_ids + game_round))
    if current_round == 0:
        # First round of the game we need to add the first ID too
        recent_entity_ids = update_recent_entities(game_round[0])
    # All subsequent rounds we just add the second ID,
    # because there is only one new ID per round
    recent_entity_ids = update_recent_entities(game_round[1])

    # ...including working, out ahead of time, which answer will win this round
    correct_answer = get_correct_answer()

    # NOW we can start to handle the game's display output...
    # Clear the screen and display the game's logo
    refresh_display()

    # Print out any debug messages we accumulated, and reset the list
    if ezdbg:
        easy_debug(ezdbg)
        ezdbg = []

    # Determine if the last round was WON or LOST...
    # We'll set the round counter to -1 if the player lost, so
    if current_round < 0:
        display_lose()
        # Ask player if they want to play again...
        if play_again():
            # - To play again we must reset the game variables
            current_round = 0
            recent_entity_ids = []
            correct_answer = None
            first_id = False
        else:
            # - Otherwise we can go ahead and exit the game-loop
            # play = False
            break

    # But if this isn't the first round then the player MUST have won previously
    # so we can display the "win" message and their current score
    elif current_round > 0:
        display_win()

    # Update the round counter to display the current round
    current_round += 1
    print(f">> Round {current_round}...\n")

    # 3. Display the game's round: First vs Second
    display_game_round()

    # 4. Ask player to guess which has the most followers:
    player_choice = get_player_choice()
    ezdbg.append([player_choice, "Player chose [ID]:"])

    # 5. Check the player's guess:
    # 6. If player was wrong: game over...
    if player_choice != correct_answer:
        # set the round counter to -1 to signify the player lost
        current_round = -1

    # 7. If player was right: play on...
    else:
        # 8. Keep track of score: update the score for a win
        score = current_round
        # The next round compares against the second option from this round
        first_id = game_round[1]

    # Update the debug output for 'recent IDs'
    # > F-String ensures the value at THIS moment is used!
    ezdbg.append([f"{recent_entity_ids}", "Recent IDs:"])

print("Thank you for playing!")
