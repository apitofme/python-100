"""
-=< 100 Days of Python >=-
-=[ Day 008 ]=-

Coding Exercise: Paint Area Calculator (L.84)
Ref: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/e242258e-5006-40f1-9228-8e3a8c7482cc?sl=0d712e20-d561-45cf-bfbf-c92981083867&st=z0IFbiDuWJfMR7kz7qBfuQgxDzjqkjal
"""
"""
Slide 1: Task
- Write a function which calculates how many cans of paint you need to
purchase in order to cover a wall of given dimensions (W x H).

Notes:
    - 1 can of paint covers 5 square meters of wall
    - Area = Width x Height
    - Since you can't buy a fraction of a can your solution should always
      round up!

IMPORTANT:
    - The function MUST be called 'paint_calc()'
    - The parameters MUST be called "height", "width" and "cover"
"""
"""
Slide 2: Solution
"""


def paint_calc(height, width, cover):
    """exercise demonstrating use of multiple parameters"""
    paint_cans = (height * width) // cover
    # compare floor-division to regular (fractional) division
    if (height * width) / cover > paint_cans:
        paint_cans += 1
    # one line version of above:
    # paint_cans = (height * width) // cover + ((height * width) % cover > 0)
    print(f"You'll need {paint_cans} cans of paint.")


# Define a function called paint_calc() so the code below works.
# 🚨 Don't change the code below 👇
test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


"""
NOTE: a one line solution to automatically round UP division would be the
result of floor division PLUS the Boolean value of the modulus of the same
equation compared to 0 (zero).

    - e.g. rounded_up = dividend // divisor + (dividend % divisor > 0)

Let's break this down...

Remember: a Boolean "True" == 1 (one) and "False" == 0 (zero)

Therefore the part AFTER the PLUS sign "+" becomes One or Zero respectively
when there IS or ISN'T a remainder.

Remember: floor-division returns just the integer component of a division
(i.e. the whole number BEFORE the decimal point)

Whenever there IS a modulo remainder the result of floor-division is LOWER
than the result of 'regular' division by the difference of the fractional
component (i.e. the numbers AFTER the decimal point).

Since the fractional component is LESS than the next whole number then we
simply need to add 1 to the result of floor-division in order to round UP.
Which (conveniently) is the numerical value of "True"!
"""
