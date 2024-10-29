"""
-=< 100 Days of Python >=-
-=[ Day 018 ]=-
"""
import random
from turtle import Turtle, Screen
"""
L.132 - Turtle Challenge 3: Drawing Different Shapes

For this challenge we want you to draw a series of shapes from a Triangle
(with 3 sides) up to a Decagon (with 10 sides), with each shape drawn in a
random colour.
"""
brush = Turtle()
window = Screen()

# Set the colourmode for RGB
# Ref: https://docs.python.org/3/library/turtle.html#turtle.colormode
window.colormode(255)
brush.pd()

for sides in range(3, 11):
    angle = 360 / sides
    colour = (r, g, b) = random.sample(range(0, 255), 3)
    # Ref: https://docs.python.org/3.12/library/random.html#random.sample
    brush.pencolor(colour)
    for _ in range(sides):
        brush.forward(100)
        brush.left(angle)

# Keep the display window open until we click on it
window.exitonclick()
