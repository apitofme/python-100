"""
Number Manipulation & F-Strings
"""
"""
Rounding a floating point number using the 'round()' function:
"""
# - to a whole number
print(round(8 / 3))
# - to a certain number of deciaml places (e.g. 2)
print(round(8 / 3, 2))
# So 'round()' takes a second optional parameter for decimal precision

"""
Floor division: [double-fslash '//']
"""
# - this operation will always return just the whole number part
print(round(8 // 3))
# - and the returned data-type is an 'integer'
print(type(8 // 3))

"""
Combination Assignment Operators:
These combine one of the basic operations with an assignment (i.e. '=').
So previously we have 'assigned' an input value, or other piece of data
to work with, to a variable name with the equals sign - e.g. variable = data

But we can also combine this with a basic math operation as follows:
"""
num = 10
# Addition -- equivalent to: num = num + 2
num += 2
print(num)

# Subtraction -- equivalent to: num = num - 4
num -= 4
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