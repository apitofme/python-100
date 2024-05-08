"""
-=< 100 Days of Python >=-
-=[ Day 004 ]=-
"""
"""
L.42 - Introduction to the Random Module

>> What is a "Module"?

Until now we have written all of our code in a single file, which is
executed from top to bottom. However as our projects become increasingly
complex we will need to write more and more code so it becomes harder
to manage it all in one file. This is where modules come in to play.

A module is an external file which contains a portion of the code we want
to use. Code is usually broken out in to separate modules in a logical
way such that an individual module provides related functionality. It is
a way to compartmentalise code in to smaller, re-usable components or
'modules'.

A module can contain code written by us or by others. This is of benefit
in several ways:
    1.  (as mentioned) It helps to keep file-sizes more manageable.
    2.  It allows for collaborative projects (different people can work
        on different modules within a larger codebase)
    3.  We can take advantage of existing modules, i.e:
        - Why waste time "re-inventing the wheel"?
        - When we can "Stand on the shoulders of Giants" instead!

To summarise:

Modules are a great way to break up a large project or codebase in to
more organised and manageable sub-sets of code and functionality. In turn
this compartmentalisation of code increases the likelihood that we can
re-use code again in different projects where we require the same
functionality (meaning we only have to write the code to solve a
particular problem or task once!).

They can also make code-collaboration easier since individual programmers
can work on separate modules, each contributing different functionality
to the overall project, whilst safely working on separate files and thus
preventing potential edit/overwrite clashes and related issues.

NOTE:
It is important to understand that in order to use a module we must first
import it in to our code. We do this using the "import" keyword:
- https://docs.python.org/3.12/reference/simple_stmts.html#the-import-statement


>> Python's "Built-in" Modules:
Ref: https://docs.python.org/3.12/py-modindex.html

The Python 'Standard Library' (SDL) comes complete with many useful
modules that are not part of the core language implementation, meaning
that their functionality is not available in Python until / unless they
are imported!

Two of the most common and useful built-in modules are the "math" module,
which "provides access to the mathematical functions defined by the C
standard" (supplementing those provided by the core Python language); and
the "random" module which "implements pseudo-random number generators for
various distributions".

Today we will learn how to import the Random module and use it to generate
some random 'behaviour' (numbers) in order to make a more realistic "Rock,
Paper, Scissors" game.


>> Let's get started...
"""
# First we need to import the Random module
import random  # nopep8
"""
This basically brings all of the code and functionality contained within
the relevant module's file and adds it to this file at runtime, at the
position of the 'import' statement (which is all handled by the Python
interpreter). However we must ensure that a module is imported before we
try to use any of it's functions, otherwise we will receive an error!
Consequently ALL required modules are typically imported at the very top
of a file before any other code!
--  Hence comments like "#nopep8" which tell the linter extensions in
    VS-Code(ium) to ignore this, as our import statement isn't on the
    first line!

The Random module provides various methods (functions) we can call when
we want to generate different kinds of random numbers. We do so by first
typing the name of the module "random" followed by a dot (i.e. full-stop
/ period) then the name of the method we want to use...
So let's go ahead and create a random integer between (and inclusive of)
'1' and '10' using the provided "randint" method:
"""
# call the 'randint' method to generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

"""
We can help further demonstrate the use of modules in Python by creating
our own custom module (see external file "my_module.py")...
"""
# We can import our custom module using it's module name
# -- i.e. the filename without the file extension ('.py')
import my_module  # nopep8

# We can now reference objects stored in that module using 'dot-notation'
# -- i.e. module_name(dot)variable_name
print(my_module.MY_PI)  # => 3.14159

"""
We can use another method from the Random module to generate a random
floating-point number between 0.0 and 1.0 (by default), however this time
the upper bound ("1.0") is NOT inclusive
-- i.e. we can get "0.999999999..." but never "1"
"""
random_float = random.random()
print(random_float)

# We can get a random floating-point number outside of the default range
# by multiplying the result by the desired upper (exclusive) bound.
# -- i.e. to get a random float between 0 and 5 (Max=4.99999...)
print(random_float * 5)

"""
L.43 - Coding Exercise: Heads or Tails
"""
# See external file: "exercise_coin_toss.py"
