"""
-=< 100 Days of Python >=-
-=[ Day 019 ]=-
"""
"""
L.142 - OOP: Understanding Object State and Instances

At this point we know how to create a 'Turtle' and use it to draw on the
'Screen'. Most importantly we start by importing both of these classes from
the "turtle" module, e.g.:

    from turtle import Turtle, Screen

Since we are importing classes we also know that, in OOP a Class contains the
code that acts as a template or blueprint from which we can create an Object.
We should also remember that, as a Class is just a blueprint, we can use it to
create any number of distinct Objects. So whilst each object created from a
given Class is built using the same blueprint, they are all individually
unique objects, independent from one another. In programming we call each of
these unique objects an INSTANCE (of that Class/Object).

-- What does this mean?

Well basically it means that we can have more than one Turtle at a time,
with each one capable of moving around and drawing on the Screen independent
of the other(s). -- Each turtle is an instance of the Turtle class.

Since each instance is distinct and independent of any other, each can have
different values assigned to their defined attributes/properties. For example
one could be set to colour Red whilst another one is Green, or Blue; one could
have it's line-width set to draw a thick line, with another set for a thin
line, etc.

As mentioned, in programming we call each unique object an *instance* of the
Class used to create it. However, we refer to the unique set of properties or
current, on-going actions/processes as the object's STATE. Again, this is
unique and independent of any other instance! For example, one Turtle could
be in the process of drawing a circle whilst another is completely stationary.
"""

"""
L.143 - Understanding the Turtle Co-Ordinate System

You may have noticed how, so far whenever we've created a new Turtle and
Screen, the turtle always appears in the middle of the screen. You may also
have figured out that this position ('home') has the X,Y coordinates of "0,0".

The coordinate system for Turtle works based on the size of the Screen, where
the Width and the Height form the X and Y axis respectively, but where the
mid-point is used as the origin for each axis' scale. This means that the
scale for each axis has both positive and negative values, each to a maximum
of HALF of the total size for that axis. Positive values proceed to the Right
and Up, with negative values to the Left and Down, for X and Y respectively.

Using methods provided by the turtle module it is possible both to read the
Screen's width and height properties, and to set them. This allows us to make
informed decisions about coordinate positions within the Screen, which we can
use to move the turtle(s) around.

For example: if we set the Screen to have a Height of 400 and a Width of 500
(measured in pixels), then we know that the scale for the X axis will go from
-250 on the left to +250 on the right, for a total of 500; and the Y axis from
-200 at the bottom to +200 at the top, total 400.

So, if we wanted to position the turtle somewhere specifically, we can set or
obtain known values for the Screen width and height, allowing us to work out
the range of values for the coordinate system. With this we can then work out
the values we want for X and Y, to place the turtle exactly where we want.

Refs:
- https://docs.python.org/3.12/library/turtle.html#turtle.screensize
- https://docs.python.org/3.12/library/turtle.html#turtle.setup
- https://docs.python.org/3.12/library/turtle.html#turtle.position
- https://docs.python.org/3.12/library/turtle.html#turtle.goto
"""
