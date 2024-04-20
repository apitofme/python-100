"""
Simple Math Operators
"""
# Add [plus sign]
3 + 5

# Subtract [dash or 'minus' sign]
7 - 4

# Multiply [star or 'asterix']
3 * 2

# Divide [forward slash]
6 / 3
# = 2.0
"""
Note: Division will always return a float!
Even if it divides cleanly in to a whole number.

Python can mix integer and floating point numbers in operations,
but the result will always be a float.
"""
print(2 + 3.0)
# = 5.0

"""
Python has other simple operators too, such as
the double-asterix for raising a number to a power:
e.g. 2 "to the power of" 3 = (2 x 2) x 2 = 8
"""
2 ** 3

"""
Order of Operations: (i.e. "BODMAS" // "PEMDAS")
- Brackets          //      Parenthases
- Order             //      Exponent
- Division          //      Multiplication
- Multiplication    //      Division
- Addition          //      Addition
- Subtraction       //      Subtraction

Note that the two acronyms have the 'M' and 'D' operations flipped!
This is becuase they are acutally considered EQUAL in priority,
as are 'A' and 'S'. So in either case the priority becomes simply
the order they are written.
"""
print(3 * 3 + 3 / 3 - 3)
# = 7.0

# Challenge: modify the above to get the answer '3'
print(3 * (3 + 3) / 3 - 3)
"""
By placing brackets around '3 + 3' we make that the highest prioriy,
so we can demonstrate the process of the equation as follows:

-       3 * (3 + 3) / 3 - 3
->      3 * (6) / 3 - 3     -- multiplication is next (leftmost)
-->     18 / 3 - 3          -- after that is division
--->    6.0 - 3               -- and lastly, subtraction
---->   = 3.0

Remember that division *always* gives a floating point number,
so even though we're dealing with whole numbers we got "6.0"
from the division of "18 / 3", after which we retain the float.
"""