"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-
"""
"""
L.19 - Primitive Data Types:

>> String: a string of characters (i.e. text) denoted by quotation marks.
As we've seen before we can print a string using the 'print()' function:
"""
print("Hello")
# We can use either single or double quotes, as long as we're consistent!
print('World')

"""
We can also access an individual character within a string by placing the
'index' position of the character we want (as an integer, starting from
the left at zero and counting up as as we move to the right) inside a pair
of square brackets '[]' after the string (or string-variable).
"""
print("Hello"[0]) # -> 'H'
world = "World"
print(world[1]) # -> 'o'

"""
It is also possible to count backwards from the end of the string!
However since zero points to the first letter on the left then the last
character (i.e. furthest right) starts at index '-1', then '-2' and so on
moving from right to left back through the string.
"""
# So the 'o' in "Hello" can be accessed at either index '4' or '-1':
print("Hello"[4])
print("Hello"[-1])

"""
>> Integer: a whole number.
Python recognises raw numbers as such and will perform operations
accordingly:
"""
print(123 + 345) # -> 468
"""
However numbers enclosed in quotation marks are treated as a string
not a number, and operations are performed as such -- e.g:
"""
print("123" + '345') # -> "123456" (i.e. string concatenation)

"""
Note: We typically use commas to make a large number more readable
(e.g. 123,456), in Python we can actually do the same thing only we use
underscores '_' instead of commas.
"""
print(123_456_789)

"""
>> Float: a 'floating-point' number
-- i.e. a decimal representation of a fractional or 'non-whole' number.
"""
pi = 3.14159 # Aside: 'pi' is also an "irrational" number! ;)

"""
>> Boolean: literally "True" or "False" values
-- equivalent to '1' or '0' respectively (blame binary!).
"""
True
False

"""
L.20 - Type Error, Type Checking and Type Conversion:
The 'type()' function returns the data-type of the given input/variable.
"""
print(type('hello')) # -> "str" -- i.e. a string
print(type(12)) # -> "int" -- i.e. an integer
print(type(12.34)) # -> "float" -- i.e. a floating-point number
print(type(True)) # -> "bool" -- i.e. a boolean

# An example problem:
length = len(input("What is your name? "))
print(type(length)) # -> "int" (integer)
print(f"Your name has " + length + " characters") # -> TypeError!
"""
When run, the line of code above results in a "TypeError" because the
data-type of the variable "length" is an integer but we are attempting
to use it in the context of string-concatentation (with the '+' symbol).

When we try to mix data-types in this way Python doesn't know how to treat
the '+' symbol since 'adding' (i.e. concatenating) strings together and
actual mathematical addition of numbers are two very different operations.
So, since the string part has no numerical meaning and the integer (at
least as far as Python is concerned) has no textual meaning, it throws an
error.

-- Note: the 'len()' function also returns a TypeError if given a number!

Anyway, in order to fix this error we can use another function in Python
to convert the variable's data-type to a string:
"""
str_length = str(length)
print(type(str_length)) # -> "str" (string)
print(f"Your name has " + str_length + " characters")

"""
There are of course functions to convert to other data-types too:
"""
int_number = int("123") # converts the string "123" to an integer
print(type(int_number))

float_number = float("3.14") # converts the string to a floating-point
print(type(float_number))

"""
It is also possible to convert to a Boolean value using the 'bool()'
function. Remember earler we said that Boolean values (i.e. True / False)
can also be represented as '1' or '0'
"""
print(bool(1)) # -> "True" - converts the integer '1' to a Boolean
print(bool(0)) # -> "False"

# However there are some quirks to consider when converting to a 'bool':
# - any number that is NOT zero equates to "True" (even negative numbers)!
print(bool(2)) # -> "True"
print(bool(-1)) # -> "True"

# - anything else that is considered to have a value is also "True",
#   this includes a string of the number zero
print(bool("0")) # -> "True"
print(bool(3.14)) # -> "True"

# - an empty string however DOES equate to "False"
print(bool("")) # -> "False"
# ...As does any other EMPTY data-structure, but we'll get to those later!

"""
L.21 - Coding Exercise: Data Types
"""
# See external file: "exercise_data_types.py"
