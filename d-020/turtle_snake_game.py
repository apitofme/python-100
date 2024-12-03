"""
-=< 100 Days of Python >=-
-=[ Day 020 ]=-

Project: Build the 'Snake' Game
NOTE: The goal for this project will be split over the next 2 days!
"""
from turtle import Turtle, Screen
import time
"""
Snake Game - Part 1:

Over the course of today's lessons we will begin to implement our own version
of the classic 'Snake' arcade game, made famous (again) by Nokia mobile phones
in the 90's.

> L.147 - Screen Setup and Creating a Snake Body
> L.148 - Animating the Snake Segments on Screen
> L.149 - Create a Snake Class & Move to OOP
> L.150 - How to Control the Snake with a Keypress
"""


class Snake:
    """Defines all properties and methods belonging to the 'Snake' object
    for the Turtle Snake Game
    """

    # Define constants:
    SEGMENT_SIZE = 20
    START_LENGTH = 3

    def __init__(self):
        self.segments = []
        # Initialise the starting Snake body segments:
        for i in range(self.START_LENGTH):
            segment = self.new_segment()
            segment.setx(-(self.SEGMENT_SIZE * i))
            self.add_segment(segment)

    @property
    def length(self):
        """Returns an Integer: the length of the 'segments' List"""
        return len(self.segments)

    def new_segment(self):
        """Create a new segment (i.e. a Turtle object) for the Snake.
        Returns a Turtle object instance"""
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        # Resize turtles down to 10x10:
        # segment.resizemode('user')
        # segment.shapesize(0.5, 0.5, 1)
        return segment

    def add_segment(self, segment=None):
        """Adds a new segment to the Snake's body"""
        if segment is not None:
            self.segments.append(segment)
        else:
            self.segments.append(self.new_segment())

    def get_head_position(self):
        """Get the position for the 'head' segment of the Snake"""
        return self.segments[0].pos()

    def set_head_position(self, x, y=None):
        """Set the position for the 'head' segment of the Snake"""
        if y is not None:
            self.segments[0].setpos(x, y)
        else:
            self.segments[0].setpos(x)

    def move(self):
        """Moves the snake's body"""
        # Working from the last segment towards the 'head'...
        for n in range(self.length-1, 0, -1):
            # Set the position of the current segment
            # to that of the one in front of it...
            self.segments[n].setpos(
                self.segments[n-1].pos()
            )
        # Finally update the position of the 'head' segment:
        self.segments[0].forward(self.SEGMENT_SIZE)


# Initialise and configure Screen object:
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Turtle: Snake Game")
# Turn animation off
window.tracer(0)
# NOTE: MUST manually call 'update()' to refresh the screen!

snake = Snake()
window.update()
# window.exitonclick()

game_over = False
while not game_over:
    window.update()
    time.sleep(0.125)
    snake.move()

window.exitonclick()
