"""
-=< 100 Days of Python >=-
-=[ Day 019 ]=-
"""
from turtle import Turtle, Screen, TK
import random
"""
L.143 & L.144 - Challenge: Create a Racing Turtles Minigame

> Create a Screen and populate it with multiple Turtles. Each one should be a
different colour, and they should be positioned spaced out vertically along
the left-hand edge of the screen.

> Prompt the player to guess which turtle will win the race.

> Have the turtles move at random increments across the screen until one has
reached the "finish line" (i.e. the right hand edge of the screen).

> Check which turtle has won the race and notify the player if they won or
lost their bet.
"""


def initialise_turtles():
    """Initialises the Turtle objects for the Race:
    Determines the Screen dimensions and calculates starting positions,
    placing each Turtle along the left-hand edge of the screen.
    Returns a List of initialised Turtle objects"""
    # Pre-calculate coordinates:
    x_scale = window.window_width() // 2
    y_scale = window.window_height() // 2
    divisions = len(colours)
    if divisions % 2 == 0:
        equal_dist = y_scale / (divisions // 2 + 1)
    else:
        equal_dist = y_scale / ((divisions + 1) // 2)
    # print(f"Eq.D = {equal_dist}")

    all_turtles = []
    for n, colour in enumerate(colours):
        # set up the turtle:
        t = Turtle(shape='turtle')
        t.penup()
        t.color(colour)

        # set up the start position:
        start_x = -(x_scale) + 10  # <- Not off screen!
        start_y = -(y_scale) + (equal_dist * (n + 1))
        # ...compensate for even number of divisions...
        if divisions % 2 == 0:
            # ...by adding half of the equal distance
            start_y += equal_dist / 2
        # print(start_y)
        t.goto(start_x, start_y)

        all_turtles.append(t)

    return all_turtles


def get_player_bet():
    """Ask the player to bet (guess) which Turtle will win the Race:
    Displays a TextInput window with a prompt.
    Returns a String of the player's bet (validated to a Turtle colour)"""
    player_bet = ""
    while player_bet.lower() not in colours:
        player_bet = window.textinput(
            title="Place your bets..",
            prompt="Which turtle will win the race? Enter a colour: "
        )
    return player_bet


def race_turtles(all_turtles: list):
    """Races the given list of Turtle objects by moving them in small,
    random increments across the Screen (global object).
    Returns a String identifying the race winner (by colour)"""
    # Set up for the race:
    finish_line = window.window_width() // 2 - 25  # <- Not off screen!
    race_winner = None

    # Race the turtles:
    while race_winner is None:
        for t in all_turtles:
            x_pos = t.xcor()
            # Calculate a move for the turtle a random distance forward:
            new_pos = x_pos + random.randint(1, 10)
            # If the new position is BEFORE the finish line...
            if new_pos < finish_line:
                # ...move the Turtle to the new position
                t.setx(new_pos)
            # Otherwise...
            else:
                # ...prevent the Turtle from going past the finish line
                t.setx(finish_line)
                # If this Turtle was the FIRST to reach the finish...
                if race_winner is None:
                    # ...then they're the winner:
                    race_winner = t.pencolor()
    return race_winner


def check_winner(player_bet: str, race_winner: str):
    """Returns a String based on the winner of the race vs player's bet"""
    if race_winner == player_bet.lower():
        return "Congratulations, you won!"
    return "Sorry, you lost the bet!"


# Initialise the Screen object:
window = Screen()
window.setup(width=500, height=400)
# [DEBUG]:: Sanity checks (help my understanding of the different methods)
# print(f"Canvas: {window.screensize()}")
# print(f"Window: w={window.window_width()}, h={window.window_height()}")

# Define the racer's colours:
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# MAIN GAME PROCESS:
turtles = initialise_turtles()
bet = get_player_bet()
winner = race_turtles(turtles)

# Race results:
msg_title = "Race Results:"
msg_text = f"The {winner.capitalize()} turtle won.\n"
msg_text += check_winner(bet, winner)
# Tap in to the "TK" class from the turtle module (tkinter object)
# to display a messagebox window on our screen:
TK.messagebox.showinfo(title=msg_title, message=msg_text)

# Automatically close the race window:
window.bye()
