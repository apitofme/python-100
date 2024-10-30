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

for _ in range(100):
    colour = (r, g, b) = random.sample(range(0, 255), 3)
    pen.color(colour)
    pen.circle(100)
    # Change the angle so the next circle is offset
    pen.left(3.6)

# Keep the display window open until we click on it
window.exitonclick()
