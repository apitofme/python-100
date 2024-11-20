"""
-=< 100 Days of Python >=-
-=[ Day 019 ]=-
"""
from turtle import Turtle, Screen
"""
L.140 - Higher Oder Functions & Turtle Event Listeners

In this lesson we'll learn how to set up what we call "Event Listeners" which
will allow us to 'listen' for screen 'events' (i.e. key-presses) so that we
can control the Turtle with our keyboard.
"""
pen = Turtle()
window = Screen()
"""
Once we have our 'Screen' object we use can use the "listen()" method to set
the object in to 'event listening' mode. This sets the system's focus to the
Screen object, allowing us to capture key-events.
- Ref: https://docs.python.org/3.12/library/turtle.html#turtle.listen
"""
window.listen()
"""
The Screen module provides several different methods to allow us to detect
different types of screen-events. The one we'll be using for now is the
"onkey()" method, which binds a function to a key-event.
- Ref: https://docs.python.org/3.12/library/turtle.html#turtle.onkey

The 'onkey' method requires us to pass a function as a parameter so that it can
be called when the assigned key is pressed. When we want to pass a function as
a parameter we must pass it by reference. -- If you remember, when we use the
parentheses after a function name it calls the function to run immediately.
So, in order to pass it by reference we must give the function name ONLY,
without the parentheses.
"""
# autopep8: off
def event_function():
    """Example key-event function to make the Turtle move forwards 10 paces"""
    pen.forward(10)
# autopep8: on


window.onkey(key="space", fun=event_function)
"""
The 'onkey' method is an example of what is known as a "Higher order function",
because it takes another function as a parameter. These are functions that are
designed to work with other functions.

NOTE: Whenever we're using methods that we haven't written ourselves it is
always a good idea to use "keyword arguments", where we assign the values to
parameters by name within the function call [e.g. func(param1=val1)], rather
than "positional arguments" where we just pass the values in a defined order.
This also helps with readability, allowing us to understand at a glance what
the values are being assigned to, rather than having to look up the reference
implementation.
"""

# Keep the display window open until we click on it
window.exitonclick()
