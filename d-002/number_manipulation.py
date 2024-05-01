"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-
"""
"""
L.24 - Number Manipulation & F-Strings:
"""
"""
The 'round()' Function:
Ref: https://docs.python.org/3/library/functions.html#round

This built-in function in Python allows us round a floating point number:
"""
# - to a whole number
print(round(8 / 3)) # => 3
# - or to a specified number of deciaml places (e.g. 2)
print(round(8 / 3, 2)) # => 2.67
"""
As you can see the second parameter is optional, and is used to specify
decimal precision (i.e. how many digits we want after the decimal point)

Note: 'round()' can have sometimes exhibit surprising behaviour due to
the limitations of how computers handle decimal fractions with floating
point numbers (i.e. badly!)
"""

"""
Floor Division:

Floor division is a division operation that rounds the result down
to the nearest whole number (integer). In Python we can perform a
floor division using the double forward-slash operator -- i.e. '//'.
When using this form of division we effectively "throw away" the
fractional part (if any) that the normal division would produce.

So the result of a floor division is just the whole number part
-- i.e. the bit before the decimal point
"""
print(8 // 3) # => 2
# Notice how the result is different from what we got using 'round()'
"""
Also, remember how division in Python always returns a floating point
number, even when a number divides cleanly (i.e. with no remainder or
fractional component)?

Well since floor division doesn't produce a fractional component it will
always return an integer ('int')!
"""
print(type(8 // 3)) # => 'int'

"""
Combination Assignment Operators:

Previously we have 'assigned' an input value (or other piece of data to
work with) to a variable name with the equals sign -- e.g. variable = data

However Python also has a short-hand notation which allows us combine an
assignment with a basic math operation, as follows:
"""
# First we assign a value to a variable using the equals sign
num = 0
"""
Now we can perform an operation whilst re-assigning the new value back
on to the variable using an assignment operator:
"""
# Addition -- equivalent to: num = num + 2
num += 4
print(num)

# Subtraction -- equivalent to: num = num - 4
num -= 2
print(num)

# Multiplication -- equivalent to: num = num * 3
num *= 3
print(num)

# Division -- equivalent to: num = num / 6
num /= 6
print(num)
"""
This offers a convenient short-hand way to update the value stored on a
variable 'in-place' (i.e. overwrite the previous value). Particularly for
any kind of incremental counter or other variable that is updated on each
cycle through a loop.
"""

"""
F-Strings: -- i.e. "Formatted String Literals"
Ref: https://docs.python.org/3/reference/lexical_analysis.html#f-strings

An f-string allows us to use different data-types in a string without the
need to convert them first [e.g. with 'str()']. In Python we define an
f-string by simply typing an 'f' before the opening qutation-mark when
declaring a string -- i.e.

    "This is a string"
    f"This is an f-string!"

Any data or expression we want to be interpreted inside of the f-string
must be wrapped in a pair of curly-braces '{}' within the string,
which is then evaluated at run time.

For example: Given 3 different data types...
"""
score = 5               # an 'int'
height = 1.8            # a 'float'
is_winning = True       # a 'bool'

# We can print them all out using an f-string (without converting them)
print(f"Your score is {score}; Your height is {height}; and it is \
    {is_winning} that you are winning!")

"""
L.25 - Coding Exercise: Life in Weeks
"""
# See external file: "exercise_life_in_weeks.py"
