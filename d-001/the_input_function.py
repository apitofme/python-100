"""
-=< 100 Days of Python >=-
-=[ Day 001 ]=-
"""
"""
L.11 - The Input Function:
"""
# Sure, now we can print output:
print("What is your name?")

# But how about we get your input on this:
input("What is your name?")

# That's neat but where did it go?
# How can we do anything with that?
print("Hello " + input("What is your name?") + "!")

# Don't forget to comment:
# "like and subscribe" using the hash/pound sign '#'
# - It may seem redundant since we've already been using it,
#   but comments can really help you to understand you code
#   when you come back to it later

"""
L.12 - Coding Exercise: Input Function
"""
# See external file: "exercise_input.py"

"""
L.13 - Python Variables:

When we take user input as we did before we're only actually using it
at the moment it's created, which is rather limiting, but what if
we could store that data to use, process and re-use again later?
That's where "variables" come in.

We create a variable by first typing in a name for it, this is how we
will be able to refer to it again later. Then we 'assign' the data we
want to store to the name using the assignment operator '='. Now
whenever we want to access that piece of data we can use the variable
name we created.

We demonstrate this in the example below where the user input was stored
in the variable 'name', then printed out by simply passing that variable
in to the print function (instead of the raw text or input).
"""
name = input("What is your name?")
print(name)

# Variables are (by definition) 'variable', this means they can be changed
name = "Something Else"
print(name)
# This time when we print 'name' the output is different,
# because we changed the value (data) assigned to that variable.

"""
L.14 - Coding Exercise: Variables
"""
# See external file: "exercise_variables.py"

"""
L.15 - Naming Variables

Technically we can name our variables almost anything we want, so long
as it isn't a keyword reserved by Python. However it is generally good
practice to give them a readable, meaningful name as this will help you
(and others) reading your code at a later date to understand it.

Part of the whole philosophy or thinking behind the 'readable' intent
of the Python language is the idea that code is read much more often
than it is written. So do "future you" a favour and make your code as
clear and intelligible as possible!


Naming Rules:
There are some basic rules to the names we can use in Python too...

- A variable name must be a single, un-broken string of text.
  You can use multiple words but there can't be any spaces between them.
  To do this we can join multiple words together with underscores '_'
  -- e.g. "my_long_variable_name"

- A variable name cannot start with a number.
  Though they are allowed to contain numbers at any other position.
  -- i.e. "1_variable" is not allowed, but "variable_1" is fine

- Finally (as we mentioned above) you shouldn't use a name that is
  already used by Python for something (such as a function or class).
  -- e.g. 'input' is a bad name for a variable because there is already
     a function with the same name!

NOTE:
If you ever get a 'NameError' it is most likely because you mistyped
or misspelt one of the variable names you were trying to use. This isn't
any kind of spell-checking, it only occurs because (when) a name is not
recognised (because it hasn't been previously assigned).
"""
# e.g. if we assign a value to "name"
name = "Fred Blogs"
# but mistype or misspell that variable name when we try to print it
print(nama)  # <- This will cause a "NameError"!
