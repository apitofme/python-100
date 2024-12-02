"""
-=< 100 Days of Python >=-
-=[ Day 020 ]=-

Project: Build the 'Snake' Game
NOTE: The goal for this project will be split over the next 2 days!
"""
from turtle import Turtle, Screen
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
# Define constants:
SNAKE_BODY_UNIT_SIZE = 20
SNAKE_START_LENGTH = 3


def get_head_position():
    """Get the position for the 'head' segment of the Snake"""
    return snake_body[0].pos()


def set_head_position(x, y):
    """Set the position for the 'head' segment of the Snake"""
    head = snake_body[0]
    head.setpos(x, y)


# Initialise and configure Screen object:
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Turtle: Snake Game")

# Initialise starting 'snake' turtles:
snake_body = []
for _ in range(SNAKE_START_LENGTH):
    t = Turtle(shape="square")
    t.penup()
    t.color("white")
    snake_body.append(t)

snake_length = len(snake_body)

for i in range(snake_length):
    head_x, head_y = get_head_position()
    if i > 0:
        new_x = head_x - (SNAKE_BODY_UNIT_SIZE * i)
        new_y = head_y  # <- Currently Horizontal!
        snake_body[i].setpos(new_x, new_y)

window.exitonclick()
