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
made use of such as 'print()', 'len()' and 'input()'. So we already know
that, although they do different things, we utilise all of these functions
in basically the same way:

    - First we type the name of the function (e.g. "print")
    - Which is followed by a pair of parentheses "()"
    - Inside the parentheses is where we can pass any parameters or data

Function names are reserved keywords in Python, which is why we should
avoid using any of them as a variable name as this could overwrite the
function in our code.

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

Of course Python can't provide every function we will ever possibly need,
so it is important for us to learn how to write our own functions. This
will allow us to design and implement code in a much more reliable and
reusable way, and allow us to create larger, more complex programs. It
really is one of the key stepping-stones on our journey to becoming a
programmer, and will genuinely "take your skills to the next level"!


>> Let's get functional:

In order to create (or rather "DEFINE") our own functions we must use the
"def" keyword, this tells the Python interpreter that what follows is a
function definition, and it looks like this...
"""


def my_function():
    print("Hello from 'my_function'!")


"""
Now if we were to run our code now we wouldn't see anything, there would
be no output, because all we have done so far is to DEFINE our function,
we have yet to CALL it. So let's go ahead an do that...
"""
my_function()  # => "Hello from 'my_function'!"
# Remember the parentheses after the name tells Python to CALL the function

"""
So as with our variables previously (in Python) we can name our functions
almost anything we like, so long as we avoid any reserved keywords!
Function names also uses the same 'snake_case' convention that we use for
variable names. The key differences are:

    - We use the "def" keyword before the name
    - We place a set of parentheses after the name
    - Then finally we place a colon ":" after the parentheses

The colon at the end is important because it tells the Python interpreter
that everything indented beneath this line is part of our function
definition, which ends when the indentation level returns to the same at
which the function definition started.
"""

"""
L.6 - Coding Exercise: 
"""
# See external file: "exercise_.py"
