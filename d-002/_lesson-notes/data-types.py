"""
Data Types
"""
# String: a string of characters (i.e. text)
print("Hello"[-1])

# Integer: a whole number
print(123 + 345)

"""
Note: we typically use commas to make a large number more readable
(e.g. 123,456), in Python we can actually do the same thing, only
we use underscores '_' instead of commas.
"""
print(123_456_789)

# Float: a 'floating point' number
# i.e. a decimal representation of a fractional or 'non-whole' number
3.14159

# Boolean: True or False (also 1 or 0 respectively - blame binary)
True
False

# Type Tests:
# The 'type()' function returns the data-type of a given variable
print(type('hello')
print(type(12))
print(type(12.34))

# An example problem:
length = len(input("What is your name? "))
"""
The line of code below would result in a "TypeError" and fail to run!
This is because the data-type of 'length' is an "int"
and Python won't let us concatenate an integer value with a string!
"""
#print(f"Your name has " + length + " characters")
print(type(length))

"""
In order to fix this we actually have several options in Python, however
for this example we will simply convert the type to a string:
"""
str_length = str(length)

# so (remembering to change which variable name we reference)
# this should now work:
print(f"Your name has " + str_length + " characters")