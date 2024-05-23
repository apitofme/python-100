"""
-=< 100 Days of Python >=-
-=[ Day 008 ]=-
"""
"""
L.82 - Functions with Inputs

Quick refresh on Functions:
    - Defined using the "def" keyword with the name given in 'snake_case'
    - Contain a block of code, executed when the function is called
    - Optionally have positional/named "parameters" to pass "arguments"
      to define configuration options or pass data for processing

Previously when we have created our own functions we have done so without
specifying any 'parameters'. When using some of the built-in functions
however we have made use of their specified parameters in order to pass
'arguments' to the function, e.g.:

    - print("This string is technically an 'argument' value")

    - range(0, 10, 2) -- each number is an 'argument' given for a specific
      named parameter [start, stop, step]


We create a variable by defining a name and assigning a value (data) to it
-- e.g. name = 'value'

Well when we create a function which accepts inputs the term 'parameter' is
used to describe the reference name, whilst the 'argument' is the data/value
assigned to it. You can think of it this way:

    - we DEFINE any parameter(s) when we define a function
    - we PASS any argument(s) to a function when we call it

NOTE: parameters are separate from 'local variables' defined within the
function's code-block. Additionally if a parameter does NOT have a default
value specified in the function definition then a value (argument) MUST be
given when calling the function!
"""


def greet(name):
    """exercise demonstrating a function with input parameters"""
    print(f"Hello {name} and welcome!")
    print(f"- {name} has called the 'greet()' function.\n")


greet("Chris")

"""
L.83 - Positional vs. Keyword Arguments

>> Multiple Parameters:

As we've seen some functions accept multiple arguments, this is because
they have multiple parameters defined. Let's go ahead now and update our
previous example so that it has more than one parameter...
"""


def greet_two(name, location):
    """example demonstrating multiple parameters"""
    print(f"Hello {name}")
    print(f"what is it like in {location}?\n")


greet_two("Chris", "Staffordshire")

# demonstrate "positional arguments" by swapping the order:
greet_two("Staffordshire", "Chris")
# => "Hello Staffordshire"
# => "What is it like in Chris?"
"""
Positional Arguments:
This means that arguments given to a function are assigned in the order
(i.e. position) in which they were defined. So in the 'greet_two()'
function the "name" parameter is defined first so it takes the first value
(argument) given when the function is called, and "location" is assigned
the second argument because it is the second parameter. This is the
standard behaviour for functions in Python.

NOTE: in addition to syntax-highlighting most code-editors and IDEs these
days come with some form of 'IntelliSense' (i.e. code-completion hints and
prompting). Typically this will hover a tooltip style window above the code
you're typing. For functions this will usually show what arguments (if any)
are required whilst also hinting at which positional argument is currently
expected (e.g. by underlining the parameter name).

Keyword Arguments:
You may also pass arguments by specifying the keyword name to which they
should be assigned, in the format "name=value". This allows you to pass
them in any order rather than the order in which they were defined.
"""
# call 'greet_two()' again, this time using keyword arguments
greet_two(location="Staffordshire", name="Chris")

"""
L.84 - Coding Exercise: Paint Area Calculator
"""
# See external file: "exercise_paint_calculator.py"
