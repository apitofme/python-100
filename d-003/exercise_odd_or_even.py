"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-

Coding Exercise: Odd or Even (L.31)
"""
"""
Slide 1: Task
- Write a program that works out if a given number is od or even.
"""
number = int(input())
"""
Notes:
Even numbers are numbers which can be divided by 2 with no remainder
(i.e. nothing after the decimal point).

Remember the division operator divides a number precisely, even in to a
decimal fraction when necessary, and always returns a floating-point
number regardless. Therefore we need a different operator, one that only
divides as far as the divisor will go in to the dividend whole, and gives
the rest as a remainder.
-- e.g. 5 / 2 => 2 x 2 + 1 => 2 goes in to 5 twice with 1 remainder

>> Introducing the Modulo! - The modulo is a mathematical operation which
returns the remainder of a division. In other words it performs a division
only so far as the divisor goes in to the dividend whole and returns the
number left over when that is no longer possible.
-- e.g:
    14 / 4 => 4 x 3 + 2 => 12 + 2
    => 4 goes in to 14 three whole times, with 2 left over
    So the remainder or "modulo" of that division is 2.
    This equation can therefore be written as "14 mod 4 = 2"

In Python we use the percent symbol '%' to perform a "mod" operation.
"""
"""
Slide 2: Solution
"""
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
"""
Here we're effectively saying "IF the modulo of the given number divided
by 2 is equal to 0 (zero) then it is an EVEN number", because there is no
remainder. Then if that statement is false (i.e. there IS a remainder)
then ('else') the number must be ODD!
"""

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/f50f12c1-f7ab-46c3-8cb9-c2a8cb67574d?sl=50399863-208a-4c76-893a-5278b0d97b52&st=fB4KmKPMODKhNRMBbqLIeK6q2r0UyTPW
"""
