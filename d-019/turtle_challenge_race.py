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
window = Screen()
window.setup(width=500, height=400)

# [DEBUG]:: Sanity checks (help my understanding of the different methods)
# print(f"Canvas: {window.screensize()}")
# print(f"Window: w={window.window_width()}, h={window.window_height()}")

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Pre-calculate coordinates:
x_scale = window.window_width() // 2
y_scale = window.window_height() // 2
divisions = len(colours)
if divisions % 2 == 0:
    equal_dist = y_scale / (divisions // 2 + 1)
else:
    equal_dist = y_scale / ((divisions + 1) // 2)
# print(f"Eq.D = {equal_dist}")

turtles = []
for n, colour in enumerate(colours):
    # set up the turtle:
    t = Turtle(shape='turtle')
    t.penup()
    t.color(colour)
    t.name = colour
    print(f"Turtle has been given the name: {t.name}")
    # set up the start position:
    start_x = -(x_scale) + 10  # <- Not off screen!
    start_y = -(y_scale) + (equal_dist * (n + 1))
    # ...compensate for even number of divisions...
    if divisions % 2 == 0:
        # ...by adding half of the equal distance
        start_y += equal_dist / 2
    # print(start_y)
    t.goto(start_x, start_y)
    # store the turtle
    turtles.append(t)

# Take the player's bet (with validation):
bet = ""
while bet.lower() not in colours:
    bet = window.textinput(
        title="Place your bets..",
        prompt="Which turtle will win the race? Enter a colour: "
    )

# Set up for the race:
finish_line = x_scale - 25  # <- Not off screen!
winner = None
race_over = False

# Race the turtles:
while not race_over:
    for t in turtles:
        x_pos = t.xcor()
        # Calculate a move for the turtle, a random distance forward...
        n_pos = x_pos + random.randint(1, 10)
        # ...but prevent it from going off screen
        if n_pos > finish_line:
            t.setx(finish_line)
            if winner is None:
                winner = t.pencolor()
        else:
            t.setx(n_pos)
    # Check for winner before looping
    if winner is not None:
        race_over = True

# Check the winner:
msg_title = "Race Results:"
msg_text = f"The {winner.capitalize()} turtle won.\n"
if winner == bet.lower():
    msg_text += "Congratulations, you won!"
else:
    msg_text += "Sorry, you lost the bet!"

# Tap in to the "TK" class from the turtle module (tkinter object)
# to display a messagebox window on our screen:
TK.messagebox.showinfo(title=msg_title, message=msg_text)

window.exitonclick()
