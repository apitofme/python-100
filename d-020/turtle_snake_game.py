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
        self.head = self.segments[0]

    @property
    def length(self):
        """Returns an Integer: the length of the 'segments' List"""
        return len(self.segments)

#    @property
#    def head(self):
#        """Returns a Turtle object: the First in the 'segments' List"""
#        return self.segments[0]
# NOTE: The 'head' will ALWAYS be the first item in the segments list!

    @property
    def tail(self):
        """Returns a Turtle object: the Last in the 'segments' List"""
        return self.segments[-1]

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
        return self.head.pos()

    def set_head_position(self, x, y=None):
        """Set the position for the 'head' segment of the Snake"""
        if y is not None:
            self.head.setpos(x, y)
        else:
            self.head.setpos(x)

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

    def turn_left(self):
        """Turns the Snake 90 degrees to the Left"""
        self.head.lt(90)

    def turn_right(self):
        """Turns the Snake 90 degrees to the Right"""
        self.head.rt(90)

#    def direction_up(self):
#        """Changes the Snake's heading to Up/North"""
#        self.head.seth(90)

#    def direction_down(self):
#        """Changes the Snake's heading to Down/South"""
#        self.head.seth(270)

#    def direction_left(self):
#        """Changes the Snake's heading to Left/West"""
#        self.head.seth(180)

#    def direction_right(self):
#        """Changes the Snake's heading to Right/East"""
#        self.head.seth(0)


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
window.listen()
# window.onkey(snake.direction_up, "Up")
# window.onkey(snake.direction_down, "Down")
window.onkey(snake.turn_left, "Left")
window.onkey(snake.turn_right, "Right")

game_over = False
while not game_over:
    window.update()
    time.sleep(0.125)
    snake.move()

window.exitonclick()
