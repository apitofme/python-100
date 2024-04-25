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

This built-in function in Python allows us round a floating point number...
"""
# - to a whole number
print(round(8 / 3)) # -> 3
# - OR - to a specified number of deciaml places (e.g. 2)
print(round(8 / 3, 2)) # -> 2.67
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
print(8 // 3) # -> 2
# Notice how the result is different from what we got using 'round()'
"""
Also, remember how division in Python always returns a floating point
number, even when a number divides cleanly (i.e. with no remainder or
fractional component)?

Well since floor division doesn't produce a fractional component it will
always return an integer ('int')!
"""
print(type(8 // 3))

"""
Combination Assignment Operators:

Previously we have 'assigned' an input value (or other piece of data to
work with) to a variable name with the equals sign -- e.g. variable = data

However Python has a kind of short-hand notation which allows us combine
this assignment with a basic math operation, as follows:
"""
# First we assign a variable name a value using the equals sign
num = 0

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
F-Strings:

These allow us to use different data-types in a string without the need to
convert them first (i.e. with 'str()'), and to use them all we need to do
is to type an 'f' before we start to declare a string, i.e:

    "This is a string"
    f"This is an f-string!"

Then whenever we want to use a stored variable in an f-string we simply
wrap the variable name in a pair of curly-braces '{}'
"""
score = 5
height = 1.8
is_winning = True
print(f"Your score is {score}; Your height is {height}; and it is {is_winning} that you are winning!")
