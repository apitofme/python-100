"""
-=< 100 Days of Python >=-
-=[ Day 021 ]=-

Project: Build the 'Snake' Game
NOTE: For "Part 2" all OOP Classes are now in their own files!

>> Snake Class
"""
from turtle import Turtle
from enum import Enum


class Direction(Enum):
    """Enum Class defining directions for the Snake's movement"""
    UP = 90
    LEFT = 180
    DOWN = 270
    RIGHT = 0


class Snake:
    """Class defining all properties and methods belonging to the 'Snake'
    object for the Turtle Snake Game
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

    def up(self):
        """Changes the Snake's heading to Up/North"""
        if self.head.heading() != Direction.DOWN.value:
            self.head.seth(Direction.UP.value)

    def down(self):
        """Changes the Snake's heading to Down/South"""
        if self.head.heading() != Direction.UP.value:
            self.head.seth(Direction.DOWN.value)

    def left(self):
        """Changes the Snake's heading to Left/West"""
        if self.head.heading() != Direction.RIGHT.value:
            self.head.seth(Direction.LEFT.value)

    def right(self):
        """Changes the Snake's heading to Right/East"""
        if self.head.heading() != Direction.LEFT.value:
            self.head.seth(Direction.RIGHT.value)

    def turn_left(self):
        """Turns the Snake 90 degrees to the Left"""
        self.head.lt(90)

    def turn_right(self):
        """Turns the Snake 90 degrees to the Right"""
        self.head.rt(90)
