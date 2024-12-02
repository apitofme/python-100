"""
-=< 100 Days of Python >=-
-=[ Day 019 ]=-
"""
from turtle import Turtle, Screen
"""
L.141 - Challenge: Make an Etch-a-Sketch App

The goal for this challenge is to use event listeners and key-event bindings
to create a Turtle program where the movement is controlled by the User via
the keyboard, in essence recreating the basis of the classic childhood toy
"Etch-a-Sketch".

Use the 'W,A,S,D' keys for movement and the 'C' key to clear and reset the
screen, moving the Turtle back to the center.
"""
# Create objects:
pen = Turtle()
window = Screen()

scale_factor = 1
# NOTE: Maybe separate the applied scale-factor for MOVEMENT and TURNING!

# autopep8: off
# pylint: disable=missing-function-docstring
# Define the necessary functions:
def move_forward():
    #print(f"Forward: scale-factor: {scale_factor}")
    pen.fd(1 * scale_factor)

def move_backward():
    #print(f"Backwards: scale-factor: {scale_factor}")
    pen.bk(1 * scale_factor)

def turn_left():
    #print(f"Left: scale-factor: {scale_factor}")
    pen.lt(1 * scale_factor)

def hard_left():
    pen.lt(90)

def turn_right():
    #print(f"Right: scale-factor: {scale_factor}")
    pen.rt(1 * scale_factor)

def hard_right():
    pen.rt(90)

def direction_up():
    pen.seth(90)

def direction_down():
    pen.seth(270)

def direction_left():
    pen.seth(180)

def direction_right():
    pen.seth(0)

# pylint: disable=global-statement
def increase_scale():
    global scale_factor
    scale_factor += 1
    print(scale_factor)

def decrease_scale():
    global scale_factor
    if scale_factor > 1:
        scale_factor -= 1
        print(scale_factor)
    else:
        print("Scale Factor cannot go below '1'!")

def screen_reset():
    global scale_factor
    pen.reset()
    scale_factor = 1
# autopep8: on


# Set key-event bindings:
window.onkey(key="w", fun=move_forward)
window.onkey(key="s", fun=move_backward)
window.onkey(key="a", fun=turn_left)
window.onkey(key="d", fun=turn_right)
window.onkey(key="c", fun=screen_reset)
window.onkey(key="KP_Add", fun=increase_scale)
window.onkey(key="KP_Subtract", fun=decrease_scale)
window.onkey(key="q", fun=hard_left)
window.onkey(key="e", fun=hard_right)
window.onkey(key="Up", fun=direction_up)
window.onkey(key="Down", fun=direction_down)
window.onkey(key="Left", fun=direction_left)
window.onkey(key="Right", fun=direction_right)

# Set screen focus for event listening
window.listen()
# window.mainloop()

# Keep the display window open until we click on it
window.exitonclick()
