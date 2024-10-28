"""
-=< 100 Days of Python >=-
-=[ Day 018 ]=-
"""
from turtle import Turtle, Screen
"""
L.128 - The Turtle Graphics Module and Documentation

Today we're going to use a built-in Python module called "Turtle", which is a
graphical library (based on tkinter), and essentially it allows us to draw in a
dedicated window on the screen. The window provides the canvas, and we draw by
using commands to move the 'turtle' around, change it's size/shape/colour,
lift/drop it's pen and so on.

There will be a number of challenges using this library over the next few
lessons, each growing in complexity. However these aren't just about your code,
part of the challenge in these short projects is learning to use documentation,
and research how to do what you need to with the module in order to use it.
This is something every developer/programmer does regularly, regardless of
skill or experience, especially when using a new module for the first time!

Below are some links which will be useful for you to reference while completing
these lessons, though you should also feel comfortable doing your own research.
Use a search engine and StackOverflow (for example) to help you figure out how
to complete these challenges.

Refs:
- Documentation: https://docs.python.org/3/library/turtle.html
- Colour Picker: https://trinket.io/docs/colors
- Colour Guide: https://cs111.wellesley.edu/reference/colors
"""

"""
L.129 - Turtle Challenge 1: Draw a Square
- The square should be 100 units long on each side.
"""
brush = Turtle()

# Use our "Turtle" to draw a square
brush.pendown()
for _ in range(4):
    brush.forward(100)
    brush.left(90)
brush.penup()

# Keep the display window open until we click on it
window = Screen()
window.exitonclick()
