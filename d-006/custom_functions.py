"""
-=< 100 Days of Python >=-
-=[ Day 006 ]=-
"""
# pylint: disable=missing-function-docstring
"""
L.60 - Defining and Calling Functions in Python
Ref: https://docs.python.org/3.12/library/functions.html

>> Familiar with functions:

Python comes with many "built-in" functions, some of which we have already
made use of such as 'print()', 'len()' and 'input()'. So, although they do
different things we already know that we utilise all of these functions in
basically the same way:

    - First we type the name of the function (e.g. "print")
    - Which is followed by a pair of parentheses "()"
    - Inside the parentheses is where we can pass any parameters or data

NOTE: Function names are NOT treated as reserved 'keywords' by Python so
(re)using one won't actually cause an error or crash. However we should
still try to avoid accidentally reassigning any of them in our code as
doing so would make that particular function unavailable, because the name
used to reference it will have now be pointing to something else!

Whilst some functions don't require any parameters others may take one or
more. Sometimes we simply pass some data (e.g. a String or a List) that we
want the function to process. Other functions however may allow/require us
to define certain operational parameters to achieve the output we desire.
For example: 'range()' where we typically give a 'start' and a 'stop', and
(optionally) a 'step' parameter.

The order in which parameters are given is very important too as functions
expect them in a specific order, even when some parameters are allowed to
be omitted. Some functions however allow for 'named' parameters, which can
be given in any order as long as they are assigned, i.e:

    - function(param2=p2value, param1=p1value)

Not all parameters are named, and those that are don't necessarily require
the name to be used IF they're given in the prescribed order. For instance
in the example above notice that "param2" is given before "param1", which
is fine because they are assigned by name. However (typically) it would
also be possible to provide them without name assignment as follows:

    - function(p1value, p2value)


>> Let's get functional:

Of course Python can't provide every possible function we will ever need
so it is important for us to learn how to write our own functions. This
will allow us to design and implement code in a much more reliable and
reusable way, enabling us to create larger and more complex programs. It
really is one of the key stepping-stones on our journey to becoming a
programmer, and will genuinely "take your skills to the next level" !!

So, in order to create (or rather "DEFINE") our own functions we must use
the "def" keyword, which tells the Python interpreter that what follows is
a function definition, and it looks like this...
"""


def my_function():
    print("Hello from 'my_function'!\n")


"""
Now if we were to run our code at this point we wouldn't see anything,
there would be no output because all we have done so far is DEFINE our
function, we have yet to CALL it. So let's go ahead an do that...
"""
my_function()  # => "Hello from 'my_function'!"
# Remember the parentheses after the name tells Python to CALL the function

"""
As with our variables previously in Python, we can name our functions
almost anything we like as long as we avoid any reserved keywords, and
ideally (as previously mentioned) any existing functions or other named
references.

Function names also uses the same 'snake_case' convention we use for
variable names, with a preference for "longer, more descriptive names".
Ref: https://llego.dev/posts/python-function-naming-conventions-best-practices/


The key points to remember are:

    - We use the "def" keyword before the name
    - We place a set of parentheses after the name
    - Then finally we place a colon ":" after the parentheses

The colon at the end is important because it tells the Python interpreter
that everything indented beneath this line is part of our function
definition, which only ends when the indentation level returns to the same
at which the function definition started.


>> Reuse and Resist:

The importance of functions is that they allow us to make portions of our
code modular and reusable, reducing the amount of code we need to write,
making us and our programs more efficient.

To help visualise this we can look at a website called Reeborg's World:
- https://reeborg.ca/reeborg.html?lang=en&mode=python
- "Reeborg's world is intended to help beginners to learn programming,
  using Python (Javascript is also supported)."

This features a grid-map and a little robot character called Reeborg.
The robot has a very limited set of default commands we can give it
(available via the Reeborg Keyboard), which we can type in to the panel
on the right-hand side. These commands are functions (written in Python)
which include 'move()' and 'turn_left()', and by using these we can
instruct the robot to navigate around the grid. Note however that there
is no function for "turn_right".

If we type 'turn_left()' in the code-panel and click the Play button to
run it we will see that the little robot turns 90 degrees to the left.
Using this knowledge we can deduce that in order to get the robot to
conceptually "turn right" (i.e. face to the right) we can actually just
tell it to "turn left" three times, since this will rotate the robot
270 degrees to the Left ... which is the same as 90 degrees to the Right
(as there are 360 in a full circle).

With this knowledge we can simply write our OWN function to make the robot
turn right, as follows:

    def turn_right():
        turn_left()  # => Reeborg is rotated 90 degrees Left
        turn_left()  # => R. rotated another 90deg Left (now at 180)
        turn_left()  # => R. rotated another 90deg Left (now at 270)

In fact, given the limited set of instructions we can use we could imagine
a situation where we want to be able to turn the robot around. Which with
the previous example we know would require two "turn left" commands to turn
the character 180 degrees. Therefore it might make more sense if we defined
the functions as follows:

    def turn_around():
        turn_left()  # => Reeborg is rotated 90 degrees Left
        turn_left()  # => R. rotated another 90deg Left (now at 180)
    
    def turn_right():
        turn_around()  # => This gets us 2/3rds of the way round (180)
        turn_left()  # => So another 90deg Left gets us facing right

Now any time we want to tell Reeborg to turn around or turn right we can
do so with one line of code, calling the relevant function, rather than
having to type out "turn_left()" multiple times.

So we can see how using and reusing functions can save us time and effort,
making our (programming) lives easier and our programs more efficient.
"""

"""
L.61 - Reeborg's World: "Hurdle 1"
- The Hurdles Loop Challenge

World Info:
Reeborg has entered a hurdles race. Make him run the course, following
the path shown.

What you need to know:
    - The functions move() and turn_left().


>> Solution:

    # Turn Right (i.e. turn left 3 times)
    def turn_right():
        for i in range(3):
            turn_left()

    # Jump Hurdle (Note: does NOT include forward movement!)
    def jump():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

    # There are 6 hurdles to jump in order to reach the finish line
    for i in range(6):
        move()
        jump()

"""

"""
L.62 - Indentation in Python

It doesn't matter how many levels of indentation are 'inside' our function,
we can have as many as we need for whatever code we use. So remember that
conditional statements and loops both require code to be indented too, and
indentation levels add together as required -- i.e. the code block under
an IF statement that is inside a FOR loop, which is itself inside of a
function would have 3 levels of indentation. The FUNCTION definition is
complete once the indentation level returns to the same at which the
function started -- e.g:
"""


def example_function():
    # Function code starts indented beneath the function definition.
    print("Starting 'example_function'...\n")
    for i in range(6):
        # For loop code is indented beneath the loop statement,
        # so code here is at 2x indentation levels.
        print(f"{i+1} times through the loop,")
        if i % 2 != 0:
            # Conditional code is indented beneath the conditional
            # statement, which means it is now 3x levels deep.
            print(f"Only IF '{i}' is an ODD number,")
        # When code returns to here (i.e. 2x levels deep)
        # the conditional statement has finished.
        print("But no more conditionals here.\n")
    # When code returns to here (i.e. 1x level deep)
    # the FOR loop has finished.
    print("OUTSIDE of the Loop, but still INSIDE the Function!\n")


# Finally any code here with no indentation (i.e. at the same level the
# function definition started) is OUTSIDE of and NOT part of the function!
print("This is OUTSIDE of the function and was written AFTER the function \
    definition but BEFORE the function CALL!")
print("Let's call the function now:\n")
# So we'll call the function:
example_function()
# Then print this statement:
print("This is last, and only AFTER the function has been CALLED!")
