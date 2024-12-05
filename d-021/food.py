"""
-=< 100 Days of Python >=-
-=[ Day 021 ]=-

Project: Build the 'Snake' Game
NOTE: For "Part 2" all OOP Classes are now in their own files!

>> Food Class
"""
from turtle import Turtle
from random import randint


class Food(Turtle):
    """Class defining all attributes and methods relating to the Food
    objects for the Snake Game"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Places the 'food' Turtle Object at a random location"""
        # Keep the food a sensible distance from the edges of the Screen...
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
        # Place the food in a random location:
        self.goto(random_x, random_y)
