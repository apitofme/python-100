"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-

Coding Exercise: Leap Year (L.34)
"""
"""
Slide 1: Task
- Write a program that works out whether a given year is a leap year.
"""
year = int(input())
"""
Notes:
We can work out if a particular year is a leap year or not using the
following rules:
    - Every year that is divisible by 4 with no remainder
    - EXCEPT for any year that is divisible by 100 with no remainder
    - UNLESS the year is also divisible by 400 with no remainder
"""
"""
Slide 2: Solution
"""
# First we check if the year is cleanly divisible by 4 (no remainder)
if year % 4 == 0:

    # When that is the case...
    # We must next check if it is also cleanly divisible by 100
    if year % 100 == 0:

        # Should that ALSO be the case, then...
        # Finally we check if it is cleanly divisible by 400
        if year % 400 == 0:
            # If it IS then we have a Leap year
            print("Leap year")
        else:
            # But if NOT then it is not a Leap Year 
            print("Not leap year")
        
    # When the year IS cleanly divisible by 4 but NOT by 100
    else:
        # Then we have a Leap Year
        print("Leap year")
    
# Otherwise, the year is NOT cleanly divisible by 4 os is NOT a Leap Year!
else:
    print("Not leap year")

"""
My Solution:
"""
# Let's start with the simplest condition first...
# If the year is NOT evenly divisible by 4 (with no remainder)
# then it is NOT a leap year.
if year % 4 != 0:
    print("Not leap year")
# Otherwise...
else:
    # We know the year IS evenly divisible by 4, so now...
    # If the year is NOT evenly divisible by 100...
    if year % 100 != 0:
        # ...then it IS a leap year
        print("Leap year")
    # However if the year IS evenly divisible by 100 we must now test...
    # If the year is NOT evely divisible by 400...
    elif year % 400 != 0:
        # ...in which case it is NOT a leap year
        print("Not leap year")
    # Finally, in ALL other cases
    # i.e. 'year' IS evenly divisible by 4, and by 100, AND by 400...
    else:
        # Then the year IS a leap year!
        print("Leap year")

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/3aa8ecef-1215-4988-8e52-a3c59e931231?sl=157049e7-1073-4eb9-b52c-43baeeb3da5f&st=E2QWBmWXaz8cmisjGtKOpTz1jhxdTg9v
"""
