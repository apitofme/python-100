"""
-=< 100 Days of Python >=-
-=[ Day 019 ]=-
"""
from turtle import Turtle, Screen
"""
L.143 & L.144 - Challenge: Create a Racing Turtles Minigame

> Create a Screen and populate it with multiple Turtles. Each one should be a
different colour, and they should be positioned spaced out vertically along
the left-hand edge of the screen.

> Prompt the player to guess which turtle will win the race.
"""
window = Screen()
window.setup(width=500, height=400)

# [DEBUG]:: Sanity checks (help my understanding of the different methods)
# print(f"Canvas: {window.screensize()}")
# print(f"Window: w={window.window_width()}, h={window.window_height()}")

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

bet = window.textinput(
    title="Place your bets..",
    prompt="Which turtle will win the race? Enter a colour: "
)

# Pre-calculate coordinates:
x_scale = window.window_width() // 2
y_scale = window.window_height() // 2
divisions = len(colours)
if divisions % 2 == 0:
    equal_dist = y_scale / (divisions // 2 + 1)
else:
    equal_dist = y_scale / ((divisions + 1) // 2)
print(f"Eq.D = {equal_dist}")

turtles = []
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
    print(start_y)
    t.goto(start_x, start_y)
    # store the turtle
    turtles.append(t)

window.exitonclick()
