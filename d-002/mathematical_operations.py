"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-
"""
"""
L22 - Simple Math Operators:
"""
# Addition, which uses the plus sign.
3 + 5  # => 8

# Subtraction, which uses the 'minus' sign (a.k.a hyphen / dash).
7 - 4  # => 3

# Multiplication, uses the asterisk or 'star' symbol.
3 * 2  # => 6

# Division, using the forward-slash symbol.
6 / 3  # => 2.0
"""
Note: Division will always return a float, even if it divides cleanly!

Also, Python can mix integer and floating point numbers in operations,
but again the result will always be a float.
"""
print(2 + 3.0)  # => 5.0

"""
Python has other useful math operators too, such as the double-asterisk
for raising a number to a power:
-- e.g. 2 "to the power of" 3 [ i.e. (2 x 2) x 2 = 8 ]
"""
2 ** 3  # => 8

"""
Order of Operations: (i.e. "BODMAS" // "PEMDAS")
- Brackets          //      Parentheses
- Order             //      Exponent
- Division          //      Multiplication
- Multiplication    //      Division
- Addition          //      Addition
- Subtraction       //      Subtraction

Note that the two acronyms have the 'M' and 'D' operations flipped!
This is because they are actually considered EQUAL in priority,
as are 'A' and 'S'. So in either case the priority becomes simply
the order they are written.
"""
print(3 * 3 + 3 / 3 - 3)  # => 7.0

# Challenge: modify the above to get the answer '3'.
print(3 * (3 + 3) / 3 - 3)
"""
By placing brackets around '3 + 3' we make that the highest priority,
so we can demonstrate the process of the equation as follows:

>       3 * (3 + 3) / 3 - 3     -- we start with what's inside the '( )'
->      3 * (6) / 3 - 3         -- multiplication is next (leftmost) so...
-->     18 / 3 - 3              -- after that is division...
--->    6.0 - 3                 -- and lastly the subtraction...
---->   = 3.0                   -- giving us the answer '3'

Remember that division always results in a floating point number, so even
though we're dealing with whole numbers we actually get "6.0" from the
division of "18 / 3", after which we retain the float through all
subsequent operations!
"""

"""
L.23 - Coding Exercise: BMI Calculator
"""
# See external file: "exercise_bmi_calculator.py"
