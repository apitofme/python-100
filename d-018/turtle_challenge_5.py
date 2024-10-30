"""
-=< 100 Days of Python >=-
-=[ Day 018 ]=-
"""
import random
from turtle import Turtle, Screen
"""
L.135 - Turtle Challenge 5: Draw a Spirograph
"""
pen = Turtle()
window = Screen()

# Pre drawing set up
window.colormode(255)
pen.down()
pen.speed(0)
# Ref: https://docs.python.org/3.12/library/turtle.html#turtle.speed


def draw_spirograph(radius, count):
    """Draws {count} number of circles with a radius of {radius}
    Each offset by the result of: 360 / {count}"""
    for _ in range(count):
        r, g, b = random.sample(range(0, 255), 3)
        pen.color((r, g, b))
        pen.circle(radius)
        # Change the angle so the next circle is offset
        pen.left(360 / count)


draw_spirograph(100, 30)

# Keep the display window open until we click on it
window.exitonclick()
